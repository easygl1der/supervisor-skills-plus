---
name: sv-slides
description: >-
  Entry point for LaTeX Beamer decks for math and statistics group meetings:
  a 6 to 10 slide weekly report that loads last week's next steps, or a 12
  to 18 slide critical paper talk with estimand, identification and
  reproducibility slides. Compiles, lints, renders and exports notes.
  Routes to one sv-slides sub-command and says which. Use when the user
  needs group-meeting slides, a weekly report deck or a paper talk.
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
