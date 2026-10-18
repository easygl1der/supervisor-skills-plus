---
name: sv-figure-plot
description: >-
  Produces data and mathematical figures from code, saving the figure and
  the script together: Matplotlib or Seaborn in a reusable plotting script,
  Plotly for interactive views, vector output sized to the column, and
  numbers that trace to the project's numbers file. Applies the results
  figure guidance and universal rules. Use when the user wants a plot, chart
  or mathematical figure generated from data or a formula.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-figure-plot

Assembled from existing parts of the former `figure-designer` (ADR 0021);
it adds no new rules.

## Load

| Need | Load |
|---|---|
| Tool choice: Matplotlib and Seaborn (section 5), Plotly (section 7), what to avoid (section 9) | shared `tools.md` |
| Vector output, canvas and font size, colour | shared `design-rules.md` |
| Results figures: what to compare, layout, annotation | `../sv-figure-design/references/experimental-results.md` |
| Numbers on the figure | research-core `core/figures.md` and `core/integrity.md` (traceable numbers) |

See: ../sv-figure/references/tools.md
See: ../sv-figure/references/design-rules.md
See: ../sv-figure-design/references/experimental-results.md

## How to work

1. Read the data from the file the project names as its numbers source;
   never type numbers into the script.
2. Keep one reusable plotting script beside the figure (the `plot_utils.py`
   pattern in the design procedure) and save the figure as PDF or SVG.
3. Render, look at the output, fix, and say what was checked.

R (ggplot2) is accepted when the project already uses R; this library has
no R-specific rules yet, so only the universal rules apply.

## Hand-offs

- Design of the figure before plotting: `sv-figure-design`.
- Numbers that do not trace to a run: `experiment-workflow`.
