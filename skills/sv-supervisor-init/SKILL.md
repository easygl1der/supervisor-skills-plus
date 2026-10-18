---
name: sv-supervisor-init
description: >-
  Starts a research project: interviews the user one short block at a time
  (field, paper type, stage, venue and deadline with its official source,
  repositories and the one writable source of truth, data and compute,
  records and co-author note macros), writes research.yaml after showing
  the diff, and sets up docs with STATUS, TODO, ADR 0001 and logs. Use when
  a project or repository has no research.yaml yet.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-supervisor-init

Init of the former `research-supervisor` plus Task 1 of the former
`sv-supervisor-records`.

1. Run "Step 1: Init" of `../sv-supervisor/references/procedure.md`: the
   five question blocks, then copy research-core
   `assets/templates/research.yaml`, fill it, and show the diff before
   writing. "unknown" is an accepted answer.
2. Run "Task 1: Initialize" of
   `../sv-supervisor-records/references/procedure.md`: ask before creating
   `docs/`, copy the templates, fill Sources of truth in STATUS, write ADR
   0001, add private paths to `.gitignore`.
3. A field with no profile loads `_template.md`; offer
   `sv-write-style-mine` to build one.

See: ../sv-supervisor/references/procedure.md
See: ../sv-supervisor-records/references/procedure.md

## Hand-offs

- After init, the first brief: `sv-supervisor-brief`.
