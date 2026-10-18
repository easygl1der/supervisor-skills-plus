# Round procedure

The detailed procedure behind `sv-review-loop`: setup, the three checks and the
regression re-run, which findings the loop may apply on its own, how changes
are recorded, the oscillation guard, and the stop rules.

## Contents
1. Setup
2. Findings: ids and fields
3. Check 1: research-writing fit
4. Check 2: venue and field style fit
5. Check 3: language and de-AI
6. Regression re-run of check 1
7. Which edits the loop may apply
8. Applying and recording a change
9. Oscillation guard
10. Stop rules
11. Why the order is research, venue, language
12. Evidence

## 1. Setup

1. **Scope.** The files or sections named by the user. Default: the
   manuscript files reachable from `repos.paper.main_file`, without the
   bibliography. Out-of-scope text is read for context, never edited.
2. **Budget.** `max_rounds` from the user, else `research.yaml`
   `check_loop.max_rounds`, else 3.
3. **Branch and base.** Work on a branch `check-loop/<date>` from the
   paper's source of truth (`source_of_truth.paper`). Record the base commit
   in the log. If the paper is co-edited on Overleaf, pull first and run
   `sv-supervisor-records` `sync_guard.py` before pushing back; never copy over.
4. **Locked list.** Build it before round 1 and paste it into the log:
   - accepted ADRs in `docs/adr/` that fix wording, numbers printed,
     section layout or reporting rules (for example which agreement values
     print);
   - the term table (term, definition, rejected readings), saved as a
     tab-separated file for `span_guard.py --terms`
     (`term<TAB>rejected1;rejected2`);
   - spans the user names as locked (an abstract already entered in a
     submission form, a paragraph an advisor signed off).
5. **Inputs per check.** Claim ledger and numbers file
   (`source_of_truth.numbers`); field profile; venue profile; sv-write-style-apply
   dynamic skill (`style.dynamic_skill`); overlays (`style.overlays`).
   Note any input that is missing; its items become `unknown`, not `pass`.
6. **Authorization.** Ask once before round 1: "apply authorized edits" (the
   default) or "report only". In report-only mode the loop runs one round and
   stops.

## 2. Findings: ids and fields

Id: `CL-r<round>-c<check>-<nn>`, for example `CL-r2-c3-04`. The regression
re-run uses check `1R`.

Fields: location (file:line and the first words), what is wrong, rule
source (checklist id, profile rule with its `[src:]`, ADR number, or the
`sv-write-humanize-audit` finding id and syndrome), rule status (confirmed or
candidate), edit class (`authorized`, `needs-author`, `report-only`),
proposed edit, outcome (applied in commit X, deferred, blocked by guard,
reverted by regression).

## 3. Check 1: research-writing fit

Load the field profile ("Rigor and threats", "Checklist additions") and the
`research-core` checklists `writing.md`, `integrity.md` and `threats.md`.
Run, for the spans in scope:

| Question | Items |
|---|---|
| Every claim within its evidence; nothing claimed that was not measured | WR-20, WR-21, WR-22, WR-23 |
| Scope words present where pooled or subset results are generalized | WR-19, TH-01, TH-02 |
| Hedges on interpretations and on model-read or text-derived data, never on measured counts | WR-18, TH-05, `claims-evidence.md` section 5 |
| Novelty claims scoped and stated once | WR-24 |
| Every number in prose, tables and captions matches the claim ledger or numbers file, with a denominator | WR-01, WR-16, WR-17, IN-01, IN-02, IN-03 |
| Agreement values named and printed under the written rule | IN-04, IN-05, IN-06 |
| Threats cover the claims made, are true of the paper, and keep contradicting results | TH-08, TH-10, TH-11 |
| Field additions | the profile's prefixed items (for example `SE-` items) |

Numbers procedure: list every number in scope (a regular expression over
digits and percentages is enough to start), map each to a ledger or numbers
file row, and report unmapped numbers and mismatches. Never correct a value
from memory or from another sentence.

Typical authorized check-1 edits: adding a scope phrase that the ledger
states ("pooled across the studied repositories"); restoring a hedge on a
model-read measure; moving a hedge from a measured count to its
interpretation; adding "to our knowledge" to a verified novelty claim;
replacing a causal verb with an associational one. Anything that needs new
data, a new analysis or a decision is `needs-author`.

## 4. Check 2: venue and field style fit

Run `sv-write-style-apply` in check mode with the project's dynamic skill and the
venue profile. It reports deviations; the loop decides what to apply.

- Structure and section order against the venue and field profile
  ("Typical structure").
- Section lengths against `review.page_budget`; the page-filling priority
  (WR-11) when short; never pad.
- Contribution format (the venue profile decides list or prose).
- Tone and tense conventions of the exemplars.
- Citation form (`\citet` vs "Author et al.~\cite"), required sections
  (data availability, AI-use statement).

Inputs passed: target sections, the round number, ADRs and the term table.
Its findings carry `JA-r<round>-<nn>` ids and a status: `open` (may be
applied under section 7), `locked` (touches a locked decision: report only),
`advisory` (candidate or weakly supported rule: report only unless the user
opted in), `repeat` (raised in an earlier round: counts as a returning
finding for the oscillation stop). Keep the JA id in the log row next to the
CL id.

If `sv-write-style-apply` or the dynamic skill is not available, run the venue and
field profile items only and mark corpus-derived items `unknown`. Structural
moves (reordering sections, merging subsections) are `needs-author` unless
the user asked for them; check 2 applies wording-level fixes only.

## 5. Check 3: language and de-AI

Run `sv-write-humanize-audit` in `audit` mode on the spans in scope, with the context
profile `academic` and the overlays from `style.overlays`. Take its finding
list. Apply `authorized-if-run` findings that pass section 7; carry the
others as residuals. Overlays and the venue profile decide punctuation;
without them, punctuation is never edited.

## 6. Regression re-run of check 1

After the check-3 edits, re-run check 1 on every span changed in this round
(the whole scope if cheap). A check-3 edit that broke a check-1 item (a
deleted scope qualifier, a removed hedge, a number moved out of a sentence
that needed it, a caveat cut that was the only statement of a threat) is
reverted in the same round and recorded with outcome "reverted by
regression". This is not an oscillation: the revert happens inside the
round, before the round is closed.

## 7. Which edits the loop may apply

All of these must hold; otherwise the finding is carried as a residual.

1. The finding cites a rule, and the rule's status is `confirmed` (a
   `candidate` rule is advisory unless the user opted in for this run).
2. The edit is inside the scope and outside protected content (numbers,
   citations, `\ref`/`\label`, math, terms, quotations, LaTeX structure,
   reviewer-note macros) and outside every locked span.
3. The edit adds no fact, number, citation or claim the sources do not hold,
   and the output span is not longer than needed (de-AI contract).
4. The edit does not contradict an accepted ADR or the term table.
5. `span_guard.py check` reports no ERROR for it (section 9).
6. When two rules conflict, the precedence order in `research-core`
   (`precedence.md`) decides: venue call, ADR, venue profile, field profile,
   core, overlay, skill suggestion. Same-level conflicts are not resolved by
   the loop: both positions go to the author.

## 8. Applying and recording a change

1. Apply the authorized edits of one check, grouped by rule source.
2. Commit each group: `CL-r<k>-c<n>: <short summary> [<rule ids>]`. Never mix
   loop edits with feedback fixes, syncs or unrelated changes.
3. Record it: `python scripts/span_guard.py record <paper_dir> --state
   docs/log/<date>-check-loop.spans.json --round <k> --check <n> --rule
   "<rule ids>" --terms <terms.tsv>`. The base defaults to the head of the
   previous record.
4. Add a row per finding to the round table in the log, with the commit and
   the diffstat (`git diff --stat <base>..<commit>`).
5. If the project compiles, build once per round and note page count and
   new warnings.

## 9. Oscillation guard

- A span changed in round k may not be changed back in round k+1 unless the
  check cites a **different** rule than the one that changed it. Then the
  change is applied, flagged in the log, and the conflict between the two
  rules goes to the author (an ADR fixes it for later rounds).
- A change back under the same rule, or with no rule, is blocked: the span
  stays as it is, the finding is a residual with outcome "blocked by guard",
  and the loop stops at the end of the round (oscillation detected).
- Locked decisions are never flipped, whatever rule a check cites. A finding
  that would flip one is reported to the author as a possible reason to
  supersede the ADR.
- Reverting an older round (k-2 or earlier) is allowed only with a reason in
  the log; `span_guard.py` reports it as WARNING.
- Every re-edit of a span changed earlier (INFO from `span_guard.py`) gets a
  one-line reason in the log.

## 10. Stop rules

Stop at the end of the first round where any of these holds, and write the
stop reason in the log:

1. **All pass:** every check reports no failing confirmed item.
2. **No change:** the round applied no edit (only residuals remain).
3. **Oscillation:** the guard blocked a change back, or the same finding id
   pattern reappeared after being fixed.
4. **Budget:** `max_rounds` reached.

Report every residual with its id, rule, edit class and the reason it was
not applied. `needs-author` residuals become TODO items with the CL id
(`sv-supervisor-records`).

## 11. Why the order is research, venue, language

Language edits made before content edits get thrown away, and content edits
made late reintroduce defects that the language pass had already cleared.
In the evidence project, the senior co-author's last pass after the
deadline extension added exact numbers and scoping, and in the same pass two
bold finding headlines were merged into one paragraph, while a duplicated
results sentence from an earlier session had stayed in the text until that
same pass commented it out.
[src: note:n06§1.5; arc:ol:ba3f1ee; note:n06§0.3] (confirmed)

So each round checks what the paper claims first, then whether it reads as
the venue expects, and only then the wording. Check 1 re-runs after check 3
because a wording pass is the step most likely to delete a scope qualifier
or a hedge. [src: note:n06§2.6; note:n06§2.3] (confirmed)

## 12. Evidence

- Numbers were trimmed from prose and restored several times within days,
  and a results table count went back and forth across sessions: the rule
  that held was "one exact number per claim, the rest in tables", decided
  once. [src: note:n06§2.3] (confirmed)
- Hedges on model-read data were removed and restored, and the last pass
  eroded one while re-scoping others. [src: note:n06§2.6] (confirmed)
- Locked terms changed late, and one term change was reverted by a stale base
  and re-applied. [src: note:n06§2.8] (confirmed)
- A scope qualifier was trimmed and restored within about thirty hours with
  no reason stated for either edit. [src: note:n06§1.10] (candidate)
- Upstream has no whole-manuscript loop with a round budget; `sv-write-polish`
  stays single-pass. [src: note:n01§4.3] (confirmed)
