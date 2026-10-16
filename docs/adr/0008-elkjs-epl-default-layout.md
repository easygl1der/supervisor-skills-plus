# ADR 0008: elkjs kept under EPL-2.0 and used as the default auto-layout

Status: accepted
Date: 2026-10-16
Deciders: Claude Code (licence check, layout test), owner (review)

## Context
The SPEC listed KaTeX, rough.js, elkjs and dagre as "all MIT". The upstream
`kieler/elkjs` LICENSE.md is the Eclipse Public License 2.0; the bundled file
header says `EPL-2.0 OR GPL-3.0-or-later`. In the 2026-10-16 tests, dagre
layouts with straight edges ran lines under other nodes, which read as an extra
causal path; elk routed edges with fewer crossings.

## Options considered
1. Drop elkjs, keep dagre only (MIT): simpler licence, worse figures.
2. Modify or re-license the bundle: not allowed under EPL.
3. Keep `elk.bundled.js` unmodified with its notice, record EPL-2.0, make ELK
   the default and keep dagre as fallback.

## Decision
Option 3. `templates/auto-dag-elk.html` is the default for more than six nodes;
`auto-dag-dagre.html` is the fallback. Edges follow the layout's routed paths.
`THIRD_PARTY.md` records EPL-2.0 (secondary GPL-3.0) and the source URL.

## Consequences
- EPL-2.0 is weak copyleft per file: changes to the bundle would have to be
  published under EPL. We do not change it.
- `skills/study/kit/README.md` still says elkjs is MIT and needs correcting.

## Do not
- Do not edit `elk.bundled.js`; replace it whole on upgrade.

## Sources
`skills/study/kit/vendor/elk.bundled.js` (lines 18 to 26), `THIRD_PARTY.md`,
`skills/study/references/visuals.md` §1 and §6,
SPEC "vendored ... 均 MIT" line, upstream `kieler/elkjs` LICENSE.md (read 2026-10-16).
