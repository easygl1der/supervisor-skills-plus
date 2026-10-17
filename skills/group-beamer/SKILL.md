---
name: group-beamer
description: >-
  Builds LaTeX Beamer decks for math and statistics group meetings in two
  modes: a 6 to 10 slide weekly report that loads last week's next steps,
  and a 12 to 18 slide critical paper talk with estimand, identification,
  and reproducibility slides. Compiles with latexmk and XeLaTeX, lints
  overlays and density, and stores decks through research-records. Use when
  preparing a group meeting, weekly progress slides, or a paper presentation.
license: CC-BY-NC-SA-4.0
---

# Group Beamer

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

- Manuscript prose: `paper-writer`, `deai-writing` (`academic`).
- A one-page paper card only: `paper-quickread`.
- Understanding a paper before you can present it: `study`.
- Figures that are not slides: `figure-designer`.

## Step 0: Load context

1. Mode: `weekly-report` (default audience `advisor`) or `paper-talk`.
   Audience `advisor` or `peer` (see `audience.md`).
2. Load `research-core` field profile (`causal` or `stats` when that is the
   project field). Load `group-preferences.md` (may be an empty slot).
3. Weekly: `docs/STATUS.md`, latest `docs/log/*-group-meeting.md` next
   steps, git log since the last meeting, Linear if enabled.
4. Paper-talk: the `paper-quickread` card (or MinerU markdown). Never extract
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
   title verb matches claim level), then `deai-writing` `audit` with the
   `slides` profile. Speaker notes (`\note{}`) use `academic`.
6. Export notes with `scripts/export_notes.py`. Save through
   `research-records` Task 8: `docs/log/<date>-group-meeting.md` and
   `docs/meetings/<date>/` (`.tex`, PDF, notes).

See: references/weekly-report.md
See: references/paper-talk.md
See: references/audience.md
See: references/slide-rules.md
See: references/quality-gates.md
See: references/speaker-notes.md
See: references/causal-slides.md
See: references/group-preferences.md

## Outputs

- Approved outline, then a compiling `.tex` and PDF.
- Exported `notes.md`.
- research-records log plus `docs/meetings/<date>/`.

## Hand-offs

- `paper-quickread`: card in for paper-talk.
- `research-bridge`: link-to-project slide.
- `figure-designer`: TikZ DAGs; Graphviz PDF only for large or changing graphs.
- `research-records`: accumulation and last-week next steps.
- `deai-writing`: `slides` profile on frames; `academic` on `\note{}`.
- `pre-submission-reviewer` devil's-advocate pass plus
  `research-core` `fields/causal.md` reviewer questions, as the substitute
  for a missing Critic checklist.
- `style-mine`: later fill of `group-preferences.md` from past decks.
- `research-supervisor`: routes group-meeting slide requests here.
