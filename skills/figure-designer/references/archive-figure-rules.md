# Figure rules from a full paper project (FR1 to FR21)

These rules come from the figure history of one empirical software
engineering paper, traced commit by commit in the evidence notes
(note:n07 Part A). They add process and data-integrity rules to the
single-figure design rules in `design-rules.md`. Each rule is stated for any
field; scope tags say where the evidence is narrower. Source format follows
`research-core` `references/core/precedence.md`. The checklist items that
enforce these rules are in `research-core`
`references/checklists/figures.md` (FG-01 to FG-26).

## Contents
1. The rules FR1 to FR21
2. Figure mirrors methodology: the procedure
3. Table or figure
4. AI sketch, native rebuild, human redline
5. AI-look markers
6. Renderer, PDF, caption and preview in sync
7. Numbers in figures come from scripts
8. What the evidence does not settle

## 1. The rules FR1 to FR21

Scope: G general, SE software engineering or empirical mining, V venue rule.

| # | Rule | Scope | Source |
|---|---|---|---|
| FR1 | Number the overview's boxes. The method text has one same-named run-in ("Step k: ...") per box, in the same order. After every redraw check both directions: box count equals step count, every step has a box. | G | [src: note:n07§A.8; arc:chat:group@2026-09-29T11:42; arc:chat:group@2026-10-02T22:26; arc:msr:9809b8c; arc:msr:0f96193; arc:msr:b5c0045] (candidate) |
| FR2 | Write the method text first, then draw the overview from it. When they disagree, redraw the figure from the text. | G | [src: note:n07§A.8; arc:msr:0f96193] (candidate) |
| FR3 | Every number printed inside a figure comes from the same script or ledger as the text. A number copied from a sketch, an AI image or a reference figure is a placeholder until re-sourced. | G | [src: note:n07§A.1; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md; arc:msr:393f596] (confirmed) |
| FR4 | AI images explore layout only. Rebuild natively, run a human redline pass on a screenshot, then edit by hand. Do not ship or upscale AI raster art. | G | [src: note:n07§A.8; arc:msr:e4ebb61; arc:msr:b73f7df] (candidate) |
| FR5 | Remove AI-look markers (section 5). Keep only data-scale numbers. Use a plain palette. | G | [src: note:n07§A.8; arc:chat:group@2026-10-02T11:09; arc:chat:group@2026-10-02T23:19; arc:MF-04@v2] (candidate) |
| FR6 | A figure carries information a sentence cannot. Single statistics, agreement values and sample splits go in prose. | G | [src: note:n07§A.8; arc:MF-05@v2] (candidate) |
| FR7 | Present prose first, then figure, then table. In kept tables, bold the headline numbers. | G | [src: note:n07§A.8; arc:MF-15@v2] (candidate) |
| FR8 | A tabular is a table, never a panel of a figure. Split mixed composites. | G, V | [src: note:n07§A.8; arc:msr:0f96193; arc:msr:405bba7] (candidate) |
| FR9 | Do not shrink fonts or spacing locally to make a float fit. Some venues treat it as a template violation. Plot labels stay close to body size. | V | [src: note:n07§A.8; arc:chat:group@2026-10-01T09:20; arc:msr:94e651f] (confirmed) |
| FR10 | One figure per research question. An "alternative" figure stays only if it adds a finding. Decide; do not keep both. | G | [src: note:n07§A.8; arc:msr:9809b8c; arc:msr:7c705c9; arc:msr:b3dafcd; arc:msr:47221f7] (candidate) |
| FR11 | Arrange marks so the comparison the question asks about is adjacent (one bar per category with group shares inside, not one bar per group). | G | [src: note:n07§A.8] (candidate) |
| FR12 | For category-by-source shares from several data sources, use one heatmap with a pooled column and an equal-weight column; explain the colour scale and both columns in the caption. | SE | [src: note:n07§A.8] (candidate) |
| FR13 | When a panel is too small, enlarge its key text or rotate a panel before splitting the figure. | G | [src: note:n07§A.8; arc:chat:group@2026-10-03T11:32] (candidate) |
| FR14 | When a renderer or its data changes, regenerate the PDF in the same commit. When a caption changes, re-read the figure. Regenerate or delete previews with the PDF. | G | [src: note:n07§A.8; arc:ol:ba3f1ee; arc:msr:836ee75] (confirmed) |
| FR15 | One source file per figure. Drafts live outside the manuscript tree or in an ignored folder. Record which draft won and why. | G | [src: note:n07§A.8; arc:msr:e0ea09b] (candidate) |
| FR16 | Renderers run from the replication package on released data: no hard-coded counts, no path into a private sibling repository. | SE | [src: note:n07§A.8; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md] (confirmed) |
| FR17 | Labels inside figures follow the paper's label conventions by hand, because text macros do not reach figures. | G | [src: note:n07§A.8; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md] (confirmed) |
| FR18 | Every figure has the venue's accessibility description where required (for example ACM `\Description{}`), and it matches the actual layout. | V | [src: note:n07§A.8] (candidate) |
| FR19 | Validation data is drawn as validation only. A gold or held-out sample never feeds the result boxes. | SE | [src: note:n07§A.8; arc:05-figures-tables/sources/briefs/drawio-overview-brief.md] (candidate) |
| FR20 | Agent-written figure plans and reviews are checked against the latest human feedback before they are executed. | G | [src: note:n07§A.8; arc:09-paper-snapshot/figures/study-workflow-UPDATE-PLAN.md] (candidate) |
| FR21 | An introduction figure contrasts the failure modes or cases the paper studies, and its caption scopes the architecture or setting it assumes. | G | [src: note:n07§A.8; arc:msr:b73f7df; arc:ol:ba3f1ee] (candidate) |

## 2. Figure mirrors methodology: the procedure

The overview figure was the most revised figure in the evidence project,
mainly because boxes and method steps drifted apart. The 1:1 mapping held
only after the method section was rewritten as one bold run-in per box.
[src: note:n07§A.1; arc:msr:b5c0045] (candidate)

1. Freeze the method text first (FR2). List its steps in order.
2. Number every box in the overview: `1`, `2`, ... in reading order. Group
   boxes into phases only if the text has the same phases as subsections.
3. Give the method text one bold run-in per box, in the same order, with the
   same name: `\textbf{Step 3: Sample the gold set.}` Capitalization and
   wording identical in figure and text (FR17).
4. Two-way count check after every redraw and every text edit:
   - figure to text: each numbered box has exactly one run-in with its name;
   - text to figure: each run-in has exactly one box with its number;
   - counts equal; phase headings match subsection headings.
   Record the check as a small table (box number, box label, run-in label,
   section, match yes/no).
5. Validation boxes (gold sample, held-out checks) connect only to the
   validation step, never to result boxes (FR19).
6. Review the figure together with the method section on the current PDF
   with a senior co-author (FG-10).

A quick mechanical check for LaTeX sources: extract `\textbf{Step k: ...}`
run-ins from the method file and the labels from the figure source (`value=`
attributes in a `.drawio`, node text in TikZ), then compare the lists.

## 3. Table or figure

- A grid of numbers is a table. Put it in a `table` float with its own
  number, never as a panel inside a `figure` (FR8). A senior reviewer
  flagged a tabular inside a figure float as "a table" that was labelled as
  a figure. [src: arc:msr:0f96193] (candidate)
- Use a figure when the reader must see a shape: a trend, a distribution, a
  comparison across many categories, a flow. Use prose for one or two
  numbers (FR6). Use a table when readers need exact values.
- Order: claim in prose, then figure, then table (FR7). Few standalone
  tables; bold the headline numbers in those kept.
- If a figure and a table show the same numbers, keep one.

## 4. AI sketch, native rebuild, human redline

The evidence project used this sequence for its overview and introduction
figures; the version that shipped was always the hand-edited native rebuild.
[src: note:n07§A.1; note:n07§A.2] (candidate)

1. **Sketch.** An image model or a co-author's mock-up may propose a layout.
   Treat it as a layout idea only. List every number and every label in it
   as `UNVERIFIED` (FR3).
2. **Native rebuild.** Rebuild in draw.io, TikZ or a plotting script
   (`drawio-reconstruction` for faithful replication). Icons come from
   licensed libraries, not traced (FG-23). Re-source every data value from
   the analysis scripts before it enters the figure or the text.
3. **Human redline.** A human marks the screenshot: strike, keep, move.
   Apply the redline in place and keep the pre-redline version under `qa/`.
4. **Hand edits.** Final adjustments in the editor. Keep one source file
   (FR15).
5. Do not polish a raster you will redraw. Upscaling and denoising an
   AI-generated image cost time in the evidence project and the raster was
   discarded. [src: arc:msr:e4ebb61; arc:msr:b73f7df] (candidate)

## 5. AI-look markers

Reviewers in 2026 react to figures that look machine-made the way they react
to machine-sounding prose. A senior co-author asked twice to simplify an
overview because it looked "too AI". [src: note:n07§A.1; arc:chat:group@2026-10-02T23:19] (candidate)

Remove:
- a small detail line under every box;
- numbered phase badges on top of numbered steps;
- gradient pastel frames and soft shadows;
- icons placed unevenly (some touching frames, some not);
- mixed text presence (some boxes with sub-text, some without);
- decorative numbers that are not data scale.

Keep: data-scale numbers (sources, items, sample size) if they come from
scripts; one font; a plain palette (black, white, grey, one accent, or the
editor's default palette).

## 6. Renderer, PDF, caption and preview in sync

After the deadline, captions in the evidence project were edited without
regenerating the figures, and a stale preview image of an older overview
was re-added by a merge. [src: note:n07§A.1; arc:ol:ba3f1ee; arc:msr:836ee75] (confirmed)

- One commit changes the renderer, the data it reads and the exported PDF
  together.
- A caption edit triggers a re-read of the figure: every sentence in the
  caption must describe something visible (a dashed line, a column, a
  percentage under a bar).
- Previews (`*.preview.png`, contact sheets) are regenerated with the PDF or
  deleted.
- Renderers run from the replication package (FR16); check by running them
  from a fresh clone.

## 7. Numbers in figures come from scripts

The lesson. In the evidence project an inter-rater agreement value first
appeared on a co-author's reference image. The agent-built draw.io replica
copied it, and its layout fingerprint warned that displayed values were
copied from the reference without validating the research. The commit that
installed the replica also added the same value to the method text. A later
redline removed the value from the figure but not from the text, and no
computation of it exists in the archive.
[src: note:n07§A.1; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md; arc:msr:393f596] (confirmed)

Procedure:
1. Inventory every number in the figure source (labels, captions, axis
   annotations, callouts).
2. For each, find the script output or ledger row that produces it
   (`research.yaml` `source_of_truth.numbers`). Record `figure label ->
   script or ledger key`.
3. Numbers with no source become placeholders (`[TBD: source]`) and are
   listed as open items. They do not enter the text either.
4. When the reference is a sketch or an AI image, do this before the first
   commit of the rebuilt figure.
5. Hand the list to `check-loop` or `experiment-workflow` for the number
   trace.

## 8. What the evidence does not settle

- Whether an overview caption should be self-contained or short. The last
  senior pass in the evidence project cut a long, number-carrying caption to
  one line; this is one data point. [src: note:n07§A.8] (candidate)
- No evidence on figure rules for theory or mathematics papers beyond the
  render-and-inspect loop; see the field profiles.
