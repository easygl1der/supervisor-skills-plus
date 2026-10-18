---
name: sv-review-loop
description: >-
  Runs a bounded multi-round check over a manuscript: research-writing fit
  first (claims, scope, hedges, numbers, threats), then venue and field
  style, then language through a de-AI audit, with a regression re-run of
  the research check. Applies only authorized edits, guards spans against
  reversion and locked-decision flips, and writes a dated round log. Use
  when a draft needs repeated checking before review, submission or
  camera-ready.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-review-loop

Formerly `check-loop`. The full procedure, unchanged, is
`references/procedure.md` (inputs, setup, round procedure, which edits
apply, oscillation guard, stop rules, round log). Load it and follow its
Step 0 and Setup.

## Each round

1. Research-writing fit (claims, scope, hedges, numbers, threats).
2. Venue and field style fit: `sv-write-style-apply` check mode.
3. Language and de-AI: `sv-write-humanize-audit`.
4. Regression: check 1 again on the spans check 3 changed.

Default budget is three rounds (`research.yaml` `check_loop.max_rounds`).
"Report only" means one round and no edits.

## Load

| Need | Load |
|---|---|
| Every run | `procedure.md`, `round-procedure.md` |
| Starting the log | `log-template.md` |
| Span guard between checks | `scripts/span_guard.py` (commands in `procedure.md`, Oscillation guard) |

See: references/procedure.md
See: references/round-procedure.md
See: references/log-template.md

## Hand-offs

- Submission gates (anonymity, artifact, template, forms): `sv-review-once`.
- Specific comments to resolve: `sv-feedback-revise`.
- One quick wording pass: `sv-write-polish`.
