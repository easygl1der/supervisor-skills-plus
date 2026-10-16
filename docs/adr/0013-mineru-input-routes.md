# ADR 0013: PDF input through MinerU only, three routes, stop on failure

Status: accepted
Date: 2026-10-16
Deciders: owner (MinerU-only rule, token handling), Claude Code (route order, readability gate)

## Context
Generic PDF extractors drop equations, tables and reading order and merge two
columns, which breaks theory and statistics papers. The SPEC also rejected
claude-paper's pdf-parse and PyMuPDF path (D18). In the SDID test the no-token
flash route merged Table 1 cells where precision mode did not.

## Options considered
1. Any available extractor with fallbacks: always produces text, often wrong.
2. MinerU first, other extractors as fallback: same risk on failure.
3. MinerU only, through ordered routes; stop and report when none works.

## Decision
Option 3, in `skills/research-core/references/core/inputs-mineru.md`:
route 1 MinerU MCP (`mineru_parse_documents_smart`); route 2 official CLI,
precision `mineru-open-api extract` with `MINERU_TOKEN` from the user's
environment preferred, flash `flash-extract` as fallback (20 pages, 10 MB,
Markdown only, can merge table cells); route 3 local `mineru`. Ask before
uploading an unpublished manuscript. On failure, stop and list routes tried and
errors; no other extractor, no summary from the abstract or memory. A
readability gate checks headings, equations, tables and figures.

## Consequences
- Applies to paper-quickread, study and style-mine.
- Without MCP, token or local install, PDF work stops until the user acts.

## Do not
- Do not put the token in a repo, a skill file or a logged command line.
- Do not copy numbers from a table whose column order is unresolved.

## Sources
`skills/research-core/references/core/inputs-mineru.md`, ADR 0001, SPEC D18.
