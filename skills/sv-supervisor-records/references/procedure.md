<!-- Moved from skills/sv-supervisor-records/references/procedure.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Research Records

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Task 1: Initialize
- Task 2: Update status (replace, never append)
- Task 3: Record a decision (ADR)
- Task 4: Sources of truth and syncs
- Task 5: Notes lifecycle
- Task 6: De-accrete docs
- Task 7: Linear mirror (optional)
- Task 8: Group-meeting decks
- Checklist
- Outputs

## Overview

The paper body holds only the newest correct content. Everything else (what
ran, what failed, what was decided and why, what is open) lives in the
project's `docs/` folder. Local files are the source of truth; Linear is an
optional board that links back to them.

```
docs/
  STATUS.md     current state only; replace, never append
  TODO.md       actionable items with owners and IDs
  adr/          numbered decisions with alternatives; superseded, never edited
  log/          dated notes: meetings, sv-review-loop reports, runs of the day
  feedback/     response tables (sv-feedback-revise)
  guidance/     expert guidance records (sv-feedback-guidance)
  runs.md       experiment runs (experiment-workflow)
  notes/        scratch explorations; must be promoted, decided or archived
```

Why: in the evidence project the paper's source of truth changed three times
in eight days without a record, a sync erased a co-author's edits before the
deadline, and decisions referenced only by tracker ids lost their text
(`note:n08`).

## When to use this skill

- A new project, or a project with no `docs/` yet.
- "Record this decision", "why did we choose X?", a choice between real
  alternatives is about to be locked.
- Status changed: a run finished or failed, a number was verified, a blocker
  appeared, the stage changed, a deadline was fetched.
- The paper moves between git and Overleaf (or another co-edited copy), or a
  sync is about to run.
- Docs drifted from reality, or notes piled up.
- Linear is enabled and items need mirroring.

## When NOT to use this skill

- Editing the manuscript: use `sv-write-section`, `sv-write-polish`, `sv-review-loop`.
- Tracking comments on the manuscript: use `sv-feedback-revise` (it writes
  into `docs/feedback/` and `docs/guidance/` with this skill's conventions).
- Logging experiment runs in detail: use `experiment-workflow`.

## Step 0: Load context

Load `research-core` (core rules in `references/core/records.md` and
`body-text.md`, and the `records` checklist). Read `research.yaml`:
`records`, `source_of_truth`, `repos`, `deadline`.

## Task 1: Initialize

1. If `docs/` is missing, ask before creating it. Copy `STATUS.md`,
   `TODO.md`, `adr-0000-template.md` (as `docs/adr/template.md`),
   `log-entry.md`, `group-meeting-log.md`, `runs-log.md` (as `docs/runs.md`) from `research-core`
   `assets/templates/`.
   Create `docs/adr/README.md` with an index table.
2. Fill **Sources of truth** in STATUS and write ADR 0001 recording them.
3. Add private paths to `.gitignore` from day one (chat exports, other
   people's papers, local notes) so they never reach the shared paper repo.

## Task 2: Update status (replace, never append)

1. Rewrite only the affected STATUS sections so the file reads as if it were
   always correct. History goes to `docs/log/<date>-<topic>.md`.
2. Verified numbers: a row only with script, output file, code commit and
   data version.
3. Runs: ran, failed or partial, never deleted.
4. Parked material, open reviewer markers, open guidance actions: refresh from
   `sv-feedback` scripts (`list_markers.py`, `guidance_review.py`).
5. Deadline: only from a dated official source.

## Task 3: Record a decision (ADR)

1. Draft: context, at least two real options with pros and cons, decision
   with "because", consequences, and a "do not" list.
2. Show the draft; write it only after the user approves.
3. Number it, add it to the index.
4. Never rewrite an accepted ADR's decision; write a new ADR that supersedes
   it and mark the old one.
5. If a living doc (STATUS, README, codebook) still describes the old world,
   rewrite it now (Task 6).

See also `adr.md`

## Task 4: Sources of truth and syncs

1. Exactly one writable source per artifact per phase, named in STATUS and
   ADR. A switch (for example from git to Overleaf in the last day) gets an
   ADR and an announcement in the team channel.
2. Before any sync into a co-edited copy, run
   `scripts/sync_guard.py <repo> <remote> <branch>`. It fetches and refuses
   when the remote has commits the local branch does not contain, listing
   them. Merge first; never copy over.
3. After any agent write to a shared document, read the diffstat; a large
   deletion means an overwrite. Checkpoint before destructive agent edits.
4. In the last 24 hours: one editor at a time; hand over the pen explicitly.
5. After a deadline: bring the submitted version back into git and tag it
   (`submitted-<venue>-<date>`), with the uploaded PDF's hash in STATUS.

See also `sources-and-sync.md`

## Task 5: Notes lifecycle

Scratch notes go to `docs/notes/YYYYMMDD-<topic>.md` with
`status: scratch`. When a line of work ends: promote the durable facts into
STATUS or the living doc, lock lasting choices in an ADR, mark the note
`superseded` with a pointer, archive bulky material. Never keep two current
answers to the same question.

## Task 6: De-accrete docs

Rewrite living docs so they state current facts without editing narration
("now", "no longer", "after further checking"). Test each changed sentence:
would a reader who never saw the old version notice a gap? History belongs
in ADRs, logs and git. Keep load-bearing commands and safety constraints.

See also `anti-accretion.md`

## Task 7: Linear mirror (optional)

Only when `records.linear.enabled` is true. One issue per TODO item or
blocker; the issue description links to the `docs/` file, ADR and note; status
flows from files to Linear, never the reverse; no reports pasted into Linear.
Use the Linear MCP when available.

See also `linear-mirror.md`

## Task 8: Group-meeting decks

When `group-beamer` finishes a meeting deck:

1. Write `docs/log/<date>-group-meeting.md` from the research-core
   `group-meeting-log.md` template. The "Next steps" list is the input for
   the following weekly report (each item later marked done / partial /
   dropped).
2. Store `.tex`, PDF and exported notes under `docs/meetings/<date>/`.
3. Do not invent next steps that were not on the approved outline.

See also `group-meetings.md`

## Checklist

Run the `records` checklist from `research-core` (sources of truth named and
switches recorded, sync never overwrites, parked blocks listed, open items
listed, ticks record evidence, submitted version tagged). Report each item as
pass, fail, n/a or unknown with evidence.

## Outputs

Updated `docs/` files, ADR drafts for approval, sync-guard results, and a
short summary of what changed and what is still open.
