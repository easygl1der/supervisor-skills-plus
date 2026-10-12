#!/usr/bin/env python3
"""Record the spans each check-loop round changed and flag reversions.

Usage:
    python span_guard.py check  <repo> --state FILE --round K --check C --rule R
                                [--base REV] [--head REV|WORKTREE] [--terms TSV]
                                [--paths P ...]
    python span_guard.py record <repo> --state FILE --round K --check C --rule R
                                [--base REV] [--head REV|WORKTREE] [--terms TSV]
                                [--paths P ...] [--force]
    python span_guard.py report --state FILE

What it does:
  * Reads `git diff <base> <head>` (head defaults to HEAD; WORKTREE means the
    working tree) and turns every hunk into word-level change pairs
    (deleted text, inserted text).
  * A REVERSION is a new pair that deletes what an earlier recorded pair
    inserted and inserts what it deleted (whitespace-normalized; a pure
    deletion counts as reverted when the deleted text is inserted again).
  * A reversion of round K-1 with the same rule (or with no different rule)
    is an ERROR: the oscillation guard forbids it. Reverting an older round,
    or citing a different rule, is a WARNING that must be justified in the
    log.
  * A new edit that overlaps text changed in an earlier round, without
    reverting it, is reported as INFO (re-edit).
  * --terms TSV: lines "term<TAB>rejected1;rejected2". Inserted text that
    contains a rejected reading is an ERROR (the term table is a locked
    decision).
  * `record` runs the same checks and then appends this diff to the state
    file. It refuses (exit 1) on an ERROR unless --force is given.
  * --base defaults to the head recorded last in the state file, else HEAD.

Exit codes: 0 clean or warnings only, 1 errors, 2 usage or git failure.
The state file is JSON; keep it next to the log (docs/log/<date>-check-loop.spans.json).
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

WORKTREE = "WORKTREE"
MIN_CHARS = 3  # ignore pairs whose changed text is shorter than this on both sides
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def git(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)


def norm(text: str) -> str:
    return " ".join(text.split())


def resolve(repo: str, rev: str) -> str:
    if rev == WORKTREE:
        return WORKTREE
    r = git(repo, "rev-parse", "--verify", rev + "^{commit}")
    if r.returncode != 0:
        raise SystemExit(f"span_guard: cannot resolve revision {rev!r}: {r.stderr.strip()}")
    return r.stdout.strip()


def word_pairs(removed: list[str], added: list[str]) -> list[list[str]]:
    """Word-level (deleted, inserted) fragments between two blocks of lines."""
    a = " ".join(removed).split()
    b = " ".join(added).split()
    pairs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        d, i = " ".join(a[i1:i2]), " ".join(b[j1:j2])
        if len(d) < MIN_CHARS and len(i) < MIN_CHARS:
            continue
        pairs.append([d, i])
    return pairs


def read_diff(repo: str, base: str, head: str, paths: list[str]) -> dict[str, list[dict]]:
    cmd = ["diff", "--unified=0", "--no-color", "--no-renames", base]
    if head != WORKTREE:
        cmd.append(head)
    if paths:
        cmd += ["--", *paths]
    r = git(repo, *cmd)
    if r.returncode != 0:
        raise SystemExit(f"span_guard: git diff failed: {r.stderr.strip()}")
    files: dict[str, list[dict]] = {}
    current = None
    hunk = None

    def close() -> None:
        if hunk is not None and current is not None:
            hunk["pairs"] = word_pairs(hunk.pop("_rm"), hunk.pop("_add"))
            if hunk["pairs"]:
                files.setdefault(current, []).append(hunk)

    for line in r.stdout.splitlines():
        if line.startswith("diff --git"):
            close()
            hunk = None
            current = None
        elif line.startswith("+++ "):
            name = line[4:]
            current = name[2:] if name.startswith("b/") else name
        elif line.startswith("--- ") and current is None:
            continue
        elif line.startswith("@@"):
            close()
            m = HUNK.match(line)
            if not m:
                hunk = None
                continue
            hunk = {
                "old": [int(m.group(1)), int(m.group(2) or 1)],
                "new": [int(m.group(3)), int(m.group(4) or 1)],
                "_rm": [],
                "_add": [],
            }
        elif hunk is not None and line.startswith("-"):
            hunk["_rm"].append(line[1:])
        elif hunk is not None and line.startswith("+"):
            hunk["_add"].append(line[1:])
    close()
    return files


def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {"records": []}


def load_terms(path: str | None) -> list[tuple[str, list[str]]]:
    if not path:
        return []
    terms = []
    for raw in Path(path).read_text().splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) >= 2:
            rejected = [x.strip() for x in parts[1].split(";") if x.strip()]
            terms.append((parts[0].strip(), rejected))
    return terms


def reverts(prior: list[str], new: list[str]) -> bool:
    pd, pi = norm(prior[0]), norm(prior[1])
    nd, ni = norm(new[0]), norm(new[1])
    if pi and pd:
        return nd == pi and ni == pd
    if pd and not pi:  # prior deleted text; new inserts it again
        return bool(ni) and pd in ni
    if pi and not pd:  # prior inserted text; new deletes it
        return bool(nd) and pi in nd
    return False


def overlaps(prior: list[str], new: list[str]) -> bool:
    pi = norm(prior[1])
    nd = norm(new[0])
    return bool(pi) and bool(nd) and (pi in nd or nd in pi)


def analyse(state: dict, files: dict, rnd: int, rule: str, terms) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    for path, hunks in files.items():
        for h in hunks:
            for pair in h["pairs"]:
                where = f"{path}:{h['new'][0]}"
                for rec in state["records"]:
                    if rec["round"] >= rnd:
                        continue
                    for ph in rec["files"].get(path, []):
                        for pp in ph["pairs"]:
                            tag = f"round {rec['round']} check {rec['check']} ({rec['rule']})"
                            if reverts(pp, pair):
                                same_rule = rec["rule"].strip() == rule.strip()
                                if rec["round"] == rnd - 1 and same_rule:
                                    level = "ERROR"
                                    why = "reverts the previous round under the same rule"
                                elif rec["round"] == rnd - 1:
                                    level = "WARNING"
                                    why = f"reverts the previous round; cites a different rule ({rule})"
                                else:
                                    level = "WARNING"
                                    why = "reverts an older round; justify in the log"
                                findings.append((level, f"{where} {why}: {tag}: "
                                                 f"{pair[0]!r} -> {pair[1]!r}"))
                            elif overlaps(pp, pair):
                                findings.append(("INFO", f"{where} re-edits text changed in {tag}"))
                for term, rejected in terms:
                    for rj in rejected:
                        if re.search(r"\b" + re.escape(rj) + r"\b", pair[1], re.IGNORECASE):
                            findings.append(("ERROR", f"{where} inserts rejected reading {rj!r} "
                                             f"of locked term {term!r}"))
    # de-duplicate, keep order
    seen, out = set(), []
    for f in findings:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out


def cmd_check_or_record(args: argparse.Namespace, write: bool) -> int:
    repo = args.repo
    if git(repo, "rev-parse", "--git-dir").returncode != 0:
        print(f"span_guard: {repo} is not a git repository")
        return 2
    state_path = Path(args.state)
    state = load_state(state_path)
    if args.base:
        base = resolve(repo, args.base)
    elif state["records"] and state["records"][-1]["head"] != WORKTREE:
        base = state["records"][-1]["head"]
    else:
        base = resolve(repo, "HEAD")
    head = resolve(repo, args.head)
    files = read_diff(repo, base, head, args.paths or [])
    findings = analyse(state, files, args.round, args.rule, load_terms(args.terms))
    n_pairs = sum(len(h["pairs"]) for hs in files.values() for h in hs)
    print(f"span_guard: round {args.round} check {args.check}: {n_pairs} change(s) "
          f"in {len(files)} file(s), {base[:8]}..{head if head == WORKTREE else head[:8]}")
    for level, msg in findings:
        print(f"  {level}: {msg}")
    errors = any(level == "ERROR" for level, _ in findings)
    if write:
        if errors and not args.force:
            print("span_guard: not recorded; fix the reversion or cite a different rule (or --force and justify in the log)")
            return 1
        state["records"].append({
            "round": args.round, "check": args.check, "rule": args.rule,
            "base": base, "head": head, "files": files,
            "flags": [f"{level}: {msg}" for level, msg in findings],
        })
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(state, indent=1, ensure_ascii=False) + "\n")
        print(f"span_guard: recorded in {state_path}")
    return 1 if errors else 0


def cmd_report(args: argparse.Namespace) -> int:
    state = load_state(Path(args.state))
    print("| Round | Check | Rule | File | Lines (new) | Changes | Flags |")
    print("|---|---|---|---|---|---|---|")
    for rec in state["records"]:
        flags = len(rec.get("flags", []))
        if not rec["files"]:
            print(f"| {rec['round']} | {rec['check']} | {rec['rule']} | (no change) | | 0 | {flags} |")
        for path, hunks in rec["files"].items():
            spans = ", ".join(f"{h['new'][0]}-{h['new'][0] + max(h['new'][1], 1) - 1}" for h in hunks)
            n = sum(len(h["pairs"]) for h in hunks)
            print(f"| {rec['round']} | {rec['check']} | {rec['rule']} | {path} | {spans} | {n} | {flags} |")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("check", "record"):
        s = sub.add_parser(name)
        s.add_argument("repo")
        s.add_argument("--state", required=True)
        s.add_argument("--round", type=int, required=True)
        s.add_argument("--check", required=True, help="check id, e.g. 1, 2, 3 or 1R (regression)")
        s.add_argument("--rule", required=True, help="rule source, e.g. 'WR-19' or 'skill:deai-writing S2'")
        s.add_argument("--base")
        s.add_argument("--head", default="HEAD")
        s.add_argument("--terms")
        s.add_argument("--paths", nargs="*")
        if name == "record":
            s.add_argument("--force", action="store_true")
    r = sub.add_parser("report")
    r.add_argument("--state", required=True)
    args = p.parse_args()
    if args.cmd == "report":
        return cmd_report(args)
    return cmd_check_or_record(args, write=args.cmd == "record")


if __name__ == "__main__":
    sys.exit(main())
