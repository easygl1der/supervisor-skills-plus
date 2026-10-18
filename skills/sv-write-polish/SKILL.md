---
name: sv-write-polish
description: >-
  Polishes existing academic prose while preserving the author's meaning:
  grammar and flow repair, idiomatic wording, section conventions, tone
  calibration against evidence strength, and fair description of prior work.
  Light touch by default, one pass only, and every edit that could change
  scientific meaning is flagged. Use when the user asks to polish a draft,
  fix awkward wording, smooth a paragraph, or check whether a claim is too
  strong.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-polish

Formerly the language part of `paper-polish`. The full procedure, unchanged,
is `references/procedure.md`; the faithfulness rules it obeys are shared in
`../sv-write/references/faithfulness.md`. Load both, then follow the
procedure's Step 0.

## Scope of this sub-command

Does: one polishing pass (understand, find the real problem, edit, account
for the changes), the field- and venue-aware pass, section conventions,
calibration, fairness to prior work, delivery with three to five change
notes and a before/after list for meaning-risk edits.

Does not: Chinese-to-English rewriting (`sv-write-translate`), the full
de-AI contract (`sv-write-humanize-paper`), redrafting a broken section
(`sv-write-section`), repeated rounds (`sv-review-loop`).

## Load by need

| Need | Load |
|---|---|
| Every pass | `procedure.md`, shared `faithfulness.md` |
| Results, Methods, RQ transitions | `reader-logic.md` |
| Register per section | shared `section-conventions.md` |
| Verb strength and phrase alternatives | shared `academic-phrasebank.md` |
| Light AI-tone scan before delivery | shared `ai-tone-guardrails.md` |

See: references/procedure.md
See: references/reader-logic.md
See: ../sv-write/references/faithfulness.md
See: ../sv-write/references/section-conventions.md
See: ../sv-write/references/academic-phrasebank.md
See: ../sv-write/references/ai-tone-guardrails.md

## Hand-offs

- Chinese draft or heavy Chinese-English residue: `sv-write-translate`.
- Heavy AI tone, or a de-AI audit under the full contract:
  `sv-write-humanize-paper` or `sv-write-humanize-audit`.
- The section needs redrafting: `sv-write-section`.
- A claim the data may not support: `sv-review-once` or
  `sv-idea`.
- A re-check after these edits: `sv-review-loop`.
- Comments to work through: `sv-feedback-revise`.
