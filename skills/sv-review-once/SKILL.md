---
name: sv-review-once
description: >-
  Runs a read-only pre-submission review of a technical paper across five
  dimensions (macro logic, writing details, English grammar, LaTeX
  formatting, figure quality) with CRITICAL, MAJOR and MINOR findings, then
  the research-core threats, double-blind, artifact, venue-submission and
  integrity checklists, a devil's-advocate pass, and the submission-day
  runbook. Use when the user asks to review, audit or proofread a paper
  before a deadline.
license: CC-BY-4.0
disable-model-invocation: true
---

# sv-review-once

Formerly `pre-submission-reviewer`. The full procedure, unchanged, is
`references/procedure.md`; load it and follow its Step 0 (name the commit
or PDF under review; every finding refers to that version).

## Pick the timing

| When | Run |
|---|---|
| three to five days before the deadline, or after a major rewrite | Steps 0b to 9 of the procedure, Output format |
| one day before the deadline | the same, read-only against a named commit and PDF; every Blocker becomes a TODO with an owner |
| submission day | the runbook only |

## Load by step

| Step | Load |
|---|---|
| 1 and 2, macro logic and writing details | `logic-and-structure.md` |
| 3, English grammar | `grammar-rules.md` |
| 4, LaTeX format | `latex-rules.md` |
| 5 and 6, figures and banned vocabulary | `forbidden-patterns.md` |
| 7, section by section | `section-guides.md` |
| 7b, devil's advocate | `devils-advocate-pass.md` |
| submission day | `submission-day-runbook.md` |

See: references/procedure.md
See: references/logic-and-structure.md
See: references/grammar-rules.md
See: references/latex-rules.md
See: references/forbidden-patterns.md
See: references/section-guides.md
See: references/devils-advocate-pass.md
See: references/submission-day-runbook.md

## Hand-offs

- Fixing findings over several rounds: `sv-review-loop`.
- Structure not settled yet: `sv-write-skeleton` or `sv-write-intro`.
- Comments arriving from co-authors or reviewers: `sv-feedback-revise`.
