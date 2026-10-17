# Claude Code session prompt — causal style mining & monitor plan

Paste this after `cd` into `supervisor-skills-plus` (private fork). Work on **main**, no branch/PR unless the owner says otherwise.

## Intent (read first)

Open and follow:

1. `docs/plans/2026-10-17-causal-style-mining-and-monitor.md` — **source of truth**
2. This file — session contract

Goal: a repeatable pipeline so we learn (a) how causal papers are written in JASA / JRSSB / AoS / Biometrika, and (b) 刘汉中 (Hanzhong Liu) author rhetoric, then feed **style-mine** via cards in a private **causal-style-vault**. Promote to `research-core` **only** through `lessons-harvest` + **owner approval**. Never auto-merge rules daily.

## Hard constraints

- Do **not** rewrite unrelated skills in a drive-by.
- Do **not** treat **Apify** (or any single vendor) as required. **Intake/monitor source = TBD** until the owner clarifies. Until then: manual DOI/TOC list is enough to prove MinerU → `paper-quickread --style` → vault cards.
- Never paraphrase paper findings into cards/rules; rhetoric and structure only.
- Never write PDFs or full-text transcripts into this public/skills repo.
- Author profile ≠ venue profile (separate paths under vault).
- Routines: propose only; **do not create** Academic Bot crons unless marked done by the owner ("to be created later by Academic Bot").

## Liu / 汉中流 repo

- Locate or clone: `easygl1der/hanzhong-liu-research` (private).
- Build exemplar list from `papers/publications.json`, `catalog.json`, `s2-author.json`, `papers.md`, `group/`, etc.
- Dissect into vault `authors/hanzhong-liu/cards/`; keep PDFs in that repo or local study copies.

## External skills (borrow vs leave)

Read plan §5. In short:

- **Extend** in-repo `style-mine` / `paper-quickread --style` / `lessons-harvest`.
- **Borrow ideas only** from `brycewang-stanford/Awesome-Journal-Skills` (MIT) as **candidate** check dimensions; cite `[src: ...]`; do not install whole AER/QJE packs as stats top-4 rules.
- Stats top-4 have **no** ready AJS packs → exemplar route is mandatory.
- You may search and decide *which* upstream paragraphs are worth candidate lines; you may **not** skip human confirm or invent intake tooling.

## Autonomy

You decide: queue schema tweaks, which venue to fill first, digest template, exemplar order, whether M1 is manual-only this session, how to phrase candidate rules.

You do **not** decide: skipping owner approval; binding a crawl vendor; merging author into venue; auto-editing `research-core`.

## Suggested first actions this session

1. `git pull`; read the plan + `skills/style-mine/SKILL.md` + quickread `--style` path.
2. If implementing M1: scaffold vault dirs (or document temp path); write `monitor/README.md` with `source: TBD`.
3. Clone/pull `hanzhong-liu-research`; draft `authors/hanzhong-liu/exemplars.md`.
4. Optionally run **one** real top-4 causal paper end-to-end with a manual DOI.
5. Report in Chinese: what you did, what stays TBD, open questions for the owner.

## Language

- Skill files you edit: English (repo convention).
- Plan docs: Chinese OK.
- Final report to owner: Chinese.
