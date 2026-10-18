---
name: sv-figure-html
description: >-
  Produces SVG or HTML figures with the vendored offline kit: copy a
  template, edit its data block, render to PNG in headless Chrome, inspect,
  and save the HTML and PNG together. Covers explainer pages, steppers, DAGs
  and mind maps for papers, slides or the web, and figures in a Claude
  Design style. Use when the user wants an SVG, HTML or interactive figure
  rather than a plot or TikZ.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-figure-html

Uses the kit that `sv-figure-explain` owns (formerly the `study` kit, ADRs
0007 to 0011). The template table, content rules, visual tokens and the
render-and-inspect loop are in `visuals.md`; apply them to paper or slide
figures as well as study figures.

1. `python skills/sv-figure-explain/scripts/newfig.py --list`, then
   `newfig.py <template> <out.html>` (it fixes the vendor paths).
2. Edit the data block at the top of the copy.
3. Render: `skills/sv-figure-explain/kit/render.sh <out.html>` (first run:
   `npm i` in the kit folder); look at the PNG; fix; ship only at exit 0.

See: ../sv-figure-explain/references/visuals.md
See: ../sv-figure/references/design-rules.md

For a Claude Design artifact rather than a file in the repository, use the
host's design tooling; this sub-command covers files in the project.

## Hand-offs

- Learning figures inside study notes: `sv-figure-explain`.
- Paper figure design choices: `sv-figure-design`.
