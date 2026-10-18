# Transfer checks: mapping, assumptions, tests, forking paths

## Contents
1. Analogy mapping (relations, not surface features)
2. Assumption-transfer check
3. Common breaks by field
4. Cheapest falsifying test first
5. Expected result and kill criterion
6. Method shopping and the garden of forking paths
7. General mode (no project)
8. Sources

## 1. Analogy mapping (relations, not surface features)

A method works in its source because of relations between parts: which
units are compared with which, what is held fixed, what the assumptions
link. Map those relations to the project; similar-looking objects
("both are panels", "both are repositories") are not a mapping.
[src: lit:gentner1983] (confirmed)

Rows to fill, as far as the source has them:

| Element | Typical content |
|---|---|
| Unit | state, patient, repository, developer, model run |
| Treatment or input | what changes, and when; one date for all or staggered |
| Outcome or target | the measured quantity and its unit |
| Comparison | who stands in for the counterfactual |
| Time structure | pre and post periods, their number, spacing |
| Estimand | the population quantity the source estimates |
| Inference | standard errors, resampling, what dependence it allows |
| Scale | number of treated and control units, periods |

For each row write "where it breaks": the point at which the target
differs in a way that touches the method's mechanism. A break in the
treatment timing, the comparison or the estimand usually changes the
verdict; a break in scale changes the inference.

## 2. Assumption-transfer check

The source's evidence shows the method works under its assumptions in its
setting. Whether it works in the project depends on whether the
assumptions that carry the result hold there, and on what else the
project's setting needs ("it worked there" is not "it will work here").
[src: lit:cartwright2012] (candidate) Formal versions of this question
(when a causal result transports to a new population, and what must be
measured to transport it) exist for causal graphs. They need a selection
diagram and a transport formula; this skill only does the assumption-level
check and does not run do-calculus. [src: lit:pearl2014] (confirmed)

One row per assumption:

| Column | Rule |
|---|---|
| Assumption | label and location as in the source notes (for example "A2, Eq. 3.5") |
| Holds here? | yes / no / unknown; "yes" needs evidence |
| Evidence or check | the data look, test or argument that settles it; for "unknown", the cheapest check |
| If it fails | what goes wrong: bias, invalid standard errors, wrong estimand |
| Fix | variant, other estimand, robustness check only, or drop; literature verified or "to be checked" |

Also list assumptions the project needs that the source never had to make
(for example a new data-quality assumption), as extra rows.

Testable versus untestable: say which rows data can probe (pre-period fit,
balance, placebo) and which rest on argument (no anticipation, no
concurrent shock). An untestable row is decided by domain knowledge and
goes into the threats section if the method is adopted.

## 3. Common breaks by field

Not a checklist to run in full; a prompt for rows that are easy to miss.

- Causal panel methods (DID, synthetic control and their mixes): one
  adoption date versus staggered; few treated units (inference); treatment
  timing chosen because of a shock in the outcome; spillovers between
  units; outcome definition changing at adoption. The causal field profile
  asks for heterogeneity-robust estimators under staggered adoption and
  small-cluster corrections. [src: up:skills/research-core/references/fields/causal.md] (confirmed)
- SE and mining studies: selection of repositories by survivorship or
  popularity; tool adoption coinciding with other process changes;
  metrics whose meaning changes with the tool (a CI tool changes how bugs
  are found and labelled). [src: up:skills/research-core/references/fields/se.md] (confirmed)
- Statistics and ML: iid versus dependent data; model correctly specified
  or not; distribution shift between source benchmark and project data.
- Theory: the source's conditions (smoothness, compactness, rank) checked
  one by one against the project's objects, not by analogy.
- Coding, process and pipeline (added; mark rows 补): the source habit or
  toolkit is not an estimator. Common breaks: API contract (endpoint
  fields, auth, pagination or rate limits changed, so a copied client
  silently drops or duplicates records); data schema (column names, units,
  missingness codes, or join keys differ from the source notebook);
  random seeds and environment (library versions, default RNG, or
  hardware-dependent ops make a "same script" unreproducible); CI or
  metric definition drift (what counts as a failing test, a bug, or a gold
  label changed when the tool was adopted). A break here usually
  downgrades the verdict to use-with-modification or not-now until freeze
  and schema checks exist.

## 4. Cheapest falsifying test first

Design the test whose failure would end the bridge, and run it before
tests that could only confirm. Order by cost:

1. A check on data already in hand (pre-period fit, balance, weights
   concentrated on one unit).
2. A placebo: fake treatment date or fake treated units where the true
   effect is zero.
3. A known-answer simulation built from the project's own data shape.
4. A small pilot on a subset.
5. New data collection.

The idea of designing the experiment that excludes a hypothesis, rather
than one that merely agrees with it, is old. [src: lit:platt1964] (confirmed)

## 5. Expected result and kill criterion

Write both before running, in the card, with the date:

- Expected result: direction and the reason from the mapping or the
  source. A magnitude only with a source (the source paper's table, the
  project's numbers file); otherwise no magnitude.
- Kill criterion: the observation that ends or downgrades the bridge, in
  the metric of the test. When the question is "is there a meaningful
  effect", fix a smallest effect of interest and its justification first;
  an equivalence test can then show an effect is too small to matter.
  [src: lit:lakens2018] (confirmed)
- Inconclusive: what result counts as neither, and the next step for it.

Distinguishing tests of predictions from exploration that generates them
is the core of preregistration; the card is a light, private version of
that, not a registry entry. [src: lit:nosek2018] (confirmed) When the test
becomes a real experiment, `sv-experiment` writes the bar into the
run script and records changes as ADRs.

## 6. Method shopping and the garden of forking paths

Trying several methods, specifications or samples and keeping the one that
gives the hoped-for result inflates false positives even without any
conscious fishing. [src: lit:gelman2014; lit:simmons2011] (confirmed)
Guards in the card:

- List every variant to be tried (estimators, windows, samples) before the
  test; report all of them.
- A new method enters as a robustness check unless the mapping and
  transfer tables give a reason to prefer it that does not depend on its
  result.
- If the bridge was motivated by a disappointing result of the current
  method, say so in the card; that is the situation in which shopping is
  most tempting.

## 7. General mode (no project)

When there is no project, the card answers "what kind of project could use
this?":

- Portable core: the mechanism in one sentence, in project-neutral words.
- Fits when: the structural conditions from the mapping rows (for example
  "a few treated units, many controls, long pre-period").
- Does not fit when: the breaks that kill it.
- Assumptions to check in any project: the transfer table with "holds
  here?" left as the question to ask.
- A test template: the cheapest falsifying test, with slots for data,
  metric and kill criterion.

## 8. Sources

Bibliographic records checked 2026-10-17. Full texts were not re-read for
this polish. Cartwright and Hardie remains candidate (book).

- lit:gentner1983: Gentner, D. (1983). Structure-mapping: A theoretical
  framework for analogy. Cognitive Science, 7(2), 155-170.
  DOI 10.1207/s15516709cog0702_3 (confirmed)
- lit:cartwright2012: Cartwright, N., and Hardie, J. (2012). Evidence-Based
  Policy: A Practical Guide to Doing It Better. Oxford University Press.
  ISBN 9780199841622 (candidate; full text not verified)
- lit:pearl2014: Pearl, J., and Bareinboim, E. (2014). External validity:
  From do-calculus to transportability across populations. Statistical
  Science, 29(4), 579-595. DOI 10.1214/14-STS486 (confirmed)
- lit:platt1964: Platt, J. R. (1964). Strong inference. Science, 146(3642),
  347-353. DOI 10.1126/science.146.3642.347 (confirmed)
- lit:lakens2018: Lakens, D., Scheel, A. M., and Isager, P. M. (2018).
  Equivalence testing for psychological research: A tutorial. Advances in
  Methods and Practices in Psychological Science, 1(2), 259-269.
  DOI 10.1177/2515245918770963 (confirmed)
- lit:nosek2018: Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor,
  D. T. (2018). The preregistration revolution. PNAS, 115(11), 2600-2606.
  DOI 10.1073/pnas.1708274114 (confirmed)
- lit:gelman2014: Gelman, A., and Loken, E. (2014). The statistical crisis
  in science. American Scientist, 102, 460-465.
  https://www.americanscientist.org/article/the-statistical-crisis-in-science
  (confirmed article page)
- lit:simmons2011: Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011).
  False-positive psychology. Psychological Science, 22(11), 1359-1366.
  DOI 10.1177/0956797611417632 (confirmed)
