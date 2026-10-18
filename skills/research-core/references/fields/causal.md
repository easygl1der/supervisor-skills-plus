# Field profile: Causal inference

Code: CI
Status: partial
Version: 0.2 (2026-10-16)
Scope: causal inference methods and applied causal studies (identification
arguments, design-based estimators, sensitivity analysis). Current rules lean
on econometrics-journal guides; statistics and epidemiology conventions are
not yet evidenced.

## Contents
Sources; Paper types; Typical structure (with Method block for quick reads);
What reviewers and advisors care about; Tone and phrasing; Citation norms;
Figures and tables; Rigor and threats; Checklist additions; Known
disagreements; Unknown; Changelog.

Rules follow `references/core/precedence.md`. Every rule from the Awesome
Journal Skills guides (AJS) is a candidate: the guides are published but
written for specific econometrics journals. A rule becomes confirmed only when
5 to 10 exemplar papers from the user's target venues agree. Core rules still
apply, including the rule that causal language needs a causal design
(`references/core/claims-evidence.md`).

## Sources
1. Awesome-Journal-Skills (AJS), https://github.com/brycewang-stanford/Awesome-Journal-Skills,
   commit 932eb23331721b16e967c59f093781be1928b498 (cited as `@932eb23`),
   MIT License, Copyright (c) 2026 Bryce Wang. Rules are restated in our own
   words; no paragraphs are copied. Files used:
   - `Econometrica-Skills/skills/ecta-identification/SKILL.md`
   - `Econometrica-Skills/skills/ecta-robustness/SKILL.md`
   - `Econometrica-Skills/skills/ecta-writing-style/SKILL.md`
   - `Econometrica-Skills/skills/ecta-literature-positioning/SKILL.md`
   - `Econometrica-Skills/skills/ecta-tables-figures/SKILL.md`
   - `Econometrica-Skills/skills/ecta-replication-package/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-identification-strategy/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-data-analysis/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-identification-strategy/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-literature-positioning/SKILL.md`
2. No exemplar papers from the user's target venues yet.

## Paper types
- Identification or estimator paper: the contribution is a new
  identification result or an estimator with derived inference; the design
  is a vehicle, not the contribution. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- Applied causal study: the contribution is a credible estimate of a named
  estimand; at a methods journal an off-the-shelf design whose estimate is
  the whole point belongs at an applied venue instead.
  [src: guide:AJS/ecta-identification@932eb23] (candidate)
- Applied paper inside a methods venue: must argue that the application
  actually needs the new method (for example a weak first stage that the
  method is built for). [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)

## Typical structure
- Methods paper skeleton: introduction with an informal main result, setup
  and numbered assumptions, identification and asymptotic results with proof
  sketches, simulation evidence, empirical application, short conclusion,
  full proofs in a supplement. [src: guide:AJS/ecta-writing-style@932eb23] (candidate)
- Define the target parameter as a functional of the population
  distribution before any estimator appears; identification is a population
  property, not a sample one. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Order the formal core as identification, then regularity conditions, then
  consistency, rate, limiting distribution and variance estimator, then
  finite-sample evidence, then robustness.
  [src: guide:AJS/jbes-identification-strategy@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Counterfactuals and policy claims are limited to objects the
  identification argument delivers. [src: guide:AJS/ecta-identification@932eb23] (candidate)

### Method block for quick reads
When sv-quickread or study summarises a causal paper on one page, the
method block states, in this order:
- Identifying assumptions: each one by its label in the paper (exclusion,
  parallel trends, continuity at a cutoff, unconfoundedness, rank or
  support), and which result needs it. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Estimand: the population quantity (for example an average effect on a
  named population or a structural parameter), and whether it is point or
  set identified. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- Estimator: the procedure, its nuisance parts and tuning choices, and any
  first-stage correction (orthogonal score, influence-function adjustment).
  [src: guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Inference: the variance estimator or resampling scheme, the clustering or
  dependence it allows, and whether it is robust to weak identification.
  [src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23] (candidate)
- Threats: which assumption is most likely to fail in the application, the
  sensitivity analysis the authors run, and what the paper concedes.
  [src: guide:AJS/ecta-robustness@932eb23; guide:AJS/jbes-identification-strategy@932eb23] (candidate)

## What reviewers and advisors care about
1. Identification is argued, not asserted: each condition is numbered, and
   the paper shows what fails without it (a counterexample or a set that
   becomes non-singleton). [src: guide:AJS/ecta-identification@932eb23] (candidate)
2. Point versus partial identification is stated honestly; if only a set is
   identified, the set is characterised. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
3. Standard errors are licensed by a stated theorem; if an off-the-shelf
   estimator is used, cite the precise result that justifies the inference.
   [src: guide:AJS/ecta-identification@932eb23] (candidate)
4. Near the boundary of identification (weak instruments, near-singular
   Jacobian, sparse support) the paper offers inference that stays valid
   there rather than relying on pointwise asymptotics.
   [src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
5. The assumptions are plausible for the paper's own data, not only for a
   convenient model. [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)
6. Separate what is identified nonparametrically from what rests on
   functional-form assumptions. [src: guide:AJS/ecta-identification@932eb23] (candidate)

## Tone and phrasing
- Keep three kinds of statement visibly apart: assumed, proved in this
  paper, and cited from elsewhere. [src: guide:AJS/ecta-writing-style@932eb23] (candidate)
- Replace "standard regularity conditions" and "clearly identified" with
  the labelled list of conditions. [src: guide:AJS/joe-identification-strategy@932eb23; guide:AJS/ecta-identification@932eb23] (candidate)
- Report effects in interpretable units, not only as coefficients.
  [src: guide:AJS/ecta-identification@932eb23] (candidate)

## Citation norms
- For each close prior result, state one formal relation: nests it,
  generalises it, weakens its assumption, or supplies what it lacked.
  [src: guide:AJS/ecta-literature-positioning@932eb23] (candidate)
- Back every "nests" or "generalises" claim with an explicit special case,
  usually a short corollary or remark. [src: guide:AJS/ecta-literature-positioning@932eb23] (candidate)
- Attribute each identifying assumption to the work that introduced it and
  the work that first relaxed it; cite the original theorem, not a survey.
  [src: guide:AJS/ecta-literature-positioning@932eb23] (candidate)
- When the method adapts a statistics or ML idea, position it against both
  the statistics or ML original and the econometric incumbent.
  [src: guide:AJS/jbes-literature-positioning@932eb23] (candidate)

## Figures and tables
- Put the decisive identification checks in the body and the full battery
  in the appendix. [src: guide:AJS/ecta-robustness@932eb23] (candidate)
- Every table note names the estimator and the clustering or dependence
  assumption behind the standard errors. [src: guide:AJS/ecta-tables-figures@932eb23] (candidate)
- Numbers in the text match the tables exactly, and each exhibit traces to
  a named script. [src: guide:AJS/ecta-tables-figures@932eb23] (candidate)

## Rigor and threats
- Pair observational claims with a sensitivity analysis for unobserved
  confounding (for example a bound on how strong a confounder must be).
  [src: guide:AJS/ecta-identification@932eb23] (candidate)
- For staggered adoption, use estimators that remain valid under
  heterogeneous effects across cohorts, and report a pre-trend sensitivity
  analysis rather than only a pre-trend test. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- For IV designs, report first-stage strength with a measure robust to
  heteroskedasticity and an interval that stays valid under weak
  instruments. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- For regression discontinuity, report bias-aware inference and a
  manipulation test at the cutoff. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- For experiments with many outcomes, use randomization-based inference and
  control the family-wise error rate. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- Few clusters call for a wild cluster bootstrap or similar small-cluster
  correction. [src: guide:AJS/ecta-robustness@932eb23] (candidate)
- Simulation results are part of the replication package: seeded, rerun
  from one master script, environment pinned.
  [src: guide:AJS/ecta-replication-package@932eb23] (candidate)

## Checklist additions

### CI-01 Estimand defined before estimator
- [ ] Check: The target parameter is defined as a population quantity
  before any estimator, and the paper says whether it is point or set
  identified.
- Why: Readers and referees cannot judge an estimator whose target is
  implicit.
- Status: candidate
- Scope: field:ci
- Owner: sv-write-section, sv-review-once, proposal-writer
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23

### CI-02 Identifying assumptions labelled and shown to bind
- [ ] Check: Each identifying assumption is numbered, used by label in the
  results, and accompanied by what goes wrong without it.
- Why: Unlabelled or unexplained conditions are the first referee
  complaint at methods venues.
- Status: candidate
- Scope: field:ci
- Owner: sv-write-section, sv-review-once, sv-review-loop
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23

### CI-03 Inference justified by a stated result
- [ ] Check: The standard errors or intervals cite the theorem (own or
  published) that justifies them, including the dependence or clustering
  structure assumed.
- Why: Standard errors without supporting asymptotics are a common
  rejection reason.
- Status: candidate
- Scope: field:ci
- Owner: sv-review-once, sv-review-loop, experiment-workflow
- Src: guide:AJS/ecta-identification@932eb23

### CI-04 Weak or boundary identification handled
- [ ] Check: If the design can be weakly identified (weak first stage,
  sparse support near a cutoff, few treated cohorts), the paper reports
  inference that remains valid there.
- Why: Pointwise asymptotics mislead in exactly these regimes.
- Status: candidate
- Scope: field:ci
- Owner: experiment-workflow, sv-review-once
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23

### CI-05 Sensitivity analysis for the weakest assumption
- [ ] Check: The paper names the identifying assumption most likely to fail
  in its data and reports a sensitivity analysis for it.
- Why: A design is only as credible as its least plausible assumption.
- Status: candidate
- Scope: field:ci
- Owner: experiment-workflow, sv-write-section, sv-review-once
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23

### CI-06 Claims limited to identified objects
- [ ] Check: Every counterfactual or policy statement concerns an object the
  identification argument delivers; extrapolations are labelled as such.
- Why: Claims beyond the identified set are unsupported by the design.
- Status: candidate
- Scope: field:ci
- Owner: sv-write-section, sv-review-loop
- Src: guide:AJS/ecta-identification@932eb23

### CI-07 Quick-read method block complete
- [ ] Check: A one-page summary of a causal paper states identifying
  assumptions, estimand, estimator, inference and threats.
- Why: Without these five a summary cannot be checked against the paper.
- Status: candidate
- Scope: field:ci
- Owner: sv-quickread-card, sv-study
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23

## Known disagreements
- Meaning of "identification": in applied economics it often means a
  credible research design for a causal effect; in econometric theory it
  means a one-to-one map from the data distribution to the parameter; in
  statistics and epidemiology the same idea is usually phrased through
  potential outcomes or causal graphs and stated assumptions such as
  positivity and consistency. AJS takes the econometric-theory reading.
  Decide per venue via sv-write-style-mine. [src: guide:AJS/ecta-identification@932eb23] (candidate)
- Econometrics guides expect a derived limiting distribution for any new
  estimator; many applied causal venues accept a cited estimator with a
  design argument. Decide per venue. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23] (candidate)

## Unknown
- Conventions at statistics, epidemiology and ML causal venues (JASA,
  Biometrika, American Journal of Epidemiology, CLeaR, causal tracks at ML
  conferences): no AJS skill read for these; needs 5 to 10 exemplar papers
  via sv-write-style-mine (`sv-supervisor-harvest --new-field causal`).
- Whether causal graphs (DAGs) are expected in the target venues.
- Typical section lengths: not measured from exemplars.

## Changelog
- 0.1 (2026-10-13): stub created.
- 0.2 (2026-10-16): candidate rules from AJS @932eb23 (Econometrica, Journal
  of Econometrics, JBES skills); method block for quick reads; CI-01 to CI-07.
