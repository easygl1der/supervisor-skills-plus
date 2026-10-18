# TikZ render-and-inspect loop

Folded in from the owner's former local skill `tikz-diagram-review`
[src: skill:tikz-diagram-review] (confirmed). The script is vendored as
`scripts/render_tikz.py` and generalized: no fixed install path, choice of
TeX engine, optional manuscript preamble, ctex only on request.

## Contents
1. Core rule
2. Workspace layout
3. Loop
4. What to inspect on the PNG
5. Style
6. Done means inspected

## 1. Core rule

Do not recompile a large manuscript to check one TikZ figure. Develop the
figure in a small project-local workspace, render it standalone, inspect the
image, and only then include it in the paper. A TikZ figure is not done when
it compiles; it is done when the rendered image has been checked.

## 2. Workspace layout

```text
tikz/
  figures/<name>.tex        the tikzpicture only (or a small macro)
  wrappers/<name>.tex       generated standalone wrapper
  rendered/<name>.pdf|.png  render output
  review/<name>-review.md   purpose, PNG path, verdict, remaining risk
```

The manuscript includes only the stable source:
`\input{tikz/figures/<name>.tex}`. Add `tikz/wrappers/` and the PNGs to the
ignore file if the repository keeps only figure sources (one source per
figure, FR15 in `archive-figure-rules.md`).

## 3. Loop

1. State the figure's purpose in one sentence, for example "the full region
   is the union of the cut-off square and two strips". Write it in the
   review note.
2. Write `tikz/figures/<name>.tex`.
3. Render:

   ```bash
   python "$SKILL_DIR/scripts/render_tikz.py" tikz/figures/<name>.tex \
       [--engine pdflatex|xelatex|lualatex] [--preamble paper/macros.tex] \
       [--cjk] [--dpi 300] [--workspace tikz]
   ```

   `$SKILL_DIR` is the directory of this skill as resolved by the runtime.
   Use `--preamble` when the figure uses manuscript macros; the file holds
   `\usepackage` and `\newcommand` lines only. Requires `latexmk` (or the
   engine) and `pdftoppm`; without `pdftoppm` the script still writes the
   PDF and warns.
4. Open the PNG (image viewer or the Read tool) and run the inspection in
   section 4.
5. Revise and re-render until the inspection passes.
6. Fill the review note: purpose, PNG path, verdict, remaining risk.
7. Insert the figure in the manuscript and compile the manuscript once.
8. Re-check font size on the compiled page after every late edit or scale
   change (`\resizebox`, `width=`), because scaling changes the effective
   font size.

## 4. What to inspect on the PNG

- Labels do not overlap each other, arrows, axes or region boundaries.
- Mathematical symbols and names match the prose definitions exactly.
- Regions are distinguishable without colour (pattern, line style, label);
  colour is never the only cue.
- Line weights and text stay readable at the manuscript scale.
- No important label sits close to the canvas edge.
- The figure answers the purpose sentence; the reader can tell what space
  is drawn, what each marked region means, and which step of the argument it
  supports.

## 5. Style

- Explain unfamiliar encodings in the caption or the text next to the figure.
- Use explicit coordinates and stable geometry; do not rely on accidental
  spacing.
- Put long labels outside the drawing or split them with `align=center`.
- Muted fills, high-contrast borders.
- Label only meaningful tick values.
- For proof diagrams: show the set relationship first, then the estimate.

## 6. Done means inspected

Record in the review note: the PNG was opened, each item in section 4 was
checked, and the result. A figure whose PNG was never opened is reported as
`unknown` for the clarity checks, not `pass`.
