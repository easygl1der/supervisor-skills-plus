---
name: sv-write-humanize-audit
description: >-
  Runs the report-only de-AI audit: S1 to S7 scores, the five tests
  (topic-sentence, movability, asymmetry, falsifier, deletion), a gate
  verdict, and a finding list where every finding carries an edit class for
  sv-review-loop. Never edits. Use when the user wants a de-AI gate before
  review or submission, or when sv-review-loop runs its language round.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-humanize-audit

The `audit` mode of the de-AI core (formerly `deai-writing`). Load
`core.md`, follow its Step 0, and run only `audit`. The profile follows
the inference rules in `patterns.md` section 8 (academic for manuscripts,
slides for Beamer frames, academic-response for response letters).

Finding ids are `DA-<nn>` within one run; each row has location, syndrome
or pattern, severity (P0, P1, P2), rule source, proposed edit and edit
class (`authorized-if-run`, `needs-author`, `report-only`). `sv-review-loop`
decides which `authorized-if-run` findings to apply.

See: ../sv-write/references/humanize/core.md
See: ../sv-write/references/humanize/diagnosis-and-modes.md
See: ../sv-write/references/humanize/patterns.md

## Hand-offs

- Applying findings: `sv-review-loop`, or the matching humanize sub-command.
