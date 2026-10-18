---
name: sv-study-drill
description: >-
  Switches on one of the study drill options that are off by default:
  Socratic dialogue, Feynman explain-back, light self-test with confidence
  ratings, proof reconstruction with gaps for the learner, notes only, or
  Anki export of approved concept notes. High-confidence wrong answers go
  to the misconceptions file. Use when the user asks to be quizzed, tested,
  questioned Socratically, or to export cards.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-study-drill

The options of the former `study`. Load `options.md`, pick the option the
user named (`socratic`, `feynman`, `self-test`, `proof`, `notes-only`,
`anki`) and say which. Follow Step 0 and the save step of
`../sv-study/references/procedure.md`.

See: ../sv-study/references/options.md
See: ../sv-study/references/procedure.md
See: ../sv-study/references/session-save.md

Spaced review queues are not part of this library; the learner's own Anki
or review tool handles them.
