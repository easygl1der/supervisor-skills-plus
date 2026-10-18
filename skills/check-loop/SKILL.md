---
name: check-loop
description: >-
  Runs a bounded multi-round check over a manuscript: research-writing fit
  first (claims, scope, hedges, numbers, threats), then venue and field style
  through sv-write-style-apply, then language through a de-AI audit, with a
  regression re-run of the research check. Applies only authorized edits,
  records each with its rule, blocks reversions and locked-decision flips,
  and writes a dated round log. Use when a draft needs repeated checking
  before review, submission or camera-ready.
license: CC-BY-NC-SA-4.0
---

# Check Loop

## Overview

Single-pass skills each fix one kind of problem. Run one after another by
hand, they undo each other: a wording pass deletes a scope qualifier, a
content pass reintroduces a phrase the wording pass removed, a co-author
restores a number another pass trimmed. This skill runs the checks in a fixed
order, for a fixed number of rounds, and keeps the state that makes the
result trustworthy: what changed, under which rule, in which round, and what
is still open.

Each round runs three checks and one re-run:

1. **Research-writing fit**: claims within evidence, scope words, hedges on
   model-read data, numbers that match the claim ledger or numbers file,
   threats coverage.
2. **Venue and field style fit**: `sv-write-style-apply` check mode with the venue
   profile.
3. **Language and de-AI**: `sv-write-humanize-audit` in `audit` mode plus any overlays.
4. **Regression**: check 1 again on the spans check 3 changed.

The loop applies only edits that a rule authorizes, never flips a locked
decision, and stops when the checks pass, a round changes nothing, an
oscillation appears, or the budget runs out. Design: `DESIGN.md` section 6.

## When to use this skill

- A full draft or a set of sections is ready for internal review,
  submission, a revision round or camera-ready.
- After a batch of co-author or reviewer changes (`feedback-to-revision`),
  to check that the fixes did not break other rules.
- After the page count changed and text was cut or filled.
- When the user asks for "a final pass", "check everything again" or
  "iterate until clean".

## When NOT to use this skill

- One quick wording pass on one paragraph: `sv-write-polish`.
- Only the de-AI pass, with edits: `sv-write-humanize-paper` in `full` or `section` mode.
- The draft has no claims yet or no evidence behind them: `sv-write-section`
  first.
- Submission gates (anonymity, artifact, template, form fields):
  `pre-submission-reviewer`.
- Resolving specific comments: `feedback-to-revision`.

## Step 0: Load context

1. Load `research-core`: `references/core/precedence.md`,
   `claims-evidence.md`, `body-text.md`, `integrity.md`, `deai.md`; the field
   profile for `research.yaml` `field`; the venue profile for `venue`; the
   overlays in `style.overlays`; the checklists `writing.md`, `integrity.md`
   and `threats.md`.
2. From `research.yaml` read `check_loop.max_rounds` (default 3), `field`,
   `venue`, `paper_type`, `review.page_budget`, `source_of_truth` (paper and
   numbers), `repos.paper.main_file`, `style.dynamic_skill`,
   `style.overlays` and `people`.
3. Read the locked decisions: accepted ADRs in `docs/adr/` and the term table
   (term, definition, rejected readings). Read the claim ledger and the
   numbers file.
4. Report which profiles loaded and their status, and which inputs are
   missing. Items that depend on a missing input are reported `unknown`,
   never `pass`.

## Inputs

| Input | Source | Default |
|---|---|---|
| Files or sections in scope | user | manuscript files reachable from `main_file`, no bibliography |
| `max_rounds` | user, then `research.yaml` `check_loop.max_rounds` | 3 |
| Locked decisions | `docs/adr/` (accepted), term table, spans the user names | none: say so in the log |
| Mode | user | apply authorized edits (or report only: one round, no edits) |
| Candidate rules | user opt-in | advisory only |

## Setup

1. Create a branch `check-loop/<date>` from the paper's source of truth and
   note the base commit. If the paper is co-edited on Overleaf, pull first;
   push back only through `research-records` `scripts/sync_guard.py`.
2. Write the locked list into the log, and save the term table as a
   tab-separated terms file for the span guard.
3. Start `docs/log/<date>-check-loop.md` from the log template, and the span
   state file `docs/log/<date>-check-loop.spans.json`.

See: references/log-template.md

## Why research fit runs first

Language edits made before content edits get thrown away, and content edits
made late reintroduce defects. In the evidence project the last senior pass
added exact numbers and scope, and in the same pass two bold finding
headlines were merged into one paragraph; a duplicated results sentence had
survived every earlier pass. Wording passes are also the step most likely to
delete a scope qualifier or a hedge, which is why check 1 re-runs after check
3. [src: note:n06§1.5; arc:ol:ba3f1ee; note:n06§2.6] (confirmed)

## Round procedure

For round k = 1 .. `max_rounds`:

1. **Check 1, research-writing fit.** Field profile plus `writing` and
   `integrity` and `threats` items: claims within evidence (WR-20 to WR-23),
   scope words (WR-19, TH-01), hedges on interpretations and model-read data
   (WR-18, TH-05), novelty (WR-24), numbers against the ledger or numbers
   file with denominators (WR-01, WR-16, WR-17, IN-01 to IN-03), agreement
   values (IN-04 to IN-06), threats coverage (TH-08, TH-10, TH-11), and the
   field's prefixed items. Never correct a number from memory.
2. **Check 2, venue and field style fit.** `sv-write-style-apply` check mode with the
   dynamic skill and venue profile: structure, section lengths against the
   page budget, contribution format, tone and tense, citation form, required
   sections. Pass it the round number, ADRs and term table; it returns
   `JA-r<k>-<nn>` findings with status `open`, `locked`, `advisory` or
   `repeat`. Only `open` findings can be applied; `repeat` counts toward the
   oscillation stop. Without `sv-write-style-apply` or a dynamic skill, run the
   profile items only and mark corpus items `unknown`. Structural moves are
   `needs-author`.
3. **Check 3, language and de-AI.** `sv-write-humanize-audit` `audit` mode (profile
   `academic`) plus enabled overlays; take its finding list.
4. **Regression 1R.** Re-run check 1 on every span changed this round. A
   check-3 edit that broke a check-1 item is reverted inside the round.
5. After each check: apply the authorized findings, commit per rule group as
   `CL-r<k>-c<n>: <summary> [<rule ids>]`, record with the span guard, and
   add one log row per finding (applied or not).
6. Close the round: per-round summary, then test the stop rules.

Finding ids: `CL-r<k>-c<n>-<nn>`; the regression re-run uses `c1R`.

See: references/round-procedure.md

## Which edits the loop applies

An edit is applied only when all hold:

- it cites a rule whose status is `confirmed` (or a `candidate` rule the user
  opted into for this run);
- it is inside the scope and outside protected content and locked spans;
- it adds no fact, number, citation or claim the sources do not hold;
- it does not contradict an accepted ADR or the term table;
- the span guard reports no error for it.

Conflicts between rules follow `research-core` precedence (venue call, ADR,
venue profile, field profile, core, overlay, skill suggestion). Two sources
at the same level are not averaged: both positions go to the author, and
the decision becomes an ADR. Everything else is a residual with edit class
`needs-author` or `report-only`.

## Oscillation guard

- A span changed in round k may not be changed back in round k+1 unless the
  check cites a different rule. With a different rule, the change is applied
  and flagged, and the rule conflict goes to the author.
- A change back under the same rule, or with no rule, is blocked; the loop
  stops at the end of that round with stop reason "oscillation".
- Locked decisions (ADRs, the term table, locked spans) are never flipped.
- Evidence: numbers trimmed from prose and restored several times; hedges on
  model-read data removed and restored; locked terms changed late and one
  change reverted by a stale base. [src: note:n06§2.3; note:n06§2.6; note:n06§2.8] (confirmed)

`scripts/span_guard.py` turns each recorded commit into word-level change
pairs and flags any new pair that undoes an earlier one, and any inserted
rejected reading of a locked term:

```
python scripts/span_guard.py check  <paper_dir> --state <spans.json> --round 2 --check 3 --rule "WR-19" --head WORKTREE --terms terms.tsv
python scripts/span_guard.py record <paper_dir> --state <spans.json> --round 2 --check 3 --rule "WR-19" --terms terms.tsv
python scripts/span_guard.py report --state <spans.json>
```

Exit 1 means a blocked change (reversion of the previous round under the same
rule, or a rejected term reading); `record` then refuses to write. WARNING
lines (different rule, older round) and INFO lines (re-edit of a changed
span) need a one-line reason in the log.

## Stop rules

Stop at the end of the first round where:

1. **all pass**: no failing confirmed item in any check;
2. **no change**: the round applied no edit;
3. **oscillation**: the guard blocked a change back, or a fixed finding came
   back;
4. **budget**: `max_rounds` reached.

## Output: the round log

`docs/log/<date>-check-loop.md` holds: scope, base and final commit, budget,
mode, profiles, missing inputs, the locked list, the round table (round,
check, finding id, location, finding, rule source and status, edit class,
outcome, commit, diff stats), guard flags with decisions, a per-round
summary, the stop reason, a short summary of what changed, the residual
findings with owners, and the checklist report. The `span_guard.py report`
table is pasted under the round table and must agree with it.

## Checklist

Report each item as pass, fail, n/a or unknown with evidence (log row,
commit, command output):

- `writing.md`: WR-01, WR-06, WR-07, WR-10, WR-12, WR-13, WR-15 to WR-24,
  WR-28, WR-31, WR-33 (the items owned by `check-loop`, plus the claim and
  number items check 1 runs).
- `integrity.md`: IN-01 to IN-06, IN-13.
- `threats.md`: TH-01, TH-02, TH-05, TH-08, TH-10, TH-11.
- The field profile's prefixed additions and the venue profile's
  formatting items that check 2 covers.

Items with `Status: candidate` are advisory unless the user opted in.

## Outputs

- `docs/log/<date>-check-loop.md` (round log) and
  `docs/log/<date>-check-loop.spans.json` (span state).
- Commits `CL-r<k>-c<n>: ...` on the `check-loop/<date>` branch.
- A short report to the user: stop reason, rounds used, edits applied per
  check, residual findings by edit class, rule conflicts that need an ADR.
- TODO items for `needs-author` residuals, with their CL ids.

## Hand-offs

- `needs-author` content gaps (missing evidence, missing spine): `sv-write-section`.
- Rule conflicts and questioned locked decisions: `research-records` (ADR).
- TODO and STATUS updates: `research-records`.
- Remaining comments from people: `feedback-to-revision`.
- Venue style rules missing from the profile: `sv-write-style-apply`.
- Submission gates after the loop: `pre-submission-reviewer`.
- Recurring findings across projects: `lessons-harvest` reads the logs.
