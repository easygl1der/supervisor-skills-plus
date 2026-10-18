---
name: sv-experiment
description: >-
  Entry point for experiments whose printed numbers must be traceable:
  freezing corpus, samples, gold sets and model or prompt versions, the runs
  log, numbers checked into the paper, and the replication artifact. Routes
  to one sv-experiment sub-command and says which. Use when setting up,
  running, reporting or packaging experiments.
license: CC-BY-NC-SA-4.0
---

# sv-experiment

Router of the experiment group (ADR 0021). The full procedure, unchanged
from the former `experiment-workflow`, is `references/procedure.md`
(Steps 0 to 10, checklist); its scripts are in `scripts/`.

| The user says | Sub-command |
|---|---|
| freeze the corpus, sample, gold set, annotation, acceptance bar, prompt or model version | `sv-experiment-freeze` |
| log this run, runs log, state files | `sv-experiment-runs` |
| numbers in the paper, check numbers, verified numbers, STATUS numbers | `sv-experiment-numbers` |
| replication package, artifact, anonymous mirror, where data lives | `sv-experiment-replication` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md

## Hand-offs outside this group

- Decisions about the design: `sv-supervisor-records` (ADR).
- Results figures: `sv-figure-plot`.
