---
name: sv-feedback-guidance
description: >-
  Records expert guidance on a paper or experiment as a dated guidance
  record: the scenario shown, verbatim quotes, the interpretation marked as
  such, points to notice, actions with owners, due dates and done criteria,
  and the decision; later lists open, overdue and unevidenced actions. Use
  when advice arrives from a meeting, call or relayed message, or to check
  which advice was followed up.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-feedback-guidance

Mode B of the former `feedback-to-revision`. Load
`../sv-feedback/references/procedure.md`, follow its Step 0, then run
section "Mode B: Guidance" (steps 1 to 8) with `guidance-mode.md`.

Records go to `docs/guidance/YYYY-MM-DD-<role>-<topic>.md` from the
research-core `guidance-record.md` template. Follow-up check, from the
repository root:

`python skills/sv-feedback/scripts/guidance_review.py <project_dir>`

See: ../sv-feedback/references/procedure.md
See: ../sv-feedback/references/guidance-mode.md

## Hand-offs

- Actions that change the manuscript: `sv-feedback-revise`.
- Decisions that set a rule: `research-records` (ADR).
