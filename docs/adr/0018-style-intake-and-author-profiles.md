# ADR 0018: Style intake through skill-local APIs; author profiles beside venue profiles

Status: accepted
Date: 2026-10-17
Deciders: owner

## Context
Causal style mining needs exemplars from the top-4 statistics journals (JASA,
JRSS-B, Annals of Statistics, Biometrika) and from one author's publications.
The Academic MCP was not reliably reachable from every tool and covers these
journals poorly through dblp (`docs/plans/2026-10-17-causal-style-mining-investigation.md` §2.1).
`style-mine` accumulated venue and field profiles only; an author's habits had
no file of their own.

## Options considered
1. Intake through the Academic MCP: one more server to keep running; fails when it is down.
2. A separate intake skill or service: a second place for style memory.
3. A stdlib script inside `style-mine` calling Crossref and OpenAlex (Semantic Scholar when a key is set).

## Decision
Option 3. `skills/style-mine/scripts/intake_search.py` searches by journal or
author and filters an owner-curated publication list; results append to
`<STYLE_VAULT>/monitor/queue.jsonl`. Full-text resolution, PDF cache and
MinerU stay on the VPS literature pipeline (Academic MCP / Lit Scout).
Author profiles live in `authors/<slug>/` of the style vault, stack with venue
profiles (venue genre over author voice), and log every clash in a
conflict table (`skills/style-mine/references/author-profile.md`). Fields A to L
of the style card are unchanged.

## Consequences
- Claude Code, Cursor and Codex can run intake with only network access and an email.
- The vault path is one variable (`$STYLE_VAULT`); it can move into an author's repository later.
- API author profiles can contain homonyms, so a human picks the author ID and the curated list wins.

## Do not
- Do not let a scheduled run edit cards into rules, mark profiles confirmed, or touch skill files.
- Do not commit API keys, PDFs or full text to this repository.
- Do not merge an author profile into a venue profile.

## Sources
`skills/style-mine/scripts/intake_search.py`, `skills/style-mine/references/intake.md`,
`skills/style-mine/references/author-profile.md`, owner decisions 2026-10-17.
