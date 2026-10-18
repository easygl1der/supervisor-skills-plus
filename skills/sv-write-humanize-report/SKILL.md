---
name: sv-write-humanize-report
description: >-
  Removes machine-written texture from reports: weekly and progress reports,
  STATUS and other files under docs/ use the docs profile (clarity over
  voice); technical reports for outside readers use the academic profile.
  Same diagnosis and editing contract as the paper sub-command, so numbers,
  citations and terms stay protected. Use when a report, status update or
  project document reads as AI-generated.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-humanize-report

The de-AI core (formerly `deai-writing`) applied to reports. Load `core.md`
and follow its Step 0. Pick the profile from the tolerance matrix in
`patterns.md` section 8 and say which one was used:

| Text | Profile |
|---|---|
| weekly or progress report, meeting notes, STATUS, files under `docs/` | `docs` |
| technical report or white paper read outside the group | `academic` |
| public write-up of the work | `technical-blog` |

No report-specific profile exists beyond these; a rule the matrix does not
cover is reported, not invented.

Modes: `section` for one report or part of it, `full` for a long report,
`numbers` when the report carries results, `audit` for report-only.

See: ../sv-write/references/humanize/core.md
See: ../sv-write/references/humanize/diagnosis-and-modes.md
See: ../sv-write/references/humanize/editing-contract.md
See: ../sv-write/references/humanize/patterns.md

## Hand-offs

- Project records themselves (what STATUS should say): `research-records`.
- A paper-style text: `sv-write-humanize-paper`.
