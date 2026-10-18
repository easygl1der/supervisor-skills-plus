# Field profile: Statistics

Code: ST
Status: partial
Version: 0.2 (2026-10-16)
Scope: methodological and applied statistics papers (new estimators, tests,
inference procedures, simulation studies). Current rules come from
econometric-statistics and AI-statistics guides; core statistics journals are
not yet evidenced.

## Contents
Sources; Paper types; Typical structure (with Method block for quick reads);
What reviewers and advisors care about; Tone and phrasing; Citation norms;
Figures and tables; Rigor and threats; Checklist additions; Known
disagreements; Unknown; Changelog.

Rules follow `references/core/precedence.md`. Every rule from the Awesome
Journal Skills guides (AJS) is a candidate: the guides are published but
written for specific econometrics or AI-statistics venues. A rule becomes
confirmed only when 5 to 10 exemplar papers from the user's target venues
agree.

## Sources
1. Awesome-Journal-Skills (AJS), https://github.com/brycewang-stanford/Awesome-Journal-Skills,
   commit 932eb23331721b16e967c59f093781be1928b498 (cited as `@932eb23`),
   MIT License, Copyright (c) 2026 Bryce Wang. Rules are restated in our own
   words; no paragraphs are copied. Files used:
   - `Econometrica-Skills/skills/ecta-writing-style/SKILL.md`
   - `Econometrica-Skills/skills/ecta-identification/SKILL.md`
   - `Econometrica-Skills/skills/ecta-robustness/SKILL.md`
   - `Econometrica-Skills/skills/ecta-tables-figures/SKILL.md`
   - `Econometrica-Skills/skills/ecta-replication-package/SKILL.md`
   - `Econometrica-Skills/skills/ecta-literature-positioning/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-writing-style/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-identification-strategy/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-data-analysis/SKILL.md`
   - `Journal-of-Econometrics-Skills/skills/joe-tables-figures/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-writing-style/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-identification-strategy/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-data-analysis/SKILL.md`
   - `Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-literature-positioning/SKILL.md`
   - `AISTATS-Skills/skills/aistats-writing-style/SKILL.md`
   - `AISTATS-Skills/skills/aistats-experiments/SKILL.md`
   - `AISTATS-Skills/skills/aistats-related-work/SKILL.md`
2. No exemplar papers from the user's target journals yet.

## Paper types
- New estimator: identifying moment or objective, consistency and limiting
  distribution under stated conditions, and a consistent variance estimator.
  [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)
- New test: null and alternative, null limiting distribution, finite-sample
  size control and power against relevant alternatives.
  [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)
- Computational or algorithmic: same target as the slower method, plus the
  complexity or scalability gain, numerical accuracy and timing.
  [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)

## Typical structure
- Introduction: problem, where existing methods fall short, the
  contribution stated as a property in plain words, a preview of
  assumptions, main theorem and simulation evidence, roadmap. Write it last.
  [src: guide:AJS/joe-writing-style@932eb23; guide:AJS/jbes-writing-style@932eb23] (candidate)
- Reach the main result (an informal statement is fine) within the first
  two pages. [src: guide:AJS/ecta-writing-style@932eb23; guide:AJS/aistats-writing-style@932eb23] (candidate)
- Body order: setup and numbered assumptions, main results with proof
  sketches, simulation study, empirical illustration, short conclusion;
  full proofs in an appendix or supplement. [src: guide:AJS/ecta-writing-style@932eb23] (candidate)
- Proof path in the body: consistency, then rate, then limiting
  distribution, then variance estimator. [src: guide:AJS/joe-identification-strategy@932eb23; guide:AJS/joe-writing-style@932eb23] (candidate)
- The empirical illustration serves the method: pick data where the problem
  the method solves actually occurs, and keep claims about the application
  proportionate. [src: guide:AJS/joe-data-analysis@932eb23; guide:AJS/jbes-data-analysis@932eb23] (candidate)

### Method block for quick reads
When paper-quickread or study summarises a statistics paper on one page, the
method block states, in this order:
- Model: the data-generating setting, the target parameter or functional,
  and the estimator or test. [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)
- Assumptions: each numbered condition (moments, smoothness, dependence,
  rank, tuning rates), marked primitive or high-level.
  [src: guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Asymptotic properties: consistency, rate (standard or not), limiting
  distribution, variance estimator, and whether the result is pointwise or
  uniform. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Finite-sample or simulation design: DGPs (favourable and stressing),
  sample-size grid, competitors, replication count, and what was reported
  (bias, RMSE, size, power, coverage). [src: guide:AJS/joe-data-analysis@932eb23; guide:AJS/ecta-robustness@932eb23] (candidate)

## What reviewers and advisors care about
1. Regularity conditions are listed, primitive where possible, and none
   quietly assumes the conclusion; a high-level condition is verified for a
   leading example or labelled as a sufficient technical condition.
   [src: guide:AJS/joe-identification-strategy@932eb23; guide:AJS/ecta-identification@932eb23] (candidate)
2. A nonstandard rate or non-normal limit is derived, not assumed.
   [src: guide:AJS/ecta-identification@932eb23] (candidate)
3. Asymptotics without finite-sample evidence is a standard rejection
   reason. [src: guide:AJS/ecta-robustness@932eb23] (candidate)
4. The simulation regime (n, dimension, noise) matches the regime of the
   theorems. [src: guide:AJS/aistats-experiments@932eb23] (candidate)
5. Conditions are plausible for real data, including the paper's own
   application. [src: guide:AJS/jbes-identification-strategy@932eb23] (candidate)
6. The class of models covered is stated, with what is excluded.
   [src: guide:AJS/joe-identification-strategy@932eb23] (candidate)

## Tone and phrasing
- Definitions and assumptions are displayed, numbered objects, cited by
  label inside theorem statements. [src: guide:AJS/ecta-writing-style@932eb23; guide:AJS/aistats-writing-style@932eb23] (candidate)
- Each theorem gets a one-line intuition before it and a short
  interpretation after it (what it means, which assumption does the work).
  [src: guide:AJS/joe-writing-style@932eb23; guide:AJS/ecta-writing-style@932eb23] (candidate)
- Every symbol is defined before use and never reused for two things.
  [src: guide:AJS/ecta-writing-style@932eb23; guide:AJS/joe-writing-style@932eb23] (candidate)
- Keep problem-dependent constants visible instead of hiding dimension or
  condition numbers in O-notation. [src: guide:AJS/aistats-writing-style@932eb23] (candidate)
- Label conjectured or only empirically supported statements as such; do
  not mix them with proved claims in one paragraph.
  [src: guide:AJS/aistats-writing-style@932eb23; guide:AJS/ecta-writing-style@932eb23] (candidate)
- Quantify gains against a named incumbent instead of "performs better".
  [src: guide:AJS/jbes-writing-style@932eb23; guide:AJS/aistats-writing-style@932eb23] (candidate)

## Citation norms
- Name 3 to 6 incumbent methods and give a concrete delta for each
  (assumptions, rate, robustness, computation); concede regimes where an
  incumbent still wins. [src: guide:AJS/jbes-literature-positioning@932eb23; guide:AJS/ecta-literature-positioning@932eb23] (candidate)
- Cover both the statistics literature and the ML literature when the work
  sits between them; citing only one side signals rediscovery.
  [src: guide:AJS/aistats-related-work@932eb23; guide:AJS/jbes-literature-positioning@932eb23] (candidate)
- Cite the precise theorem relied on, by number, not only the paper or a
  survey. [src: guide:AJS/ecta-literature-positioning@932eb23] (candidate)

## Figures and tables
- Report empirical size at the nominal level in its own panel and
  size-adjusted power separately. [src: guide:AJS/joe-tables-figures@932eb23; guide:AJS/ecta-tables-figures@932eb23] (candidate)
- Table notes alone let a reader interpret every number: DGP, n,
  replications, nominal level, tuning values, and what each column reports.
  [src: guide:AJS/ecta-tables-figures@932eb23; guide:AJS/joe-tables-figures@932eb23] (candidate)
- Decimal precision is consistent down a column and no finer than the
  replication count supports. [src: guide:AJS/joe-tables-figures@932eb23; guide:AJS/ecta-tables-figures@932eb23] (candidate)
- Figures that show theory at work: coverage against n, power curves with
  the null and nominal level marked, a QQ plot or density of the
  standardised statistic against its limit, a log-log error plot for a
  claimed rate. [src: guide:AJS/joe-tables-figures@932eb23; guide:AJS/aistats-experiments@932eb23] (candidate)
- Clean three-rule tables; vector figures that survive grayscale.
  [src: guide:AJS/ecta-tables-figures@932eb23] (candidate)

## Rigor and threats
- Simulation designs include cases where the assumptions hold and cases
  near or past their boundary (heavy tails, dependence, weak
  identification, high dimension), so the breakdown is visible.
  [src: guide:AJS/ecta-robustness@932eb23; guide:AJS/joe-data-analysis@932eb23; guide:AJS/jbes-data-analysis@932eb23] (candidate)
- Use a grid of sample sizes, including a small one, so the reader sees the
  asymptotics take hold. [src: guide:AJS/ecta-robustness@932eb23; guide:AJS/jbes-data-analysis@932eb23] (candidate)
- Run the nearest competitor on the identical DGPs.
  [src: guide:AJS/joe-data-analysis@932eb23; guide:AJS/jbes-data-analysis@932eb23] (candidate)
- Report replication counts, Monte Carlo standard errors of rejection rates
  and coverage, and fixed seeds. [src: guide:AJS/ecta-robustness@932eb23; guide:AJS/jbes-data-analysis@932eb23] (candidate)
- Vary every tuning parameter and show sensitivity; give a data-driven
  default if results are knife-edge. [src: guide:AJS/ecta-robustness@932eb23] (candidate)
- Calibrate stress DGPs to features of the application (persistence, tails,
  cross-sectional dependence) rather than only i.i.d. Gaussian noise.
  [src: guide:AJS/jbes-data-analysis@932eb23] (candidate)
- Fix the simulation grid in a plan before running; mark later additions as
  diagnostics. [src: guide:AJS/joe-data-analysis@932eb23] (candidate)
- Cross-check a derived asymptotic variance against a high-replication
  simulation; a mismatch usually means an algebra error.
  [src: guide:AJS/joe-identification-strategy@932eb23] (candidate)
- Every simulation table regenerates exactly from seeded code via one
  master script, with runtime and hardware stated.
  [src: guide:AJS/ecta-replication-package@932eb23] (candidate)

## Checklist additions

### ST-01 Assumptions numbered and classified
- [ ] Check: Every condition is numbered, cited by label in the theorems,
  and marked primitive or high-level; high-level ones are verified for a
  leading example.
- Why: Unverifiable high-level conditions can make a theorem trivial.
- Status: candidate
- Scope: field:st
- Owner: sv-write-section, sv-review-once, sv-review-loop
- Src: guide:AJS/joe-identification-strategy@932eb23; guide:AJS/aistats-writing-style@932eb23

### ST-02 Full asymptotic chain
- [ ] Check: Consistency, rate, limiting distribution and a consistent
  variance estimator are each stated with their conditions.
- Why: Inference without a derived limit and variance estimator is not
  justified.
- Status: candidate
- Scope: field:st
- Owner: sv-write-section, sv-review-once
- Src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23

### ST-03 Favourable and stressing DGPs
- [ ] Check: The simulation includes at least one design where assumptions
  hold and one near or past their boundary, across several sample sizes.
- Why: A single favourable design proves nothing about usability.
- Status: candidate
- Scope: field:st
- Owner: experiment-workflow, sv-review-once
- Src: guide:AJS/ecta-robustness@932eb23; guide:AJS/joe-data-analysis@932eb23

### ST-04 Competitor on identical DGPs
- [ ] Check: The nearest existing method runs on exactly the same designs
  and is reported on the same scale.
- Why: Improvement is unquantified without the incumbent.
- Status: candidate
- Scope: field:st
- Owner: experiment-workflow, sv-review-loop
- Src: guide:AJS/joe-data-analysis@932eb23; guide:AJS/jbes-data-analysis@932eb23

### ST-05 Size before power
- [ ] Check: Empirical size at the nominal level is reported, and power is
  size-adjusted or shown alongside size.
- Why: Power of a size-distorted test is not meaningful.
- Status: candidate
- Scope: field:st
- Owner: experiment-workflow, sv-write-section, sv-review-loop
- Src: guide:AJS/joe-tables-figures@932eb23; guide:AJS/ecta-robustness@932eb23

### ST-06 Monte Carlo precision reported
- [ ] Check: Replication count, Monte Carlo standard errors and seeds are
  reported, and decimal precision does not exceed what they support.
- Why: Otherwise a size of 0.06 cannot be told apart from 0.05.
- Status: candidate
- Scope: field:st
- Owner: experiment-workflow, sv-review-loop
- Src: guide:AJS/ecta-robustness@932eb23; guide:AJS/jbes-data-analysis@932eb23

### ST-07 Self-contained simulation tables
- [ ] Check: Each table note states DGP, n, replications, nominal level,
  tuning values and the meaning of each column.
- Why: Referees read and recompute simulation tables on their own.
- Status: candidate
- Scope: field:st
- Owner: sv-write-section, sv-review-once
- Src: guide:AJS/ecta-tables-figures@932eb23; guide:AJS/joe-tables-figures@932eb23

### ST-08 Tuning sensitivity shown
- [ ] Check: Results are shown across a range of each tuning parameter, with
  the chosen value and selection rule stated.
- Why: Cherry-picked tuning hides fragility.
- Status: candidate
- Scope: field:st
- Owner: experiment-workflow, sv-review-once
- Src: guide:AJS/ecta-robustness@932eb23; guide:AJS/joe-data-analysis@932eb23

### ST-09 Quick-read method block complete
- [ ] Check: A one-page summary of a statistics paper states model,
  assumptions, asymptotic properties and the finite-sample or simulation
  design.
- Why: These four are what a reader needs to judge whether the method
  applies to their data.
- Status: candidate
- Scope: field:st
- Owner: paper-quickread, study
- Src: guide:AJS/joe-identification-strategy@932eb23; guide:AJS/joe-data-analysis@932eb23

## Known disagreements
- "Identification" in econometrics guides means a one-to-one map from the
  data distribution to the parameter and is a named section; core
  statistics papers often fold this into the model definition or speak of
  identifiability and do not use the word for research design. Do not
  import the econometric section heading by default; decide per venue via
  sv-write-style-mine. [src: guide:AJS/ecta-identification@932eb23; guide:AJS/jbes-identification-strategy@932eb23] (candidate)
- How much empirical application is required: JBES expects a substantive
  application, the Journal of Econometrics treats it as an illustration, and
  AISTATS values a focused simulation over extra datasets.
  [src: guide:AJS/jbes-data-analysis@932eb23; guide:AJS/joe-data-analysis@932eb23; guide:AJS/aistats-experiments@932eb23] (candidate)
- Theorem in the abstract: tolerated at JBES when empirical relevance sits
  beside it; economics journals prefer a finding first.
  [src: guide:AJS/jbes-writing-style@932eb23] (candidate)

## Unknown
- JASA, JRSSB, Annals of Statistics and Biometrika have no AJS skills.
  Their conventions (paper structure, length of simulation sections,
  theorem style, reproducibility requirements) need the 5 to 10 exemplar
  route via sv-write-style-mine (`lessons-harvest --new-field stats`).
- Bayesian methodology conventions (prior sensitivity, computation
  diagnostics): no source read.
- Typical section lengths: not measured from exemplars.

## Changelog
- 0.1 (2026-10-13): stub created.
- 0.2 (2026-10-16): candidate rules from AJS @932eb23 (Econometrica, Journal
  of Econometrics, JBES, AISTATS skills); method block for quick reads;
  ST-01 to ST-09.
