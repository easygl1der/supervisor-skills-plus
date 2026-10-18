---
name: sv-supervisor
description: >-
  Entry point for running a research project: a start-up interview that
  writes research.yaml and docs, a session brief with stage, deadline,
  blockers and next skills, project records (STATUS, TODO, decisions, logs),
  and lessons harvested into research-core. Routes to one sv-supervisor sub-
  command and says which. Use when starting a session or project, or
  updating records.
license: CC-BY-NC-SA-4.0
---

# sv-supervisor

## Overview

Router of the project group (ADR 0021). It picks one sub-command, says so
in one line ("Routing to `sv-supervisor-brief`: read-only session brief."),
loads that sub-command's SKILL.md and follows it. Sub-commands can also be
called directly; they are not auto-selected.

## Routing table

| The user says | Sub-command |
|---|---|
| where are we, what next, start of a session, which skill fits; a reading or learning request | `sv-supervisor-brief` |
| new project, this repo has no `research.yaml` | `sv-supervisor-init` |
| update STATUS or TODO, record a decision (ADR), sources of truth, sync guard, de-accrete docs, Linear mirror, log a group meeting | `sv-supervisor-records` |
| harvest lessons at a milestone, propose rules for research-core, start a new field profile | `sv-supervisor-harvest` |

The former `sv-supervisor` text is in `references/procedure.md`, its
brief script in `scripts/session_brief.py`.

See: references/procedure.md

## Hand-offs outside this group

- The work itself: `sv-write`, `sv-review`, `sv-feedback`, and the skills
  the brief's routing table names.
