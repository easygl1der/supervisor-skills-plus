#!/usr/bin/env python3
"""List rule candidates from a project's records and flag possible duplicates.

Scans, inside PROJECT_DIR:
  docs/feedback/*.md   response-table rows whose first cell is an FB- id
  docs/guidance/*.md   guidance records: "What they mean" and "Points to
                       notice" bullets, the Decision text, Actions table rows
  docs/adr/*.md        ADR title + Decision paragraph, and "Do not" bullets

For each candidate it prints the id, kind, text and source path:line, then the
existing research-core rule lines and checklist items that look similar
(token overlap over content words: mean of Dice and containment). The score is a hint for a human
reviewer, not a verdict.

Usage:
  find_rule_candidates.py PROJECT_DIR [--core DIR] [--min-score 0.35]
                          [--top 3] [--json]

--core defaults to ../../research-core/references relative to this script.
Exit 0 on success, 2 when PROJECT_DIR has none of the scanned folders.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

STOP = set(
    """a an the and or but if then else of to in on at by for with from as is are
    was were be been being it its this that these those there here we our us you
    your they their them he she his her i my me not no do does did done can could
    should would may might must will shall into onto than so such each every any
    all some more most less least very also only just about over under per via
    when where which who whom what while both either neither
    one two three use used using make made add added get got keep kept same other
    e g eg ie etc paper section""".split()
)
TOKEN = re.compile(r"[a-z][a-z0-9]+")
FB_ID = re.compile(r"^FB-[A-Za-z0-9-]+$")
G_ID = re.compile(r"^G-\d{8}-[A-Za-z0-9-]+$")
ITEM_HEAD = re.compile(r"^###\s+([A-Z]{2,3}(?:-[A-Z]{2,3})?-\d{2,3})\s+(.*)$")
PLACEHOLDER = re.compile(r"^<[^>]*>$")


def stem(tok: str) -> str:
    if len(tok) > 4 and tok.endswith("ies"):
        tok = tok[:-3] + "y"
    elif len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
        tok = tok[:-1]
    for suf in ("ing", "ed"):
        if len(tok) > len(suf) + 3 and tok.endswith(suf):
            tok = tok[: -len(suf)]
            if len(tok) > 3 and tok[-1] == tok[-2] and tok[-1] not in "aeiou":
                tok = tok[:-1]
            break
    if len(tok) > 4 and tok.endswith("e"):
        tok = tok[:-1]
    return tok


def tokens(text: str) -> set[str]:
    text = re.sub(r"\[src:[^\]]*\]", " ", text.lower())
    return {stem(t) for t in TOKEN.findall(text) if t not in STOP}


def similarity(cand: set[str], rule: set[str]) -> tuple[float, int]:
    """Mean of the Dice coefficient and the share of candidate words found in
    the rule (containment). Containment is used only when the candidate has at
    least three content words, so very short candidates do not match
    everything."""
    inter = len(cand & rule)
    if not cand or not rule:
        return 0.0, 0
    d = 2 * inter / (len(cand) + len(rule))
    if len(cand) < 3:
        return d, inter
    return (d + inter / len(cand)) / 2, inter


@dataclass
class Item:
    id: str
    kind: str
    text: str
    path: str
    line: int
    match: str = ""  # text used for similarity when it differs from text
    dups: list = field(default_factory=list)


def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text


def is_placeholder(text: str) -> bool:
    t = text.strip().strip("-").strip()
    return not t or bool(PLACEHOLDER.match(t))


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


# ---------------------------------------------------------------- project side
def scan_feedback(path: Path, rel: str) -> list[Item]:
    out: list[Item] = []
    header: list[str] | None = None
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.lstrip().startswith("|"):
            header = None if not line.strip() else header
            continue
        cells = split_row(line)
        if cells and cells[0].lower() == "id":
            header = [c.lower() for c in cells]
            continue
        if not cells or not FB_ID.match(cells[0]):
            continue

        def col(name: str, default: int) -> str:
            idx = default
            if header:
                for i, h in enumerate(header):
                    if name in h:
                        idx = i
                        break
            return cells[idx] if idx < len(cells) else ""

        comment = col("comment", 1)
        if is_placeholder(comment):
            continue
        decision = col("decision", 3)
        change = col("change", 4)
        text = comment
        if change and not is_placeholder(change):
            text += f" | change: {change}"
        if decision and not is_placeholder(decision):
            text += f" | decision: {decision}"
        out.append(Item(cells[0], "feedback", clean(text), rel, no, match=clean(comment)))
    return out


def sections(lines: list[str]) -> dict[str, list[tuple[int, str]]]:
    cur = None
    res: dict[str, list[tuple[int, str]]] = {}
    for no, line in enumerate(lines, 1):
        if line.startswith("## "):
            cur = line[3:].strip().lower()
            res[cur] = []
            continue
        if cur is not None:
            res[cur].append((no, line))
    return res


def bullets(body: list[tuple[int, str]]) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for no, line in body:
        if re.match(r"^\s*[-*]\s+", line):
            out.append((no, re.sub(r"^\s*[-*]\s+", "", line)))
        elif out and line.startswith("  ") and line.strip():
            n0, t0 = out[-1]
            out[-1] = (n0, t0 + " " + line.strip())
    return out


def scan_guidance(path: Path, rel: str) -> list[Item]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rid = path.stem
    for line in lines:
        m = re.match(r"^Record id:\s*(\S+)", line)
        if m and not is_placeholder(m.group(1)):
            rid = m.group(1)
    sec = sections(lines)
    out: list[Item] = []
    for key, tag in (("what they mean", "M"), ("points to notice", "P")):
        body = next((v for k, v in sec.items() if k.startswith(key)), [])
        for n, (no, text) in enumerate(bullets(body), 1):
            text = re.sub(r"\(confidence:[^)]*\)", "", text)
            if is_placeholder(text) or text.lower().startswith("to clarify"):
                continue
            out.append(Item(f"{rid}/{tag}{n}", "guidance", clean(text), rel, no))
    body = next((v for k, v in sec.items() if k.startswith("actions")), [])
    for no, line in body:
        cells = split_row(line) if line.lstrip().startswith("|") else []
        if len(cells) > 1 and G_ID.match(cells[0]) and not is_placeholder(cells[1]):
            out.append(Item(cells[0], "guidance-action", clean(cells[1]), rel, no))
    body = next((v for k, v in sec.items() if k.startswith("decision")), [])
    text = " ".join(l.strip() for _, l in body if l.strip())
    if text and not is_placeholder(text):
        out.append(Item(f"{rid}/D", "guidance-decision", clean(text), rel, body[0][0]))
    return out


def scan_adr(path: Path, rel: str) -> list[Item]:
    lines = path.read_text(encoding="utf-8").splitlines()
    m = re.search(r"(\d{3,4})", path.stem)
    aid = f"ADR-{m.group(1)}" if m else path.stem
    title = ""
    for line in lines:
        mt = re.match(r"^#\s+ADR\s*\d*:?\s*(.*)$", line)
        if mt:
            title = mt.group(1).strip()
            break
    status = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("Status:")), "")
    sec = sections(lines)
    out: list[Item] = []
    body = next((v for k, v in sec.items() if k.startswith("decision")), [])
    para: list[str] = []
    start = body[0][0] if body else 1
    for _, l in body:
        if not l.strip() and para:
            break
        if l.strip():
            para.append(l.strip())
    text = clean(f"{title}. {' '.join(para)}") if para else title
    if text and not is_placeholder(text):
        kind = "adr" if "superseded" not in status.lower() else "adr-superseded"
        out.append(Item(aid, kind, text, rel, start))
    body = next((v for k, v in sec.items() if k.startswith("do not")), [])
    for n, (no, b) in enumerate(bullets(body), 1):
        if not is_placeholder(b):
            out.append(Item(f"{aid}/DN{n}", "adr-do-not", clean(b), rel, no))
    return out


def scan_project(root: Path) -> tuple[list[Item], int]:
    items: list[Item] = []
    found = 0
    for sub, fn in (("feedback", scan_feedback), ("guidance", scan_guidance), ("adr", scan_adr)):
        d = root / "docs" / sub
        if not d.is_dir():
            continue
        found += 1
        for p in sorted(d.glob("*.md")):
            if p.name.lower() in ("readme.md", "index.md"):
                continue
            items.extend(fn(p, str(p.relative_to(root))))
    return items, found


# ------------------------------------------------------------- research-core side
def scan_core(core: Path) -> list[Item]:
    out: list[Item] = []
    for p in sorted(core.rglob("*.md")):
        if p.name.startswith("_") or p.parent.name == "experts":
            continue
        rel = str(p.relative_to(core))
        lines = p.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            m = ITEM_HEAD.match(line)
            if m:
                text = m.group(2)
                j = i + 1
                while j < len(lines) and not lines[j].startswith("#"):
                    if lines[j].lstrip().startswith("- [ ] Check:"):
                        chk = [lines[j].split("Check:", 1)[1].strip()]
                        k = j + 1
                        while k < len(lines) and lines[k].startswith("  ") and lines[k].strip():
                            chk.append(lines[k].strip())
                            k += 1
                        text += ". " + " ".join(chk)
                        break
                    j += 1
                out.append(Item(m.group(1), "checklist", clean(text), rel, i + 1))
                i += 1
                continue
            if re.match(r"^\s*-\s+", line) and not re.match(r"^\s*-\s+(\[ \]|Why|Status|Scope|Owner|Src):", line):
                buf = [re.sub(r"^\s*-\s+", "", line)]
                k = i + 1
                while k < len(lines) and lines[k].startswith("  ") and lines[k].strip() and not re.match(r"^\s*-\s+", lines[k]):
                    buf.append(lines[k].strip())
                    k += 1
                text = " ".join(buf)
                if "[src:" in text:
                    out.append(Item(f"{rel}:{i + 1}", "rule", clean(text), rel, i + 1))
                i = k
                continue
            i += 1
    return out


def main() -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("project", type=Path)
    ap.add_argument("--core", type=Path, default=here.parent.parent / "research-core" / "references")
    ap.add_argument("--min-score", type=float, default=0.35)
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    items, found = scan_project(a.project)
    if not found:
        print(f"no docs/feedback, docs/guidance or docs/adr under {a.project}", file=sys.stderr)
        return 2
    core = scan_core(a.core) if a.core.is_dir() else []
    if not core:
        print(f"warning: no research-core rules found under {a.core}", file=sys.stderr)
    core_tok = [(c, tokens(c.text)) for c in core]
    for it in items:
        t = tokens(it.match or it.text)
        scored = []
        for c, ct in core_tok:
            s, inter = similarity(t, ct)
            if s >= a.min_score and inter >= 2:
                scored.append((round(s, 2), c))
        scored.sort(key=lambda x: -x[0])
        it.dups = [
            {"score": s, "id": c.id, "kind": c.kind, "where": f"{c.path}:{c.line}", "text": c.text[:140]}
            for s, c in scored[: a.top]
        ]

    if a.json:
        print(json.dumps([asdict(i) for i in items], indent=2, ensure_ascii=False))
        return 0
    print(f"# Rule candidates in {a.project} ({len(items)} items; {len(core)} research-core rules indexed)")
    for it in items:
        print(f"\n{it.id}  [{it.kind}]  {it.path}:{it.line}")
        print(f"  text: {it.text[:300]}")
        if it.dups:
            print("  possible duplicates:")
            for d in it.dups:
                loc = d["where"] if d["id"] == d["where"] else f"{d['id']} ({d['where']})"
                print(f"    {d['score']:.2f}  {loc}  {d['text'][:90]}")
        else:
            print("  possible duplicates: none above threshold")
    n_dup = sum(1 for i in items if i.dups)
    print(f"\nSummary: {len(items)} candidates, {n_dup} with possible duplicates, {len(items) - n_dup} look new.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
