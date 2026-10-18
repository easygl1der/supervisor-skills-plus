# ADR 0007: Visual kit fully vendored, no CDN

Status: accepted (paths updated by ADR 0021 on 2026-10-18: the kit and visuals.md now live in skills/sv-figure-explain/)
Date: 2026-10-16
Deciders: owner (SPEC visual kit), Claude Code (file set)

## Context
Study figures must render the same in Claude Code, Cursor, Codex and offline,
and the render check runs headless Chrome on local files. CDN scripts and web
fonts fail offline and change under the user.

## Options considered
1. Load KaTeX, layout libraries and fonts from CDNs: small repo, breaks offline.
2. Install through npm per user: heavier setup, still network-bound.
3. Vendor the runtime files (about 3 MB) in `skills/sv-figure-explain/kit/vendor/`.

## Decision
Option 3. `vendor/` holds KaTeX (JS, CSS, auto-render, fonts), rough.js,
dagre, elkjs, the kit's own `kit.js`/`kit.css`, and a visual-explainer subset
in `vendor/ve/` (`ve.css`, `stepper.js`, LICENSE, NOTICE). Measured size 3.1 MB
(elkjs 1.5 MB, KaTeX fonts 1.1 MB). Templates reference only local files.
Fonts are system fonts named in CSS (Noto CJK, PingFang, LXGW WenKai), not
Google Fonts and not bundled. Only `playwright-core` is installed by npm, for
rendering; `node_modules/` is git-ignored.

## Consequences
- Figures open from disk anywhere; the repo grows by about 3 MB.
- Library upgrades are manual and must update `THIRD_PARTY.md`.

## Do not
- Do not add CDN or Google Fonts links to templates.
- Do not vendor GPL code (dagitty stays external).

## Sources
`skills/sv-figure-explain/kit/vendor/`, `skills/sv-figure-explain/kit/README.md`, `skills/sv-figure-explain/kit/package.json`,
`.gitignore` (node_modules), `skills/sv-figure-explain/references/visuals.md` §3 and §5, `THIRD_PARTY.md`.
