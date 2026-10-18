---
name: sv-supervisor-records
description: >-
  Keeps a research project's records outside the paper: STATUS with the
  current state only, TODO, numbered decision records, dated logs and
  group-meeting logs, sources of truth for paper, data and numbers with a
  sync guard, the notes lifecycle, de-accretion of docs, and an optional
  Linear mirror. Use when updating status, recording a decision, naming a
  source of truth, syncing a co-edited paper, or cleaning up project docs.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-supervisor-records

Formerly `research-records`. The full procedure, unchanged, is
`references/procedure.md`; load it and follow its Step 0.

## Load by task

| Task | Section of `procedure.md` | Also load |
|---|---|---|
| Update status (replace, never append) | Task 2 | |
| Record a decision | Task 3 | `adr.md` |
| Sources of truth and syncs | Task 4 | `sources-and-sync.md`; `scripts/sync_guard.py <repo> <remote> <branch>` |
| Notes lifecycle | Task 5 | |
| De-accrete docs | Task 6 | `anti-accretion.md` |
| Linear mirror (optional) | Task 7 | `linear-mirror.md` |
| Group-meeting decks and logs | Task 8 | `group-meetings.md` |
| A new project's `docs/` | Task 1, via `sv-supervisor-init` | |

See: references/procedure.md
See: references/adr.md
See: references/sources-and-sync.md
See: references/anti-accretion.md
See: references/linear-mirror.md
See: references/group-meetings.md

## Hand-offs

- Lessons from the records at a milestone: `sv-supervisor-harvest`.
- What to do next: `sv-supervisor-brief`.
