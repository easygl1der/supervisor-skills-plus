---
name: sv-experiment-prereg
description: >-
  Locks a confirmatory analysis before outcomes are seen: hypotheses, the
  estimand, the exact primary analysis, the decision rule, stopping and
  multiplicity are written down and frozen as a git commit, and an audit
  later proves the registration preceded every committed output and was
  never edited. Anything not registered is reported as exploratory. Use
  when a hypothesis test, an effect estimate or a p-value will support a
  claim, before the outcome data is looked at.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-experiment-prereg

The mechanism behind research-core IN-09 (planned analyses; unplanned ones
labelled exploratory) and, for `field: causal`, CI-01 (estimand before
estimator). Adapted from K-Dense-AI/science-superpowers (MIT); the freeze
and audit script is vendored in `scripts/prereg.sh`. `<skill-dir>` below is
this skill's folder.

## The rule

No confirmatory claim without a registration frozen before the outcomes
were looked at. Once the outcome has been loaded, plotted or summarised in a
way that shows the relation to be tested, that analysis is exploratory and
stays exploratory. A changed covariate, cutoff, exclusion or stopping point
after a look is a new, exploratory analysis.

Exempt, with the owner's agreement: purely descriptive reporting, method
development on simulated data, re-analysis of published results.

## Steps

1. **Before freezing, run what is cheap.** Every configuration in the plan
   has run once on non-outcome data or simulations, and the cheapest run
   that could falsify the prediction without touching the confirmatory
   outcome has been done. Do not register over a pipeline that has never
   executed.
2. **Write** `docs/prereg/YYYY-MM-DD-<topic>.md` from `template.md`: question
   and estimand, hypotheses and prediction, primary analysis, decision rule,
   sample size and stopping, multiplicity, secondary and exploratory list,
   deviations. State the result that would disconfirm the prediction; if no
   result could, reframe before freezing.
3. **Freeze**, from the project root, before touching outcomes:
   `sh <skill-dir>/scripts/prereg.sh freeze docs/prereg/<file>.md <raw data files>`.
   The freeze must be the file's first commit; it records data checksums
   and stamps the commit hash into the document. Never edit the file again;
   a new test gets a new file.
4. **Run exactly the registered analysis.** Log the run in `docs/runs.md`
   with the registration path (`sv-experiment-runs`).
5. **Audit before reporting**:
   `sh <skill-dir>/scripts/prereg.sh audit [--results <paths>] [docs/prereg/<file>.md]`.
   FROZEN, STAMP, INTEGRITY, CHRONOLOGY and DATA must all pass. Default
   results paths are `results outputs analysis figures reports derived`;
   scope with `--results` when a repository holds several studies.
6. **Separate in the paper**: registered analyses under their confirmatory
   heading with the registration's commit; everything else under
   "Exploratory", never mixed. A failed audit makes every claim under that
   registration exploratory.

See: references/template.md
See: ../sv-experiment/references/procedure.md

Self-test of the script and template: `sh <skill-dir>/scripts/selftest.sh`.

## What the audit cannot see

A peek that left no commit, outputs kept outside git, or a parallel branch
whose order against the freeze is unprovable (reported as WARN). Commit
outputs as they are produced, and say in the methods where the
registration lives.

## Checklist

- IN-09: each confirmatory result cites a registration whose audit passed;
  every other analysis is labelled exploratory.
- CI-01 (`field: causal`): the registration defines the estimand before
  any estimator.
- The audit output is saved to `docs/log/<date>-prereg-audit.md`.

## Hand-offs

- Freezing the data, samples and gold set first: `sv-experiment-freeze`.
- Numbers from the registered analysis into the paper:
  `sv-experiment-numbers`.
- The decision to register, or a deviation: `sv-supervisor-records` (ADR).
