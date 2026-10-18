---
name: sv-study-visual-explain
description: >-
  Draws the motivation or structure figure for the concept being studied,
  as the study protocol's picture step: picks a kit template, fills it from
  the session's content without inventing numbers, renders and inspects it,
  and saves the HTML and PNG next to the notes. A thin entry to the figure
  group's explain sub-command. Use when a study session needs a picture.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-study-visual-explain

The kit and its rules live in `sv-figure-explain` (ADR 0021); this entry
only keeps the study context. Load `../sv-figure-explain/SKILL.md` and
follow it, with these study defaults from step 4 "Draw" of
`../sv-study/references/procedure.md`:

- at most one motivation figure and one structure figure per concept;
- a stepper only for content with an order (derivations, algorithms,
  processes);
- render, look, fix, at most three rounds; numbers need a source or the
  label "illustrative";
- save the figure in the session's folder and embed the PNG in the notes.

See: ../sv-figure-explain/references/visuals.md
See: ../sv-study/references/procedure.md
