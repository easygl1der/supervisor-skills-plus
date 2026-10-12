# Checklist: records

Items for the records kept outside the paper: sources of truth, sync between
editors, parked material, feedback and guidance closure, decisions, and the
hygiene of checklists themselves.

Run by: research-records, research-supervisor, feedback-to-revision

## Contents
1. Sources of truth and sync
2. Parked material
3. Feedback closure
4. Guidance and decisions
5. Checklist hygiene
6. After submission

## 1. Sources of truth and sync

### RC-01 One source of truth per artifact
- [ ] Check: `docs/STATUS.md` names one writable source of truth for each
  artifact (paper, data, numbers) in the current phase.
- Why: In the evidence project the paper's source of truth changed three
  times in eight days and build notes still named the old one.
- Status: confirmed
- Scope: core
- Owner: research-records, research-supervisor
- Src: note:n08§1.2; note:n04§1.5; note:n08§5#1

### RC-02 Every switch recorded
- [ ] Check: Every change of source of truth was announced to all editors and
  recorded in an ADR, and build notes were updated in the same commit.
- Why: An unrecorded switch sends edits to the wrong copy.
- Status: confirmed
- Scope: core
- Owner: research-records
- Src: note:n08§1.2; note:n04§1.5; arc:CO-01@v2

### RC-03 Sync never overwrites
- [ ] Check: Every sync into a co-edited document checks for edits it would
  overwrite and stops instead of copying over.
- Why: A copy-over sync erased a senior co-author's edits twenty minutes
  before the deadline.
- Status: confirmed
- Scope: core
- Owner: research-records, vibe-research-workflow
- Src: arc:ol:a610d1d; arc:ol:214cc0c; arc:chat:group@2026-10-03T19:42; note:n08§5#2

### RC-04 Pushing is not syncing
- [ ] Check: After a push to version control, the co-edited copy was synced
  explicitly and checked; sync filters keep non-manuscript files out of the
  shared editor.
- Why: Co-authors kept editing a copy that the push had not updated.
- Status: candidate
- Scope: core
- Owner: research-records
- Src: arc:CO-02@v2; arc:chat:1on1@2026-09-29T11:10; arc:CO-04@v2; arc:msr:c93ef1f

### RC-05 Diffstat read after agent writes
- [ ] Check: After every agent write to a shared document the diffstat was
  read, a large deletion was treated as a whole-file overwrite, and a
  checkpoint commit preceded destructive agent edits.
- Why: Agent writes deleted hundreds of lines in one commit without notice.
- Status: confirmed
- Scope: core
- Owner: research-records, vibe-research-workflow, check-loop
- Src: arc:ol:b2ad042; arc:ol:3ae9fd3; note:n08§5#5; note:n08§5#6

### RC-06 One editor in the last day
- [ ] Check: In the last 24 hours before the deadline one channel was used,
  one person edited at a time, and the pen was handed over explicitly.
- Why: Parallel edits in the last hours caused a merge storm and lost edits.
- Status: candidate
- Scope: core
- Owner: research-supervisor, research-records
- Src: note:n08§1.3; note:n08§5#3

### RC-07 Senior bulk edits checked against agreed requirements
- [ ] Check: A large edit from a co-author was compared with earlier agreed
  requirements before it was merged, and conflicts were raised, not merged
  silently.
- Why: A bulk edit can undo decisions made earlier with other co-authors.
- Status: candidate
- Scope: core
- Owner: research-records, feedback-to-revision
- Src: arc:CO-07@v2; note:n07§B.5

### RC-08 Agents act only where allowed
- [ ] Check: Agents commit only when a human asks, stay out of sections a
  human fenced off, and close only notes marked as agent-resolvable.
- Why: Unasked agent commits and closures hid work and notes.
- Status: candidate
- Scope: core
- Owner: research-records, feedback-to-revision, check-loop
- Src: arc:CO-05@v2; arc:CO-06@v2; arc:msr:9809b8c; note:n08§5#7

### RC-09 Dashboards are views
- [ ] Check: The authoritative state of data and reviews is a file that can
  be diffed (export, state file), and `docs/STATUS.md` cites that file, not a
  dashboard.
- Why: A dashboard and its underlying data disagreed in the evidence project.
- Status: confirmed
- Scope: core
- Owner: research-records, experiment-workflow
- Src: note:n08§5#24

## 2. Parked material

### RC-10 Parked blocks listed
- [ ] Check: Every parked block (commented out, switched off, marked parked)
  has a one-line note (why, owner, restore condition) and appears in
  `docs/STATUS.md`; all are decided before the final pass.
- Why: A parked result disappeared from the paper for a day unnoticed.
- Status: candidate
- Scope: core
- Owner: research-records, paper-writer, check-loop
- Src: arc:msr:7c705c9; arc:msr:5262231; note:n06§2.9

## 3. Feedback closure

### RC-11 Feedback IDs closed or on the open list
- [ ] Check: Every comment has a stable ID with a pointer to where it was
  made and which version the commenter read; each ID is closed with
  evidence or listed as open in `docs/STATUS.md`.
- Why: Comments without IDs cannot be tracked to closure.
- Status: confirmed
- Scope: core
- Owner: feedback-to-revision, research-records
- Src: note:n05§6.1; note:n05§6.5; arc:MF-14@v2

### RC-12 Closure verified in the diff on the merged branch
- [ ] Check: Each closed ID has a commit whose message starts with the ID,
  the claimed change is present in the diff, and the check was repeated on
  the merged branch.
- Why: An agent report claimed eleven fixes that never landed; sync merges
  reverted verified fixes.
- Status: confirmed
- Scope: core
- Owner: feedback-to-revision, check-loop
- Src: arc:06-revision/REVISION-SUMMARY.md; arc:ol:214cc0c; note:n05§5.3; note:n05§5.5

### RC-13 Repeated comments reopen the earlier ID
- [ ] Check: A comment that repeats an earlier one is linked to the earlier
  ID, which is reopened.
- Why: A repeat means the earlier closure was wrong.
- Status: candidate
- Scope: core
- Owner: feedback-to-revision
- Src: note:n05§6.9

### RC-14 Conflicting requests surfaced and decided
- [ ] Check: When two reviewers asked for opposite things, both positions and
  a compromise were shown, the decision was recorded with its owner and date,
  and the reviewer whose request lost was told.
- Why: Silent resolution of conflicts re-opens them at the next review.
- Status: confirmed
- Scope: core
- Owner: feedback-to-revision, research-records
- Src: note:n05§5.4; note:n05§6.6

### RC-15 Agent comments labelled as such
- [ ] Check: Comments and reports generated by agents carry an agent origin
  label and are never attributed to a human reviewer.
- Why: Agent output labelled as a senior's comment inflated its authority.
- Status: candidate
- Scope: core
- Owner: feedback-to-revision, research-records
- Src: note:n05§6.10; note:n07§B.4

### RC-16 Response table complete
- [ ] Check: For every ID the response table gives a short quote, the
  decision (accept, partial, decline with reason, superseded by ID), the
  change, its location, the commit and the verification status.
- Why: The table is the trace reviewers and co-authors need.
- Status: candidate
- Scope: core
- Owner: feedback-to-revision, rebuttal-guidance
- Src: note:n05§6.7

### RC-17 Page effect of each change tracked
- [ ] Check: The page delta of each accepted cut or expansion is recorded so
  the page budget is known at all times.
- Why: Early cuts and late fills were not reconciled until pages ran short.
- Status: candidate
- Scope: core
- Owner: feedback-to-revision, paper-polish
- Src: note:n05§6.8

## 4. Guidance and decisions

### RC-18 Guidance records with actions and follow-up
- [ ] Check: Each piece of expert guidance is recorded in `docs/guidance/`
  with scenario, interpretation, actions with owners and due dates, and a
  dated follow-up status check.
- Why: Guidance without actions and follow-up is not acted on.
- Status: confirmed
- Scope: core
- Owner: research-records, research-supervisor
- Src: user:2026-10-13; arc:@threats-pivot

### RC-19 Decisions copied into the repository
- [ ] Check: Each locked decision is in an ADR with rejected alternatives and
  a "do not" list; decisions are copied into the repository, not kept only as
  ticket ids in an external tracker.
- Why: Tracker content can be lost; a bare ticket id explains nothing.
- Status: confirmed
- Scope: core
- Owner: research-records
- Src: note:n08§5#33; note:n08§5#35

### RC-20 Open decisions in a register
- [ ] Check: Undecided questions live in one register with their options, an
  owner and a due date.
- Why: Open decisions scattered across chats get decided by default.
- Status: candidate
- Scope: core
- Owner: research-records, research-supervisor
- Src: arc:10-requirements/DECISION-HINTS.md; arc:01-checklist/checklist.md T2

### RC-21 Requirement summaries mark what is superseded
- [ ] Check: Requirement summaries carry an explicit "superseded by" table,
  and the latest entry wins.
- Why: Two superseded requirements in the evidence project were later
  reversed again without anyone noticing.
- Status: candidate
- Scope: core
- Owner: research-records, feedback-to-revision
- Src: arc:04-comms/past-chat-group/SUMMARY.md; note:n07§B.2; note:n08§5#34

### RC-22 Transcripts are the meeting record
- [ ] Check: Meeting records are transcripts or verbatim notes; tool-made
  summaries are marked as summaries and not cited as the source.
- Why: Summaries drop and distort details.
- Status: candidate
- Scope: core
- Owner: research-records
- Src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#38

## 5. Checklist hygiene

### RC-23 Ticks record evidence, not intent
- [ ] Check: Every ticked item cites its evidence (commit, command output,
  diff, page); a tick without evidence is reported as unknown.
- Why: Ticked items in the evidence project were contradicted by the final
  paper, and verified items stayed unticked.
- Status: candidate
- Scope: core
- Owner: research-records, check-loop, pre-submission-reviewer
- Src: note:n07§B.3; note:n07§B.4; arc:RS-17@v2

### RC-24 Checklist provenance verified by hand
- [ ] Check: Every checklist item's source was written by hand from a primary
  source; machine-matched or agent-origin provenance is marked unverified and
  the item stays advisory.
- Why: Keyword-matched provenance named the wrong person for many items and
  turned agent suggestions into a senior's comments.
- Status: candidate
- Scope: core
- Owner: research-records, lessons-harvest, research-core
- Src: note:n07§B.4; arc:01-checklist/enriched/README.md

## 6. After submission

### RC-25 Submitted version synced back and tagged
- [ ] Check: After the deadline the submitted version was synced back into
  the repository and tagged.
- Why: The repository otherwise ends before the submitted text.
- Status: candidate
- Scope: core
- Owner: research-records
- Src: note:n08§1.2; note:n08§5#40
