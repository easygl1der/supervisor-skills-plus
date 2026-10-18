---
name: sv-idea
description: >-
  Entry point for judging a research idea: a full evaluation with first
  impression, fatal-flaws gate, lifecycle and capability matching,
  five-dimension scoring, paradigm-shift probe, feasibility and a verdict, or
  only the fatal-flaws gate when time is short. Routes to one sv-idea
  sub-command and says which. Use when the user asks whether an idea is
  worth pursuing, novel enough, or fatally flawed.
license: CC-BY-4.0
---

# sv-idea

Router of the idea group (ADR 0021). The full procedure, unchanged from the
former `sv-idea`, is `references/procedure.md`.

| The user says | Sub-command |
|---|---|
| evaluate this idea, is it worth a paper, score it, which venue tier | `sv-idea-evaluate` |
| any fatal flaw, quick sanity check, kill it early | `sv-idea-fatal-flaws` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md

## Hand-offs outside this group

- Literature for novelty: `sv-litreview`.
- A plan or proposal after a pass: `sv-proposal`.
- The paper skeleton after a pass: `sv-write-skeleton`.
