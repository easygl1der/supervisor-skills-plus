---
name: sv-figure-tikz
description: >-
  Builds TikZ and PGFPlots figures for LaTeX papers and decks in a
  render-and-inspect loop: a standalone render to PDF and PNG, inspection of
  the PNG for overlaps, clipping and legibility, a short review note, and
  done only when the inspection is recorded. Follows the universal figure
  rules. Use when the user wants a TikZ or PGFPlots figure written, fixed,
  or reviewed.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-figure-tikz

The TikZ loop formerly inside `figure-designer`. Load `tikz-review.md` and
follow it; render with, from the repository root:

`python skills/sv-figure-tikz/scripts/render_tikz.py <tikz_snippet.tex>`

Run `--help` first for the options the script accepts.

See: references/tikz-review.md
See: ../sv-figure/references/design-rules.md
See: ../sv-figure/references/tools.md

## Hand-offs

- Design choices before drawing: `sv-figure-design`.
- Beamer decks: `group-beamer`.
