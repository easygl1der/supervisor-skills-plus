# Field profile: AI / ML (with data-systems conventions)

Code: ML
Status: partial
Version: 0.1 (2026-10-13)
Scope: technique, new-problem and benchmark papers at ML, NLP, CV and
data-systems venues (NeurIPS, ICML, ICLR, ACL, CVPR, SIGMOD, VLDB, ICDE).

## Contents
Sources; Paper types; Typical structure; What reviewers and advisors care
about; Tone and phrasing; Citation norms; Figures and tables; Rigor and
threats; Checklist additions; Known disagreements; Unknown; Changelog.

Rules follow `references/core/precedence.md`. The upstream handbook comes
from a database (DB) lab; DB-community norms are marked as such. Core rules
are not repeated here.

## Sources
1. Upstream handbook: `handbook-en/01_Preliminary/1.1`, `03_Paper_Writing/3.1`
   to `3.5`, `04_Scientific_Plotting/4.1` to `4.4`, `06_Case_Studies/6.1` to `6.3`.
2. Upstream skills with references: tech-paper-template, benchmark-paper-
   template, intro-drafter, paper-writer, pre-submission-reviewer,
   figure-designer, idea-evaluator, rebuttal-guidance.
3. Owner skill `journal-adapt`, base rules `ml_cv_nlp.md` (ML/CV/NLP venues).
4. Upstream map of AI/ML assumptions: `notes/01-upstream-map.md` §4 to §5.
5. Exemplar papers analysed by the handbook case studies (Intro analyses
   only): Alpha-SQL (ICML 2025), AFlow (ICLR 2025), LEAD (VLDB 2026). Full
   bibliographic references are not recorded in the sources yet.

## Paper types
- Technique paper: a new method for a known problem; the main axis is the
  key idea or mechanism and the goal takes one sentence.
  [src: up:handbook-en/03_Paper_Writing/3.3_technical-paper-template.md; up:skills/tech-paper-template/SKILL.md] (confirmed)
- New problem or new setting paper: the problem definition is itself a
  contribution; the key idea supports why the definition is reasonable.
  [src: up:handbook-en/03_Paper_Writing/3.3_technical-paper-template.md; up:handbook-en/06_Case_Studies/6.3_vldb2026-lead-analysis.md] (confirmed)
- Benchmark or evaluation paper: the contribution is a gap in existing
  benchmarks, a construction pipeline, an evaluation framework and empirical
  findings; route it to benchmark-paper-template, not the technique template.
  [src: up:skills/benchmark-paper-template/SKILL.md; up:handbook-en/03_Paper_Writing/3.4_benchmark-paper-template.md] (confirmed)

## Typical structure
- Technique paper logic chain: background, at most three limitations of
  existing methods, key idea or goal, at most three challenges, one method
  module per challenge, three or four contributions each mapped to a
  section. Fix a broken link in the chain before drafting.
  [src: up:handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md; up:skills/tech-paper-template/SKILL.md] (confirmed)
- Abstract in five sentences: problem and significance, why it is unsolved,
  challenges of the problem (not of the method), method matched to the
  challenges, results on real datasets with concrete numbers and a code
  link. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Introduction in six paragraphs: problem with a concrete example,
  condensed limitations, challenges, method summary matched to the
  challenges, results with numbers, contributions matched to challenges.
  Paragraphs run about 100 to 250 words each.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; up:skills/intro-drafter/SKILL.md] (confirmed)
- Problem formulation goes words, then formal definition, then an example.
  A paper solves one problem. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Method section runs overview, workflow, then components; complex
  components get their own subsection; subsections are ordered from the
  strongest novelty to the weakest. Known techniques get minimal space.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; up:skills/pre-submission-reviewer/references/section-guides.md] (confirmed)
- Experiments run setup, end-to-end comparison against all baselines,
  further comparisons (scalability, model size), ablation, then analysis.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; skill:journal-adapt] (confirmed)
- Benchmark papers follow gap, benchmark, evaluation, insights,
  opportunities, with Figure 1 a running example, Table 1 a comparison with
  at least five benchmarks, and Figure 2 the construction pipeline.
  [src: up:skills/benchmark-paper-template/references/checklist.md] (confirmed)
- Related Work goes second to last when the paper can be read without it,
  and in Section 2 only when the method builds on that work.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)

## What reviewers and advisors care about
- Ranked: topic, then novelty and contribution, then experimental results,
  then writing. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Reviewers want a novel problem or method, a clear story and clean
  presentation; delta work (a combination of existing methods, or a
  technique already used on a similar problem) reads as insufficient.
  [src: up:handbook-en/01_Preliminary/1.1_how-to-evaluate-paper-quality.md; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Baselines must be strong and current; a baseline older than about twelve
  months against an active benchmark is a fatal flaw at idea stage.
  [src: up:skills/idea-evaluator/references/fatal-flaws.md; up:handbook-en/01_Preliminary/1.1_how-to-evaluate-paper-quality.md] (confirmed)
- Every proposed component is justified by an ablation (All, without A,
  without B, without C). [src: up:handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md; up:skills/pre-submission-reviewer/references/section-guides.md] (confirmed)
- DB community: improvement thresholds of at least 50% in performance or
  10% in accuracy are treated as ideal. Do not apply these figures to ML
  venues. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)

## Tone and phrasing
- Experiments section in past tense, the rest in present tense; the
  Conclusion in present perfect.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Without reported results, the Introduction never says "we achieved" or
  "we demonstrated". [src: up:skills/intro-drafter/SKILL.md] (confirmed)
- Active voice with "we"; intuition before formalism; contributions as
  delivered facts, not intentions; justify non-obvious design choices
  ("we use X instead of Y because"). [src: skill:journal-adapt] (confirmed)
- Avoid self-description as "novel", "state-of-the-art" or "simple yet
  effective", and do not open with a claim that deep learning revolutionized
  a field. [src: skill:journal-adapt; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)

## Citation norms
- Numeric citations by first appearance; a six-paragraph Introduction
  typically carries 15 to 25 verified references.
  [src: up:skills/intro-drafter/SKILL.md] (confirmed)
- Cite the three to five most relevant papers per claim, not ten or more.
  [src: skill:journal-adapt] (confirmed)
- DB community: take BibTeX from DBLP and use venue abbreviations (SIGMOD,
  VLDB, ICDE, TKDE). [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Related Work is grouped by approach; for each group state what it does,
  what it cannot do, and how this paper differs. Criticise the closest work
  concretely and less-related work lightly.
  [src: skill:journal-adapt; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)

## Figures and tables
- Three figure types carry the paper: the motivated example (Figure 1,
  first or second page, readable in 30 seconds), the solution overview, and
  experimental results. Draw the main figures before the text.
  [src: up:handbook-en/04_Scientific_Plotting/4.1_motivated-example-figure.md; up:handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md] (confirmed)
- Results figures: highlight the paper's method in a high-contrast colour
  and baselines in grey or light colours, with dual encoding (colour plus
  marker or line style). [src: up:handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md] (confirmed)
- The y-axis range neither hides nor exaggerates differences; state a
  non-zero origin in the figure. [src: up:handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md] (confirmed)
- Plot on a small canvas (about 150x100 pt) from one shared plotting script
  so fonts and styles match across figures.
  [src: up:handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md] (confirmed)
- Main results table lists all baselines and all metrics with the best
  result in bold (benchmarks: best and second best marked).
  [src: skill:journal-adapt; up:skills/benchmark-paper-template/references/checklist.md] (confirmed)

## Rigor and threats
- Setup names at least three real datasets (DB-lab rule), the metrics, the
  baselines and implementation details: optimizer, learning rate,
  hardware and seeds. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; skill:journal-adapt] (confirmed)
- Tune every baseline with the same effort and its best known
  configuration; document the effort.
  [src: up:skills/benchmark-paper-template/references/experiments.md] (confirmed)
- Non-deterministic runs report mean and standard deviation over repeated
  runs, and the decoding temperature; add significance tests where they
  apply. [src: up:skills/benchmark-paper-template/references/experiments.md; up:skills/benchmark-paper-template/references/checklist.md] (confirmed)
- Report secondary metrics (latency, cost) beside accuracy, and say where
  the method fails. [src: skill:journal-adapt; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- LLM-as-judge scores are validated against human ratings before use.
  [src: up:skills/benchmark-paper-template/references/benchmark-design.md] (confirmed)
- Document how training and prompt contamination of evaluation data is
  prevented. [src: up:skills/benchmark-paper-template/references/benchmark-design.md] (confirmed)
- Benchmark papers state a licence, a datasheet, hosting, ethics and a
  maintenance plan. [src: up:skills/benchmark-paper-template/references/checklist.md] (confirmed)
- Effectiveness claims require results from real runs; planned numbers
  never appear as results (evidence gates D0 to D5).
  [src: up:skills/paper-writer/references/evidence-discipline.md] (confirmed)

## Checklist additions

### ML-01 Paper type decided
- [ ] Check: The paper is classified as technique, new problem or setting,
  or benchmark, and the Introduction weights follow that type.
- Why: Each type puts the contribution in a different place.
- Status: confirmed
- Scope: field:ml
- Owner: tech-paper-template, intro-drafter, benchmark-paper-template
- Src: up:skills/tech-paper-template/SKILL.md; up:handbook-en/03_Paper_Writing/3.3_technical-paper-template.md

### ML-02 Challenge to module mapping
- [ ] Check: Each stated challenge (at most three) maps to one method module
  and each contribution to a section.
- Why: Upstream rates every break in this chain as critical.
- Status: confirmed
- Scope: field:ml
- Owner: tech-paper-template, intro-drafter, pre-submission-reviewer
- Src: up:skills/tech-paper-template/SKILL.md; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md

### ML-03 Current, fairly tuned baselines
- [ ] Check: Baselines include the strongest recent result on each
  benchmark, and tuning effort is documented equally.
- Why: Weak or under-tuned baselines are a fatal flaw.
- Status: confirmed
- Scope: field:ml
- Owner: idea-evaluator, experiment-workflow, pre-submission-reviewer
- Src: up:skills/idea-evaluator/references/fatal-flaws.md; up:skills/benchmark-paper-template/references/experiments.md

### ML-04 Implementation details for replication
- [ ] Check: Datasets, metrics, optimizer, learning rate, hardware, seeds
  and decoding settings are stated.
- Why: Missing hyperparameters block reproduction.
- Status: confirmed
- Scope: field:ml
- Owner: experiment-workflow, paper-writer, check-loop
- Src: skill:journal-adapt; up:skills/benchmark-paper-template/references/experiments.md

### ML-05 Variance reported
- [ ] Check: Non-deterministic results show mean and standard deviation over
  repeated runs; significance is tested where it applies.
- Why: Single runs cannot carry a comparison.
- Status: confirmed
- Scope: field:ml
- Owner: experiment-workflow, pre-submission-reviewer
- Src: up:skills/benchmark-paper-template/references/checklist.md

### ML-06 Motivated example figure
- [ ] Check: Figure 1 shows a real running example and the failure of
  existing methods, and the example returns as a case study.
- Why: It tells the reviewer the problem in 30 seconds.
- Status: confirmed
- Scope: field:ml
- Owner: figure-designer, intro-drafter
- Src: up:handbook-en/04_Scientific_Plotting/4.1_motivated-example-figure.md; up:handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md

### ML-07 Honest results plots
- [ ] Check: Results plots use dual encoding, a stated and reasonable axis
  origin, and one shared style script.
- Why: Misleading axes cost reviewer trust.
- Status: confirmed
- Scope: field:ml
- Owner: figure-designer
- Src: up:handbook-en/04_Scientific_Plotting/4.3_experimental-results-figure.md; up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md

### ML-08 Rebuttal claims verified
- [ ] Check: Every number in a rebuttal is traced to the paper or a new run;
  clarification items and new-experiment items are kept apart.
- Why: Unverified rebuttal numbers become commitments.
- Status: confirmed
- Scope: field:ml
- Owner: rebuttal-guidance
- Src: up:skills/rebuttal-guidance/references/checklist.md

## Known disagreements
- Number of contributions: three or four (handbook) versus at most three
  (journal-adapt ML rules) versus two to four (benchmark checklist). Decide
  per venue via journal-adapt.
  [src: up:handbook-en/03_Paper_Writing/3.1_the-essentials-of-a-research-paper.md; skill:journal-adapt; up:skills/benchmark-paper-template/references/checklist.md]
- Challenges paragraph: required in the DB-style Introduction, while the
  handbook notes that AI conferences often go straight to the method.
  [src: up:handbook-en/03_Paper_Writing/3.3_technical-paper-template.md]
- "To the best of our knowledge": listed as an anti-pattern by
  journal-adapt; the core novelty rule keeps "to our knowledge" once.
  [src: skill:journal-adapt; arc:msr:9c69675]
- Related Work position: second to last preferred (handbook) versus after
  the Introduction or integrated, used consistently (journal-adapt).
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; skill:journal-adapt]
- AI drafting: the handbook forbids LLM-generated content outright, while
  paper-writer drafts prose under evidence rules. Follow the venue and the
  team's ADR. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; note:n01§4.5]
- Em-dash ban and banned vocabulary come from the DB-lab handbook; core
  applies punctuation bans only through an overlay or venue profile.
  [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md; user:2026-10-13]

## Unknown
- Measured section lengths and page budgets per venue; exemplar papers with
  full references are needed (the three case studies cover Introductions
  only).
- Norms specific to CV and NLP papers beyond the shared ML rules.
- Expected statistical reporting for technique papers (confidence
  intervals, number of seeds) beyond mean and standard deviation.
- Compute and energy reporting expectations.
- Current venue policies on disclosing LLM use in writing.
- Bibliography style per ML venue (the DBLP rule is DB-specific).

## Changelog
- 0.1 (2026-10-13): created from upstream handbook and skills and the
  journal-adapt ML base rules.
