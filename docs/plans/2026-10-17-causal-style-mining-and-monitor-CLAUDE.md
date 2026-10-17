# Claude Code session prompt — causal style mining & monitor plan

Paste this after `cd` into `supervisor-skills-plus` (private fork). Work on **main**, no branch/PR unless the owner says otherwise.

## Intent (read first)

Open and follow:

1. `docs/plans/2026-10-17-causal-style-mining-and-monitor.md` — **source of truth**
2. This file — session contract

Goal: a repeatable pipeline so we learn (a) how causal papers are written in JASA / JRSSB / AoS / Biometrika, and (b) 刘汉中 (Hanzhong Liu) author rhetoric, then feed **style-mine** via cards in a private **causal-style-vault**. Promote to `research-core` **only** through `lessons-harvest` + **owner approval**. Never auto-merge rules daily.

## Hard constraints

- Do **not** rewrite unrelated skills in a drive-by.
- Do **not** treat **Apify** (or any single vendor) as required. Investigation (see `docs/plans/2026-10-17-causal-style-mining-investigation.md`) **recommends Crossref + OpenAlex**, with JASA RSS as an optional sidecar. **Do not bind or implement auto-monitor until the owner confirms.** Until then: manual DOI/TOC list is enough to prove MinerU → `paper-quickread --style` → vault cards.
- Never paraphrase paper findings into cards/rules; rhetoric and structure only.
- Never write PDFs or full-text transcripts into this public/skills repo.
- Author profile ≠ venue profile (separate paths under vault).
- Routines: propose only; **do not create** Academic Bot crons unless marked done by the owner ("to be created later by Academic Bot").

## Liu / 汉中流 repo

- Confirmed private repo: `easygl1der/hanzhong-liu-research`.
- **Authoritative list:** `papers/publications.json` (38 items, 2026-08-28). Readable table: `papers/papers.md`.
- **Not the CV:** `papers/catalog.json` (background papers only). S2 sidecar is incomplete (`s2-author.json` count 27).
- Remote git **does not** contain PDFs (`papers/**/*.pdf` gitignored). `by-author/liu-hanzhong/` is described in README but was **not** listed on GitHub in the 2026-10-17 probe.
- Filter exemplars from the JSON; do **not** invent a paper list. Top-4 *published* filter dump is in the investigation appendix.
- Dissect into vault `authors/hanzhong-liu/cards/`; keep PDFs in that repo or local study copies. Prefer existing arXiv LaTeX transcripts over MinerU when `transcript_kind` is `arxiv-latex`.

## External skills (borrow vs leave)

Read plan §5. In short:

- **Extend** in-repo `style-mine` / `paper-quickread --style` / `lessons-harvest`.
- **Borrow ideas only** from `brycewang-stanford/Awesome-Journal-Skills` (MIT) as **candidate** check dimensions; cite `[src: ...]`; do not install whole AER/QJE packs as stats top-4 rules.
- Also useful as *ideas*: paper-suite `venue-adapt` overlay, match-style author-vs-venue conflict table, fuhaoda `stat-writing` (CC0) apply/check heuristics. Do not copy PDF extractors.
- Stats top-4 have **no** ready AJS packs → exemplar route is mandatory.
- You may search and decide *which* upstream paragraphs are worth candidate lines; you may **not** skip human confirm, bind Apify, or auto-edit `research-core`.

## Autonomy

You decide: queue schema tweaks, which venue to fill first, digest template, exemplar order, whether M1 is manual-only this session, how to phrase candidate rules.

You do **not** decide: skipping owner approval; binding Apify or any crawl vendor; merging author into venue; auto-editing `research-core`.

## Suggested first actions this session

1. `git pull`; read the plan + investigation appendix + `skills/style-mine/SKILL.md` + quickread `--style` path.
2. If implementing M1: scaffold vault dirs (or document temp path); write `monitor/README.md` with `source: recommended crossref+openalex` (still unbound until owner confirms).
3. Read `hanzhong-liu-research` `papers/publications.json`; draft `authors/hanzhong-liu/exemplars.md` by **filtering that file**, do not invent titles.
4. Optionally run **one** real top-4 causal paper end-to-end with a manual DOI (OA/preprint only).
5. Report in Chinese: what you did, what stays unbound, open questions for the owner.

## Language

- Skill files you edit: English (repo convention).
- Plan docs: Chinese OK.
- Final report to owner: Chinese.
