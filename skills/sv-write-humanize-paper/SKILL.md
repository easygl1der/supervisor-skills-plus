---
name: sv-write-humanize-paper
description: >-
  Removes machine-written texture from a paper, thesis chapter or section
  under the academic profile: diagnoses restatement, defensiveness, false
  symmetry and reporting hygiene as S1 to S7 against a claim ledger, then
  edits only under the contract that protects numbers, citations, terms and
  LaTeX. Use when a manuscript reads as AI-generated and the user wants it
  diagnosed or rewritten, or its numbers cleaned up.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-humanize-paper

The de-AI core (formerly `deai-writing`) with the **`academic`** profile.
Load `core.md` and follow its Step 0, then run the mode below.

| User asks | Mode | Edits? |
|---|---|---|
| first contact, "how bad is it" | `diagnose` | No |
| "clean this section up" | `section` | Yes, one section |
| "rewrite the whole paper or chapter" | `full` | Yes, named files |
| numbers in prose look like a lab notebook | `numbers` | Presentation only |

Whole-paper order: `diagnose`, `full` (or `section` on the worst
sections), `numbers`, then `sv-write-humanize-audit` as the gate.

See: ../sv-write/references/humanize/core.md
See: ../sv-write/references/humanize/diagnosis-and-modes.md
See: ../sv-write/references/humanize/editing-contract.md
See: ../sv-write/references/humanize/patterns.md
See: ../sv-write/references/ai-tone-guardrails.md

## Hand-offs

- Report-only gate: `sv-write-humanize-audit`.
- Claims beyond the evidence or a missing ledger: `sv-write-section`.
- Grammar and fluency only: `sv-write-polish`.
- Inline co-author notes: `feedback-to-revision`.
