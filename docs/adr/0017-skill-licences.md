# ADR 0017: New skills use the repo licence; the owner's earlier skill stays MIT

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner

## Context
The repository is CC BY-NC-SA 4.0 (`LICENSE`), matching the upstream project.
`style-mine` (formerly `journal-adapt`) was written by the owner earlier as a
standalone MIT skill and vendored here (`skills/style-mine/README.md`). The new
skills `research-bridge` and `proposal-writer` were written in this repository.

## Options considered
1. Relicense everything to CC BY-NC-SA 4.0: would narrow terms already granted
   under MIT for style-mine.
2. MIT for all new skills: diverges from the repo licence without a reason.
3. New skills take the repo licence; style-mine and the journal-adapt stub keep MIT.

## Decision
Option 3. `research-bridge` and `proposal-writer` declare
`license: CC-BY-NC-SA-4.0` in frontmatter. `style-mine` and `journal-adapt`
declare `license: MIT`, with the original notice in `skills/style-mine/README.md`.

## Consequences
- `THIRD_PARTY.md` lists style-mine as MIT, the owner's own work.
- Six older skills still declare `CC-BY-4.0` in frontmatter
  (benchmark-paper-template, figure-designer, idea-evaluator,
  pre-submission-reviewer, tech-paper-template, vibe-research-workflow), from
  before the repo licence change in `CHANGELOG.md`; not decided here.

## Do not
- Do not copy third-party text into the CC BY-NC-SA skills without a row in
  `THIRD_PARTY.md`.

## Sources
`LICENSE`, `skills/sv-study-bridge/SKILL.md`, `skills/proposal-writer/SKILL.md`,
`skills/style-mine/SKILL.md`, `skills/style-mine/README.md`,
`skills/journal-adapt/SKILL.md`, `CHANGELOG.md` (licence change), `THIRD_PARTY.md`.
