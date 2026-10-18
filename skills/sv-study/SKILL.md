---
name: sv-study
description: >-
  Entry point for understanding-first study: explains a single concept,
  works through a paper or a textbook chapter one idea at a time, has the
  learner restate each idea and diagnoses the restatement, draws
  explanatory figures, runs optional drills, and bridges what was learned to
  the current project. Keeps a learner profile in the study vault. Routes to
  one sv-study sub-command and says which. Use when the user wants to really
  understand something.
license: CC-BY-NC-SA-4.0
---

# sv-study

## Overview

Router of the study group (ADR 0021). It picks one sub-command, says so in
one line ("Routing to `sv-study-paper`: paper mode, official PDF first."),
loads that sub-command's SKILL.md and follows it. Sub-commands can also be
called directly; they are not auto-selected.

The shared study procedure, unchanged from the former `study` skill, is
`references/procedure.md` (Step 0, the protocol per concept, diagnosis,
save, checklist); the vault script is `scripts/vault.py`; real outputs are
in `evals/`.

See: references/procedure.md
See: references/protocol.md

## Routing table

| The user says | Sub-command |
|---|---|
| explain X, I want to understand X, a single concept with no material | `sv-study-quick-explain` |
| study this paper, close reading, a paper PDF or arXiv link | `sv-study-paper` |
| study chapter N, a textbook or lecture notes | `sv-study-chapter` |
| draw it, a picture for this concept | `sv-study-visual-explain` |
| quiz me, Socratic, Feynman, proof gaps, Anki | `sv-study-drill` |
| can I use this in my project, apply what I just read | `sv-study-bridge` |

## Hand-offs outside this group

- A five-minute card before studying: `sv-quickread`.
- Many papers into a map: `sv-litreview-map`.
- Testing a bridged idea: `sv-idea`, `sv-experiment`.
