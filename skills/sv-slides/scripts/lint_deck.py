#!/usr/bin/env python3
"""Static checks for a sv-slides .tex deck.

Fails on overlay commands, more than 7 bullets or 2 boxes in a frame,
\\tiny, or a text-only share above 30%. A frame containing the comment
"% gb:text-ok <reason>" (a discussion or decision slide) is not counted as
text-only.

Usage:
  lint_deck.py <file.tex>
  lint_deck.py --selftest
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

OVERLAY_CMD = re.compile(r"\\(pause|onslide|only|uncover)\b")
OVERLAY_SPEC = re.compile(r"\\(item|begin\{frame\}|frametitle)<[^>]+>")
TINY = re.compile(r"\\tiny\b")
FRAME_SPLIT = re.compile(r"\\begin\{frame\b")
ITEM = re.compile(r"\\item\b")
BOX = re.compile(
    r"\\begin\{(block|alertblock|exampleblock|beamerboxesrounded|tcolorbox)\}"
)
SUBSTANTIVE = re.compile(
    r"\\begin\{(?:equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|"
    r"tabular|tikzpicture|theorem|lemma|proposition|definition|"
    r"algorithm|figure)\}"
    r"|\\\["
    r"|\\includegraphics"
    r"|\\begin\{columns\}"
)


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


def frames(text: str) -> list[str]:
    parts = FRAME_SPLIT.split(text)
    if len(parts) <= 1:
        return []
    bodies = []
    for part in parts[1:]:
        end = part.find(r"\end{frame}")
        bodies.append(part if end < 0 else part[:end])
    return bodies


def is_text_only(body: str) -> bool:
    return SUBSTANTIVE.search(body) is None


TEXT_OK = "GBTEXTOKMARK"  # survives comment stripping


def lint(text: str) -> list[str]:
    # "% gb:text-ok <reason>" exempts a discussion or decision frame from the text-only share
    src = strip_comments(text.replace("% gb:text-ok", TEXT_OK + "%"))
    errors: list[str] = []
    for m in OVERLAY_CMD.finditer(src):
        errors.append(f"overlay command \\{m.group(1)}")
    for m in OVERLAY_SPEC.finditer(src):
        errors.append(f"overlay spec on \\{m.group(1)}")
    for m in TINY.finditer(src):
        errors.append(r"\tiny is banned")
    fr = frames(src)
    if not fr:
        errors.append("no frames found")
        return errors
    text_only = 0
    for i, body in enumerate(fr, start=1):
        n_item = len(ITEM.findall(body))
        n_box = len(BOX.findall(body))
        if n_item > 7:
            errors.append(f"frame {i}: {n_item} bullets (max 7)")
        if n_box > 2:
            errors.append(f"frame {i}: {n_box} boxes (max 2)")
        if is_text_only(body) and TEXT_OK not in body:
            text_only += 1
    share = text_only / len(fr)
    if share > 0.30 + 1e-9:
        errors.append(
            f"text-only share {text_only}/{len(fr)} = {share:.0%} (max 30%)"
        )
    return errors


def selftest() -> int:
    bad = r"""
\begin{frame}{A}
\pause
\item a\item b\item c\item d\item e\item f\item g\item h
\begin{block}{x}y\end{block}
\begin{block}{x}y\end{block}
\begin{block}{x}y\end{block}
\tiny hi
\end{frame}
\begin{frame}{B}
only text
\end{frame}
"""
    err = lint(bad)
    assert any("pause" in e for e in err)
    assert any("bullets" in e for e in err)
    assert any("boxes" in e for e in err)
    assert any("tiny" in e for e in err)
    assert any("text-only" in e for e in err)
    good = r"""
\begin{frame}{A}
\begin{equation*} a=1 \end{equation*}
\end{frame}
\begin{frame}{B}
\includegraphics{x}
\end{frame}
\begin{frame}{C}
\begin{tabular}{c}1\end{tabular}
\end{frame}
\begin{frame}{D}
plain
\end{frame}
"""
    err2 = lint(good)
    assert err2 == [], err2
    # two text-only frames of four fail (50%), unless the discussion frame is marked (25%)
    disc = "\\begin{frame}{A}\\begin{tabular}{c}1\\end{tabular}\\end{frame}\n\\begin{frame}{C}\\begin{tabular}{c}2\\end{tabular}\\end{frame}\n\\begin{frame}{B}x\\end{frame}\n\\begin{frame}{Q}%s\nWhat next?\\end{frame}\n"
    assert any("text-only" in e for e in lint(disc % ""))
    assert lint(disc % "% gb:text-ok discussion question") == []
    print("lint_deck: selftest ok")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if len(argv) != 1 or argv[0].startswith("-"):
        print("usage: lint_deck.py <file.tex> | --selftest", file=sys.stderr)
        return 2
    path = Path(argv[0])
    if not path.is_file():
        print(f"lint_deck: not found: {path}", file=sys.stderr)
        return 2
    errors = lint(path.read_text())
    if errors:
        print(f"lint_deck: {len(errors)} violation(s)")
        for e in errors:
            print(f"  {e}")
        return 1
    print("lint_deck: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
