---
name: sv-quickread
description: >-
  Entry point for quick reads of one paper: a one-page, five-minute card in
  nine fixed sections with sourced results, graded contributions and a
  claim-evidence table, optionally with a Style Card of its writing. Routes
  to one sv-quickread sub-command and says which. Use when the user hands
  over one paper and wants its gist quickly.
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
- Several papers, a map or a survey: `sv-litreview`.
- Using it in the project: `sv-study-bridge`.
