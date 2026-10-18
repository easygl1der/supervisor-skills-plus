# Checklist: figures

Items for figures and tables in any field: clarity, figure and text
mirroring, what belongs in a figure, where figure numbers come from, and how
figures are produced. Field profiles add field-specific figure items.

Run by: sv-figure-design, sv-figure-drawio

## Contents
1. Clarity
2. Figure and text mirroring
3. What goes in a figure
4. Data in figures
5. Process and files

## 1. Clarity

### FG-01 Vector output, readable text
- [ ] Check: Every figure is vector (PDF, EPS or SVG) unless it is a photo;
  text in the compiled PDF is readable, close to body size and not below 8 pt.
- Why: Raster plots and tiny labels are the most common figure complaints.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-review-once
- Src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md; arc:CF-21@v2

### FG-02 Self-contained caption
- [ ] Check: Each caption says what is shown, the denominator, and how to read
  colour or encoding, so the figure can be read without the text; it does not
  repeat numbers already in a table.
- Why: Reviewers look at figures before reading the text.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-write-polish
- Src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md; arc:@senior-a-comments:79; arc:MF-21@v2

### FG-03 Colour is never the only cue
- [ ] Check: Categories are distinguished by colour plus a second encoding
  (marker, line style, label, pattern), and the palette is colour-blind safe.
- Why: Colour-only figures fail for colour-blind readers and in greyscale print.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design
- Src: skill:tikz-diagram-review; up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md

### FG-04 Axes, legends and ranges
- [ ] Check: Axes carry labels with units; each legend entry maps one-to-one
  to a mark; axis origin and range do not exaggerate differences.
- Why: A misleading axis is read as a misleading claim.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design
- Src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md

### FG-05 Names match the text
- [ ] Check: Every name inside a figure (modules, steps, categories, labels)
  matches the text exactly, including capitalization; labels inside figures
  were checked by hand because text macros do not reach them.
- Why: A figure that uses other names than the text looks like a different study.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-review-loop
- Src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md; note:n07§A.8 FR17; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md F6

### FG-06 No local font shrinking
- [ ] Check: No figure, table or caption is made to fit by shrinking fonts or
  spacing locally; when a panel is too small, its key text is enlarged or a
  panel is rotated before the figure is split.
- Why: Local shrinking can break the template rules and makes floats unreadable.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-write-polish
- Src: arc:chat:group@2026-10-01T09:20; arc:chat:group@2026-10-03T11:32; note:n07§A.8 FR9; note:n07§A.8 FR13; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 2. Figure and text mirroring

### FG-07 Overview boxes and method steps match both ways
- [ ] Check: The overview figure's boxes are numbered; the method section has
  one same-named run-in per box in the same order; after every redraw the box
  count equals the step count and every step has a box.
- Why: A senior reviewer reads the overview and the method side by side.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio, sv-write-section
- Src: arc:chat:group@2026-09-29T11:42; arc:msr:9809b8c; arc:msr:b5c0045; arc:MF-01@v2; note:n07§A.8 FR1

### FG-08 Method text first, overview from the text
- [ ] Check: The method text was written before the overview was drawn; where
  they disagree, the figure was redrawn from the text.
- Why: Drawing first produces boxes the method never describes.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-write-section
- Src: arc:msr:0f96193; note:n07§A.8 FR2

### FG-09 One integrated overview
- [ ] Check: The study overview is one integrated figure, not a set of
  separate panels.
- Why: Panels hide the flow between steps.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio
- Src: arc:MF-03@v2; note:n07§B.5

### FG-10 Overview reviewed with the method text
- [ ] Check: A senior co-author reviewed the finished overview together with
  the method section, on the current PDF.
- Why: The overview was the most revised figure in the evidence project.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-supervisor-brief
- Src: arc:CO-08@v2; arc:chat:1on1@2026-09-27T23:21; note:n07§B.5

## 3. What goes in a figure

### FG-11 A figure says what a sentence cannot
- [ ] Check: Each figure carries information that cannot be said in one
  sentence; single statistics, agreement values and sample splits are in prose.
- Why: A figure for one number wastes space and attention.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-write-section
- Src: arc:MF-05@v2; note:n07§A.8 FR6

### FG-12 A grid of numbers is a table
- [ ] Check: No table is placed as a panel of a figure; mixed composites of
  plot and table are split.
- Why: Tables and figures have different reading rules and numbering.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-write-polish
- Src: arc:msr:0f96193; arc:msr:405bba7; note:n07§A.8 FR8

### FG-13 Text, then figure, then table
- [ ] Check: Results are presented prose first, then figure, then table;
  standalone tables are few; kept tables bold the headline numbers.
- Why: Readers take the finding from prose and the detail from tables.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-write-section
- Src: arc:chat:1on1@2026-09-29T11:51; arc:MF-15@v2; arc:01-checklist/checklist.md TB5; note:n07§A.8 FR7

### FG-14 One figure per message
- [ ] Check: Each research question has at most one figure for its main
  message; an alternative figure stays only if it adds a finding.
- Why: Keeping both versions postpones a decision and costs space.
- Status: candidate
- Scope: core
- Owner: sv-figure-design
- Src: arc:msr:9809b8c; arc:msr:47221f7; note:n07§A.8 FR10

### FG-15 The asked comparison is adjacent
- [ ] Check: Marks are arranged so the comparison the research question asks
  about sits side by side (for example one bar per category with group shares
  inside, not one bar per group).
- Why: Readers compare adjacent marks; distant comparisons are missed.
- Status: candidate
- Scope: core
- Owner: sv-figure-design
- Src: arc:chat:1on1@2026-09-28T23:29; note:n07§A.8 FR11

### FG-16 Every measured dimension shown or scoped out
- [ ] Check: Every measured dimension the method introduces appears in a
  figure or table with its denominator, or the text says why it is left out.
- Why: A coded dimension that silently disappears looks like a hidden result.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-review-loop
- Src: arc:01-checklist/checklist.md F5; note:n07§B.5; unverified (human origin in chat)

### FG-17 Introduction figure shows the problem
- [ ] Check: An introduction figure, if present, contrasts the failure modes
  or cases the paper studies, and its caption states the assumptions under
  which the contrast holds.
- Why: A concrete, failure-revealing example motivates faster than prose.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-write-intro
- Src: arc:chat:1on1@2026-09-28T23:15; arc:ol:ba3f1ee; up:skills/sv-review-once/references/procedure.md; note:n07§A.8 FR21

## 4. Data in figures

### FG-18 Numbers in figures come from scripts
- [ ] Check: Every number inside a figure comes from the same script or
  ledger as the text; a number copied from a sketch, an AI image or a
  reference figure is treated as a placeholder until re-sourced.
- Why: In the evidence project an agreement value entered the paper from a
  reference image and was never traced to data.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio, sv-review-loop
- Src: note:n07§A.1; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md; note:n07§A.8 FR3

### FG-19 Renderer, PDF and caption in sync
- [ ] Check: When a renderer or its data changed, the figure PDF was
  regenerated in the same commit; when a caption changed, the figure was
  re-read; previews were regenerated or deleted.
- Why: Captions edited after the deadline no longer matched their figures.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-experiment
- Src: arc:ol:ba3f1ee; arc:msr:836ee75; note:n07§A.8 FR14; user:2026-10-13 (promoted: failure had a clear bad outcome)

### FG-20 Renderers run from the replication package
- [ ] Check: Every figure renderer runs from the replication package on the
  released data, with no hard-coded counts and no path into a private
  repository.
- Why: A renderer that needs private files cannot be checked by artifact reviewers.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-experiment
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H9; note:n07§A.7; note:n07§A.8 FR16; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 5. Process and files

### FG-21 AI images explore layout only
- [ ] Check: AI-generated images were used, if at all, only to explore
  layout; the shipped figure was rebuilt natively, redlined by a human on a
  screenshot, then edited by hand; no AI raster art or upscaled AI image ships.
- Why: AI raster art carries invented numbers and an AI look.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio
- Src: arc:msr:e4ebb61; arc:msr:b73f7df; note:n07§A.8 FR4

### FG-22 No AI-look markers
- [ ] Check: Figures have no detail line under every box, no numbered phase
  badges, no gradient pastel frames, uneven icon placement or mixed text
  density; only data-scale numbers stay; the palette is plain.
- Why: Reviewers read AI-styled figures the way they read AI-styled prose.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio, sv-write-humanize-paper
- Src: arc:msr:0f96193; arc:MF-04@v2; note:n07§A.8 FR5

### FG-23 Icons from licensed libraries
- [ ] Check: Icons come from real icon libraries, and each licence is
  recorded next to the figure source; no icon is traced from another figure.
- Why: Traced icons carry unclear rights and an inconsistent look.
- Status: confirmed
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio
- Src: user:2026-10-13; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md

### FG-24 One source file per figure, drafts recorded
- [ ] Check: Each figure has one source file; drafts live outside the
  manuscript tree or in an ignored folder; the record says which draft won
  and why.
- Why: Draft fan-out without a record repeated decisions already made.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-supervisor-records
- Src: arc:msr:e0ea09b; note:n07§A.7; note:n07§A.8 FR15

### FG-25 No retired figures, nothing needed is ignored
- [ ] Check: No retired or superseded figure is referenced, and no file the
  build needs is excluded by an ignore rule.
- Why: Both break a clean build from a fresh clone.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-review-once
- Src: arc:MF-20@v2; arc:MF-23@v2; note:n07§B.5

### FG-26 Agent figure plans checked against latest feedback
- [ ] Check: Before an agent-written figure plan or review is executed, it is
  checked against the latest human feedback on that figure.
- Why: Agent plans in the evidence project re-introduced elements a senior
  had just asked to remove.
- Status: candidate
- Scope: core
- Owner: sv-figure-design, sv-figure-drawio, sv-feedback-revise
- Src: note:n07§A.8 FR20
