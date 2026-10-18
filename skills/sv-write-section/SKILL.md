---
name: sv-write-section
description: >-
  Drafts publishable paper prose from the author's own materials, from one
  paragraph to a full manuscript, across STEM and non-STEM fields. Builds the
  claim ledger before prose, traces every factual claim to user input,
  verified retrieval or field common knowledge, and runs the citation
  verification ladder. Use when the user asks to write a section, an
  abstract, turn results or notes into paper text, or draft a full paper.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-section

Formerly `paper-writer`. The full workflow, unchanged, is
`references/workflow.md` (Step 0, capability check, Phases 0 to 6, red
flags, literature searching, checklist). Load it first.

## Hard rules

1. Every factual claim comes from the user's materials, this session's
   verified retrieval, or field common knowledge that carries no numbers,
   names, or comparisons. Model memory is never a source.
2. Delivered prose contains zero bracketed placeholder tags.
3. Concrete details the user did not provide are not written.
4. Claim strength never exceeds evidence strength.
5. Real and planned results are phrased differently and never mixed.
6. Internal planning never leaks into the output.

## Load by task

| Task | Load |
|---|---|
| Any section | `workflow.md`; shared `evidence-discipline.md`, `prose-delivery.md` |
| Results, numbers or proofs in the text | Phase 0 claim ledger in `workflow.md` first |
| STEM sections other than the Introduction | `section-guidance.md` |
| Empirical study skeleton | shared `empirical-study-skeleton.md` |
| Theory or `field: math` | `math-paper.md`; `scripts/scaffold_paper.py` for a fresh folder |
| Review before delivery | `verification-checklist.md`; shared `verification-ladder.md` |
| Citations | shared `citation-style.md` |
| Introduction | stop: `sv-write-intro` |
| Benchmark paper not yet planned | stop: `sv-write-skeleton` |

See: references/workflow.md
See: references/section-guidance.md
See: references/math-paper.md
See: references/verification-checklist.md
See: ../sv-write/references/evidence-discipline.md
See: ../sv-write/references/prose-delivery.md
See: ../sv-write/references/verification-ladder.md
See: ../sv-write/references/citation-style.md
See: ../sv-write/references/empirical-study-skeleton.md

## Hand-offs

- After a draft: `sv-review-loop`, offered at the end of every full-section
  delivery.
- A light language pass: `sv-write-polish`; AI tone: `sv-write-humanize-paper`.
- Venue style from exemplars: `sv-write-style-apply`.
- Comments on the draft: `sv-feedback-revise`.
- The core claim may not hold: `sv-review-once` or `idea-evaluator`.
