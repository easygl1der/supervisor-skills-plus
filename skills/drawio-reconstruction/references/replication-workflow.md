# Replication workflow: fingerprint, modules, assets, data values

Folded in from the owner's former local skill `drawio-figure-replication`
[src: skill:drawio-figure-replication] (confirmed), with the worked example
from the evidence project's overview replica
[src: arc:05-figures-tables/sources/drawio/overview-reference-replica/LAYOUT_FINGERPRINT.md; arc:05-figures-tables/sources/drawio/overview-reference-replica/SVG_ASSETS.md; arc:05-figures-tables/sources/drawio/overview-reference-replica/qa] (confirmed)
and the figure history in note:n07 Part A.

## Contents
1. Output folder
2. Layout fingerprint
3. Module-first build with module QA crops
4. SVG and icon asset provenance
5. Re-source every data value when the reference is a sketch
6. Generator script and redline revisions
7. Minimal mxGraph XML patterns
8. What went wrong in the evidence project

## 1. Output folder

Work in an isolated folder next to the figure source in the project (not
in a downloads folder), for example `figures/<name>-replica/`:

```text
<name>.drawio            uncompressed XML, the one source for this figure
<name>.png               exported preview
LAYOUT_FINGERPRINT.md    section 2
SVG_ASSETS.md            section 4 (or <name>_icons/ATTRIBUTION.tsv)
<name>_icons/            icon files and ATTRIBUTION.tsv
DATA_VALUES.md           section 5
build_<name>.py          optional coordinate-based generator
qa/                      module drawio files, module PNGs, comparison crops,
                         pre-redline copies, validation JSON
```

Do not overwrite user-provided sources. One `.drawio` per figure: in the
evidence project one file held three figures on separate pages while a
second copy of one of them existed elsewhere, so the two could diverge
[src: note:n07§A.1] (candidate).

## 2. Layout fingerprint

Write it before generating any XML. Fields:

- reference file name and pixel size; background;
- modules (panels, phases, lanes) with approximate bounds `x, y, w, h`;
- contents of each module (cards, labels, icons, badges) and the
  connectors inside it;
- cross-module connectors, listed separately;
- styles: font family, text colours, palette, corner radii, gradients;
- what stays editable, what is an embedded SVG, which stencils are reused;
- uncertainty: texture or lighting that will be approximated, typeface
  width, icon contours;
- **data values**: every number and date shown in the reference, with the
  note that they are copied for layout only (section 5).

The evidence replica's fingerprint was a short table: one row per phase
module with bounds, contents and connectors, then a cross-module connector
line, styles, editability and uncertainty. Its last sentence said that the
displayed study values were copied from the reference without validating
them. That warning was correct and was not acted on (section 8).

## 3. Module-first build with module QA crops

For figures with several panels, lanes, tables or many crossing connectors:

1. Build one module at a time, ideally one generator function per module.
2. For each module match: frame size, internal grid, labels, icons, local
   arrows, badges and small legends.
3. Export the module alone (for example `build_<name>.py --module 1` writes
   `qa/module-1.drawio` and `qa/module-1.png`).
4. Make a side-by-side comparison crop: reference region left, module export
   right (`qa/module-1-comparison.png`). Review the module crops first; they
   are the primary review surface. The full-figure preview is the final
   integration check.
5. Add cross-module connectors only after every module passes, in a
   separate integration step, so routing fixes do not move module internals.
6. Record each module's status in the inventory (`pending`, `done`,
   `needs-fix`, `accepted`).

The evidence replica kept, per phase, the module `.drawio`, its PNG, a
comparison image and a final crop under `qa/`, plus a validation JSON.

## 4. SVG and icon asset provenance

- Find icons before drawing them, in the order of `icon-sources.md`:
  draw.io stencils, registered libraries, web search, then a simple native
  shape.
- Store each standalone SVG under `<name>_icons/`; prefer a square
  `viewBox`, consistent stroke widths, round caps and joins, no filters.
- Never trace a protected logo or brand mark. The evidence replica reused
  the draw.io built-in stencil for a platform logo, adjusting only the
  fills, and stored the stencil XML next to the figure.
- Record every asset: one row in `ATTRIBUTION.tsv` (source, path, licence,
  author, retrieval date). The older `SVG_ASSETS.md` form, a table of asset,
  meaning and provenance (original, generic, or derived from the
  reference), is acceptable for original icons, but library icons need the
  licence columns.
- Embed SVGs as `shape=image` data URIs so the `.drawio` is portable, and
  keep the standalone files for reuse.

## 5. Re-source every data value when the reference is a sketch

A replica copies what it sees. When the reference is a sketch, an AI image,
a co-author's mock-up or a figure from another paper, the numbers and dates
in it are not data.

1. While writing the fingerprint, list every number, date, count, statistic
   and named setting in the reference in `DATA_VALUES.md`:
   `label | value in reference | status`.
2. Status starts as `UNVERIFIED`. Put a visible placeholder in the replica
   (`[n = ?]`, `[TBD]`) or the value with a `TBD` comment in the generator,
   never the copied value as final.
3. For each value, find the script output or ledger row that produces it
   (`research.yaml` `source_of_truth.numbers`). Record the key and set the
   status to `sourced`. Values without a source are removed or stay
   placeholders and are reported to the user.
4. Do not copy any value from the replica into the paper text. Text numbers
   come from the same scripts (FG-18).
5. Only data-scale numbers belong in an overview figure; statistics such as
   agreement values go in prose (FG-11).

This step overrides the fidelity contract: visual fidelity applies to
layout, style and icons, not to the truth of the numbers.

## 6. Generator script and redline revisions

- A coordinate-based generator (`build_<name>.py`) that writes uncompressed
  XML makes rebuilds and module exports cheap.
- Apply a human redline as a separate, re-runnable revision step that
  edits the existing cells (the evidence replica used a revision script
  called by the generator before saving), and keep the pre-redline `.drawio`
  and PNG under `qa/`.
- Once the figure moves into the paper and people edit it by hand in the
  draw.io editor, the hand-edited file is the source. Retire the generator
  or regenerate from it only after merging the hand edits back. Two sources
  for box names (the generator and hand edits) caused label flip-flops in
  the evidence project [src: note:n07§A.1] (candidate).

## 7. Minimal mxGraph XML patterns

Restated from the former local skill's reference.

```xml
<mxfile host="Electron" pages="1">
  <diagram name="Figure" id="fig">
    <mxGraphModel page="1" pageWidth="1600" pageHeight="900" math="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="box1" value="Step 1: Collect" vertex="1" parent="1"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#333333;fontFamily=Helvetica;fontSize=14;">
          <mxGeometry x="100" y="80" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="box2" value="Step 2: Filter" vertex="1" parent="1"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#333333;fontFamily=Helvetica;fontSize=14;">
          <mxGeometry x="320" y="80" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="icon1" value="" vertex="1" parent="1"
          style="shape=image;aspect=fixed;image=data:image/svg+xml,%3Csvg...%3E;">
          <mxGeometry x="40" y="86" width="48" height="48" as="geometry"/>
        </mxCell>
        <mxCell id="e1" edge="1" parent="1" source="box1" target="box2"
          style="endArrow=classic;html=1;rounded=0;strokeColor=#333333;strokeWidth=1.5;">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

- Group containers: children use coordinates relative to the parent.
- URL-encode SVGs inside `image=data:image/svg+xml,...`; XML-escape `&`,
  `<`, `>` and quotes in `value` attributes.
- Deterministic ids (`m1_card3_label`) make diffs and redlines readable.
- Validate with `xmllint --noout <file>` and `check_drawio.py`; export with
  `export_drawio.py`. Treat GPU warnings from the draw.io CLI as non-blocking
  when the exit code is 0 and the PNG exists.

## 8. What went wrong in the evidence project

- An inter-rater agreement value on a co-author's reference image was
  copied into the replica, and the commit that installed the replica added
  it to the method text. A redline later removed it from the figure, not
  from the text, and no computation of it exists in the archive.
  [src: note:n07§A.1; arc:msr:393f596] (confirmed)
- Six generated layout variants were never adopted and left no decision
  record. [src: note:n07§A.1] (candidate)
- The replica kept AI-look markers from the reference (detail lines under
  every step, numbered phase badges, gradient frames) until a senior
  redline removed most of them. [src: note:n07§A.1; arc:05-figures-tables/sources/drawio/overview-reference-replica/qa/redline-validation.json] (candidate)
