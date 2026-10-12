#!/usr/bin/env python3
"""Create a LaTeX scaffold for a mathematics or theory paper.

Adapted from the owner's former `paper` skill (skill:paper). Change from the
original: main.tex now inputs one file per section from sections/.
Refuses to overwrite existing files.

Usage: python scaffold_paper.py <dir> [--title "Paper Title"] [--author "Name"]
"""
import argparse
from pathlib import Path

MAIN_TEX = r"""\documentclass[11pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage[nameinlink,capitalize]{cleveref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\title{TITLE_PLACEHOLDER}
\author{AUTHOR_PLACEHOLDER}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Write a concise abstract here.
\end{abstract}

\input{sections/introduction}
\input{sections/main-results}
\input{sections/proofs}

\bibliographystyle{alpha}
\bibliography{references}

\appendix
\input{sections/appendix}

\end{document}
"""

SECTIONS = {
    "introduction": "\\section{Introduction}\n\\label{sec:introduction}\n\n"
    "State the problem, context, and main contributions.\n",
    "main-results": "\\section{Main Results}\n\\label{sec:main-results}\n\n"
    "\\begin{theorem}\n\\label{thm:main}\nState the main theorem with all assumptions.\n"
    "\\end{theorem}\n\n\\begin{proof}[Proof idea]\nGive the proof strategy; "
    "the full proof is in \\cref{sec:proofs}.\n\\end{proof}\n",
    "proofs": "\\section{Proofs}\n\\label{sec:proofs}\n\n"
    "Develop supporting lemmas and proofs.\n",
    "appendix": "\\section{Appendix}\n\\label{app:appendix}\n\n"
    "Add long computations here.\n",
}

GITIGNORE = """build/
*.aux
*.bbl
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.synctex.gz
*.toc
"""


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a LaTeX paper scaffold.")
    parser.add_argument("target", help="Target paper directory")
    parser.add_argument("--title", default="Paper Title")
    parser.add_argument("--author", default="Author Name")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    for dirname in ("sections", "figures", "build"):
        (target / dirname).mkdir(exist_ok=True)

    main_tex = MAIN_TEX.replace("TITLE_PLACEHOLDER", args.title).replace(
        "AUTHOR_PLACEHOLDER", args.author
    )
    write_new(target / "main.tex", main_tex)
    for name, body in SECTIONS.items():
        write_new(target / "sections" / f"{name}.tex", body)
    write_new(target / "references.bib", "% Add BibTeX entries here.\n")
    write_new(target / ".gitignore", GITIGNORE)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
