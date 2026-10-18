---
name: sv-slides
description: >-
  Entry point for LaTeX Beamer decks for math and statistics group meetings:
  a weekly report that carries last week's next steps forward, or a critical
  paper talk with estimand, identification and reproducibility slides,
  compiled, linted and rendered. Routes to one sv-slides sub-command and
  says which. Use when the user needs group-meeting slides.
license: CC-BY-NC-SA-4.0
---

# sv-slides

Router of the slides group (ADR 0021). The full procedure, unchanged from
the former `group-beamer`, is `references/procedure.md` (modes, audience,
Step 0, workflow, accumulation, checklist); themes and skeletons are in
`templates/`, the compile loop in `scripts/`, real runs in `evals/`.

| The user says | Sub-command |
|---|---|
| weekly report, progress report, this week's slides | `sv-slides-weekly` |
| present this paper, paper talk, journal club | `sv-slides-talk` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md

## Hand-offs outside this group

- De-AI audit of the deck: `sv-write-humanize-slides`.
- Figures: `sv-figure`.
- The meeting log: `sv-supervisor-records`.
