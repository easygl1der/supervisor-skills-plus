---
name: sv-write-skeleton
description: >-
  Plans a paper's logic skeleton before any prose. Technique and new-problem
  papers get the thinking-template table and four self-consistency checks;
  benchmark papers get the five-pillar audit, the six-part Introduction chain
  and a Section 2 to 7 outline; RQ-driven empirical studies get the empirical
  skeleton. Use when the user asks for a paper skeleton, logic chain, thinking
  template, or a benchmark plan before writing.
license: CC-BY-4.0
disable-model-invocation: true
---

# sv-write-skeleton

Formerly `tech-paper-template` and `benchmark-paper-template`; their full
text is in `references/technique.md` and `references/benchmark.md`.

## Pick the route, then load only its files

Decide the paper type from `research.yaml` `paper_type`, or from the user's
material, and say which route was taken.

| Paper type | Load | Output |
|---|---|---|
| `technique`, or new problem or setting (AI/ML, systems, databases) | `technique.md`, `paper-types.md`, `thinking-template.md`, `consistency-checks.md`; `worked-examples.md` only when an example helps | Positioning, thinking template, four checks, severity summary |
| `benchmark` | `benchmark.md`, then per pillar: `gap-analysis.md`, `benchmark-design.md`, `construction-pipeline.md`, `experiments.md`, `paper-structure.md`; `checklist.md` for the self-check; `instantiation-template.md` when the user wants a fillable form | Five-pillar table, Introduction chain, Section 2 to 7 outline, unresolved Critical and Major items |
| `empirical-study` (RQ-driven mining, survey, qualitative) | `../sv-write/references/empirical-study-skeleton.md` and the field profile's "Typical structure" | Section skeleton with one RQ block per question |
| `theory`, or `field: math` | Hand to `sv-write-section` (math route) | |

`orchestrator-notes.md` is historical context only; do not load it for a
task.

See: references/technique.md
See: references/benchmark.md
See: ../sv-write/references/empirical-study-skeleton.md

## Rules

- A benchmark found while on the technique route stops and switches route,
  as `technique.md` Step 1 says.
- Every failed consistency check is CRITICAL and is fixed in the plan, not
  in prose.
- The skeleton is a working document for the author and advisor; nothing
  from it is pasted into the manuscript.

## Hand-offs

- Skeleton passes: `sv-write-intro` for the Introduction, `sv-write-section`
  for the other sections.
- The idea itself is unvetted: `idea-evaluator`.
