#!/usr/bin/env python3
"""List reviewer markers in LaTeX sources, including hidden ones.

Usage:
    python list_markers.py <paper_dir> [--macros todo,seniorA] [--json]

Reports, per .tex file:
- live markers: \\<macro>{...}
- commented-out markers: % ... \\<macro>{...}   (a note hidden, not resolved)
- markers inside \\iffalse ... \\fi blocks
- note-display switches such as \\shownotesfalse / \\notesfalse
- PARKED comments (%% PARKED ...)

Macros default to the comment macros in research.yaml `people[].comment_macro`
when a research.yaml is found in <paper_dir> or its parents, else `todo`.
Exit code 0 always; this is a report, not a gate.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def macros_from_yaml(start: Path) -> list[str]:
    for d in [start, *start.parents]:
        y = d / "research.yaml"
        if y.exists():
            found = re.findall(r"comment_macro:\s*['\"]?\\\\?\\?([A-Za-z]+)", y.read_text())
            if found:
                return found
    return ["todo"]


def scan(path: Path, macros: list[str]) -> list[dict]:
    out = []
    pat = re.compile(r"\\(" + "|".join(map(re.escape, macros)) + r")\s*\{")
    in_iffalse = 0
    for no, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        stripped = line.lstrip()
        if re.match(r"\\iffalse\b", stripped):
            in_iffalse += 1
        if re.search(r"\\(shownotes|notes|todos)false\b", line) and not stripped.startswith("%"):
            out.append({"file": str(path), "line": no, "kind": "notes-hidden", "text": line.strip()[:160]})
        if re.match(r"%+\s*PARKED", stripped):
            out.append({"file": str(path), "line": no, "kind": "parked", "text": stripped[:160]})
        for m in pat.finditer(line):
            pct = line.find("%")
            commented = pct != -1 and pct < m.start() and (pct == 0 or line[pct - 1] != "\\")
            kind = "commented-out" if commented else ("in-iffalse" if in_iffalse else "live")
            out.append({"file": str(path), "line": no, "kind": kind, "macro": m.group(1),
                        "text": line[m.start():m.start() + 160].strip()})
        if re.match(r"\\fi\b", stripped) and in_iffalse:
            in_iffalse -= 1
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paper_dir")
    ap.add_argument("--macros", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = Path(a.paper_dir).resolve()
    macros = a.macros.split(",") if a.macros else macros_from_yaml(root)
    rows = []
    for tex in sorted(root.rglob("*.tex")):
        rows += scan(tex, macros)
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["kind"]] = counts.get(r["kind"], 0) + 1
        rel = Path(r["file"]).relative_to(root)
        print(f"{r['kind']:14} {rel}:{r['line']}  {r['text']}")
    print("summary:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "no markers",
          f"(macros: {', '.join(macros)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
