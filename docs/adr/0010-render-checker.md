# ADR 0010: Render checker with layout checks; a figure ships only at exit 0

Status: accepted
Date: 2026-10-16
Deciders: Claude Code (checks added after tests), owner (review)

## Context
In the 2026-10-16 tests, auto-layout drew straight edges that passed under
other nodes and through labels; a reader takes such a line as an extra causal
link. Visual review alone missed some of these.

## Options considered
1. Human or model looks at the PNG only: misses small crossings.
2. Pixel diffing against references: no references exist for new figures.
3. Geometric checks in headless Chrome, plus looking at the PNG.

## Decision
Option 3. `skills/study/kit/render.mjs` reports: text-box overlap (tight text
bounds), overflow outside `#fig`, `text-on-line` (sampled stroke points inside
a label box; occluded parts ignored via `elementsFromPoint`; opt out with
`data-cross-ok`), `edge-through-node`, KaTeX errors, JS errors and unfilled
`{{placeholders}}`. Exit 0 clean, 2 warnings, 3 no Chrome. Fix and rerender at
most three rounds, then change template. The study checklist requires exit 0
and a look at the PNG before delivery.

## Consequences
- Intentional crossings must be marked `data-cross-ok`.
- Checks cover SVG geometry, not meaning (arrow direction is still checked by eye).

## Do not
- Do not deliver a figure with warnings.

## Sources
`skills/study/kit/render.mjs` (header, checks, exit codes),
`skills/study/references/visuals.md` §4 and §6, `skills/study/SKILL.md` §4 and checklist.
