# Slide rules

Table of contents: density, overlays, boxes, tables, columns, fonts,
TikZ, colour, pacing, endings.

## Density

- Assertion titles (a full phrase). Generic titles ("Results") only on
  section dividers.
- At most 6 bullets, each at most 2 lines (about 15 words). Lint cap is 7.
- At most 5 new symbols and 2 display equations per slide.
- At least one formula, figure, table, theorem, or algorithm. Text-only
  slides at most 30% of the deck. A slide with at most 3 short text-only
  bullets must be merged or enriched.
- Discussion, decision, blocker and link-to-project slides may be text
  only: mark the frame with a comment `% gb:text-ok <reason>` and
  `lint_deck.py` leaves it out of the 30% count. Never add a formula only to
  pass the lint; a filler equation is a finding in the visual review.
- One idea per slide. Worked example within 2 slides of a definition.
  Theorem and proof on separate slides.

## Overlays (banned)

No `\pause`, `\onslide`, `\only`, `\uncover`, or overlay specs (`<2->`).
Reveal by duplicating the frame and muting earlier items (grey text or
a faded TikZ layer). Build a formula the same way.

## Boxes

Inside a box: one display equation or 2 to 3 short bullets, never both.
No `\qquad` and no negative `\vspace` inside a box. Equations wider than
about 70% of `\textwidth` must be split before boxing. At most 2 coloured
boxes per slide. Beamer suppresses overfull warnings inside blocks: every
box needs a visual check.

## Tables, columns, fonts

- booktabs, no vertical rules, centred. `\vspace{4pt}` before a `\toprule`
  that sits under the frame title. At most 6 to 7 columns and 8 to 10 rows.
  Split at group boundaries; repeat the header; title "(cont'd)".
- `\resizebox` is last resort. Set only width or height on an image.
- Columns `[T]`, 0.48/0.48 for comparisons; never nested; at most 3 columns.
- Never `\tiny`. `\footnotesize` is last resort. TikZ labels at least
  `\footnotesize`.

## TikZ and colour

Solid = observed, dashed or hollow = counterfactual. Compute on-curve
points; do not hard-code. Palette (colour-blind safe): 0173B2, DE8F05,
029E73, CC78BC. Contrast at least 4.5:1. No red/green binary pairs.
3 to 5 colours total. One emphasis (bold or colour) per slide.

## Pacing and ending

About 1 slide per 1.5 to 2 min. At most 3 to 4 consecutive theory slides
before an example. Section divider every 5 to 8 slides. References is
second-to-last, then thank-you, then `\appendix` with 3 to 5 backup slides
behind a divider. Backup slides are out of timing.

Fix overflow in this order: vertical space, consolidate lists, inline a
display equation, shrink the image (100% to 80% or 70%), then font size,
never below 0.85em and never `\tiny`.
