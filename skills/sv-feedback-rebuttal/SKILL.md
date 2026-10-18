---
name: sv-feedback-rebuttal
description: >-
  Provides actionable peer-review rebuttal guidance, not finished rebuttal
  prose: inventories and classifies concerns, matches the reviewer mindset
  and strategy on ML venues, gives per-concern plans with evidence pointers,
  and picks a conference, journal or internal response format. Use when the
  user pastes reviewer comments, asks how to respond to a reviewer, needs a
  journal revision letter plan, or says the reviewer ignored the rebuttal.
disable-model-invocation: true
---

# sv-feedback-rebuttal

Formerly `rebuttal-guidance`. The full procedure, unchanged, is
`references/procedure.md`. Load it and follow its Step 0; when the round's
response table `docs/feedback/<round>.md` from `sv-feedback-revise`
exists, it is the inventory.

## Load by step

| Step | Load |
|---|---|
| 2, classify concerns | `concern-classification.md` |
| 3, reviewer mindset (ML venues only) | `mindset-matching-heuristics.md`, `mindset-library.md` |
| 4, strategy priorities (ML venues only) | `strategy-dimensions.md` |
| 5, per-concern plans | `response-templates.md` |
| 6, integrity gate | `checklist.md` |
| Format: conference, journal, internal | `response-formats.md` |

Other venues skip Steps 3 and 4 and use the venue-neutral formats.

See: references/procedure.md
See: references/concern-classification.md
See: references/mindset-matching-heuristics.md
See: references/mindset-library.md
See: references/strategy-dimensions.md
See: references/response-templates.md
See: references/checklist.md
See: references/response-formats.md

## Hand-offs

- Building the response table first: `sv-feedback-revise`.
- De-AI on the letter the author wrote: `sv-write-humanize-letter`.
