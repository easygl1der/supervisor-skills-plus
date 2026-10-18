---
name: sv-review
description: >-
  Entry point for reviewing a manuscript before it leaves the group: a
  one-time pre-submission audit across five dimensions with research-core
  sub-checklists, a devil's-advocate pass and a submission-day runbook, or a
  bounded multi-round check of research fit, venue style and language with a
  round log. Routes each request to one sv-review sub-command and says which.
  Use when the user asks to review, audit, proofread or re-check a draft.
license: CC-BY-NC-SA-4.0
---

# sv-review

## Overview

Router of the review group (ADR 0021). It picks one sub-command, says so in
one line ("Routing to `sv-review-once`: read-only audit, no edits."), loads
that sub-command's SKILL.md and follows it. Sub-commands can also be called
directly; they are not auto-selected. If both rows fit, ask one question
naming the two.

## Routing table

| The user says | Sub-command |
|---|---|
| review this paper, audit before submission, proofread, one day or one week before the deadline, submission-day runbook | `sv-review-once` |
| final pass, check everything again, iterate until clean, re-check after a batch of fixes | `sv-review-loop` |

`sv-review-once` reports and never edits. `sv-review-loop` applies only
rule-authorized edits, records them in a round log, and stops on a budget.

## Hand-offs outside this group

- Comments to resolve, or a response letter: `sv-feedback`.
- Drafting, polishing or de-AI editing: `sv-write`.
- Recording decisions and TODOs from the review: `research-records`.
