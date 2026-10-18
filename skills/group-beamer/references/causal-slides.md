# Causal slides

Table of contents: card, roadmap, C-word, notation, DAGs.

Field names below are used as slide slots. Cite the sources; do not paste
their prose. Petersen and van der Laan (Epidemiology 2014); Lundberg,
Johnson, Stewart (ASR 2021); Hernan, "The C-Word" (AJPH 2018); Ding,
*A First Course in Causal Inference*, arXiv:2305.18793 (CC BY 4.0).

## Paper card

Question / Estimand / Identification / Key assumption / Main result /
Robustness / Biggest threat / External validity. Add "presenter's
interpretation" on Estimand when the paper is vague, and "what would
change my mind". An unstated estimand is itself a warning.

## Roadmap (one slide each when the paper is causal)

1. Target: unit, population, intervention, time; potential outcomes.
   If vague: pick one reading, write it in potential outcomes, label it
   presenter's interpretation; list alternatives in backup.
2. Identification: assumptions to a functional of the observed-data law.
   Mark each assumption knowledge-based vs convenience.
3. Estimation: estimator and uncertainty; not a substitute for
   identification.
4. Gap: the causal-to-statistical gap is not closed by a better estimator;
   only sensitivity analysis bounds it. "None reported" is a critique point.

## C-word rule

If the aim is causal, the question slide says so. Results slides report
the estimate and interval with no causal verb. The causal reading, with
the assumptions it needs, lives on the discussion slide. Flag causal
readings of covariate coefficients (Table 2 fallacy).

## Notation defaults (Ding, arXiv:2305.18793)

Units \(i=1,\ldots,n\); covariates \(X_i\); treatment \(Z_i\); outcomes
\(Y_i(1), Y_i(0)\); observed \(Y_i = Z_i Y_i(1)+(1-Z_i)Y_i(0)\).
\(\tau\) ATE (say finite-population vs super-population). \(\tau_T\) ATT,
\(\tau_C\) ATC. \(\mu_z(X)=E(Y\mid Z=z,X)\). \(e(X)=\mathrm{pr}(Z=1\mid X)\).
Ignorability \(Z \perp\!\!\!\perp \{Y(1),Y(0)\} \mid X\). IV: \(Z\)
assignment, \(D\) receipt, complier effect \(\tau_c\). Do not reuse \(U\)
for both compliance type and unmeasured confounding in one deck.

Translate the paper into this default on one notation slide, or keep the
paper's symbols and show the mapping once. Never mix both.

## DAGs

TikZ; solid observed, dashed or hollow counterfactual. Reuse
`sv-figure-design` outputs. Graphviz PDF only for large or changing graphs.
