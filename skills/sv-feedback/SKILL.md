---
name: sv-feedback
description: >-
  Entry point for handling feedback: turns comments from advisors,
  co-authors, reviewers or agents into tracked revisions with IDs, one
  change per comment and diff verification; records expert guidance with
  actions and follow-up; and plans peer-review rebuttals by reviewer
  mindset and strategy. Routes each request to one sv-feedback sub-command
  and says which. Use when feedback, advice or reviews arrive.
license: CC-BY-NC-SA-4.0
---

# sv-feedback

## Overview

Router of the feedback group (ADR 0021). It picks one sub-command, says so
in one line ("Routing to `sv-feedback-revise`: intake and triage first."),
loads that sub-command's SKILL.md and follows it. Sub-commands can also be
called directly; they are not auto-selected.

## Routing table

| The user says | Sub-command |
|---|---|
| inline notes, an annotated PDF, a review report, chat requests, what is still open, did we address everything | `sv-feedback-revise` |
| advice from a meeting, call or relayed message; which advice actions are overdue | `sv-feedback-guidance` |
| reviewer comments to answer, rebuttal help, response to R1, the reviewer ignored the rebuttal, journal revision letter | `sv-feedback-rebuttal` |

Typical order in a review round: `sv-feedback-revise` builds the response
table, then `sv-feedback-rebuttal` plans the reviewer-facing text from it.

The shared procedure and scripts of revise and guidance live in this
folder (`references/procedure.md`, `scripts/`).

See: references/procedure.md

## Hand-offs outside this group

- Re-checking the manuscript after the changes: `sv-review-loop`.
- ADRs, TODO and STATUS: `research-records`.
- After the project: `lessons-harvest` reads the tables and records.
