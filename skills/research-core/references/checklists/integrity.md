# Checklist: integrity

Items that protect the claims a paper makes about its own data: where each
number comes from, what agreement values mean, what was fixed before results
were seen, and what AI did in the research.

Run by: experiment-workflow, sv-review-once, sv-review-loop

## Contents
1. Number traceability
2. Agreement values
3. Fixed before results
4. Disclosure and conduct

## 1. Number traceability

### IN-01 Every printed number traceable
- [ ] Check: Every number in the paper (text, tables, figures, captions) is
  listed under "Verified numbers" in `docs/STATUS.md` with its script, output
  file, input data version and code commit; no commit identifier is a placeholder.
- Why: Untraceable numbers are the integrity failure reviewers and venues
  treat most harshly.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-review-loop, sv-supervisor-records
- Src: note:n08§5#17; arc:01-checklist/CHECKLIST-UPDATE-SUMMARY.md RP-11; arc:RP-12@v2

### IN-02 Numbers in figures follow the same rule
- [ ] Check: Numbers drawn inside figures are in the same "Verified numbers"
  list; none were copied from a sketch, an AI image or a reference figure.
- Why: A figure number copied from an image is not data.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-figure-design, sv-review-loop
- Src: note:n07§A.1; note:n07§A.8 FR3

### IN-03 Frozen-input identifiers printed consistently
- [ ] Check: Identifiers of frozen inputs (snapshot date, reference-set
  version, codebook version) are the same everywhere they are printed and in
  the package.
- Why: Mismatched identifiers suggest results come from different data.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-review-loop
- Src: arc:RS-14@v2; arc:RP-07@v2; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 2. Agreement values

### IN-04 Agreement values backed by raw label sets
- [ ] Check: Every inter-rater or model-versus-reference agreement value has
  the independent label sets and a script that recomputes it, kept with the
  data; if the label sets do not exist, the method describes what was done
  and the number is dropped.
- Why: In the evidence project a human-agreement value was printed with no
  computation record behind it.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-review-once, sv-review-loop
- Src: arc:msr:393f596; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B1; arc:RS-17@v2; note:n04§1.6

### IN-05 Each agreement value named
- [ ] Check: Each agreement value says which comparison it is (human with
  human, model with reference, or the reporting bar); values are never merged
  into one headline.
- Why: Several values with one name made the evidence project's agreement
  story inconsistent.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-write-section, sv-review-loop
- Src: arc:10-requirements/DECISION-HINTS.md U1; arc:01-checklist/checklist.md C2; user:2026-10-13 (promoted: failure had a clear bad outcome)

### IN-06 Reporting rule written once and applied everywhere
- [ ] Check: The rule for which values print (which run, which threshold,
  where) is written once in an ADR and applied in every section, including
  the data availability statement.
- Why: A rule applied in one section and broken in another reads as
  selective reporting.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-review-loop, sv-supervisor-records
- Src: arc:msr:9c69675; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H1; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 3. Fixed before results

### IN-07 Evaluation reference frozen before model output is seen
- [ ] Check: The evaluation reference, codebook and gate order were frozen
  before any model output was viewed; every later correction is logged, and
  results before and after the correction are reported and disclosed.
- Why: Correcting the reference after seeing model output inflates agreement.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-review-once
- Src: arc:11-mining-github-issue-audit/tree/docs/notes/gold-review/overlay-high14-review.md; arc:MF-08@v2; note:n08§5#20

### IN-08 Acceptance bars set before the run
- [ ] Check: Acceptance bars (agreement thresholds, stopping rules) were
  written before the run and are enforced in the run script.
- Why: A bar chosen after the result is not a bar.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow
- Src: note:n08§5#21

### IN-09 Planned analyses, exploratory ones labelled
- [ ] Check: The analysis follows the planned tests; any unplanned analysis
  is labelled exploratory in the text.
- Why: Unlabelled post-hoc analyses inflate false positives.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, idea-evaluator
- Src: arc:RS-01@v2; arc:RS-03@v2; user:2026-10-13 (promoted: failure had a clear bad outcome)

### IN-10 Prompt versions logged
- [ ] Check: When a model labels or generates data, each prompt version is
  kept with its agreement on the reference set, any rollback, and a one-line
  reason for the change.
- Why: Without a version log, the reported result cannot be tied to a prompt.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow
- Src: note:n08§5#22; user:2026-10-13 (promoted: failure had a clear bad outcome)

### IN-11 Disagreements turned into numbered rules
- [ ] Check: Each annotation disagreement that changed the guidelines is
  recorded as a numbered rule in a file in the repository.
- Why: Rules kept only in someone's head are lost when the annotator changes.
- Status: candidate
- Scope: core
- Owner: experiment-workflow, sv-supervisor-records
- Src: arc:res:7e4a35c; note:n08§5#23

## 4. Disclosure and conduct

### IN-12 AI use in the research disclosed in the method
- [ ] Check: The method names each model used in the research, its version,
  settings and prompts, and any AI help in building reference data or
  analysis code that conclusions rely on.
- Why: Venues require it; undisclosed AI use in the method undermines the results.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, sv-write-section, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G9; note:n08§5#19

### IN-13 No hidden text aimed at reviewers or review tools
- [ ] Check: The PDF and source contain no hidden or invisible text, white
  text or metadata instructions aimed at reviewers or automated review tools.
- Why: Prompt injection aimed at reviewers is prohibited conduct.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-review-loop
- Src: arc:10-requirements/venue/fse-2027-requirements.md
