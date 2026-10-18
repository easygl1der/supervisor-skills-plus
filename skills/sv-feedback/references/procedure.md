<!-- Moved from skills/feedback-to-revision/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Feedback to Revision

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Mode A: Revision (comments on the manuscript)
- Mode B: Guidance (expert advice on a paper or experiment)
- Worked examples
- Checklist
- Outputs
- Hand-offs

## Overview

Comments arrive through many channels and get lost, half-done, silently
undone or hidden. This skill gives every comment an identity, a decision, a
change, a commit and a verified status, so the author always knows what is
open and can prove what was done.

It also keeps **guidance records**: when an expert advises on a paper or an
experiment, the record says what they saw, what they said, what they mean,
what to watch, what to do by when, and later whether it was done.

Evidence base: one SE paper with 111 tracked requests across five channels;
61% were verified as addressed, 12% left no trace, and several "done" claims
were not in the diff (`note:n05`).

## When to use this skill

- Inline notes in the LaTeX source (`\todo{}`, a senior's note macro).
- An annotated PDF, a review report, a meta-review, a chat thread with
  requests, a comment file, or an agent's review.
- Advice from a meeting, call or relayed message about the paper or an
  experiment (guidance mode).
- "What is still open?", "did we address everything?", "draft the response
  letter".

## When NOT to use this skill

- No comments exist and the user wants a review: use `sv-review-once`.
- Writing the reviewer-facing rebuttal prose: build the table here, then use
  `sv-feedback-rebuttal`.
- Pure language polishing: use `sv-write-polish` or `sv-review-loop`.

## Step 0: Load context

Load `research-core` (core rules, the field and venue profiles, and the
`records` and `master` checklists). From `research.yaml` read `people` (which
note macros exist and whether an agent may resolve them), `repos.paper`,
`source_of_truth.paper` and `review.page_budget`.

Core principles that bind every step: `research-core`
`references/core/feedback-loop.md`.

## Mode A: Revision (comments on the manuscript)

### A1. Ingest and assign IDs

1. Collect every comment from every channel into one intake table
   (`docs/feedback/<round>.md`, from the `response-table.md` template).
2. ID: `FB-<origin>-<nn>`. Origins: `A`, `B`, ... for co-authors (roles),
   `ADV` advisor, `R1`, `R2`, ... reviewers, `AG` agent, `SELF`. Add a channel
   tag when useful: `FB-A-INL-03` inline, `FB-B-P11` PDF, `FB-A-CH-20` chat.
3. For each comment record: a short quote in the original language, the
   source pointer (file and line; commit and line; PDF page plus the caption
   or nearby text; chat timestamp), and **the version the commenter read**.
4. PDF annotations: run `scripts/extract_pdf_comments.py <pdf> <out_dir>`.
   Key each note to the float label or caption text, not "Table 4", because
   numbering shifts during revision. Flattened drawings cannot be extracted;
   ask for the text.
5. Inline notes: run `scripts/list_markers.py <paper_dir>`. It also reports
   commented-out notes, notes inside `\iffalse`, switched-off note display
   and parked blocks.

See also `intake-and-triage.md`

### A2. Triage

For each ID: type, size (S/M/L), needs-author-decision, duplicate-of,
conflicts-with, re-raise-of, stale-version flag, image-only (needs a text
restatement), page effect. Separate process requests (submission metadata,
sync) from text revisions.

Show the triage table. Ask the author to decide every item marked
needs-decision and every conflict. For a conflict, present both positions
and one compromise; record the decision and its owner. Decisions that set a
rule go to an ADR (`sv-supervisor-records`).

### A3. Apply one change per comment

- One commit per ID (or per tight group of duplicates). The commit message
  starts with the ID: `FB-B-P11: allocation table to two sentences in Design`.
- Never mix comment fixes with sync merges, checkpoints or unrelated edits.
- A terminology comment is a sweep: search every file, figure label and
  caption; list remaining spots in the Done note.
- When a comment says "replace X with Y", write Y in the same commit that
  removes X, so content is never lost in between.
- Keep the diff minimal; preserve labels, references and protected content.

See also `apply-and-verify.md`

### A4. Marker lifecycle

- An agent may resolve only notes whose macro is marked
  `agent_may_resolve: true` in `research.yaml`.
- For all other notes the agent drafts the fix and appends a Done note inside
  the marker: what changed, where, what remains. The reviewer or the student
  closes it.
- Never delete, comment out or hide (`\shownotesfalse`) an unresolved note.
  Before the final pass, every remaining or commented-out marker is listed as
  an open item.

### A5. Verify

1. For each ID, take the claimed change (from the Done note, the agent report
   or the commit message) and find it in the actual diff. A report is evidence
   of intent, not of change.
2. For mechanical replacements, diff the rendered text, not only the source
   (a macro expanded by hand once dropped a character from a name).
3. After every merge, sync or pull, re-run verification on the merged
   branch; stale-base pushes and sync bots have reverted verified fixes.
4. Re-run `scripts/list_markers.py` and compare with the intake.

### A6. Close and report

Fill the response table: ID, short quote, decision (accept, partial,
decline with reason, superseded by ID), change summary, location after the
change (section and label), commit, verification status (`by diff` or
`pending`). Report counts per status, open items with owners, page delta,
and conflicts decided. This table feeds `sv-feedback-rebuttal`.

## Mode B: Guidance (expert advice on a paper or experiment)

1. Create `docs/guidance/YYYY-MM-DD-<role>-<topic>.md` from the
   `guidance-record.md` template in `research-core`.
2. Fill **Scenario** first: what was shown (version, commit, figure, result,
   experiment state) and what was asked. Flag advice given on an older
   version.
3. **What they said**: short verbatim quotes with times. Use the transcript or
   the chat export, not a tool-written summary.
4. **What they mean**: the interpretation, marked as such, with confidence
   and the questions to clarify with them.
5. **Points to notice**: risks, red lines, assumptions they challenged.
6. **Actions**: `G-<date>-<n>` with owner, due date or milestone, a concrete
   done-criterion, and links to TODO, FB or ADR IDs.
7. **Decision**: accept, partial or decline with the reason.
8. Later, `scripts/guidance_review.py <project_dir>` lists open and overdue
   actions and actions marked done without evidence. Update the **Follow-up
   check** table with the commit, run id or file that proves each action.

See also `guidance-mode.md`

## Worked examples

Six anonymized examples from the evidence project: a terminology sweep via an
inline note, a table mislabelled as a figure, a table reduced to two
sentences, a procedural opener rewritten, a fast fix that broke a name, and
an agent report whose fixes never landed.

See also `worked-examples.md`

## Checklist

Run the `records` checklist items owned by this skill (feedback IDs closed or
listed open, response table complete, repeated comments reopened, agent
comments labelled, page effect tracked, guidance actions followed up) and the
`master` gate on hidden reviewer notes. Report each item as pass, fail, n/a
or unknown with evidence.

## Outputs

- `docs/feedback/<round>.md`: intake, triage and response table.
- `docs/guidance/*.md`: guidance records with actions and follow-up.
- Commits whose messages start with FB or G IDs.
- A short report: counts per status, open items, overdue guidance, conflicts
  and their decisions.

## Hand-offs

- Response letter prose: `sv-feedback-rebuttal`.
- Multi-round language and style checks after the changes: `sv-review-loop`.
- ADRs, TODO and STATUS updates: `sv-supervisor-records`.
- After the project: `sv-supervisor-harvest` reads the tables and guidance records.
