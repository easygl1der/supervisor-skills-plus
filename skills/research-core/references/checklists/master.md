# Checklist: master

Index of the eight topic checklists plus the gate items that cut across them.
Run it before any submission or major hand-over; it does not replace the topic
files, it decides whether the paper may ship.

Run by: research-supervisor, pre-submission-reviewer

## Contents
1. Topic checklists
2. Gate items

## 1. Topic checklists

| File | What it checks |
|---|---|
| `writing.md` | Framing, structure, terms, numbers in prose, hedging, citations, de-AI pass |
| `figures.md` | Figure clarity, figure and text mirroring, table versus figure, figure data, figure process |
| `threats.md` | Scope of claims, alternative explanations, limits of reference data, agreement of threats and results |
| `double-blind.md` | Identity traces in the paper, the artifact and everything a reviewer can open |
| `artifact.md` | Replication package completeness, build, data hosting, data availability statement |
| `venue-submission.md` | Official call, page limit, template, required sections, submission form, upload timing |
| `integrity.md` | Number traceability, agreement values, frozen references, pre-set bars, AI-use disclosure |
| `records.md` | Sources of truth, sync, parked material, feedback and guidance closure, checklist hygiene |

Field and venue profiles add items with their own prefixes; load those whose
`Scope` matches the project.

## 2. Gate items

### MA-01 Read-only full check one day early
- [ ] Check: A read-only full pre-submission check (all topic checklists plus
  a review pass) ran at least one day before the deadline, against a named
  commit. Every Blocker it found has an owner and is treated as stop-ship.
- Why: In the evidence project the final read-only check named the identity
  leak that later had to be fixed after the deadline; its Blockers had no owners.
- Status: candidate
- Scope: core
- Owner: pre-submission-reviewer, research-supervisor, check-loop
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B1; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B2; note:n08§5#37; note:n07§B.3

### MA-02 No reviewer-visible markers
- [ ] Check: The compiled PDF and the source contain no todo macros, `TODO`
  comments that print, placeholder text, bracketed placeholder tags or
  unresolved reference marks. Every parked block has a decision.
- Why: Leftover markers tell reviewers the paper is unfinished; parked blocks
  can hide a missing result.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, check-loop, paper-polish
- Src: up:skills/paper-writer/references/verification-checklist.md; arc:FP-07@v2; arc:01-checklist/checklist.md T1; note:n07§B.5

### MA-03 No hidden unresolved notes
- [ ] Check: No unresolved co-author or reviewer note was deleted, commented
  out or hidden by switching off note display. Every note still open is on
  the open list in `docs/STATUS.md` before the notes are switched off.
- Why: Hiding a note is not resolving it; in the evidence project agent edits
  commented out notes that only the student was meant to close.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, feedback-to-revision, research-records
- Src: arc:msr:9809b8c; arc:msr:815305e; note:n05§5.2; note:n05§6.5

### MA-04 Same numbers and claims everywhere
- [ ] Check: Abstract, introduction preview, research-question answers,
  takeaway boxes and conclusion state the same findings with the same scope
  words, denominators and numbers. No claim is stronger in the abstract or
  conclusion than in the results.
- Why: Cross-section mismatches were the largest single audit list in the
  evidence project's final check.
- Status: candidate
- Scope: core
- Owner: pre-submission-reviewer, check-loop, paper-polish
- Src: arc:01-checklist/checklist.md A5; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; arc:@senior-a-comments:79-100; note:n07§B.5

### MA-05 Devil's-advocate pass
- [ ] Check: A devil's-advocate pass lists the strongest objections a
  reviewer could raise from the paper's own numbers, and each is answered in
  the text, scoped in threats, or recorded as a known weakness.
- Why: Objections found by the authors are cheaper than objections found by
  reviewers.
- Status: candidate
- Scope: core
- Owner: pre-submission-reviewer, research-supervisor
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; arc:01-checklist/checklist.md T14; skill:se-paper-reviewer; note:n07§B.5

### MA-06 Open guidance actions closed
- [ ] Check: Every guidance record in `docs/guidance/` has each action marked
  done, dropped with a reason, or carried to `docs/TODO.md` with an owner, and
  its follow-up check is dated.
- Why: Expert guidance that is recorded but never followed up is lost at the
  deadline.
- Status: confirmed
- Scope: core
- Owner: research-supervisor, research-records
- Src: user:2026-10-13; arc:@threats-pivot
