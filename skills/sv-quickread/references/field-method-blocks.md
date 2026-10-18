# Method block by field (section 4 of the quickread)

## Contents
1. How to pick the block
2. Blocks by field
3. Blocks by paper type (any field)
4. Assumption list conventions

## 1. How to pick the block

Use the paper's field from Step 2. When the research-core field profile has
a "Method block for quick reads" subsection, it overrides the short version
here. A paper spanning two fields (for example causal ML) uses the stricter
block (causal) and adds one line from the other.

## 2. Blocks by field

| Field | The method block must state | Common traps |
|---|---|---|
| Causal inference | Estimand (ATE, ATT, LATE, CATE, a policy value), identifying assumptions with their names (unconfoundedness, overlap, exclusion, parallel trends, no interference), the estimator (regression, IPW, AIPW/doubly robust, IV/2SLS, DiD, synthetic control, RD), inference (standard errors, bootstrap, placebo or permutation), and which assumption is testable | Calling an estimator an estimand; dropping overlap; reporting a LATE as an ATE |
| Statistics | Model and parameter of interest, assumptions (independence, moments, sparsity, regularity), estimator, asymptotic results (consistency, rate, limiting distribution, efficiency), finite-sample or simulation design (n, replications, data-generating process) | Treating a simulation as proof; omitting the rate's conditions |
| Mathematics | Main theorem(s) in one line each, the chain of lemmas that leads to them, the key idea of the proof (the one step that does the work), what is new versus cited | Restating the abstract instead of the theorem; losing hypotheses |
| Software engineering | RQs, data (source, sampling frame, time window, size as printed), method (mining pipeline, coding scheme, statistics), validity threats (construct, internal, external, conclusion) and how each is handled | Dropping the denominator; mixing tool claims with empirical findings |
| AI/ML | Task and setting, architecture or algorithm, training data and compute, baselines, evaluation metrics and benchmark, ablations | Calling a benchmark gain a general capability; missing seeds and variance |

Sources: causal and statistics blocks follow the research-core profiles
`causal.md` and `stats.md` (econometrics-journal guidance, status
candidate); SE follows `se.md`; AI/ML follows `ai-ml.md`; mathematics
follows `math.md` and the owner's `paper` skill. [src: up:skills/research-core/references/fields/se.md; skill:paper] (candidate)

## 3. Blocks by paper type (any field)

| Type | Replace or add |
|---|---|
| Theory | Section 5 becomes a theorem table; section 4 gives the proof route (for asymptotics: consistency, then rate, then distribution, then variance estimation) |
| Survey | Section 4 states the taxonomy axes; section 5 lists the comparison tables' headings, not values |
| Benchmark | Section 4 states construction and validity checks of the benchmark; section 5 copies headline numbers with the evaluation protocol |
| Position | Sections 5 and 7 note that claims are argued, not tested |

The proof route for asymptotic results is the order in which econometrics
theory papers present them. [src: guide:AJS/joe-writing-style] (candidate)

## 4. Assumption list conventions

- Number assumptions as the paper does (Assumption 1, A2, (C1)); if the
  paper does not number them, write A1, A2 and mark "编号为补".
- One line per assumption in plain words, then the symbol form if short.
- Mark each as testable, partly testable, or untestable, and say how the
  paper checks it (placebo, pre-trends, first-stage F, balance table) or
  that it does not.
- An assumption used in a theorem but stated only in an appendix is listed
  with its appendix location.
