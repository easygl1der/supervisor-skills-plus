<!-- Moved from skills/group-beamer/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Group Beamer

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Modes
- Audience
- Step 0: Load context
- Workflow
- Accumulation across meetings
- Checklist
- Evals
- Outputs
- Hand-offs

## Overview

Produce Beamer decks for research group meetings in math, statistics, and
causal inference. Two first-class modes: `weekly-report` (progress; the
longer `progress` variant lives under it) and `paper-talk` (critical paper
presentation). Default theme is Moloch from TeX Live. SimplePlus is the
minimal alternative. `sysu-like` is an own green look-alike (SYSU colours
only; logos stay local and untracked). Compile with `latexmk -xelatex`.
CJK via `ctex`. Not Marp, not PPTX.

## When to use this skill

- Weekly group meeting, progress report, or "slides for the advisor".
- Presenting a paper to the group, with critique and a link to our project.
- Rebuilding last week's next steps into this week's status.

## When NOT to use this skill

- Manuscript prose: `sv-write-section`, `sv-write-humanize-paper` (`academic`).
- A one-page paper card only: `sv-quickread`.
- Understanding a paper before you can present it: `sv-study`.
- Figures that are not slides: `sv-figure-design`.

## Modes

| Mode | Slides | Spine |
|---|---|---|
| `weekly-report` | 6 to 10 | conclusions first; last week's next steps marked done / partial / dropped; results with sources; blockers; decisions needed; next steps with owner, date and kill criterion |
| `progress` (under weekly-report) | 10 to 14 | the same spine by topic: what is locked, what is open, the next experiment or lemma |
| `paper-talk` | 12 to 18 | the paper's section tree mapped to slide groups, then the critical slides below |

Critical slides every paper talk carries (`paper-talk.md`, `causal-slides.md`):

1. Paper card: Question, Estimand, Identification, Key assumption, Main
   result, Robustness, Biggest threat, External validity. An unstated
   estimand is a finding; our reading is labelled "presenter's
   interpretation".
2. Identifying assumptions ranked by strength, each marked knowledge-based
   or convenience, with what breaks when it fails.
3. Results as numbers with table or page; no causal verb on that slide. The
   causal reading and its assumptions go on the discussion slide.
4. Claim against evidence, from the quickread tags (proved / empirical /
   conjectured). A slide may narrow a paper's claim, never strengthen it.
5. Link to our project (from a `sv-study-bridge` card when one exists).
6. Reproducibility: rerun, or simulate under a violated assumption.
7. A closing discussion question for the group, not a slogan.

## Audience

`audience: advisor` (default) or `peer` changes placement, never facts.

- Advisor: conclusions, blockers and decisions needed come first; each
  decision is a boxed question with options; derivations, proofs, extra
  robustness tables and notation go to `\appendix`, each backup slide
  hyperlinked from the main slide it supports.
- Peer: derivations and experiment details stay in the main body when they
  are the point of the meeting; in a paper talk the replication and
  assumption-violation slides move into the main body.
- Both: one idea per slide, sentence titles, fewer slides than minutes,
  the simple sufficient condition before the general theorem.

## Step 0: Load context

1. Mode: `weekly-report` (default audience `advisor`) or `paper-talk`.
   Audience `advisor` or `peer` (see `audience.md`).
2. Load `research-core` field profile (`causal` or `stats` when that is the
   project field). Load `group-preferences.md` (may be an empty slot).
3. Weekly: `docs/STATUS.md`, latest `docs/log/*-group-meeting.md` next
   steps, git log since the last meeting, Linear if enabled.
4. Paper-talk: the `sv-quickread` card (or MinerU markdown). Never extract
   a PDF with pypdf or ad hoc scripts.
5. Theme: `moloch-cjk` unless the user names `simpleplus-cjk` or `sysu-like`.

## Workflow

1. Load context. Missing numbers become `TODO`. Do not invent.
2. Outline gate. Per slide: assertion title, content, evidence source, new
   notation. Stop until the owner approves. Then draft in batches of 5 to 8
   slides.
3. Draft from `templates/skeleton-weekly.tex` or
   `templates/skeleton-paper-talk.tex` plus the chosen theme wrapper.
4. Compile-check loop, at most 4 rounds: `scripts/build.sh`,
   `scripts/check_log.py`, `scripts/lint_deck.py`, `scripts/render_pages.sh`
   (inspect pages in batches of 3). Fix spacing before font size. Check
   every box visually (Beamer hides overfull warnings inside blocks).
5. Read-only review: visual, pedagogy, claims (narrow never strengthen;
   title verb matches claim level), then `sv-write-humanize-slides` `audit` with the
   `slides` profile. Speaker notes (`\note{}`) use `academic`.
6. Export notes with `scripts/export_notes.py`. Save through
   `sv-supervisor-records` Task 8: `docs/log/<date>-group-meeting.md` and
   `docs/meetings/<date>/` (`.tex`, PDF, notes).

## Accumulation across meetings

Each meeting leaves a record that the next weekly report reads:

1. After the meeting, `sv-supervisor-records` writes
   `docs/log/<date>-group-meeting.md` from the research-core
   `group-meeting-log.md` template: mode, audience, what happened, decisions
   (linked ADRs) and the Next steps table (item, owner, date, kill
   criterion). Next steps come from the approved outline or the spoken
   close, never from memory.
2. The next weekly report loads the latest such log and marks every item
   done, partial or dropped, with a one-line reason for partial and dropped.
   Items are not silently removed; a dropped item stays visible once.
3. Partial items carry forward into the new Next steps with their original
   date shown. An item partial for three meetings in a row is raised as a
   blocker or a decision for the advisor.
4. With no prior log, slide 3 says so and the marks are skipped.
5. Decks and notes stay under `docs/meetings/<date>/`; STATUS keeps only the
   current state. Paper talks are logged the same way, and their
   link-to-project slide is a candidate input for `sv-study-bridge`.

See also `weekly-report.md`
See also `paper-talk.md`
See also `audience.md`
See also `slide-rules.md`
See also `quality-gates.md`
See also `speaker-notes.md`
See also `causal-slides.md`
See also `group-preferences.md`

## Checklist

Report each item as pass, fail, n/a or unknown, with evidence (page,
`check_log.py` or `lint_deck.py` output, log entry):

- The outline was approved before drafting.
- No invented numbers; every number has a table, page, script or commit,
  and missing data is `TODO`.
- `check_log.py`: no overfull box above 10pt and no undefined reference or
  citation; every box inspected on the rendered page.
- `lint_deck.py`: no overlay commands, at most 7 bullets and 2 boxes per
  slide, no `\tiny`, text-only slides at most 30 percent (frames marked
  `% gb:text-ok` with a reason are exempt; no filler formulas).
- Title verbs at or below the claim level; results slides carry no causal
  verb; the causal reading names its assumptions.
- Weekly report: every item from the last log is marked done, partial or
  dropped.
- Paper talk: paper card, ranked assumptions, reproducibility slide and a
  closing discussion question are present.
- `sv-write-humanize-slides` `audit` with the `slides` profile ran; notes checked under
  `academic`.
- Notes exported; deck and log saved through `sv-supervisor-records` Task 8.

## Evals

Real runs, compiled and checked: `evals/2026-10-17-weekly/` (Chinese,
advisor, with the sv-supervisor-records meeting log) and
`evals/2026-10-17-paper-talk-sdid/` (English, peer, SDID; numbers checked
against the paper's tables). Each has `slides.tex`, `slides.pdf` and the
exported `notes.md`.

## Outputs

- Approved outline, then a compiling `.tex` and PDF.
- Exported `notes.md`.
- sv-supervisor-records log plus `docs/meetings/<date>/`.

## Hand-offs

- `sv-quickread`: card in for paper-talk.
- `sv-study-bridge`: link-to-project slide.
- `sv-figure-design`: TikZ DAGs; Graphviz PDF only for large or changing graphs.
- `sv-supervisor-records`: accumulation and last-week next steps.
- `sv-write-humanize-slides`: `slides` profile on frames; `academic` on `\note{}`.
- `sv-review-once` devil's-advocate pass plus
  `research-core` `fields/causal.md` reviewer questions, as the substitute
  for a missing Critic checklist.
- `sv-write-style-mine`: later fill of `group-preferences.md` from past decks.
- `sv-supervisor`: routes group-meeting slide requests here.
