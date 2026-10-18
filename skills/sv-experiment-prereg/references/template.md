# Pre-registration template

Copy to `docs/prereg/YYYY-MM-DD-<topic>.md` in the project, fill every
section, then freeze. Fields marked (CI) come from the research-core causal
profile and apply when `field: causal`; drop them otherwise. Adapted from
the pre-registration template of K-Dense-AI/science-superpowers (MIT).

## Contents

- Header
- Question and estimand
- Hypotheses and prediction
- Primary analysis
- Decision rule
- Sample size and stopping
- Multiplicity
- Secondary and exploratory analyses
- Deviations

```markdown
# Pre-registration: <topic>

**Frozen at commit:** <stamped by prereg.sh freeze>
**Project decision record:** docs/adr/<NNNN>-<...>.md (optional)
**Data freeze:** sv-experiment-freeze manifest or runs.md row (optional)

## Question and estimand
- Question: <one sentence>
- Estimand (CI): <population quantity, for example the average effect of
  treatment on <outcome> among <population>; point or set identified>
- Identifying assumptions (CI): A1 <...>; A2 <...>; what breaks without each

## Hypotheses and prediction
- H0: <...>
- H1 (directional where justified): <...>
- Predicted direction and, if prior work gives one, magnitude with source

## Primary analysis (exact)
- Model or test: <for example OLS: y ~ d + x1 + x2, HC2 errors>
- Variables and their construction: <...>
- Transformations: <...>
- Inclusion and exclusion rules: <fixed now>
- Covariates: <fixed now>
- Software and version: <...>

## Decision rule
- Supports H1 if: <exact criterion>
- Does not support H1 if: <exact criterion>
- The result that would disconfirm the prediction: <stated, so the
  registration is falsifiable>

## Sample size and stopping
- N (fixed) or the pre-specified sequential design: <...>
- Power: <...> at alpha <...> for effect <...> (source of the effect size)
- No optional stopping; no peek-and-extend.

## Multiplicity
- Number of confirmatory tests: <...>
- Correction: <Bonferroni, Holm, a single pre-specified primary, ...>

## Secondary and exploratory analyses
- <listed now; reported under an Exploratory heading, never as confirmatory>

## Deviations
- Any deviation is reported with its reason and makes the affected
  analysis exploratory.
```
