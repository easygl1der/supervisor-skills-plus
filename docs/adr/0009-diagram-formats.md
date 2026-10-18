# ADR 0009: HTML (SVG plus KaTeX) is the default diagram format

Status: accepted (paths updated by ADR 0021 on 2026-10-18: the kit and visuals.md now live in skills/sv-figure-explain/)
Date: 2026-10-16
Deciders: owner (SPEC D9 to D12), Claude Code (template set)

## Context
Mermaid output was judged monotonous (D10). Manim generation fails often and
is slow (D9, citing TheoremExplainAgent). Excalidraw templates, D2 and AI
illustrations produced wrong structure, mixed fonts or wrong numbers (D12).
HTML with SVG and KaTeX reproduced textbook TikZ figures in about a second.

## Options considered
1. Mermaid default: quick, plain, weak math.
2. Graphviz or TikZ as main tools: good layout, slow to iterate, no interaction.
3. HTML (SVG plus KaTeX) templates; Graphviz only for very large graphs; TikZ
   only for paper figures.

## Decision
Option 3. Every figure is saved as `<name>.html` (source, interactive) and
`<name>.png` (rendered); Markdown notes embed the PNG. Graphviz (`dot -Tsvg`
embedded in HTML) only when browser layout fails on dozens of nodes. No Manim;
Mermaid is not a default. Steppers (`stepper.html`, `stepper-proof.html`,
`stepper-trace.html`, `stepper-plot.html`) only for content with an order:
derivations, algorithms, processes. GIF is an export of a stepper.

## Consequences
- Rendering needs Chrome (`render.sh` exit 3 when missing); in the web app the
  HTML is shown as an artifact and the PNG rendered later.
- Two files per figure.

## Do not
- Do not use Manim. Do not use a stepper for unordered content.

## Sources
`skills/sv-figure-explain/references/visuals.md` (intro, §1, §5), `skills/sv-study/SKILL.md` §4,
`skills/sv-figure-explain/kit/templates/`, SPEC D9, D10, D11, D12.
