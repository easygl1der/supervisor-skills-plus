---
name: sv-figure-explain
description: >-
  Draws explanatory figures for learning: scene cards, four-panel comics,
  textbook and auto-laid-out DAGs, mind maps, explainer pages and steppers
  for proofs, algorithms and numeric processes, built from the vendored
  offline kit as HTML with SVG and KaTeX, rendered to PNG and inspected.
  Never invents numbers. Use when a concept, paper or chapter needs a
  picture in study notes, or the study skill asks for one.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-figure-explain

Owns the visual kit formerly in `study` (`kit/`, ADRs 0007 to 0011) and its
rules. `visuals.md` is the template table, content and visual rules, and
the render-and-inspect loop; `visual-scenarios.md` maps scenarios to
patterns.

1. Pick a template from `visuals.md` section 1 (at most two or three
   figures per concept).
2. `python skills/sv-figure-explain/scripts/newfig.py <template> <out.html>`
   next to the notes that embed it.
3. Edit the data block; render with `skills/sv-figure-explain/kit/render.sh`
   (`--full --figures`, `--steps [--gif]` as `visuals.md` says); inspect
   the PNG; save HTML and PNG together.

See: references/visuals.md
See: references/visual-scenarios.md

## Hand-offs

- The learning session itself: `sv-study`.
- Non-learning HTML figures: `sv-figure-html`.
