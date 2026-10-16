# Harvest procedure

## Contents
1. Input map
2. Extracting candidates
3. Sources for project and expert evidence
4. Dedupe against research-core
5. Classifying the target
6. Lifecycle decisions
7. Expert digests
8. Harvest report, diff and approval
9. Branch, versioning and changelog
10. New-field flow
11. Worked example (synthetic project)

Design basis: DESIGN section 3.4 and the owner's decisions of 2026-10-13
(all four kinds of expert notes feed this skill; the library grows with every
paper). [src: up:DESIGN.md; user:2026-10-13]

## 1. Input map

| Input | Where | What to look for |
|---|---|---|
| Feedback tables | `docs/feedback/*.md` | Accepted comments whose fix is a pattern, not a one-off; repeated comments (same request twice); declined comments with a reason that states a principle |
| Guidance records | `docs/guidance/*.md` | "What they mean" and "Points to notice" bullets; actions that set a habit; the Decision line |
| ADRs | `docs/adr/*.md` | Decisions with a reason that would hold in the next project; "Do not" lists; superseded ADRs (a rule that failed) |
| Check-loop logs | `docs/log/*-check-loop.md` | Findings that recurred across rounds; oscillations (a span flipped back and forth means two rules conflict); residual findings |
| Other logs | `docs/log/*.md` | Incidents: lost work, overwritten edits, late discoveries, desk-reject risks |
| STATUS | `docs/STATUS.md` | Parked items, open risks, what was cut at the end and why |
| Git history | `git log`, `git log -p` on the paper and research repos | Trims and restores, reverts, late large diffs, fix commits that cite FB or G ids; used to verify that a lesson really happened |
| Revision logs | `<manuscript>_revised/revision_summary.md` (style-mine) | "Rule candidate: YES" lines |
| Expert notes | see section 7 | Advisor and co-author comments, reviewer reports, published writing guides, the owner's own lessons |

Read the records first, git last. Git confirms or refutes what the records
claim (a "done" that never landed is itself a lesson for `records`).

Start with the helper script, which lists candidate items from feedback,
guidance and ADR files with possible duplicates:

```
python skills/lessons-harvest/scripts/find_rule_candidates.py <project_dir> [--min-score 0.35] [--json]
```

Logs, STATUS, git history and expert notes are read by hand.

## 2. Extracting candidates

Write every candidate into one table (the harvest report, section 8):

```
| HC | Candidate rule (general wording) | Evidence (sources) | Kind of input | Target | Lifecycle | Duplicate of | Decision |
|---|---|---|---|---|---|---|---|
| HC-01 | Each method step opens with the reason it is needed. | proj:<slug>/docs/feedback/r1.md (FB-ADV-01) | feedback | checklist (exists) | add source | WR-06 | |
```

Rules for wording a candidate:

- General: no project names, data, numbers, people or tools that only this
  project uses. If the lesson cannot be stated without them, it is
  project-only.
- One rule per line, stated as what to do (or not do), with the reason when
  the source gives one.
- Separate the lesson from the incident: "Sync never overwrites" is the
  rule; the overwritten afternoon is the evidence.
- Do not merge two sources that say different things into one averaged rule
  (precedence file, section 1). Record both and propose one option.

Skip: one-off typo fixes, pure taste with no stated reason (unless the owner
wants it as an overlay), and anything already settled as project-only in an
ADR.

## 3. Sources for project and expert evidence

Use only the prefixes of `research-core/references/core/precedence.md`:

| Evidence | Cite as |
|---|---|
| Feedback row, guidance record, ADR, log in a project repo | `proj:<project>/<path>` and the row or record id in the rule text or the Src line |
| A commit | through the feedback row or ADR that names it; or the log entry quoting it |
| Published guide, book, paper, talk | `lit:<key>` with the full reference in the target file's Sources |
| Venue call | `venue:<url>@<date>` |
| The owner's own lesson or decision | `user:<date>` |
| The first evidence project (private archive) | the `arc:` forms already defined |

Never cite a source that was not opened in this session. Never invent dates,
quotes or counts. If a lesson rests on memory only, ask the owner and cite
`user:<date>` if they confirm it.

## 4. Dedupe against research-core

For each candidate:

1. Check the script's "possible duplicates" (a token-overlap hint, not a
   verdict).
2. Grep research-core for the key terms and for checklist titles:
   `grep -rn -i "<term>" skills/research-core/references/`
   and list IDs with `grep -rn "^### [A-Z]" skills/research-core/references/checklists/`.
3. Decide:

| Finding | Action |
|---|---|
| Same rule, same direction | Add this project's source to the existing rule or item. If the existing sources come from a different project, propose promotion to `confirmed` |
| Same topic, narrower or broader | Edit the existing rule's scope only if both sources support the new wording; otherwise add a new line and note the relation |
| Opposite direction | Do not overwrite. Add a "Known disagreements" entry (profile) or open a decision for the owner; the old rule stays until decided |
| No match | New rule or item |

Also check deprecated rules: a candidate that matches a deprecated rule
needs the deprecation reason re-examined, not a silent revival.

## 5. Classifying the target

Ask in this order; the first "yes" decides.

1. Does it depend on this project's data, tools, people, names or numbers?
   **project-only**: stays in the project's ADRs or docs. Not written to
   research-core.
2. Is it one person's stylistic preference without a reader-facing reason
   (punctuation bans, word bans)? **overlay** under
   `references/fields/overlays/`, off by default.
3. Is it set by one venue's call, or seen only in one venue's papers?
   **venue** profile `references/venues/<venue>.md`.
4. Does it depend on the field's methods, paper types or reviewer
   expectations? **field** profile `references/fields/<field>.md` (under the
   matching heading).
5. Does it hold for any research paper or project record? **core**
   (`references/core/<file>.md`).

Then, independently: can a reader check it on an artifact and record pass or
fail with evidence? If yes, also propose a **checklist** item in the file
whose scope matches (`writing`, `figures`, `threats`, `double-blind`,
`artifact`, `venue-submission`, `integrity`, `records`, `master`, or the
profile's "Checklist additions" for field and venue items). Use the item
format of the precedence file, the next free ID with the file's prefix, an
Owner list of existing or planned skills, and `Status: candidate` unless
section 6 says otherwise.

## 6. Lifecycle decisions

| Situation | Status |
|---|---|
| One project, or one expert (advisor, co-author, reviewer) | `candidate` |
| Same rule now supported by two or more distinct projects (`proj:` slugs, or `arc:` plus a `proj:`) | `confirmed` |
| Stated by a published guide (`lit:`), the venue call (`venue:`), or decided by the owner (`user:<date>`) | `confirmed` |
| One project, but failure had a clear bad outcome and the owner promotes it | `confirmed`, Src ends `user:<date> (promoted: <reason>)` |
| Contradicted by later evidence, and the owner agrees | `deprecated: <reason, with source>`; keep the line |

Checklists enforce only `confirmed` items; `candidate` items are advisory.
A promotion or deprecation is a change like any other: it appears in the
diff and the changelog.

## 7. Expert digests

Four kinds of expert notes feed the library:

| Kind | `Kind:` value | Typical raw record | Default status of resulting rules |
|---|---|---|---|
| Advisor or co-author comments | `advisor`, `coauthor` | `docs/guidance/*.md`, feedback rows | candidate |
| Reviewer reports | `reviewer` | `docs/feedback/<review round>.md` | candidate (confirmed if the venue call says the same) |
| Published writing guides, talks, blogs | `guide` | URL or reference | confirmed when the guide states it directly |
| The owner's own lessons | `self` | owner's notes, a log entry | confirmed when the owner says so (`user:<date>`), else candidate |

Write one digest per source to
`research-core/references/experts/<field>/<source-id>.md`, with
`<source-id>` = `<yyyy-mm>-<kind>-<short-topic>`, in the format of
`references/experts/README.md` (Context, Points with the rule candidate each
became, Outcome).

Anonymization:

- Roles, never names (student, senior co-author A, advisor, reviewer 2). A
  published guide's author may be named in the full reference only.
- No lab, group, repository, dataset, ecosystem or paper names; no project
  URLs; no dataset sizes or result numbers. Describe the domain generically
  if needed.
- Paraphrase; quotes under 25 words, in the original language if needed
  (CJK is allowed in references).
- Raw notes stay in the private project repo; the digest's `Raw record:`
  line points to them with `proj:`.

## 8. Harvest report, diff and approval

1. Write the report in the **project** repo:
   `docs/log/<date>-lessons-harvest.md` (research-core `log-entry.md` header,
   `Kind: note`), containing the candidate table with targets, duplicates
   and proposed lifecycle, plus the list of digests to write.
2. Prepare the edits to research-core in the working tree of the library
   repo and show the full `git diff` (or, before branching, the proposed
   lines per file).
3. Ask the owner per candidate: accept, edit, project-only, or reject.
   Record the answer in the report's Decision column.
4. Apply only accepted changes. Run the library checks:
   `scripts/lint_skills.py`, `scripts/check_checklists.py`,
   `scripts/check_sources.py`, `scripts/check_shared_sync.py`.

## 9. Branch, versioning and changelog

- Branch in the library repo: `git switch -c learn/<source>` where
  `<source>` is the project slug or the expert source id
  (`learn/2026-11-guide-results-writing`). Commit there; never merge it
  yourself. The owner reviews and merges.
- For every touched profile: bump `Version: <x.y> (<date>)` (minor step per
  harvest) and add a Changelog line naming the source and counts
  (`- 0.2 (<date>): harvest from <source>: 3 rules added, 1 promoted.`).
- For a touched checklist file without a version line, add
  `Version: 0.2 (<date>)` under the title and a `## Changelog` section at
  the end on the first harvest.
- Repo `CHANGELOG.md`: one line per harvest under `## [Unreleased]`
  (create the heading if missing), for example
  `- research-core: harvest from <source> (N added, M promoted, K deprecated).`
- Commit message: `learn(<source>): <summary>`, listing the HC ids.

## 10. New-field flow

`lessons-harvest --new-field <name>`:

1. Choose the field code (two letters, unused by other profiles).
2. Copy `references/fields/_template.md` to `references/fields/<name>.md`;
   set `Status: stub`, `Version: 0.1 (<date>)`, and add it to the field
   table in research-core's SKILL.md.
3. Ask the owner for 5 to 10 exemplar papers (target journals or top venues
   of the field) and any expert sources (guides, advisor notes).
4. Run `style-mine` in Profile mode on the exemplars. It returns
   `field-proposals.md` with rule lines, each with its supporting `lit:`
   keys and the consensus threshold, plus Known disagreements and Unknown
   entries.
5. Dedupe and classify those proposals as in sections 4 and 5, digest the
   expert sources (section 7), and continue with sections 8 and 9.
6. Status moves `stub` to `partial` when the profile has rules under at
   least half of its headings, and to `evidenced` when a project in the field
   has used it and been harvested. The owner decides each step.

Nothing is invented to fill headings; empty headings stay empty, and open
questions go under Unknown.

## 11. Worked example (synthetic project)

A synthetic project with one feedback table, one guidance record and one
ADR (the test set used for the helper script) produced 10 items:

- A co-author asked for one name per concept. The script matched the core
  body-text rule and WR-12: same direction, so the action is "add source";
  because WR-12's sources come from a different project, propose promotion.
- An advisor point said captions must be self-contained. Matched FG-02: add
  source.
- An advisor point said experiments must not start before the acceptance
  bar is written. Matched IN-08: add source.
- An ADR chose a three-hue colour-blind safe palette with marker shapes as a
  second cue. Matched FG-03 for the second cue; the three-hue limit had no
  match, so it is a new candidate. One advisor's palette taste with no
  stated reader reason classifies as an overlay or project-only, not a field
  rule.
- The guidance action (redraw figure 2) is project-only.
