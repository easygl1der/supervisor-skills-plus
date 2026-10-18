<!-- Moved from skills/lessons-harvest/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Lessons Harvest

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Inputs
- Procedure
- New field: `--new-field <name>`
- Checklist
- Outputs
- Hand-offs

## Overview

`research-core` should get better with every paper, assignment and new
field. This skill is how it learns. At a milestone, it reads what a project
recorded (feedback, guidance, decisions, sv-review-loop findings, status, git
history) and what experts said, extracts lessons as general rules with
sources, removes the ones the library already has, decides where each new
rule belongs, and proposes the change for the owner to approve on a
`learn/<source>` branch. [src: up:DESIGN.md; user:2026-10-13]

It never merges on its own, never writes names or project details into the
library, and never states a rule without a source.

## When to use this skill

- After a submission, after reviews arrive, after an assignment is graded,
  or at the end of a project.
- When expert notes arrive: advisor or co-author comments, a reviewer
  report, a published writing guide or talk, or the owner's own lessons.
- `--new-field <name>`: a project starts in a field that has no profile, or
  a `stub` profile needs filling.
- When the owner asks to promote, demote or deprecate a rule.

## When NOT to use this skill

- Handling comments on the current manuscript: `sv-feedback-revise`.
- Recording a decision for the current project: `sv-supervisor-records` (ADR).
- Building a venue's style profile from exemplars: `sv-write-style-mine` (this
  skill calls it in the new-field flow and merges its proposals).
- Looking up a rule: `research-core` directly.

## Step 0: Load context

1. Load `research-core`: `SKILL.md`, `references/core/precedence.md` (source
   formats, rule and item formats, status lifecycle, the 2026-10-13
   promotion note), `references/experts/README.md`, and the field and venue
   profiles named in the project's `research.yaml`. Load the checklists the
   candidates may land in, and `checklists/records.md` (RC-24 provenance).
2. From `research.yaml` read `project`, `field`, `venue`, `paper_type`,
   `stage`, `records.dir` and `people` (roles only).
3. Identify the harvest source: a project slug (`learn/<project>`) or an
   expert source id (`learn/<yyyy-mm>-<kind>-<topic>`).
4. Confirm the library repo path and that its working tree is clean before
   any edit.

## Inputs

Project records (paths relative to the project root; `records.dir` may
change `docs/`):

- `docs/feedback/*.md` response tables (FB ids, decisions, commits)
- `docs/guidance/*.md` guidance records (G ids, interpretations, actions)
- `docs/adr/*.md` decisions, including superseded ones
- `docs/log/*.md`, especially sv-review-loop round logs
- `docs/STATUS.md` and `TODO.md` (parked items, risks, what was cut)
- git history of the paper and research repos (to verify that lessons
  happened)
- `revision_summary.md` rule candidates from `sv-write-style-mine`

Expert notes, four kinds (all accepted, decision of 2026-10-13):

1. advisor and co-author comments
2. reviewer reports
3. published writing guides, talks and blogs
4. the owner's own lessons

## Procedure

### 1. List candidates

Run the helper on the project:

```
python skills/sv-supervisor-harvest/scripts/find_rule_candidates.py <project_dir>
```

It prints each candidate item from `docs/feedback/`, `docs/guidance/` and
`docs/adr/` (ID, kind, text, source path and line) and the research-core rule
lines and checklist items that look similar (token-overlap score; a hint,
not a verdict). Add `--json` for machine-readable output and `--min-score`
to widen or narrow the duplicate search. Then read logs, STATUS, git history
and expert notes by hand.

### 2. Extract candidate rules

Write each lesson as one general rule (`HC-nn`) in the harvest table: what to
do, why (when the source says), and its sources. Strip project names, data,
numbers, people and tools. A lesson that cannot be stated without them is
project-only. Two sources that disagree are recorded side by side, never
averaged.

### 3. Attach sources

Use only the precedence-file prefixes: `proj:<project>/<path>` with the FB,
G or ADR id; `lit:<key>` for published work; `venue:<url>@<date>`;
`user:<date>`; existing `arc:` ids. Cite only what was opened in this
session. Commits are cited through the record that names them.

### 4. Dedupe against research-core

Check the script's hints, then grep research-core for the key terms and
checklist titles. Same direction: add the new source to the existing rule
(and propose promotion if the sources now span two projects). Opposite
direction: a Known disagreement or an owner decision, never a silent
overwrite. A match with a deprecated rule reopens the deprecation reason.

### 5. Classify the target

First "yes" wins: depends on this project (project-only); one person's taste
without a reader reason (overlay, off by default); one venue (venue
profile); one field (field profile, matching heading); any research paper
(core). Independently, if it is checkable with evidence, also propose a
checklist item in the matching file with the next free ID, Owner list and
Src line.

### 6. Apply the lifecycle

- `candidate`: one project or one expert.
- `confirmed`: two or more distinct projects; or a published guide, the
  venue call, or the owner (`user:<date>`); or an owner promotion with
  `(promoted: <reason>)`.
- `deprecated: <reason>`: contradicted later and the owner agrees; the line
  stays.

Checklists enforce only confirmed items.

### 7. Write expert digests

For each expert source, write an anonymized digest to
`research-core/references/experts/<field>/<source-id>.md` in the README
format: Kind, Field, Project, Raw record (`proj:` path, private), Date;
Context; Points, each with the rule candidate it became; Outcome. Roles not
names; no lab, repository, dataset or paper names; no project numbers;
quotes under 25 words.

### 8. Show the diff and get approval

Write the harvest report to the project's
`docs/log/<date>-lessons-harvest.md`. Prepare the research-core edits and
show the full diff. Ask the owner per candidate: accept, edit, project-only
or reject. Apply only accepted changes and run `scripts/lint_skills.py`,
`scripts/check_checklists.py`, `scripts/check_sources.py` and
`scripts/check_shared_sync.py`.

### 9. Commit on a learn branch

In the library repo: `git switch -c learn/<source>`, commit with
`learn(<source>): <summary>` listing the HC ids. Bump each touched profile's
`Version` and add a Changelog line; give a touched checklist file a version
line and Changelog on its first harvest; add one line to the repo
`CHANGELOG.md` under `## [Unreleased]`. Do not merge: the owner reviews and
merges.

See also `harvest-procedure.md`

## New field: `--new-field <name>`

1. Pick an unused two-letter field code.
2. Copy `research-core/references/fields/_template.md` to
   `fields/<name>.md`; set `Status: stub`, `Version: 0.1 (<date>)`; add it
   to research-core's field table.
3. Ask for 5 to 10 exemplar papers and any expert sources. Do not invent
   rules to fill headings.
4. Run `sv-write-style-mine` in Profile mode on the exemplars; it returns
   `field-proposals.md` with rule lines citing each supporting exemplar
   (`lit:` keys) under a consensus threshold, Known disagreements and
   Unknown entries.
5. Dedupe, classify and digest as above; continue with steps 8 and 9.
6. The owner moves the status `stub` to `partial` to `evidenced` as evidence
   accumulates.

## Checklist

Report pass, fail, n/a or unknown with evidence for:

- research-core `checklists/records.md` RC-24: every new or changed item's
  source was written by hand from a primary source; machine-matched
  provenance (including this skill's duplicate hints) is never used as a
  source.
- RC-23: ticks and promotions record evidence, not intent.
- `check_checklists.py`: unique IDs, required fields, valid owners.
- `check_sources.py`: every resolvable source resolves.
- Anonymization: no names, project identifiers or project numbers in
  research-core files or digests (grep the diff for the project slug,
  people's names and repository names before committing).
- Lifecycle: every new line has a status; promotions cite the second project
  or the guide; deprecations keep the line and the reason.

## Outputs

- Project repo: `docs/log/<date>-lessons-harvest.md` (candidate table,
  decisions, digests written).
- Library repo, on `learn/<source>`: edited core files, profiles,
  checklists or overlays; new expert digests; bumped versions and
  changelogs; one `CHANGELOG.md` line.
- For `--new-field`: a new field profile (status `stub` or `partial`).

## Hand-offs

- Owner review and merge of `learn/<source>`.
- Filling a field or venue profile from exemplars: `sv-write-style-mine`.
- Project-only lessons: `sv-supervisor-records` (ADR or STATUS note in the
  project).
- Next project start: `sv-supervisor` loads the updated profiles via
  `research-core`.
