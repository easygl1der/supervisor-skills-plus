#!/usr/bin/env python3
"""Export Beamer \\note{...} bodies to Markdown (# Slide N).

Handles one-level nested braces. Comments are stripped first.

Usage: export_notes.py <file.tex> [notes.md]
"""

from __future__ import annotations

import sys
from pathlib import Path


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            out.append(line[i])
            i += 1
        lines.append("".join(out))
    return "\n".join(lines)


def extract_notes(text: str) -> list[str]:
    src = strip_comments(text)
    notes: list[str] = []
    needle = r"\note"
    i = 0
    while True:
        j = src.find(needle, i)
        if j < 0:
            break
        k = j + len(needle)
        while k < len(src) and src[k].isspace():
            k += 1
        if k >= len(src) or src[k] != "{":
            i = j + len(needle)
            continue
        depth = 0
        start = k + 1
        p = k
        while p < len(src):
            ch = src[p]
            if ch == "\\" and p + 1 < len(src):
                p += 2
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    notes.append(src[start:p].strip())
                    i = p + 1
                    break
            p += 1
        else:
            break
    return notes


def to_markdown(notes: list[str]) -> str:
    if not notes:
        return "# Speaker notes\n\n(no \\note{} found)\n"
    parts = ["# Speaker notes", ""]
    for n, body in enumerate(notes, start=1):
        parts.append(f"# Slide {n}")
        parts.append("")
        parts.append(body)
        parts.append("")
    return "\n".join(parts)


def main(argv: list[str]) -> int:
    if not argv or argv[0].startswith("-"):
        print("usage: export_notes.py <file.tex> [notes.md]", file=sys.stderr)
        return 2
    tex = Path(argv[0])
    if not tex.is_file():
        print(f"export_notes: not found: {tex}", file=sys.stderr)
        return 2
    md = to_markdown(extract_notes(tex.read_text()))
    if len(argv) >= 2:
        Path(argv[1]).write_text(md)
        print(f"export_notes: wrote {argv[1]}")
    else:
        sys.stdout.write(md)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
