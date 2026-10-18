---
name: sv-quickread
description: >-
  Entry point for quick reads of a single paper: a one-page, five-minute
  card in nine fixed sections with results copied with sources, graded
  contributions and a claim-evidence table, and optionally a Style Card of
  the paper's writing for venue profiles. Routes to one sv-quickread
  sub-command and says which. Use when the user hands over one paper and
  wants to know quickly what it says.
license: CC-BY-NC-SA-4.0
---

# sv-quickread

Router of the quick-read group (ADR 0021). The full procedure, unchanged
from the former `paper-quickread`, is `references/procedure.md`; its
scripts are `scripts/check_quickread.py` and `scripts/index_append.py`.

| The user says | Sub-command |
|---|---|
| quick read, what does this paper say, triage, a card for the literature map | `sv-quickread-card` |
| also dissect its writing, a style card, --style | `sv-quickread-style` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md

## Hand-offs outside this group

- Depth on one part of the paper: `sv-study-paper`.
- Several papers, a map or a survey: `deep-research`.
- Using it in the project: `sv-study-bridge`.
