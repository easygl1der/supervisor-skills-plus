# Figure rules for every field

Field-specific figure rules live in the field profiles; the procedure lives
in `sv-figure-design` and `sv-figure-drawio`.

## Clarity
- Vector output, readable text (close to body size), self-contained caption
  that says what is shown, the denominator and how to read colour.
  [src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md; arc:CF-21@v2] (confirmed)
- Colour is never the only cue. [src: skill:tikz-diagram-review] (confirmed)
- Names in the figure match names in the text; labels inside figures follow
  the paper's label conventions by hand, because macros do not reach them.
  [src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md; note:n07§A.8 FR17] (confirmed)
- A grid of numbers is a table, not a figure panel. [src: arc:msr:0f96193; arc:msr:405bba7] (candidate)
- One figure per message; do not keep an "alternative" figure that adds no
  finding. [src: note:n07§A.8 FR10] (candidate)
- Do not shrink fonts locally to make a float fit. [src: arc:chat:group@2026-10-01T09:20; note:n07§A.8 FR9] (candidate)

## Overview figures
- Number the boxes; the method text has one run-in per box, in the same
  order and with the same names. Check both directions after every redraw.
  [src: arc:chat:group@2026-09-29T11:42; arc:msr:9809b8c; arc:msr:b5c0045; note:n07§A.8 FR1] (candidate)
- Write the method text first, then draw the overview from it.
  [src: arc:msr:0f96193; note:n07§A.8 FR2] (candidate)

## Data in figures
- Every number inside a figure comes from the same script as the text. A
  number copied from a sketch, an AI image or a reference figure is a
  placeholder until it is re-sourced. [src: note:n07§A.1; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md] (confirmed)
- When a renderer or its data changes, regenerate the PDF in the same commit;
  when a caption changes, re-read the figure; regenerate or delete previews.
  [src: note:n07§A.8 FR14] (candidate)
- Figure renderers run from the replication package on released data.
  [src: note:n07§A.8 FR16] (candidate)

## Process
- AI images may explore layout only. Rebuild natively, then do a human
  redline pass, then edit by hand. Do not ship AI raster art.
  [src: note:n07§A.8 FR4] (candidate)
- Icons come from real libraries with recorded licences, not from tracing.
  [src: user:2026-10-13; arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md] (confirmed)
- One source file per figure; drafts outside the manuscript tree; record
  which draft won and why. [src: note:n07§A.8 FR15] (candidate)
