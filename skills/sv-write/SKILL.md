---
name: sv-write
description: >-
  Entry point for all research writing: plans a paper skeleton, drafts an
  Introduction or other sections, polishes or translates existing prose,
  critiques a draft without editing, removes machine-written texture from
  papers, reports, slides and letters, and mines or applies venue style.
  Routes each request to one sv-write sub-command and says which. Use when
  the user asks for help writing, revising, polishing, de-AI editing or
  styling a paper or other research text.
license: CC-BY-NC-SA-4.0
---

# sv-write

## Overview

This is the router of the writing group (ADR 0021). It does no writing
itself: it picks one sub-command, says so in one line ("Routing to
`sv-write-polish`: light language pass only."), loads that sub-command's
SKILL.md and follows it. The user can also call any sub-command directly
with `/sv-write-<name>`; sub-commands are not auto-selected.

If the request fits two rows equally well, ask one question that names the
two candidates. Never run several sub-commands in one go unless the user
asked for that sequence.

## Routing table

| The user says | Sub-command |
|---|---|
| paper skeleton, logic chain, thinking template, plan a benchmark paper | `sv-write-skeleton` |
| write or restructure the Introduction, outline the Intro | `sv-write-intro` |
| write a section, turn results or notes into text, abstract, full draft | `sv-write-section` |
| polish, fix the wording, smooth this, is this claim too strong | `sv-write-polish` |
| translate my Chinese draft, rewrite Chinese-English | `sv-write-translate` |
| what is wrong with this draft, critique, do not edit | `sv-write-critique` |
| remove AI tone from a paper or thesis chapter | `sv-write-humanize-paper` |
| remove AI tone from a weekly report, progress or technical report | `sv-write-humanize-report` |
| remove AI tone from slides or a Beamer deck | `sv-write-humanize-slides` |
| remove AI tone from a proposal, rebuttal letter or email | `sv-write-humanize-letter` |
| de-AI audit only, gate check, report without edits | `sv-write-humanize-audit` |
| dissect an exemplar, build a venue, field or author profile, find a journal's new papers, borrow methods | `sv-write-style-mine` |
| revise my paper for a venue, does this fit the venue (sv-review-loop round 2) | `sv-write-style-apply` |

## Shared references

These files live once, in this folder, and the sub-commands point here:

- `evidence-discipline.md`, `prose-delivery.md`, `verification-ladder.md`,
  `citation-style.md`, `empirical-study-skeleton.md` (drafting).
- `faithfulness.md`, `section-conventions.md`, `academic-phrasebank.md`,
  `ai-tone-guardrails.md` (editing existing prose).
- `humanize/`: the de-AI core (`core.md`), its diagnosis, editing contract,
  pattern catalog and the avoid-ai-writing licence.

See: references/faithfulness.md
See: references/humanize/core.md

## Hand-offs outside this group

- Multi-round checks after any writing step: `sv-review-loop`.
- Reviewer-style audit of a finished manuscript: `sv-review-once`.
- Comments from co-authors, advisors or reviewers: `sv-feedback-revise`.
- Whether the idea holds at all: `sv-idea`.
- Figures: `sv-figure-design`.
- Rule changes learned from writing work: `sv-supervisor-harvest`.
