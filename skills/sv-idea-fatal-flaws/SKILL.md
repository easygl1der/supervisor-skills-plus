---
name: sv-idea-fatal-flaws
description: >-
  Runs only the early gate of the idea evaluation: the audit against the ten
  canonical fatal flaws (no novelty against the closest work, wrong venue,
  wrong baseline, weak motivation, capability mismatch, unverifiable claim,
  ethical or data blocker, scope, solution hunting, no failure case), at
  most two flaws reported with detection rule and defense. Use when the
  user wants a quick check before a full evaluation.
license: CC-BY-4.0
disable-model-invocation: true
---

# sv-idea-fatal-flaws

Load `../sv-idea/references/procedure.md`, follow Step 0, Step 1 and
"Step 2: Fatal-flaws audit (early gate)" with `fatal-flaws.md`, then stop
and report in the output format's sections 1 and 2. A data-refuted core
mechanism locks the verdict, as the procedure says. Otherwise offer
`sv-idea-evaluate` for the full scoring.

See: ../sv-idea/references/procedure.md
See: ../sv-idea/references/fatal-flaws.md
