# group-beamer: Step 2 design proposal (not implemented)

Status: proposed 2026-10-17; the owner paused the work after Step 2. Nothing
under `skills/group-beamer/` exists yet. Reference notes:
`docs/handoff/group-beamer-notes.md`. Prompt: `group-beamer-PROMPT.md`.

## Layout

```
skills/group-beamer/
  SKILL.md                 triggers, modes, Step 0, workflow, outline gate, checklist, outputs, hand-offs
  references/
    weekly-report.md       6-10 slides; `progress` variant; loads last week's next steps
    paper-talk.md          12-18 slides; critique slides; optional replication segment
    audience.md            advisor vs peer placement rules
    slide-rules.md         per-slide limits, no overlays, boxes, tables, colour, pacing
    quality-gates.md       compile/check loop, review passes, claim-level rules
    speaker-notes.md       \note{} content and Markdown export
    causal-slides.md       estimand/identification card, roadmap, C-word rule, notation defaults (Ding)
    group-preferences.md   empty slot for the group's conventions (owner, or style-mine later)
  templates/
    moloch-cjk/            wrapper over the installed Moloch package (colours, ctex, notes)
    simpleplus-cjk/        SimplePlus .sty vendored (Unlicense) + wrapper
    sysu-like/             own green theme from SYSU colours only; logos supplied locally
    skeleton-weekly.tex, skeleton-paper-talk.tex
  scripts/
    build.sh               latexmk -xelatex; refuses and names what to install if xelatex/theme missing
    check_log.py           Overfull/Underfull parser mapped to pages, severity (>10pt critical); selftest
    render_pages.sh        pdftoppm 150 dpi (fallback PyMuPDF), batches of 3 for inspection
    lint_deck.py           no overlays, <=7 bullets, <=2 boxes, no \tiny, text-only share <=30%
    export_notes.py        \note{} to notes.md
```

## Modes

- `weekly-report` (default audience advisor; 6-10 slides): conclusion first;
  last week's next steps marked done / partial / dropped; results; blockers;
  decisions needed; next steps; details in the appendix. Inputs:
  research-records STATUS and logs, git log since the last meeting, Linear if
  enabled. `progress` is a longer topic-level variant.
- `paper-talk` (12-18 slides): rebuild the paper's section tree, map to slide
  groups. Critique slides: question and estimand card (Method Atlas fields;
  unstated estimand flagged and our reading labelled presenter's
  interpretation); identifying assumptions ranked by strength; what breaks
  under violation; claim vs evidence from quickread tags; link to project
  (research-bridge); reproducibility (rerun or simulate a violation; optional
  Reading-Group-2026 segment). Results slides give numbers; the causal
  reading goes on the discussion slide (Hernan 2018).
- `audience: advisor | peer` decides what stays in the main body.

## Workflow

1. Load context (records, quickread card, causal/stats profiles, group preferences).
2. Outline gate: claim-style titles, content, evidence source, new notation per slide; owner approves.
3. Draft in batches of 5-8 slides; numbers copied with table/page reference; missing data is `TODO`.
4. Compile-check loop, at most 4 rounds: build, check_log, lint_deck, render, inspect pages in batches of 3; fix spacing before font size; every box checked visually (Beamer hides overfull warnings in blocks).
5. Read-only review passes: visual, pedagogy, claims (narrow never strengthen; title verb matches claim level), deai-writing `slides` profile.
6. Speaker notes from the final render, in `\note{}` and exported Markdown.
7. Save via research-records: `docs/log/<date>-group-meeting.md` (next steps) and `docs/meetings/<date>/` (.tex, PDF, notes).

## Integration

paper-quickread (card in), research-bridge (link slide), figure-designer
(TikZ DAG render script; Graphviz for large graphs), research-records (log
and accumulation), deai-writing (new `slides` profile plus Beamer detection),
pre-submission-reviewer devils-advocate pass plus causal profile reviewer
criteria (substitute for the missing Critic checklist), style-mine (mine
group conventions from past decks), research-supervisor (routing row), ADR,
README lists, THIRD_PARTY rows.

## Open decisions (owner)

1. TeX install on SG: BasicTeX + `tlmgr install latexmk moloch beamertheme-simpleplus ctex ...` + `brew install poppler` (about 1 GB), or full MacTeX (about 5 GB).
2. Moloch: depend on the installed package (recommended) or vendor unmodified.
3. SYSU: own look-alike theme or drop.
4. Overlays: ban and use frame duplication (recommended) or allow simple `\pause`.
