# ADR 0015: Reading and learning requests route by intent, without research.yaml

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner (SPEC item 2), lead agent (routing text in progress)

## Context
`research-supervisor` routes by project stage read from `research.yaml`, and
runs init when the file is missing. A request such as "read this paper" or
"explain this chapter" has no project stage and should not trigger init
(SPEC item 2).

## Options considered
1. Require `research.yaml` for every request: forces init for a one-off read.
2. Separate router for reading skills: two entry points.
3. One router; reading and learning intent is checked before stage logic.

## Decision
Option 3. Reading and learning requests route to `paper-quickread`, `study`,
`deep-research` (literature-map mode) or `research-bridge` (also
`proposal-writer` and `style-mine` in the current draft) without requiring
`research.yaml` and without init. An explicit reading or learning intent wins
over the stage table; when a project exists its stage is mentioned in one line.
Project-stage routing applies only when `research.yaml` exists.

## Consequences
- Reading skills work in any directory.
- The `deep-research` literature-map mode named here is not yet present in
  `skills/sv-litreview/` in the working tree.

## Do not
- Do not run init for a reading or learning request.

## Sources
`skills/research-supervisor/SKILL.md` (working-tree draft, "Reading and learning:
route by intent"), SPEC item 2 and D16, `DESIGN.md` (reading skills paragraph).
