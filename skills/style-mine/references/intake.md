# Exemplar intake (skill-local APIs)

## Contents
1. What intake does and does not do
2. Setup
3. Journal search
4. Author search
5. Author exemplars from a publication list
6. Queue and the promotion gate

## 1. What intake does and does not do

`scripts/intake_search.py` finds candidate exemplar papers by journal or by
author. It calls public APIs directly from the skill, so it runs the same in
Claude Code, Cursor or Codex, with no MCP server:

| Source | Used for | Needs |
|---|---|---|
| Crossref | new articles by journal ISSN; an author's works by ORCID | `INTAKE_MAILTO` (polite pool) |
| OpenAlex | abstracts (for the keyword pass), OA status, author disambiguation | `INTAKE_MAILTO` (polite pool) |
| Semantic Scholar | extra journal search and author papers | only when `SEMANTIC_SCHOLAR_API_KEY` is set |

Out of scope here, and kept on the VPS literature pipeline (Academic MCP /
Lit Scout): full-text resolution, PDF download and cache, and MinerU
conversion. Intake stops at metadata, a keyword mark and a legal OA link;
the owner or that pipeline supplies the Markdown that Dissect reads
(`research-core` `references/core/inputs-mineru.md`).
[src: user:2026-10-17] (confirmed)

## 2. Setup

Keys and the email live in the shell environment only, never in git:

```bash
export INTAKE_MAILTO="owner@example.org"          # polite pool for Crossref and OpenAlex
export SEMANTIC_SCHOLAR_API_KEY="..."              # optional
python skills/style-mine/scripts/intake_search.py --selftest
```

Without `INTAKE_MAILTO` the script warns and Crossref may answer HTTP 429.
On 429 or 5xx every source waits the server's `Retry-After`, or 8, 15 and
30 s, then stops with the error. Semantic Scholar calls are spaced at least
1.2 s apart and are skipped entirely when the key is unset (`--s2-id` then
prints a notice). No Academic MCP is involved at any step.

Flags (`intake_search.py --help`): `journal <slug|ISSN> [--since DATE]
[--max N] [--all] [--queue FILE]`; `author "<name>" [--openalex-id ID]
[--s2-id ID] [--since DATE] [--queue FILE]`; `exemplars <publications.json>
--author "<name>" [--top4]`; `--selftest`. `--since` defaults to 1 January
of the current year; `--max` (Crossref rows) defaults to 200.

## 3. Journal search

```bash
python intake_search.py journal jasa --since 2026-06-01            # causal hits only
python intake_search.py journal biometrika --since 2026-01-01 --all # every article, marked hit / no_hit
```

Slugs `jasa`, `jrssb`, `aos`, `biometrika` are pinned to both ISSNs of each
journal, which keeps out the old JRSS-B (Methodological) series and Annals
of Applied Statistics; any other ISSN can be passed directly. The keyword
pass uses unambiguous causal phrases on title plus abstract; broad stems
("identif", "matching", "randomiz") flagged mostly non-causal JASA papers in
the 2026-10-17 test and are left to the human screen with `--all`.
Output columns: issued, venue, keyword hits, OA status, DOI, title. An OA
link is kept only for green, gold or arXiv copies; publisher hybrid links
usually need access and are dropped.

## 4. Author search

```bash
python intake_search.py author "<author name>"                                   # candidates, then stop
python intake_search.py author "<author name>" --openalex-id A50... --since 2024-01-01
```

Without an ID the script prints candidate authors (institution, works count,
ORCID) and stops: picking the right person is a human decision, and common
names have many homonyms. With an OpenAlex ID it lists that author's works,
plus Crossref works carrying the author's ORCID; `--s2-id` adds Semantic
Scholar when a key is set. OpenAlex author profiles can still contain
homonym works (the 2026-10-17 test showed engineering and biology papers
under the statistician's ID), so an owner-curated publication list always
wins over API results.

## 5. Author exemplars from a publication list

```bash
gh api repos/<owner>/<repo>/contents/papers/publications.json \
  -H "Accept: application/vnd.github.raw" > /tmp/publications.json
python intake_search.py exemplars /tmp/publications.json --author "<author name>" --top4
```

Prints a Markdown table (year, venue, status, the author's role: first,
corresponding `*`, last or middle, title, DOI or arXiv ID) filtered from the
list, never invented. Paste it into the vault's `authors/<slug>/exemplars.md`
and pick exemplars there (`references/author-profile.md`). The list itself
stays in its own repository.

## 6. Queue and the promotion gate

`--queue <vault>/monitor/queue.jsonl` appends records whose DOI (or title,
when there is no DOI) is new; existing lines are never rewritten. Each record
carries `filter` (`keyword_hit` or `no_hit`, which the owner changes to
`human_keep` or `human_skip` with a reason) and `status` (`new`, then
`fetched`, `transcribed`, `carded` or `skipped`).

A scheduled run may only append to the queue. Cards, author profiles and
venue profiles in the vault are drafts until the owner confirms them; rules
reach this skill's files or `research-core` only through `lessons-harvest`
after that confirmation (hard rule 6). No job edits skill files on a timer.
