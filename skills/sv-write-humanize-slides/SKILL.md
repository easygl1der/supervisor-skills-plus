---
name: sv-write-humanize-slides
description: >-
  Removes machine-written texture from slide decks: frame titles and bodies
  use the slides profile (one hedge per claim, a selling point stated once
  per deck, no slogan closers, title verbs at or below the evidence level),
  while Beamer note text uses the academic profile. Use when a Beamer or
  other deck reads as AI-generated, or when the group-meeting deck skill
  calls for its de-AI audit.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-humanize-slides

The de-AI core (formerly `deai-writing`) with the **`slides`** profile for
frames and **`academic`** for `\note{}` text, as defined in `patterns.md`
section 8. A `.tex` file with `\documentclass{beamer}` or `\begin{frame}`
is inferred as slides.

Load `core.md` and follow its Step 0. Default mode is `audit` (what
`group-beamer` calls); `section` edits named frames when the user asks for
edits.

See: ../sv-write/references/humanize/core.md
See: ../sv-write/references/humanize/patterns.md
See: ../sv-write/references/humanize/editing-contract.md
See: ../sv-write/references/humanize/diagnosis-and-modes.md

## Hand-offs

- Building or restructuring the deck: `group-beamer`.
- Figures that look generated: `sv-figure-design`.
