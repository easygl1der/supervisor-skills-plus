# Methods-borrowing card mode

## Contents
1. Purpose and hard rules
2. Method Card format
3. Phase A: transfer matrix
4. Phase B: ranked borrowings
5. Phase C: implementation brief (user gate)
6. Phase D: optional prose hand-off
7. Files and maintenance

Generalized from an archived project skill that borrowed analysis methods
from a related-work corpus to strengthen a study's research questions,
without importing other papers' findings. [src: note:n02§8]

## 1. Purpose and hard rules

Style cards describe how papers write. Method Cards describe how papers
**analyze**: unit of analysis, sampling, measurement, quality assurance,
statistics. Use this mode when the user wants to strengthen research
questions, a labeling or measurement design, or the threats section using
methods from related papers.

1. Method Cards only: describe pipelines, units, tests and QA. Never quote or
   paraphrase findings, numbers or conclusions of the source papers.
2. Never import another paper's empirical claims, magnitudes or taxonomies
   into the manuscript as if they were the project's own.
3. Do not edit the manuscript, the analysis code or the results unless the
   user explicitly asks to implement one borrowing (Phase C).
4. Preserve the project's locked design: anything recorded in
   `docs/adr/` or listed as P1 in the dynamic skill (codebook, gates,
   statistical tests already chosen) is not reopened here. Propose an ADR
   instead if a borrowing would change it.

## 2. Method Card format

One card per paper, or per cluster of closely related papers.

```
## Method Card: <paper_id or cluster id>
Citation keys: lit:<key>[, lit:<key> ...]
Paper type: <empirical study | technique | benchmark | ...>

1. Research questions (as types, not content): <characterize | compare | predict | explain>
2. Unit of analysis: <issue, commit, function, participant, model run, ...>
3. Data source and sampling: <population, filters, snapshot vs longitudinal, censoring handled?>
4. Measurement / labeling: <manual coding, codebook origin, automated labels, model-assisted labels>
5. Quality assurance: <agreement statistic type, adjudication, held-out gold, confidence screening>
6. Analysis: <tests, effect sizes, models, stratification before pooling>
7. Validity handling: <which threats are addressed and how, as procedures>
8. Artifact: <what is released, how numbers are regenerated>
9. Transfer notes: <what would need to be true in the target study to reuse each element>
```

Section 9 is the only place for judgement; sections 1 to 8 are descriptive.

## 3. Phase A: transfer matrix

Map each candidate technique to a target research question or design
element. No code yet.

```
| Technique | Source (lit: keys) | Target RQ / design element | Feasibility | Data needed | Threat if misapplied |
|---|---|---|---|---|---|
```

Feasibility labels:

- **Now**: same data, no new collection (for example, extra metrics on the
  existing gold set).
- **Near**: a subsample audit or linking to records already in the metadata.
- **Future**: needs new fields, pipelines or collection (for example,
  survival analysis needing censoring data that was not kept).

The "Threat if misapplied" column is required. A borrowing whose unit of
analysis differs from the target study's unit is flagged there.

## 4. Phase B: ranked borrowings

Group the matrix rows into three tiers and rank inside each tier:

1. **Tier 1, implementable without new data.** Strengthens a result or a
   measurement directly. Name the target RQ or design element.
2. **Tier 2, strengthens interpretation.** Belongs in discussion, threats or
   future work; may justify a design choice by precedent.
3. **Tier 3, position only, do not import as analysis.** Different unit,
   different oracle or different population; cite for positioning only.

For each item give one line: technique, source keys, target, why it helps,
and the main risk.

## 5. Phase C: implementation brief (user gate)

Only when the user asks to implement a Tier 1 or Tier 2 item:

```
## Implementation brief: <technique>
- Source: lit:<key>[, ...] (method only)
- Target: <RQ or design element>
- Files to touch: <scripts, tables, sections>
- New tables or figures: <...>
- Statistical test and effect size: <...>
- Sample size or power note: <...>
- Threats paragraph: <what to add, as a procedure>
- Acceptance bar set before running: <...>
- Not doing: <explicit exclusions>
```

Wait for confirmation before editing TeX or running anything. Analysis work
goes to `experiment-workflow` (runs log, number traceability); a design
change gets an ADR via `sv-supervisor-records`.

## 6. Phase D: optional prose hand-off

If the user also wants prose aligned to a venue, run Phase 1 of this skill
on the venue corpus. Method Cards inform Methods and Results structure only;
they never supply numbers or claims.

## 7. Files and maintenance

- Cards: `<style.dynamic_skill>/method-cards/<id>.md` (or
  `<related-work folder>/_method_cards/` without a research.yaml).
- Matrix and ranking: `<style.dynamic_skill>/method-cards/transfer-matrix.md`.
- When papers are added to the related-work corpus, regenerate cards for the
  clusters closest to the target RQs first.
- With a large corpus, cards can be produced in parallel, one worker per
  paper; each worker's prompt includes hard rule 1.
