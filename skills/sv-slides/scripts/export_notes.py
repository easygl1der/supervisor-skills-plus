#!/usr/bin/env python3
"""Export Beamer \\note{...} bodies to Markdown (## Slide N, N = frame number).

Handles one-level nested braces. Comments are stripped first.

Usage: export_notes.py <file.tex> [notes.md]
       export_notes.py --selftest
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


ESCAPES = {r"\#": "#", r"\%": "%", r"\&": "&", r"\_": "_", r"\$": "$", r"\{": "{", r"\}": "}"}


def unescape(s: str) -> str:
    for k, v in ESCAPES.items():
        s = s.replace(k, v)
    return s


def extract_notes(text: str) -> list[tuple[int, str]]:
    """Return (frame number, note) pairs; frames without notes are skipped, not renumbered."""
    src = strip_comments(text)
    notes: list[tuple[int, str]] = []
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
                    frame = src.count(r"\begin{frame}", 0, j)
                    notes.append((frame, unescape(src[start:p].strip())))
                    i = p + 1
                    break
            p += 1
        else:
            break
    return notes


def to_markdown(notes: list[tuple[int, str]]) -> str:
    if not notes:
        return "# Speaker notes\n\n(no \\note{} found)\n"
    parts = ["# Speaker notes", ""]
    last = None
    for frame, body in notes:
        if frame != last:  # two notes in one frame stay under one heading
            parts.append(f"## Slide {frame}")
            parts.append("")
            last = frame
        parts.append(body)
        parts.append("")
    return "\n".join(parts)


def selftest() -> int:
    src = (
        "\\begin{frame}\\titlepage\\note{open}\\end{frame}\n"
        "\\begin{frame}{No note}x\\end{frame}\n"
        "% \\note{commented out}\n"
        "\\begin{frame}{R}\\note{PR \\#1 at 50\\% {nested}}\\note{second}\\end{frame}\n"
    )
    notes = extract_notes(src)
    assert notes == [(1, "open"), (3, "PR #1 at 50% {nested}"), (3, "second")], notes
    md = to_markdown(notes)
    assert "## Slide 3" in md and "## Slide 2" not in md and md.count("## Slide 3") == 1
    print("export_notes: selftest ok")
    return 0


def main(argv: list[str]) -> int:
    if argv and argv[0] == "--selftest":
        return selftest()
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
