#!/usr/bin/env python3
"""Render a TikZ snippet through a standalone wrapper and write a PNG for review.

Generalized from the owner's former local skill `tikz-diagram-review`.
No fixed install path, no fixed TeX engine, optional manuscript preamble.

Usage:
  python render_tikz.py tikz/figures/<name>.tex
  python render_tikz.py fig.tex --workspace path/to/tikz --engine pdflatex \
      --preamble paper/preamble.tex --dpi 300

Layout created under the workspace (default: ./tikz relative to the cwd):
  figures/  wrappers/  rendered/  review/

Needs latexmk (or the chosen engine on PATH) and pdftoppm (poppler).
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_PREAMBLE = r"""\documentclass[tikz,border=6pt]{standalone}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathreplacing,fit,backgrounds}
"""

REVIEW_TEMPLATE = """# {name} review

Purpose (one sentence):

Rendered PNG: `{png}`

Checklist:

- [ ] No label overlaps another label, arrow, axis or region boundary
- [ ] Symbols and names match the prose definitions
- [ ] Regions are distinguishable; colour is not the only cue
- [ ] Line weights and text readable at manuscript scale (close to body size)
- [ ] No important label close to the canvas edge
- [ ] The figure answers the stated purpose

Verdict:

Remaining risk:
"""


def run(cmd: list[str], cwd: Path) -> None:
    proc = subprocess.run(cmd, cwd=cwd)
    if proc.returncode != 0:
        raise SystemExit(f"command failed ({proc.returncode}): {' '.join(cmd)}")


def build_wrapper(snippet: Path, wrapper_dir: Path, preamble: Path | None, cjk: bool) -> str:
    rel = os.path.relpath(snippet, wrapper_dir).replace("\\", "/")
    parts = [BASE_PREAMBLE]
    if cjk:
        parts.append("\\usepackage[UTF8]{ctex}\n")
    if preamble is not None:
        pre_rel = os.path.relpath(preamble, wrapper_dir).replace("\\", "/")
        parts.append(f"\\input{{{pre_rel}}}\n")
    parts.append("\\begin{document}\n")
    parts.append(f"\\input{{{rel}}}\n")
    parts.append("\\end{document}\n")
    return "".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tikz_file", help="TikZ snippet (.tex) holding a tikzpicture or a small macro")
    ap.add_argument("--workspace", default="tikz", help="workspace directory (default ./tikz)")
    ap.add_argument("--engine", default="pdflatex", choices=["pdflatex", "xelatex", "lualatex"])
    ap.add_argument("--preamble", help="optional file with the manuscript's macros and packages "
                    "(no \\documentclass, no \\begin{document})")
    ap.add_argument("--cjk", action="store_true", help="load ctex (use with --engine xelatex)")
    ap.add_argument("--dpi", type=int, default=220)
    args = ap.parse_args()

    snippet = Path(args.tikz_file).resolve()
    if not snippet.exists():
        raise SystemExit(f"missing TikZ file: {snippet}")
    preamble = Path(args.preamble).resolve() if args.preamble else None
    if preamble is not None and not preamble.exists():
        raise SystemExit(f"missing preamble file: {preamble}")

    ws = Path(args.workspace).resolve()
    dirs = {k: ws / k for k in ("figures", "wrappers", "rendered", "review")}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    name = snippet.stem
    wrapper = dirs["wrappers"] / f"{name}.tex"
    wrapper.write_text(build_wrapper(snippet, dirs["wrappers"], preamble, args.cjk), encoding="utf-8")

    if shutil.which("latexmk"):
        cmd = ["latexmk", f"-{args.engine}" if args.engine != "pdflatex" else "-pdf",
               "-interaction=nonstopmode", "-file-line-error", "-halt-on-error", wrapper.name]
    elif shutil.which(args.engine):
        cmd = [args.engine, "-interaction=nonstopmode", "-file-line-error", "-halt-on-error", wrapper.name]
    else:
        raise SystemExit(f"neither latexmk nor {args.engine} found on PATH")
    run(cmd, cwd=dirs["wrappers"])

    built = dirs["wrappers"] / f"{name}.pdf"
    if not built.exists():
        raise SystemExit(f"expected PDF was not produced: {built}")
    pdf = dirs["rendered"] / f"{name}.pdf"
    shutil.copyfile(built, pdf)

    png = dirs["rendered"] / f"{name}.png"
    if shutil.which("pdftoppm"):
        run(["pdftoppm", "-png", "-singlefile", "-r", str(args.dpi), str(pdf),
             str(dirs["rendered"] / name)], cwd=ws)
    else:
        print("warning: pdftoppm not found; PNG not written, inspect the PDF", file=sys.stderr)

    review = dirs["review"] / f"{name}-review.md"
    if not review.exists():
        review.write_text(REVIEW_TEMPLATE.format(name=name, png=png), encoding="utf-8")

    print(f"wrapper: {wrapper}")
    print(f"pdf:     {pdf}")
    print(f"png:     {png}")
    print(f"review:  {review}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
