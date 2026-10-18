# Claims match evidence

## Contents
1. The claim ledger
2. Numbers
3. Scope and hedging
4. Novelty and causality
5. Model-read data
6. Checks

## 1. The claim ledger

Before drafting or revising a section, list its claims in a ledger
(`assets/templates/claim-ledger.md`): one row per claim with the exact
number(s), the scope (population, subset, denominator), the source (script
and output file, or citation) and the code/data commit. Prose is written from
the ledger, not the other way round. [src: up:skills/sv-write/references/evidence-discipline.md; skill:deai-paper-writing; note:n02§11.5] (confirmed)

Without a ledger, fluent prose arrives first and the numbers and scope are
patched in later, if at all. In the evidence project an agreement value
entered the text from a reference image and was never traced to data.
[src: note:n07§A.1; arc:msr:393f596; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B1] (confirmed)

## 2. Numbers

- Every printed number comes from a script; the script, its output file and
  the commit are recorded in `docs/STATUS.md` under "Verified numbers" before
  the number enters the paper. [src: note:n08§5#17; arc:01-checklist/CHECKLIST-UPDATE-SUMMARY.md RP-11] (confirmed)
- The same quantity is printed identically everywhere (abstract, intro, RQ
  sections, summary boxes, conclusion, figures, captions). [src: note:n07§B.5; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md §5] (candidate)
- One number per claim sentence in prose; exact counts belong in tables.
  Avoid lists of percentages in a sentence. [src: arc:@senior-a-comments:79-100; note:n06§2.3] (candidate)
- Name the denominator wherever a share is cited. [src: arc:@senior-a-comments:38-43; note:n07§B.5] (candidate)

## 3. Scope and hedging

- Hedge interpretations, never measured facts. A measured share is stated
  plainly; what it might mean is hedged once. [src: skill:humanize-paper; note:n02§10] (confirmed)
- Scope claims to what was studied ("in the studied repositories", "pooled
  over ecosystems"). When a pooled result does not hold in every group, say so
  in the same sentence. [src: arc:msr:24d8c65; note:n06§2.6] (candidate)
- One precise caveat where it matters; long disclaimers go to methods or
  threats. [src: arc:@senior-a-comments:158-171] (candidate)

## 4. Novelty and causality

- Novelty claims carry "to our knowledge" and are stated once, after what
  prior work does. [src: arc:msr:9c69675; arc:RW-01@v2] (candidate)
- Causal language needs a causal design. Otherwise write the association and,
  if an explanation is offered, label it as untested ("one possible reason,
  which our data do not test"). [src: arc:msr:9c69675; note:n06§2.6] (candidate)
- Do not claim what was not measured (for example severity, effort, or code
  size when only text labels or calendar time were measured).
  [src: arc:CF-12@v2; arc:CF-29@v2; arc:msr:9c69675] (candidate)

## 5. Model-read data

When labels come from a model reading text (an LLM classifier, an annotator
reading issue text), every claim built on them carries a reader qualifier
once per paragraph ("as the tracker text describes them"). Dimensions whose
agreement is below the stated bar are described as the model's reading, not
as ground truth. [src: arc:msr:643836a; arc:msr:3e7bab0; note:n06§2.6-2.7] (candidate)

## 6. Checks

- Every sentence with a number maps to a ledger row.
- Every ledger row has a script or a citation.
- No claim is stronger in the abstract or conclusion than in the results.
- `writing.md` and `integrity.md` checklists cover these items.
