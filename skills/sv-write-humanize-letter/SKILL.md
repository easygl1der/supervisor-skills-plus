---
name: sv-write-humanize-letter
description: >-
  Removes machine-written texture from letters and applications: response
  letters, rebuttals and emails to advisors use the academic-response
  profile (version narration expected, one polite opener allowed);
  proposals and grant applications use the academic profile. Same
  protected-content contract as the paper sub-command. Use when a rebuttal,
  response letter, email, proposal or grant text reads as AI-generated.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-humanize-letter

The de-AI core (formerly `deai-writing`) applied to letters. Load `core.md`
and follow its Step 0. Profiles come from `patterns.md` section 8:

| Text | Profile |
|---|---|
| response letter, rebuttal | `academic-response` |
| email to an advisor or co-author | `academic-response` (closest existing profile; no email profile is defined) |
| thesis proposal, research plan, grant application | `academic` |

Say which profile was used. Modes: `section` for one letter or one part of
a proposal, `full` for a whole proposal, `audit` for report-only.

See: ../sv-write/references/humanize/core.md
See: ../sv-write/references/humanize/patterns.md
See: ../sv-write/references/humanize/editing-contract.md
See: ../sv-write/references/humanize/diagnosis-and-modes.md

## Hand-offs

- Rebuttal strategy and content: `sv-feedback-rebuttal`.
- Proposal content: `sv-proposal`.
- Point-by-point comment handling: `sv-feedback-revise`.
