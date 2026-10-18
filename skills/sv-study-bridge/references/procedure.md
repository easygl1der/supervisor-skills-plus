<!-- Moved from skills/sv-study-bridge/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Research Bridge

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Workflow
- Checklist
- Outputs
- Evals
- Hand-offs
- Sources

## Overview

Reading and studying produce understanding; a project needs a decision.
This skill turns one source (a paper card from `sv-quickread`, notes from
`sv-study`, a concept note in the study vault) into a one-page **bridge card**
for the current project:

1. **Can it be used here?** A verdict from five: use as the main method,
   use with a named modification, use as a robustness check only, not now
   (a precondition is missing), or no.
2. **How?** Which step of the project's pipeline it replaces or adds, and
   what changes in data, estimand or claims.
3. **The cheapest test that could prove the bridge wrong**, written before
   anything runs: data, metric, expected result, kill criterion.

Three habits make the card worth more than a gut feeling
(`transfer-checks.md`):

- **Map relations, not surface features.** A source method works because of
  a structure (who is treated, what is compared, what is assumed); the
  mapping table says where that structure exists in the project and where
  the analogy breaks. [src: lit:gentner1983] (confirmed)
- **Assumptions travel, results do not.** Every identifying or modelling
  assumption of the source is checked against the project's setting with
  evidence; a result proved or measured in the source is never quoted as if
  it held in the project. Formal transport formulas need a selection
  diagram and are not solved here. [src: lit:cartwright2012] (candidate);
  [src: lit:pearl2014] (confirmed)
- **Decide before you look.** Expected result, kill criterion and the list
  of variants to try are fixed before the test runs, so a method is not
  kept because one of many tries looked good. [src: lit:nosek2018; lit:gelman2014] (confirmed)

The skill does not score novelty or feasibility (`idea-evaluator`), run or
freeze experiments (`experiment-workflow`), or write decision records
(`sv-supervisor-records`). It prepares their inputs and hands off.

Default output language is Chinese with technical terms in English; it
follows the user's language.

## When to use this skill

- After `sv-quickread` or `sv-study`: "can I use this in my project?",
  "how would this apply to my data?", or the same question in Chinese.
- Choosing between a method the project uses now and one just read about.
- A reviewer or advisor suggested a method and the user wants to know
  whether it fits before spending time on it.
- Section 9 of a quickread card ("link to my research") needs to become
  concrete.

## When NOT to use this skill

- Understanding the method itself is still shaky (the learner profile says
  "not studied" or the user cannot state its assumptions): `sv-study` first.
- No card or notes exist yet for the source: `sv-quickread` first. This
  skill does not read PDFs.
- Judging whether a whole new research idea is worth a paper:
  `idea-evaluator`.
- Running, logging or freezing the validation experiment:
  `experiment-workflow`.
- Surveying many methods for the project: `deep-research`.

## Step 0: Load context

1. Load `research-core`: `references/core/claims-evidence.md`,
   `references/core/integrity.md` (bars fixed before results), the field
   profile of the project (`research.yaml` `field`) and of the source when
   it differs (for example a causal method entering an SE project), and the
   design-time items of the checklist `threats.md`.
2. Read `research.yaml`: `project`, `field`, `subfield`, `paper_type`,
   `stage`, `experiments`, `data`; then the RQs and current blockers in
   `docs/STATUS.md` and the ADR index in `docs/adr/README.md`, so the card
   does not contradict a locked decision without saying so.
3. **No `research.yaml`**: ask one question, "what is the current project in
   one or two sentences (question, data, current method or blocker)?". If
   the user answers, continue with that as the project. If the user
   declines or has no project yet, switch to **general mode**: the card
   lists the kinds of projects the source fits, its portable assumptions,
   and a test template, and writes no project-specific verdict.
4. Resolve the reading root as `sv-quickread` does (`research.yaml`
   `reading.dir`, `<project>/reading/`, `$STUDY_VAULT`, `./reading/`) and
   say which one was used.

## Workflow

### Step 1: Collect the source, with locations

Read what exists for the source, in this order: `quickread.md` (sections
3, 4 and 8), `method.md`, `insights.md`, `reflection.md`, the concept note
`concepts/method-<name>.md`, the learner's entry in
`profile/knowledge.yaml`, and any recorded misconception about the method
in `profile/misconceptions.md` (the card addresses it when it touches a
transfer row). Find the folder through `index.json` when the
user names only the paper. Note for each fact the location in the source
(section, equation, table) as the card or notes record it. Do not re-derive
or extend the source's claims; open questions stay open (copy items marked
"not checked" or "pending" as such).

If the learner's `proficiency_ai` for the method is missing or below
"can use", say so in one line and offer `sv-study`; continue only if the user
wants to.

### Step 2: Pin the target

In one line each, from `research.yaml`, STATUS and what the user said:
research question, unit and sample, treatment or intervention (or input),
outcome or target quantity, current method, and the pain point the source
is supposed to fix. If the source addresses none of the project's pain
points, say so: "no bridge" is a valid result and ends the card early.

### Step 3: Map source to target

Fill the mapping table: each structural element of the source (units,
treatment timing, outcome, comparison, time structure, estimand,
inference) against its counterpart in the project, with a column for where
the analogy breaks. A break in a structural element (for example block
versus staggered timing) is a finding, not a footnote.

### Step 4: Assumption-transfer check

One row per assumption of the source, copied with its label and location:
holds in the project (yes, no, unknown), the evidence or the check that
would settle it, the consequence if it fails, and the fix (a variant, a
different estimand, a robustness check, or drop the method). Literature
for a fix (an extension, a variant) is cited only after it is verified;
otherwise the row says "variant to be checked" and the check goes to
`deep-research`. Mark own reasoning as added (Chinese label in the card).

See also `transfer-checks.md`

### Step 5: Verdict and how

Pick one of the five verdicts with a "because" naming the decisive rows of
steps 3 and 4. Then say how: the pipeline step that changes (before and
after), what the claim in the paper would become (scope words from
`claims-evidence.md`), and what the method does not buy. Keep a robustness
check honest: it is reported whatever it shows.

### Step 6: Minimal validation experiment

Design the cheapest test that could kill the bridge, before any test that
could only confirm it. Write it pre-registration style:

- **Question**: the one assumption or claim it tests, and which transfer
  rows it does not test.
- **Data**: existing data or a subset first; a placebo, a known-answer
  simulation or a pre-period split before new collection.
- **Procedure and metric**: the estimator or script, the metric, the
  variants to be tried, all listed now.
- **Expected result**: direction and the reason; a magnitude only with a
  source, otherwise none.
- **Kill criterion**: the observation that ends the bridge or downgrades
  the verdict, fixed now; a minimum effect of interest when a size matters.
- **Next step per outcome**: pass, fail, inconclusive.
- **Budget**: hours of the user's time, and what is reused.

Numbers in the card come from the source or from the project's numbers
file; never invent a value or an effect size.

See also `bridge-card.md`

### Step 7: Save

With a project: `docs/notes/YYYYMMDD-bridge-<slug>.md` with
`status: scratch`, following the `sv-supervisor-records` notes lifecycle. In
general mode: `bridge.md` in the source's paper folder (or next to the
concept note). Link back to the source files. In an environment that
cannot write files, print the card.

### Visuals (optional)

A before and after picture of the project pipeline with the new step
highlighted helps when the user asks for it or the change touches more than
two steps. Use the `sv-study` kit (`skills/sv-figure-explain/kit/`, rules in
`skills/sv-figure-explain/references/visuals.md`, pattern list in
`skills/sv-figure-explain/references/visual-scenarios.md`, row "learning applied":
small multiples plus a state-machine replay) and embed the PNG. Never
required; the card stands without it.

## Checklist

Report pass, fail or n/a with evidence:

- Source files read are listed; every source fact carries its location;
  "not checked" items from the source stay marked.
- Target pinned in one line per element, from `research.yaml`, STATUS or the
  user (or general mode stated).
- Mapping table has a "where it breaks" entry for every row (or "none
  found" with the reason).
- Every source assumption has a transfer row with evidence or the check
  that would settle it; own reasoning marked as added.
- Verdict is one of five and names the decisive rows.
- Validation test: expected result and kill criterion written before
  running; variants listed; no invented numbers; cheapest falsifying test
  first.
- Cited extensions or variants verified, or marked to be checked.
- Locked ADRs respected, or the conflict named.
- Design-time items of `threats.md` relevant to the change (alternative
  explanations, data gaps) reported as pass, fail or unknown.

## Outputs

```
<project>/docs/notes/YYYYMMDD-bridge-<slug>.md     with a project
<reading-root>/papers/<paper>/bridge.md            general mode
<same folder>/fig-bridge-*.html, .png              optional figure
```

The card itself: source and target, mapping table, assumption-transfer
table, verdict with how, validation test, hand-offs.

## Evals

Worked cards (real outputs, not stubs) live in `evals/`: project-mode
SDID, general-mode MLE, and a non-estimator process bridge (notebook
habit to `experiment-workflow`). `skills/sv-study/evals/bridge/` is a
pointer to those paths. Shared reading notes stay under
`skills/sv-study/evals/reading/`.

This skill does not compute Pearl-Bareinboim transport formulas or run
do-calculus. The card checks assumptions at mapping level only.

## Hand-offs

- The bridge shapes a new idea or changes the paper's scope:
  `idea-evaluator` (the card's mapping and transfer tables are its input).
- The validation test is to be run: `experiment-workflow` (freeze data,
  write the bar into the run script, log the run).
- Adopting or rejecting the method is decided: `sv-supervisor-records` (ADR
  with the rejected alternative; the card is the context).
- An assumption or a variant needs literature: `deep-research`.
- The method itself is not yet understood: `sv-study`.
- No card for the source yet: `sv-quickread`.

## Sources

Bibliographic records checked 2026-10-17; full texts were not re-read for
this polish. Cartwright and Hardie remains candidate (book; ISBN only).

- lit:gentner1983: Gentner, D. (1983). Structure-mapping: A theoretical
  framework for analogy. Cognitive Science, 7(2), 155-170.
  DOI 10.1207/s15516709cog0702_3 (confirmed)
- lit:cartwright2012: Cartwright, N., and Hardie, J. (2012). Evidence-Based
  Policy: A Practical Guide to Doing It Better. Oxford University Press.
  ISBN 9780199841622 (candidate; full text not verified)
- lit:pearl2014: Pearl, J., and Bareinboim, E. (2014). External validity:
  From do-calculus to transportability across populations. Statistical
  Science, 29(4), 579-595. DOI 10.1214/14-STS486 (confirmed)
- lit:nosek2018: Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor,
  D. T. (2018). The preregistration revolution. PNAS, 115(11), 2600-2606.
  DOI 10.1073/pnas.1708274114 (confirmed)
- lit:gelman2014: Gelman, A., and Loken, E. (2014). The statistical crisis
  in science. American Scientist, 102, 460-465.
  https://www.americanscientist.org/article/the-statistical-crisis-in-science
  (confirmed article page; no single Crossref DOI used here)
