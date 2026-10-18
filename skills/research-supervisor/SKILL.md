---
name: research-supervisor
description: >-
  Optional entry point for a research project: starts new projects with an
  interview that writes research.yaml and the docs files, works out the
  current stage from research.yaml and repository signals, shows blockers,
  overdue guidance, open reviewer markers and the next deadline with its
  source, then routes to one to three skills with reasons. Never does the
  work itself. Use when starting a session, starting a project, or asking
  what to do next.
license: CC-BY-NC-SA-4.0
---

# Research Supervisor

## Overview

With more than twenty other skills, the main cost is knowing which one to run. This
skill reads the project's state, says where the project stands and what is
blocking it, and names the next one to three skills with a reason for each.
It writes only the project set-up files at init. Drafting, reviewing,
running experiments and editing records belong to the skills it routes to.

Why: the evidence project went through ten stages with very different needs,
and its worst moments came from confusion over where the paper was edited and
when the deadline was (`note:n04` §5 S1-S10, §1.1, §1.5).

## When to use this skill

- Start of a work session on a project ("where are we?", "what next?").
- A new project, or a repo with no `research.yaml`.
- The user is unsure which skill fits a request.
- A reading or learning request (a paper, a textbook chapter, a concept,
  a set of papers, a proposal): route by intent, with or without a project.

## When NOT to use this skill

- The user already named the task and the skill: go straight there.
- Any actual work: drafting, polishing, reviewing, running, recording.

## Reading and learning: route by intent

These requests do not need `research.yaml` and never trigger init. Route
on what the user asked for, before any stage logic:

| Request | Skill |
|---|---|
| a quick structured read of one paper; its writing style (`--style`) | `paper-quickread` |
| understand a concept, a paper in depth, or a textbook chapter | `study` |
| map a body of literature, find gaps, plan next reads | `deep-research` (literature-map mode) |
| "can I use this in my project?", a minimal validation experiment | `research-bridge` |
| thesis proposal, research plan, grant application | `proposal-writer` |
| a style profile from exemplar papers | `sv-write-style-mine` |
| group-meeting slides, weekly report, paper talk | `group-beamer` |

Priority: an explicit reading or learning intent wins over the stage table;
if a project exists, mention its stage in one line and continue with the
routed skill. Usual chain: `paper-quickread` (triage) then `study`
(understanding) then `research-bridge` (use in a project) then
`idea-evaluator` or `experiment-workflow`; several cards then
`deep-research` literature-map; a plan then `proposal-writer`.
[src: user:2026-10-16] (confirmed)

## Step 0: Load context

Load `research-core` (`references/core/records.md`, `precedence.md`, the
field and venue profiles named in `research.yaml`, and the `master` and
`records` checklists). Read `research.yaml`: `stage`, `deadline`, `field`,
`venue`, `paper_type`, `repos`, `source_of_truth`, `experiments`, `records`.

## Step 1: Init (only when `research.yaml` is missing)

Ask, one short block at a time, and accept "unknown" for any answer:

1. Project slug, field (`se`, `ai-ml`, `math`, `stats`, `causal` or other),
   paper type, current stage.
2. Venue and year; deadline and the official URL it comes from (fetch the
   call, store a dated copy; a deadline heard in a meeting is not a source).
   Double-anonymous review? Page budget?
3. Repositories: paper, Overleaf (if any), research, artifact. Where is the
   paper edited now (the one writable source of truth)?
4. Data location (git, LFS, external host) and compute backend (`local`,
   `colab`, `vps`).
5. Records: local only, or a Linear mirror too. Co-author roles and their
   comment macros, and which ones an agent may resolve.

Then copy `research-core` `assets/templates/research.yaml` to the project
root, fill it, and show the diff before writing. Hand the `docs/` set-up
(STATUS, TODO, ADR 0001 for sources of truth, runs log, `.gitignore` for
private material) to `research-records` Task 1. A field with no profile
loads `_template.md`; offer `sv-write-style-mine` to build one.

## Step 2: Session brief

Run the read-only brief:

```bash
python scripts/session_brief.py <project_dir> [--paper-dir paper/]
```

It reports the stage in `research.yaml` and the stage the signals suggest,
blockers from `docs/STATUS.md`, overdue guidance actions and done-without-
evidence actions (`feedback-to-revision` `guidance_review.py`), open,
commented-out and hidden reviewer markers (`list_markers.py`), unverified
feedback rows, the next deadline with its source, and records warnings.

Stage signals, strongest first: reviewer feedback ids present, rebuttal;
deadline within 7 days, submission; live markers or unverified feedback,
internal review; a draft exists, writing; runs logged in the last 14 days,
experiments; none of these, idea or design. When the explicit stage and the
signals differ, show both and ask; do not change `stage` without the user.

Show the user, in this order and in at most 12 lines: stage, next deadline
with source and days left, blockers, overdue guidance, open markers, records
warnings. Missing deadline source and missing STATUS are reported as
problems, not filled in.

## Step 3: Route

Pick one to three skills from the table for the stage, plus any that a
blocker or warning calls for. Give each a one-line reason tied to what the
brief showed (a blocker, a marker count, days to deadline).

| Stage | Skills (first choice first) |
|---|---|
| no `research.yaml` | `research-supervisor` init, then `research-records`; `research-core` is loaded by every skill |
| idea | `idea-evaluator`, `deep-research`, `research-bridge` (an idea came from a paper or concept just studied) |
| design | `idea-evaluator` (empirical or theory route), `experiment-workflow` (freeze, sampling, gold), `research-records` (ADRs) |
| experiments | `experiment-workflow`, `research-records`, `vibe-research-workflow` (agent coding habits) |
| writing | `sv-write` (routes to skeleton, intro, section, style and humanize sub-commands) |
| figures | `figure-designer`, `drawio-reconstruction` |
| internal-review | `feedback-to-revision`, `check-loop`, `sv-write-polish` |
| submission | `pre-submission-reviewer`, `check-loop`, `experiment-workflow` (artifact, numbers check) |
| rebuttal | `feedback-to-revision`, `rebuttal-guidance` |
| camera-ready | `sv-write-polish`, `experiment-workflow` (de-anonymized artifact), `research-records` (tag the submitted version) |
| project finished, or expert notes arrived | `lessons-harvest` |

Overrides from the brief:
- Deadline within 7 days and no read-only full check yet: `pre-submission-reviewer`
  first, at least one day before the deadline.
- Overdue guidance or unverified feedback: `feedback-to-revision`.
- Source of truth unnamed, STATUS stale, deadline without source:
  `research-records`.
- Printed numbers without verified rows, or an agreement value without raw
  label sets: `experiment-workflow`.
- Last 24 hours before the deadline: remind the team to use one editor at a
  time and one channel (`research-records`).

## Step 4: Hand off

Name the chosen skill and what to pass it (files, IDs, the blocker). Stop.
Do not start the routed work in this skill.

## Checklist

Run from `research-core`:
- `records`: RC-01 (one source of truth named), RC-06 (one editor in the
  last day, when the deadline is within a day), RC-18 and RC-20 (guidance
  records and open decisions); STATUS updated within 14 days; the deadline
  has a dated official source (`venue-submission` VS-01).
- `master`: MA-01 (read-only full check scheduled a day early) when the
  stage is submission; MA-06 (open guidance actions closed).

Report each item as `pass`, `fail`, `n/a` or `unknown` with evidence (the
brief's output line, the file).

## Outputs

- At init: `research.yaml` (after the user approves the diff) and a hand-off
  to `research-records` for `docs/`.
- Each session: the brief (stage, deadline and source, blockers, overdue
  guidance, markers, warnings) and the routing decision with reasons.

## Hand-offs

Every row of the routing table. Records changes always go through
`research-records`; this skill does not edit `docs/`.
