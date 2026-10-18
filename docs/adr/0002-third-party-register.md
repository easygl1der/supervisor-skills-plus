# ADR 0002: One root THIRD_PARTY.md for vendored code and borrowed ideas

Status: accepted (paths updated by ADR 0021 on 2026-10-18: the kit and visuals.md now live in skills/sv-figure-explain/)
Date: 2026-10-16
Deciders: owner (SPEC change list), Claude Code (format, licence checks)

## Context
The reading upgrade vendors JavaScript libraries into `skills/sv-figure-explain/kit/vendor/`
and adapts ideas from about fifteen public skill repositories
(`notes/10-reading-sources.md` §14). Their licences differ (MIT, Apache-2.0,
EPL-2.0, CC BY-SA 4.0, none). The repository itself is CC BY-NC-SA 4.0
(`LICENSE`), so every borrowed item needs its own licence on record.

## Options considered
1. Licence notes only inside each skill: scattered, easy to miss on export.
2. Rely on `notes/10-reading-sources.md`: it is a research log, not a register.
3. One table at the repo root, each row checked against the upstream LICENSE.

## Decision
Option 3. `THIRD_PARTY.md` lists material, where it is used, source and commit,
licence, copyright line and the date checked. Licences are read from the
upstream LICENSE file (GitHub API), not from SPEC or registry pages. Ideas
taken from repositories without a licence are listed as "ideas only, rewritten".
Material deliberately not bundled (dagitty, GPL-2.0) is listed too.

## Consequences
- A new vendored file or borrowed idea needs a row before it lands.
- Per-file notices still stay next to the code (`kit/vendor/ve/LICENSE`,
  the EPL header in `elk.bundled.js`).

## Do not
- Do not record a licence that was not read from the source.
- Do not paste text from repositories that have no licence file.

## Sources
`THIRD_PARTY.md`, `LICENSE`, `notes/10-reading-sources.md`,
`docs/handoff/supervisor-plus-reading-upgrade-SPEC.md` (change list, D19).
