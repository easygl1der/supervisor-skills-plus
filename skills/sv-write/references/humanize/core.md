<!-- Moved from skills/deai-writing/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# De-AI Writing

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- The one question
- Diagnosis vocabulary (S1 to S7)
- Editing contract (summary)
- Modes
- Pattern catalog and the academic profile
- Writing principles
- Never inject
- Guardrails
- What only the author can add
- Verification block
- Inline notes
- Checklist
- Outputs
- Hand-offs
- Credits

## Overview

Reviewers now read many model-polished drafts and stop trusting a paper on
pattern-match. What gives a draft away is mostly not single words but
habits: every claim said four times, objections nobody raised, every part
presented as equally important, raw statistics pasted into prose, and prose
smoothed to a uniformity no person keeps up. This skill finds those habits,
names them, and removes them without touching what the paper claims.

Three former skills are merged here:

- the owner's `deai-paper-writing` kit is the spine: the S1 to S7 diagnosis,
  the claim ledger, the information-gain and asymmetry tests, the rule that
  the output is never longer than the input, and the five modes;
- `avoid-ai-writing` (MIT, Conor Bronsdon) gives the editing contract, the
  never-inject list, the tiered pattern catalog, the verification block and
  context profiles, to which an `academic` profile is added;
- the owner's `humanize-paper` gives the writing principles: Williams'
  *Style*, hedge interpretations not facts, `% TODO: verify` for unverifiable
  superlatives, keep the author's plainness, and minimal LaTeX diffs.

Evidence that this matters in practice: a senior co-author's inline note
asked to "fix AI smells" in a section title, and an agent had introduced the
phrase (`arc:msr:0f96193`, fixed in `arc:msr:9ef4a07`; `note:n05`); a figure
palette was judged "too AI" in the group chat (`arc:chat:group@2026-10-02T22:28`).

## When to use this skill

- A draft or section reads as generated (by a model or by an author on
  autopilot) and should not.
- Before an internal review or submission, as a report-only audit.
- `sv-review-loop` round check 3 calls this skill in `audit` mode.
- Numbers in prose look like a lab notebook (decimals, p-values inline).

## When NOT to use this skill

- Grammar, fluency or a first language pass on one section: `sv-write-polish`.
- Claims that do not match the evidence or a missing claim ledger:
  `sv-write-section` first; this skill reports such gaps, it does not fill them.
- Resolving co-author or reviewer notes in the source: `sv-feedback-revise`.
- Multi-round passes across research fit, venue fit and language:
  `sv-review-loop`, which calls this skill for the language part.
- Judging whether someone used AI. The catalog gives signals, not proof.

## Step 0: Load context

1. Load `research-core`: `references/core/deai.md` (the short contract),
   `claims-evidence.md`, `body-text.md`, `precedence.md`; the field profile
   for `research.yaml` `field` (section "Tone and phrasing"); the venue
   profile for `venue`; every overlay in `style.overlays`; and the checklist
   `references/checklists/writing.md`.
2. From `research.yaml` read `field`, `venue`, `paper_type`, `style.overlays`,
   `source_of_truth.numbers` and `people` (which note macros exist).
3. Read the project's locked decisions: accepted ADRs in `docs/adr/` and the
   term table (term, definition, rejected readings). Locked spans and terms
   are protected content.
4. Load the claim ledger if one exists (`research-core` template
   `claim-ledger.md`); `diagnose` extends it.
5. Say which profiles and overlays were loaded and their status. Without
   `research.yaml`, use the `academic` profile, no overlays, and report
   venue-dependent rules as unknown.

## The one question

For every sentence: **does it do one job, plainly?** Not "does it break a
rule". When a sentence sounds generated, say it the way a colleague would
explain it aloud. [src: skill:humanize-paper] (confirmed)

## Diagnosis vocabulary (S1 to S7)

| Code | Syndrome | Typical fix |
|---|---|---|
| S1 | Over-closed narrative loop: 1:1 motivation-component-analysis-result lattice, a callback after every result | One closing callback per major section; let structure be uneven |
| S2 | Restatement redundancy: the same claim paraphrased in every section | Claim ledger, one canonical location per claim; cut the rest |
| S3 | Preemptive defensiveness: arguing with imagined reviewers | Keep an objection only if a reader would raise it and the paper answers it with its own evidence; at most two |
| S4 | Missing storyline, analysis dumping | Spine: unknown before, made possible, establishing analysis, falsifier; rank PRIMARY / SUPPORTING / DUE DILIGENCE |
| S5 | Reporting hygiene failure | Mode `numbers` |
| S6 | Padding to page count | Positioning clauses in related work; specific future work; fill pages by priority |
| S7 | Surface style: lexicon, rhythm, metadiscourse | Pattern catalog under the context profile |

Two tests decide close calls:

- **Information-gain test:** could a competent reader of the preceding text
  have produced this sentence? Then delete it.
- **Asymmetry test:** does the text say anywhere that one thing matters much
  more than another? If not, it was shaped to look thorough.

Three principles: say it once, in the strongest place; earn the closure;
concrete beats comprehensive. [src: skill:deai-paper-writing] (confirmed)

See also `diagnosis-and-modes.md`

## Editing contract (summary)

1. **Candidate, finding, authorized edit.** A pattern match is a candidate.
   It becomes a finding only after pass conditions, context profile,
   protection and meaning are checked. A finding becomes an edit only when
   the mode and the user's scope authorize it. [src: skill:avoid-ai-writing] (confirmed)
2. **Protected content** is never changed by a style edit: numbers,
   citations and `\ref`/`\label`, math and theorem statements, terms in the
   term table, quotations, ADR-locked spans, LaTeX structure, reviewer-note
   macros. Report findings inside it instead.
3. **Source fidelity.** No new facts, stance, causality or confidence. A gap
   becomes `[AUTHOR: question]` or `% TODO: verify <claim>`.
4. **Not longer.** The output is not longer than the input unless expansion
   was requested. [src: skill:deai-paper-writing] (confirmed)
5. **No uniform replacement.** Do not trade one repeated pattern for another,
   such as the same two connectors chained after a punctuation ban.
   [src: note:n02§11.4; skill:humanize-paper] (confirmed)
6. **Punctuation defers.** Dash, semicolon and colon rules come from the
   venue profile or an overlay; without them they are density judgments, not
   bans. [src: user:2026-10-13; note:n02§11.4] (confirmed)

See also `editing-contract.md`

## Modes

| Mode | Edits? | Input | Output |
|---|---|---|---|
| `diagnose` | No | Whole paper | Claim ledger, closure map, defensiveness inventory, density and spine audit, surface counts, three-sentence verdict |
| `full` | Yes, named files | Whole paper or chapter | Revised text after five ordered passes (structure, defence, paragraphs, sentences, numbers), change log, statistics, open author items, what was protected, verification |
| `section` | Yes, one section | One section | Revised section against its contract (abstract, introduction, related work, method, results, conclusion), change log, contract PASS/FAIL |
| `numbers` | Presentation only | Tables, captions, sentences with numbers | Issue table (same value, new presentation), conventions sentence, over-precise numbers, inconsistencies flagged |
| `audit` | No | Named files or sections | S1 to S7 scores, five tests (topic-sentence, movability, asymmetry, falsifier, deletion), gate PASS/FAIL, finding list with edit classes |

Defaults: first contact runs `diagnose`; "clean this up" runs `section` on the
named scope with minimal wording edits; a gate request runs `audit`. Run order
for a whole paper: `diagnose`, `full` (or `section` on the worst sections),
`numbers`, then `audit`.

### `audit` mode and `sv-review-loop`

`audit` never edits. Its finding list is the interface to `sv-review-loop`: one
row per finding with id, location, syndrome or pattern, severity (P0, P1,
P2), rule source, proposed edit and edit class:

- `authorized-if-run`: a deletion or wording edit that `full` or `section`
  would make under the contract;
- `needs-author`: needs content, a decision, or touches a locked span;
- `report-only`: judgment call, protected content, or out of scope.

`sv-review-loop` decides which `authorized-if-run` findings to apply in its round
and records them. Finding ids are `DA-<nn>` within one audit run.

## Pattern catalog and the academic profile

The catalog has Tier 1A frequency markers (reported separately from Tier 1B
clarity edits, which are not authorship evidence), Tier 2 cluster words,
Tier 3 density words, rationed words with per-paper caps (for example
"novel" at most twice), sentence and paragraph patterns with P0 to P2
severity, and whole-text tests (rhythm, over-polishing, reshuffle immunity,
treadmill effect).

The `academic` profile is the default for manuscripts. In it, technical
senses are kept (robust statistics, test harness, software ecosystem, loss
landscape), bold claim sentences and contribution lists pass where the field
or venue profile prescribes them, hedging follows "interpretations, not
measurements", and punctuation rules defer to venue and overlays. The
`slides` profile is for Beamer decks (`sv-slides` calls `audit` with
it); speaker notes stay on `academic`.

The canonical banned-word list is the shared
`ai-tone-guardrails.md` in `sv-write/references/`.

See also `patterns.md`
See also `skills/sv-write/references/ai-tone-guardrails.md`

## Writing principles

- Characters as subjects, actions as verbs, stress at the sentence end; one
  point per paragraph, stated early (after Williams, *Style*).
- Hedge interpretations ("the results suggest"), never measured facts; verb
  strength matches evidence strength.
- An unverifiable "first", "only" or "outperforms all" gets
  `% TODO: verify`; a verified novelty claim carries "to our knowledge".
- Keep the author's voice, including its plainness; fix real grammar errors.
- A paper defends; a review hedges. Do not import response-letter softening.
- Leave LaTeX machinery alone; keep one sentence per line if the file does;
  edit only the sentences that change.

[src: skill:humanize-paper; note:n06§2.6] (confirmed)

## Never inject

A rewrite may not add: a perspective or experience the source lacks,
manufactured stakes, a foil the source did not argue, performed candor,
dashes for drama, staccato fragments, invented specifics (numbers, names,
datasets, mechanisms), or a new uniform pattern. A fabricated specific is
worse than the vague wording it replaced. [src: skill:avoid-ai-writing] (confirmed)

## Guardrails

Reject any edit that removes a real limitation or negative result, removes
statistical analysis instead of relocating it, breaks a term, drops a
citation, turns necessary overlap into a gap, makes prose informal to sound
human, cuts results or mechanisms instead of scaffolding, or adds what the
author cannot verify. [src: skill:deai-paper-writing] (confirmed)

## What only the author can add

A pass removes tells; it cannot supply presence. At the end of `full` and
`audit`, list the author-only items that are missing (a surprising number,
a rejected design choice, an honest asymmetry, an arbitrary choice labelled
as such, a failure with a mechanism, a contestable judgment, deliberate
unevenness, the authors' own rhythm) and ask the author to add some by hand.
Never write them on the author's behalf.

## Verification block

Every run ends with: **Editing passes** (used and limit), **Checks** (what
ran; this library ships no detector, so the reading is "model-only" unless
the project adds one), **Residuals** (findings left and why), **Stop reason**.
Report-only modes state 0 editing passes. [src: skill:avoid-ai-writing] (confirmed)

## Inline notes

Notes such as `\todo{}` or a senior's comment macro are requests with an
owner. Leave them in place and hand them to `sv-feedback-revise`; never
hide or resolve them here.

## Checklist

Run these items from `research-core` `references/checklists/writing.md` and
report each as pass, fail, n/a or unknown with evidence (file and line, or
the change-log row):

- WR-31 De-AI pass under the contract (protected content unchanged, output
  not longer, no new uniform pattern).
- WR-32 Punctuation bans only from an overlay or the venue.
- WR-33 No scaffolding or process preambles.
- WR-18 Hedge interpretations, not measurements.
- WR-09 Paragraphs build on each other (reshuffle test).
- WR-10 Each caveat once (S3).
- WR-12 One name per concept (no synonym cycling on terms).
- WR-24 Novelty claims scoped and stated once (rationed items).

Items with `Status: candidate` are advisory.

## Outputs

- `diagnose`: the five artifacts and verdict, as a report; optionally the
  extended claim ledger.
- `full`, `section`, `numbers`: edited files (minimal diff) or returned
  text, change log, statistics, open author items, protected items, the
  verification block.
- `audit`: scores, tests, gate, finding list with edit classes; no edits.
- When run inside a project, a dated note in `docs/log/` if the user asks;
  `sv-review-loop` writes its own log.

## Hand-offs

- Multi-round checking with research and venue fit: `sv-review-loop`.
- Claims beyond the evidence, a missing spine or ledger: `sv-write-section`.
- Venue style deviations: `sv-write-style-apply` check mode.
- Single-pass fluency and grammar: `sv-write-polish`.
- Inline co-author and reviewer notes: `sv-feedback-revise`.
- Figures that look generated: `sv-figure-design`.
- Recurring tells across projects: `sv-supervisor-harvest` proposes catalog or
  profile changes.

## Credits

The editing contract, never-inject list, verification block and pattern
catalog are adapted from `avoid-ai-writing` by Conor Bronsdon, MIT License;
the license text is in `LICENSE-avoid-ai-writing.txt` in this folder. The
diagnosis vocabulary and modes come from the owner's `deai-paper-writing`
kit; the writing principles from the owner's `humanize-paper` skill.
