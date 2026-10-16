# ADR 0003: paper-quickread has nine fixed sections, 700 target, 900 cap

Status: accepted
Date: 2026-10-16
Deciders: owner (SPEC §3 overview length, open question 3), Claude Code (numbers after a real-paper test)

## Context
The SPEC set a one-page overview of at most 700 Chinese characters and left
the limit open until tested on a real paper. The SDID eval
(`skills/study/evals/reading/papers/2026-10-16_arkhangelsky_sdid/quickread.md`)
needed method, claim and limitation content that a hard 700 cut squeezed out.
Free-form summaries also vary too much to compare across papers.

## Options considered
1. Hard limit 700, free layout: strict but cut needed content in the test.
2. No length limit: cards grow into reviews.
3. Nine fixed sections, target 700, hard cap 900, checked by a script.

## Decision
Option 3. `skills/paper-quickread/references/template-9.md` fixes nine sections
(meta and two tags; problem; core idea; field method block; results table;
contributions with proved/empirical/conjectured/cited tags; claim-evidence
table; limitations in two columns; relevance) with a per-section budget.
Body text outside tables and formulas: target 700 Chinese characters (450
English words), hard cap 900 (600 words). `scripts/check_quickread.py` checks
heading order, two tags, the length (error above 900, warning above 700),
sourced results rows, 3 to 5 tagged contributions and the limitations table.

## Consequences
- Every card has the same shape, so `deep-research` and `study` can read them.
- Tables do not count, so detail moves into tables rather than prose.
- The checker counts CJK characters plus English words against one number
  (default 900); the 600-word English cap is not enforced unless
  `--max-chars 600` is passed.

## Do not
- Do not add a tenth section or drop one; mark it empty with a reason instead.

## Sources
`skills/paper-quickread/references/template-9.md` §1,
`skills/paper-quickread/scripts/check_quickread.py`, `skills/paper-quickread/SKILL.md`,
SPEC lines on the 700 overview and open question 3.
