# ADR 0011: explainer-page template is driven by one PAGE data block

Status: accepted (paths updated by ADR 0021 on 2026-10-18: the kit and visuals.md now live in skills/sv-figure-explain/)
Date: 2026-10-16
Deciders: Claude Code (template design, adapted from visual-explainer)

## Context
A full concept page (question, intuition figure, mechanism, boundaries,
what to remember) mixes prose, SVG and KaTeX. Editing layout code per page
invites broken markup and inconsistent style.

## Options considered
1. Write each page by hand in HTML: flexible, inconsistent, error-prone.
2. Generate from Markdown: loses figure types and small multiples.
3. A fixed template whose only edited part is a JSON-like data block.

## Decision
Option 3. `skills/sv-figure-explain/kit/templates/explainer-page.html` renders from
`const PAGE = {title, kicker, h1, lead, sections, remember}`. Each section has
`h2`, a `figure` with `type` `svg` (hand SVG), `cards` (small multiples) or `dag`
(drawDAG spec, `layout: 'elk'`), and a `caption` that may contain KaTeX. The
same "edit the data block only" rule holds for the other templates (SPEC,
CARDS, PANELS, BRANCHES). Render with `render.sh --full --figures`.

## Consequences
- Pages share the Paper style tokens from `vendor/ve/ve.css`.
- New figure kinds need a template change, not a page change.

## Do not
- Do not edit the template's layout or style code for a single page.

## Sources
`skills/sv-figure-explain/kit/templates/explainer-page.html` (header comment, `const PAGE`),
`skills/sv-figure-explain/references/visuals.md` §1 and §4 step 1.
