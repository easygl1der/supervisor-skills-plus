---
name: sv-litreview
description: >-
  Entry point for literature work: a survey-grade investigation with frozen
  questions, adversarial search, verified citations and a calibrated
  synthesis, or a literature map built from the cards and notes already
  read. Routes to one sv-litreview sub-command and says which. Use when the
  user needs a survey, related work, or a map of their reading.
license: CC-BY-NC-SA-4.0
---

# sv-litreview

Router of the literature group (ADR 0021). The full procedure, unchanged
from the former `deep-research`, is `references/procedure.md`.

| The user says | Sub-command |
|---|---|
| survey this topic, what is known about X, related work from scratch | `sv-litreview-survey` |
| map what I have read, find gaps among my cards, plan next reads | `sv-litreview-map` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md

## Hand-offs outside this group

- One paper quickly: `sv-quickread`; one paper in depth: `sv-study-paper`.
- A related-work section as paper prose: `sv-write-section`.
