---
name: research-core
description: >-
  Shared foundation for every research skill in this library: core rules that
  hold in any field, field and venue profiles, checklists with sourced items,
  and project templates such as research.yaml, STATUS.md and guidance records.
  Use when another skill says to load research-core, when setting up a research
  project, or when a rule, profile or checklist item needs to be looked up,
  added or corrected.
license: CC-BY-NC-SA-4.0
user-invocable: false
---

# Research Core

## Overview

This skill holds the rules and data the other skills share. It does not write
or review anything on its own. Other skills load it first, then do their work
with the rules that apply to the current project.

Three layers, from general to specific:

1. **Core rules** hold in every field (claims match evidence, the paper body
   holds only current content, records live outside the paper, integrity).
2. **Field profiles** describe one field (structure, what reviewers care
   about, tone, citation norms, figures, rigor, extra checklist items).
3. **Venue profiles** describe one venue (page limits, template, anonymity,
   required sections, desk-reject causes).

Projects add a fourth layer of their own in the project repo (decisions in
`docs/adr/`, optional style overlays). Project rules never go into this skill.

## When to use this skill

- Another skill's step 0 says "load research-core".
- A project has no `research.yaml` yet and needs one.
- A rule, profile or checklist item has to be looked up, cited, added,
  corrected or retired.

## When NOT to use this skill

- To draft, polish or review text: use `sv-write-section`, `sv-write-polish`,
  `sv-review-loop` or `sv-review-once`, which load this skill themselves.
- To learn new rules from a finished project or from expert notes: use
  `sv-supervisor-harvest`, which proposes edits to this skill.

## Step 0: Resolve the project context

1. Find `research.yaml` at the project root. If it is missing, offer to create
   it from `assets/templates/research.yaml` (or hand off to
   `sv-supervisor`, which interviews the user).
2. Read `field`, `venue`, `paper_type`, `stage`, `review`, `style.overlays`
   and `people`.
3. Load, in this order:
   - all files in `references/core/` that the calling skill needs
     (the precedence file always);
   - `references/fields/<field>.md`, or `references/fields/_template.md` with
     a warning when the field has no profile;
   - `references/venues/<venue>.md` when it exists;
   - overlays named in `style.overlays` from `references/fields/overlays/`;
   - the checklist files the calling skill names.
4. Tell the user which profiles were loaded and their status
   (`evidenced`, `partial`, `stub`). A `stub` profile adds no rules.

See: references/core/precedence.md

## Core rules

| File | What it covers |
|---|---|
| `references/core/claims-evidence.md` | Claim ledger, scope words, hedging, numbers with sources |
| `references/core/body-text.md` | Anti-accretive body text, why before how, terms, definitions |
| `references/core/deai.md` | Short contract for removing AI tells; the full method is in the `sv-write-humanize-*` sub-commands |
| `references/core/feedback-loop.md` | Comment IDs, one change per comment, verify the diff, never hide notes |
| `references/core/figures.md` | Figure rules that hold in every field |
| `references/core/records.md` | Records outside the paper, sources of truth, sync rules |
| `references/core/integrity.md` | Agreement numbers, frozen gold, pre-set bars, AI-use disclosure, traceable numbers |
| `references/core/precedence.md` | What wins when rules conflict; how to cite sources |
| `references/core/inputs-mineru.md` | PDF input only through MinerU; routes; stop on failure |
| `references/core/ai-collaboration.md` | Human-in-charge rules for AI-assisted coding, figures and writing (formerly the `research-core` (`core/ai-collaboration.md`) skill); phase guides and tool matrix in `references/vibe/` |

See: references/core/claims-evidence.md
See: references/core/body-text.md
See: references/core/deai.md
See: references/core/feedback-loop.md
See: references/core/figures.md
See: references/core/records.md
See: references/core/integrity.md
See: references/core/inputs-mineru.md
See: references/core/ai-collaboration.md

## Field profiles

| File | Status |
|---|---|
| `references/fields/se.md` | evidenced (empirical SE and MSR first) |
| `references/fields/ai-ml.md` | partial |
| `references/fields/math.md` | partial |
| `references/fields/stats.md` | stub |
| `references/fields/causal.md` | stub |
| `references/fields/_template.md` | template for a new field |

See: references/fields/_template.md
See: references/fields/se.md
See: references/fields/ai-ml.md
See: references/fields/math.md
See: references/fields/stats.md
See: references/fields/causal.md

Style overlays are optional rule sets a project switches on, for example an
advisor's punctuation preferences.

See: references/fields/overlays/no-semicolons-no-dashes.md

## Venue profiles

See: references/venues/_template.md
See: references/venues/fse.md

A venue profile quotes the official call with its URL and fetch date. Items
the call leaves unclear are marked CONFIRM. A deadline heard in a meeting is
not a source.

## Checklists

| File | Run by |
|---|---|
| `references/checklists/master.md` | sv-supervisor, sv-review-once |
| `references/checklists/writing.md` | sv-write-section, sv-write-intro, sv-write-polish, sv-write-humanize-paper, sv-review-loop |
| `references/checklists/figures.md` | sv-figure-design, sv-figure-drawio |
| `references/checklists/threats.md` | idea-evaluator, sv-review-once |
| `references/checklists/double-blind.md` | sv-review-once, experiment-workflow |
| `references/checklists/artifact.md` | experiment-workflow, sv-review-once |
| `references/checklists/venue-submission.md` | sv-review-once |
| `references/checklists/integrity.md` | experiment-workflow, sv-review-once, sv-review-loop |
| `references/checklists/records.md` | sv-supervisor-records, sv-supervisor, sv-feedback-revise |

See: references/checklists/master.md

Running a checklist:

1. Load the named file plus the field and venue additions whose `Scope`
   matches the project.
2. For each item report `pass`, `fail`, `n/a` or `unknown`, with the evidence
   (file and line, commit, command output). A tick without evidence counts as
   `unknown`.
3. Items with `Status: candidate` are advisory: report them, do not block.
4. Items with `Status: deprecated` are skipped.

## Expert notes

Anonymized digests of expert guidance (advisors, co-authors, reviewers,
published writing guides, the user's own lessons) live under
`references/experts/<field>/`. Raw notes stay in the private project repo.

See: references/experts/README.md

## Project templates

`assets/templates/` holds `research.yaml`, `STATUS.md`, `TODO.md`,
`adr-0000-template.md`, `log-entry.md`, `group-meeting-log.md`, `guidance-record.md`,
`response-table.md`, `claim-ledger.md`, `runs-log.md` and
`data-manifest.tsv`. Copy them into a project; never edit them in place for
one project.

## Changing this skill

- Every rule and checklist item carries a source (`Src:` or `[src: ...]`).
  The source formats are listed in the precedence file.
- New rules start as `candidate`. They become `confirmed` when seen in two or
  more projects, or when a published guide or the venue states them. Rules
  contradicted later become `deprecated` with the reason; they are not
  deleted.
- `sv-supervisor-harvest` proposes changes on a `learn/<source>` branch; the user
  approves before merge.
- After editing, run `python scripts/lint_skills.py` and
  `python scripts/check_checklists.py` from the repo root.
