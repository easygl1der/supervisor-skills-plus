---
name: sv-supervisor-brief
description: >-
  Gives a read-only session brief for a research project: the stage in
  research.yaml and the stage the repository signals suggest, the next
  deadline with its source, blockers, overdue guidance, open reviewer
  markers and records warnings, then routes to one to three skills with a
  reason each. Routes reading and learning requests by intent. Never does
  the work. Use when starting a session or asking what to do next.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-supervisor-brief

The session part of the former `research-supervisor`. Load
`../sv-supervisor/references/procedure.md` and run, in order:

1. "Reading and learning: route by intent" when the request is about
   reading, learning or a proposal (no `research.yaml` needed, no init).
2. "Step 0: Load context".
3. "Step 2: Session brief", from the repository root:
   `python skills/sv-supervisor/scripts/session_brief.py <project_dir> [--paper-dir paper/]`.
   Show at most 12 lines: stage, deadline with source and days left,
   blockers, overdue guidance, open markers, records warnings.
4. "Step 3: Route" and "Step 4: Hand off". Stop there.

When `research.yaml` is missing and the request is not about reading or
learning: `sv-supervisor-init`.

See: ../sv-supervisor/references/procedure.md

## Rules

- Never change `stage` without the user; show both stages when they differ.
- A missing deadline source or missing STATUS is reported, not filled in.
- Records edits go through `sv-supervisor-records`; this sub-command writes
  nothing.
