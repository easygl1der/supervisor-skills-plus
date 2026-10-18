---
name: sv-write-critique
description: >-
  Critiques a draft without editing it: runs the source-recall and
  verification checklist, the reader-logic checks, the logic-chain
  consistency checks when a skeleton exists, and the research-core writing
  checklist, then says whether each problem is language, structure, or a
  claim the evidence may not carry. Returns findings only. Use when the user
  asks what is wrong with a draft, wants a critique, or says not to edit.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-critique

A report-only pass assembled from checks that already exist in the writing
group. It changes nothing in the manuscript.

## Step 0

Follow the Step 0 of `../sv-write-section/references/workflow.md`
(research.yaml, core rules, field and venue profiles, writing checklist),
and read the claim ledger in `docs/claims/` when one exists.

## Checks, in order

1. **Facts and sources.** Walk
   `../sv-write-section/references/verification-checklist.md` on the draft:
   facts, evidence matching, cross-section discipline, formulas and tables,
   delivery format.
2. **Reader logic** for Results, Methods and RQ transitions:
   `../sv-write-polish/references/reader-logic.md`.
3. **Logic chain**, when the paper has a skeleton or is a technique paper:
   the four checks in `../sv-write-skeleton/references/consistency-checks.md`.
4. **Writing checklist.** The research-core `writing` items and the field
   additions whose scope matches, each reported as pass, fail, n/a or
   unknown with evidence (file and line, or the quoted sentence).
5. **Classify every finding** the way the polish procedure's "When the
   problem is deeper than language" section does: language (polish),
   beyond sentence repair (redraft), or a core claim that may not hold
   (audit).

See: ../sv-write-section/references/workflow.md
See: ../sv-write-section/references/verification-checklist.md
See: ../sv-write-polish/references/reader-logic.md
See: ../sv-write-skeleton/references/consistency-checks.md
See: ../sv-write-polish/references/procedure.md

## Output

A findings table: id, location, check, finding, class (language,
redraft, claim), suggested sub-command. No rewritten text, unless the user
then asks for a fix.

## Hand-offs

- Language findings: `sv-write-polish`.
- Redraft findings: `sv-write-section` or `sv-write-intro`.
- Claim findings: `sv-review-once` or `idea-evaluator`.
- AI-texture findings: `sv-write-humanize-audit`.
