#!/usr/bin/env python3
"""Session-start brief for a research project. Read-only.

Usage:
    python session_brief.py <project_dir> [--paper-dir DIR] [--today YYYY-MM-DD]

Prints: the stage from research.yaml and the stage the signals suggest;
blockers from docs/STATUS.md; overdue guidance actions and unverified
feedback (sv-feedback/scripts/guidance_review.py); open reviewer
markers (sv-feedback/scripts/list_markers.py); the next deadline
with its source; and records warnings (no source for the deadline, STATUS
not updated in 14 days, no source of truth named).

Signals: rebuttal (reviewer feedback ids FB-R*), submission (deadline within
7 days), internal-review (live markers or unverified feedback), writing (a
.tex file with \\begin{document}), experiments (a runs-log row in the last
14 days), else idea/design. Exit 0 always.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
F2R = [HERE.parents[2] / "sv-feedback" / "scripts",
       Path.home() / ".claude" / "skills" / "sv-feedback" / "scripts"]


def yaml_get(text: str, *path: str) -> str:
    """Tiny reader for the research.yaml template layout (no PyYAML needed)."""
    try:
        import yaml  # type: ignore
        node = yaml.safe_load(text) or {}
        for p in path:
            node = node.get(p) if isinstance(node, dict) else None
        return "" if node is None else str(node)
    except ImportError:
        pass
    if len(path) == 1:
        m = re.search(rf"^{path[0]}:\s*([^#\n]*)", text, re.M)
        return m.group(1).strip().strip("'\"") if m else ""
    block = re.search(rf"^{path[0]}:\s*(?:\{{(.*?)\}}|\n((?:[ \t]+.*\n?)+))", text, re.M)
    if not block:
        return ""
    body = block.group(1) or block.group(2) or ""
    m = re.search(rf"\b{path[1]}:\s*(\"[^\"]*\"|'[^']*'|[^,#}}\n]*)", body)
    return m.group(1).strip().strip("'\"") if m else ""


def script(name: str) -> Path | None:
    return next((d / name for d in F2R if (d / name).exists()), None)


def run(args: list[str]) -> str:
    return subprocess.run([sys.executable, *args], capture_output=True, text=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    ap.add_argument("--paper-dir")
    ap.add_argument("--today")
    a = ap.parse_args()
    root = Path(a.project_dir).resolve()
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    ry = root / "research.yaml"
    if not ry.exists():
        print("research.yaml: MISSING -> run sv-supervisor init")
        return 0
    y = ry.read_text()
    stage = yaml_get(y, "stage") or "unset"
    dl_date, dl_src = yaml_get(y, "deadline", "date"), yaml_get(y, "deadline", "source")
    paper = Path(a.paper_dir).resolve() if a.paper_dir else root
    status = root / "docs" / "STATUS.md"
    st = status.read_text() if status.exists() else ""
    warn: list[str] = []

    # deadline
    days = None
    m = re.search(r"\d{4}-\d{2}-\d{2}", dl_date if dl_date not in ("None", "null") else "")
    if m:
        days = (dt.date.fromisoformat(m.group(0)) - today).days
        if not dl_src:
            warn.append("deadline has no dated official source (research.yaml deadline.source)")
    else:
        warn.append("no deadline in research.yaml")

    # markers and guidance
    markers, overdue, unverified, reviews = [], [], [], False
    lm = script("list_markers.py")
    if lm:
        try:
            markers = json.loads(run([str(lm), str(paper), "--json"]) or "[]")
        except json.JSONDecodeError:
            warn.append("list_markers.py output unreadable")
    gr = script("guidance_review.py")
    if gr:
        out = run([str(gr), str(root), "--today", today.isoformat()])
        overdue = [l for l in out.splitlines() if l.startswith(("OVERDUE", "NO-EVIDENCE"))]
        unverified = [l for l in out.splitlines() if l.startswith("UNVERIFIED")]
        reviews = any(re.search(r"\bFB-R\d", l) for l in unverified)
    if not (lm and gr):
        warn.append("sv-feedback scripts not found; markers and guidance not checked")
    fb = root / "docs" / "feedback"
    if fb.is_dir() and any(re.search(r"\|\s*FB-R\d", p.read_text()) for p in fb.glob("*.md")):
        reviews = True

    # draft and runs
    draft = any("\\begin{document}" in p.read_text(errors="replace")
                for p in paper.rglob("*.tex") if "docs" not in p.parts)
    runs_recent = False
    rl = root / "docs" / "runs.md"
    if rl.exists():
        for d in re.findall(r"^\|[^|]*\|\s*(\d{4}-\d{2}-\d{2})", rl.read_text(), re.M):
            runs_recent |= (today - dt.date.fromisoformat(d)).days <= 14

    live = [x for x in markers if x.get("kind") in ("live", "commented-out", "in-iffalse", "notes-hidden")]
    if reviews:
        sig = "rebuttal"
    elif days is not None and 0 <= days <= 7:
        sig = "submission"
    elif live or unverified:
        sig = "internal-review"
    elif draft:
        sig = "writing"
    elif runs_recent:
        sig = "experiments"
    else:
        sig = "idea/design"

    # STATUS
    blockers = []
    sec = re.search(r"^## Blockers\s*\n(.*?)(?=^## |\Z)", st, re.M | re.S)
    if sec:
        blockers = [l.strip() for l in sec.group(1).splitlines() if l.strip().startswith("-") and "<blocker>" not in l]
    if not status.exists():
        warn.append("docs/STATUS.md missing -> sv-supervisor-records Task 1")
    else:
        lu = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", st)
        if not lu or (today - dt.date.fromisoformat(lu.group(1))).days > 14:
            warn.append("STATUS.md not updated in the last 14 days (or no date)")
        if not re.search(r"^\| *Paper *\| *[^|<\s]", st, re.M):
            warn.append("STATUS.md names no source of truth for the paper")

    print(f"Stage: {stage} (research.yaml); signals suggest: {sig}"
          + ("" if sig.split("/")[0] in stage or stage in sig else "  <- differs, confirm with the user"))
    print(f"Next deadline: {dl_date or 'none'} ({'in %d days' % days if days is not None else 'n/a'}); source: {dl_src or 'MISSING'}")
    print(f"Blockers ({len(blockers)}):", *blockers or ["none listed"], sep="\n  ")
    print(f"Guidance overdue or done without evidence ({len(overdue)}):", *overdue or ["none"], sep="\n  ")
    kinds: dict[str, int] = {}
    for x in markers:
        kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
    print("Open markers:", ", ".join(f"{k}={v}" for k, v in sorted(kinds.items())) or "none",
          f"| unverified feedback rows: {len(unverified)}")
    print(f"Signals: draft={draft} runs_last_14d={runs_recent} reviews={reviews}")
    for w in warn:
        print(f"WARN {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
