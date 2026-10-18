---
name: sv-figure
description: >-
  Entry point for every figure task: design advice for a paper's core
  figures, reconstruction of a reference image as editable draw.io, plots
  from code in Python or R, TikZ figures, HTML or SVG figures, posters, and
  explanatory figures for learning. Routes each request to one sv-figure
  sub-command and says which. Use when the user asks to design, draw, plot,
  rebuild, review or explain anything visual.
license: CC-BY-NC-SA-4.0
---

# sv-figure

## Overview

Router of the figure group (ADR 0021). It picks one sub-command, says so in
one line ("Routing to `sv-figure-plot`: results figure from data."), loads
that sub-command's SKILL.md and follows it. Sub-commands can also be called
directly; they are not auto-selected.

## Routing table

| The user says | Sub-command |
|---|---|
| design Figure 1, the method overview, or the results figures; review a figure | `sv-figure-design` |
| rebuild this image, screenshot or sketch as draw.io | `sv-figure-drawio` |
| plot this data, matplotlib, seaborn, R, a results chart from code | `sv-figure-plot` |
| TikZ or PGFPlots figure for LaTeX | `sv-figure-tikz` |
| SVG or HTML figure, interactive figure, a figure in Claude Design style | `sv-figure-html` |
| poster | `sv-figure-poster` |
| explain a concept with a picture, a diagram for study notes | `sv-figure-explain` |

## Shared references

`references/design-rules.md` (universal rules), `references/tools.md`
(tool matrix) and `references/archive-figure-rules.md` (rules learned from
the evidence project) apply to every sub-command.

See: references/design-rules.md
See: references/tools.md
See: references/archive-figure-rules.md

## Hand-offs outside this group

- Numbers shown in a figure: `experiment-workflow` (traceable numbers).
- Figure-related writing (captions in prose, results text): `sv-write`.
- Slides: `group-beamer`.
