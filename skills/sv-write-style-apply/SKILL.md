---
name: sv-write-style-apply
description: >-
  Applies a mined style profile to a manuscript without adding facts or
  changing technical content: section-by-section revision with diagnosis,
  revision and a per-paragraph log of rule candidates, or a report-only venue
  and field fit check for sv-review-loop round 2. Needs a dynamic writing skill
  from the sv-write-style-mine sub-command. Use when revising a paper for a target
  venue or asking whether a draft fits it.
license: MIT
disable-model-invocation: true
---

# sv-write-style-apply

Formerly the apply loop of `style-mine`. Before anything, load the hard
rules and follow the Step 0 and input check of
`../sv-write-style-mine/references/procedure.md`. When no dynamic writing
skill exists for the destination, run `sv-write-style-mine` Build first and
wait for the human gate.

See: ../sv-write-style-mine/references/hard-rules.md
See: ../sv-write-style-mine/references/procedure.md
See: ../sv-write/references/faithfulness.md

| Mode | Trigger | Section below |
|---|---|---|
| Revise | "revise my paper for <venue>" | Phase 2 |
| Check | called by `sv-review-loop`, or "does this fit the venue?" | Check mode |

## Phase 2: Manuscript revision

Load only the dynamic skill and the manuscript. For each section: Round 1
diagnosis (problem type, severity, rule, venue match score 1 to 5), Round 2
revision under P1 to P5 with no new content, Round 3 a per-paragraph log
with a "Rule candidate" field. Collect rule candidates in
`revision_summary.md`; they feed `sv-supervisor-harvest`.

LaTeX sources in a git repo may be edited in place with a minimal diff when
the user agrees; otherwise output Markdown sections.

See: references/revision-phase.md

## Check mode (sv-review-loop round 2)

Report-only. Inputs: target sections, the dynamic skill (or, if missing, the
venue and field profiles with reduced coverage), ADRs and the term table,
and the round number from `sv-review-loop`. Check structure, lengths against
budget, contribution format, results paragraph shape, tone, citation form
and the P5 phrases. Each finding gets `JA-r<round>-<nn>`, a location, the
rule it deviates from (`DS-nn` with support, or a profile rule with its
source), observed vs expected, severity and status (`open`, `locked`,
`advisory`, `repeat`). Never edit; return the report to `sv-review-loop`, or
write `docs/log/<date>-style-mine-check.md` when run alone.

See: references/check-mode.md


## Hand-offs

- Rule candidates from the revision logs: `sv-supervisor-harvest`.
- Multi-round checks and applying check findings: `sv-review-loop`.
- AI tells beyond the P5 list: `sv-write-humanize-paper`.
- Missing content found in diagnosis: `sv-write-section`, `sv-write-intro`.
