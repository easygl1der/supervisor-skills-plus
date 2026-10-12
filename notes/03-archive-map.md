# 03 — Evidence archive map

Archive: `~/Projects/supervisor-skills-msr-tpa` (private, `easygl1der/supervisor-skills-msr-tpa`, HEAD `669b29a`, 474 MB with LFS media).
Project: an empirical SE/MSR study of GitHub issues in proof-assistant ecosystems, submitted to FSE 2027 (double-anonymous). All paths below are relative to the archive root. Timezone in the archive is Asia/Shanghai (UTC+8).

This note maps what exists, how trustworthy each source is, how to cite it, and which later note or skill it feeds. Phase 2 does the actual mining.

## 1. Privacy and anonymization rules for anything derived from here

- The archive names real people (co-authors, a relayed advisor), a real Overleaf project id, real GitHub accounts, a real anonymous-mirror URL, and the paper's real title. None of these may appear in public-facing files of `supervisor-skills-plus` (skills, checklists, handbook case 6.4).
- Reusable material uses roles: **Student** (first author, implementation and most writing), **Senior co-author A** (writing organization, desk-reject red lines; the archive's "Hao"), **Senior co-author B** (methods figure, page budget, repo hub; the archive's "Jimmy/zhimin"), **Advisor (relayed)**. Mapping stays in `private/CASE.md` (gitignored).
- Paper specifics are generalized: "proof-assistant issue trackers" may stay as the domain only in the anonymized case study if the user approves; otherwise "a niche software ecosystem". Decide in Phase 3 (open question).
- WeChat images (`04-comms/**/media`, `assets`, `raw`) are never copied into the skill repo.

## 2. Top-level index files

| File | Lines | What | Trust |
|---|---:|---|---|
| `README.md` | 46 | Pack purpose, layout, notes that Overleaf history only has synced commits | High (meta) |
| `INDEX.md` | 26 | Folder map with counts | High (meta) |
| `GAPS.md` | 20 | 14 known gaps (see §5) | High; authoritative for "no evidence" |
| `TIMELINE.md` | 55 | Phase timeline with evidence column; ⚠ marks unmatched chat/commit | Medium-high; each row cites a source |
| `TIMELINE_DRAFT.md` (= `_import/TIMELINE_DRAFT.md`, identical) | 390 | Long narrative §0–§9: research history, detours ("DFT"), decisions, who did what, push history. Generated 2026-10-10 from a box export | **Secondary narrative.** Cites research-repo paths that are mostly *not* in this archive (`docs/notes/...` lives in the research repo; partial copies under `11-*/tree/docs/`). Verify before citing |
| `PROCESS.md` | 52 | 9-stage process skeleton, decision log (8 rows), 5 detours, artifact map | Medium; a synthesis, cite underlying sources instead |
| `SUPERVISOR_SKILLS_MAPPING.md` | 55 | Earlier mapping of archive → upstream skills, 9 proposed new skills, gaps | Input to Phase 3, not evidence |
| `SOURCES.md` | 26 | Absolute Mac paths of live repos | Pointer only |
| `MEDIA_MANIFEST.md` | 24 | 16 files ≥5 MB (WeChat JPGs) in LFS | Meta |
| `EXTRACTION_PROMPT.md`, `CLAUDE_*_PROMPT.md` | — | Prompts for this work; `CLAUDE_MASTER_PROMPT.md` supersedes the other two | Instructions, not evidence |

## 3. Folder map

### `00-upstream-supervisor/` (1 file)
Pointer README to HKUSTDial/Supervisor-Skills. No content. Not needed now that the full upstream is cloned.

### `01-checklist/` (12 files) — checklist evolution. Feeds notes/07 (checklist diffs) and `checklists/`.

| File | Lines | What |
|---|---:|---|
| `versions/FULL-PAPER-CHECKLIST.v1.md` | 248 | v1 one-line checklist (backup) |
| `FULL-PAPER-CHECKLIST.md` (= `versions/FULL-PAPER-CHECKLIST.md`, identical) | 3891 | **Master v2 (2026-09-29)**, 140 items, each `### <ID>` block has *What to check / Misreadings to avoid / Provenance (Who, Where, Quote) / Refs*. Prefixes: CF 30 (content & framing), MF 24 (methodology & figures), RS 19 (RQs & stats), RW 13 (related work & citations), AH 13 (advisor), TH 11 (threats), RP 13 (repro), CO 10 (collaboration), FP 7 (final pass), plus U1–U5 unresolved conflicts and a Superseded appendix. Tags `[LATEST]/[OUTDATED]/[PAPER-FOLLOW]/[OK]` |
| `enriched/{group-chat,jimmy-chat,paper-refs,cursor-history}.md` + README | 663/755/2260/631 | Source packs used to generate v2. IDs **GC-01…GC-16** (group chat), **J-01…J-35** (1:1 chat; J-35 = C-035 "text → figure → table"), cursor thread IDs |
| `checklist.md` (= `checklist-from-paper-repo.md`, identical) | 443 | The paper-repo `checklist.md` (FSE submission writing checklist, G/T/W/A section IDs; referenced by `03-skills/README.md`) |
| `FINAL-CHECKLIST-2026-10-02.md` | 273 | Final read-only pre-submission check: blockers, item status, avoid-ai-writing audit, Adams rhetoric pass, cross-section consistency, devil's-advocate review |
| `CHECKLIST-UPDATE-SUMMARY.md` | 139 | 2026-09-29 verification of TH-01…TH-11 and RP-01…RP-11 |

Data-quality note: the v2 provenance lines are machine-generated. Example: `CF-01` provenance reads "Who: Hao (乐绎华)", but 乐绎华 is the student, not Hao (`FULL-PAPER-CHECKLIST.md` ~line 50). Re-verify every provenance before reusing an item.

### `02-comments-hao/` (3 files; identical copies under `10-requirements/hao/`) — the senior co-author's written comments. Feeds notes/05 (feedback-to-revision table).

| File | Lines | What |
|---|---:|---|
| `comments_hao.md` | 185 | Original comments (terms table; "proof assistant" not "theorem prover"; §2.1–2.8 writing/organization: context before methodology, why before how, no study-plan narrative, no number laundry lists, Q→why→method→result→implication per RQ, SE motivation, substance-first openings, one caveat not many) |
| `comments.md` | 250 | Consolidated actionable revision checklist (2026-09-28) derived from the above + prior Overleaf tree |
| `adams-skill-revision-comments.md` | 256 | 2026-09-28 agent-generated comments (12 subagents, one issue each) applying the Adams/SAIL skill; P0/P1/P2 priorities; `[AUTHOR]` = needs fact check. **Agent output, not a human comment** |

### `03-skills/` (18 files) — skills the team used in Cursor, mirrored 2026-10-01. Audited in notes/02.
`se-paper-writing` (1017 lines), `se-paper-refinement` (508), `se-paper-reviewer` (196), `avoid-ai-writing` (317 + 743-line patterns + LICENSE), `journal-adapt` (490 + base_rules for economics, cs_engineering, general_academic, ml_cv_nlp), `adams-sail-issue-mining` (247 + six-papers ref), `msr-tpa-rq-method-borrow` (111). `README.md` maps each skill to checklist IDs (G1, T14, §3–4, A1–A5, W5) and states "Checklist items always win if a skill suggestion conflicts".

### `04-comms/` (250 files, 105 images) — communications. Feeds notes/04, 05, 08.

| Folder | Span | Content | Granularity |
|---|---|---|---|
| `20260929-1007-wechat-group/` | 09-29 11:41 → 10-07 12:11 | 3-person group chat: `messages.jsonl` (384 msgs, fields speaker/ts/text/media/sources), `transcript.md` (1602 lines), `media/` (48 files incl. a shared `checklist.md` and `study-workflow.pdf`) | **Minute timestamps.** Best citable chat source |
| `past-chat-group/` | 09-22 → 09-29 | Earlier group export: `SUMMARY.md` (requirements + "superseded" tables), `REFS.md`, assets (2 overview drawio versions, FSE PC related-work scan), `raw/` (18) | SUMMARY is date-level only |
| `past-chat-jimmy/` | 09-22 → 09-29 | Student ↔ senior co-author B 1:1: `SUMMARY.md` (C-0xx requirement IDs), `REFS.md`, `raw/` (47: merged chat text, `jimmy-main-pdf-comments/` PDF annotation extracts, `parse-pdf-comments` output, `user-supplied-relays.md`) | Raw text has timestamps; SUMMARY date-level |
| `20260926-jimmy-advisor-paper-glimpse/` | 09-26 | Relayed advisor reading notes (readability of internal jargon, Dx provenance, §3.1 overkill, missing Isabelle, cross-domain baseline) + `stackoverflow-baseline-candidate.md` | Second-hand (relay) |
| `20260920-msritp-meeting/` | 09-20 | Meeting notes: RQ numbering locked, writing order (numbers into Overleaf → paper skill → human edit) | Notes, single source |
| `20260910-zhimin-d4d5-threats/` | 09-10/11 | Coverage wall → "put it in threats, pivot to RQ2" decision, label-purpose rule; screenshots | Notes + screenshots |
| `cursor-history-chat/` | 09-27 → 09-29 | 41–42 Cursor agent session summaries (`*/SUMMARY.md`, `INDEX.md`, `MERGED-SUMMARY.md`) | Agent-written summaries |

`PAST-CHAT-INDEX.md` is the paper repo's `local-refs/past-chat/README.md` (paths inside it are relative to that repo, not this archive).

### `05-figures-tables/` (140 files, 39 images) — figure evidence. Feeds notes/07 (figure iterations) and figure-designer / drawio-reconstruction.
- `final/`: shipped figures with sources: `study-workflow.{drawio,pdf}`, `intro-failure-modes.{drawio,pdf}`, `rq1/`, `rq2/` (R/Python renderers, CSVs, KM curves, median TTC matrix), `rq3/`, `appendix/`.
- `sources/drawio/`: overview iterations (`Overview - GitHub issue mining.drawio` → `... reference replica.drawio`), `overview-reference-replica/` (build script, SVG icon set, layout fingerprint, QA phases 1–3, redline validation JSON, pre-redline 2026-09-28 snapshot), `overview-variants/` (variants.yaml + generator).
- `sources/briefs/`: `overview-figure-prompt.md` (665 lines), `drawio-overview-brief.md`.
- `discussion/FIGURE-DISCUSSION-INDEX.md`: 7 topics → decisions (four-panel → single three-stage workflow; each figure box ↔ same-named prose subsection; RQ1 heatmap instead of bars; text → figure → table hierarchy).
- `METHODOLOGY-FIGURES-REVIEW.md`, `METHODOLOGY-FIGURES-ACTION-ITEMS.md`, `fse-2027-requirements.md`.

### `06-revision/` (2 files)
`REVISION-SUMMARY.md` (508 lines): before/after LaTeX for the design-section revision driven by `comments_hao.md` §2.x. Good source for comment → change pairs (verify against patches). `BUILD.md`: build instructions.

### `07-overleaf-history/` (375 files) — the strongest evidence. Feeds notes/04, 05, 06.

| Item | What |
|---|---|
| `msr-tpa-commits.tsv`, `msr-tpa-diffstat.tsv`, `msr-tpa-commit-summaries.md`, `msr-tpa-SUMMARY-TABLE.md` | 105 commits of the collaboration paper repo (2026-09-26 → 10-03); real commit messages; resolved author + basis |
| `overleaf-*.tsv/md` | 252 commits of the Overleaf git (2026-08-01 → 10-04); many are `Update on Overleaf.` / `Sync GitHub main @ <sha>` |
| `patches-msr-tpa/` (105), `patches-overleaf/` (252) | Full `git show` per commit, named `YYYYMMDD-HHMM_<sha>.patch` → **cite as `<sha>` + this path** |
| `*-SECTION-EVOLUTION.md` | Changes per section file in time order (msr-tpa: 425 lines) |
| `*-CHAT-XREF.md` | Commit ↔ group-chat messages within ±2h (73 msr-tpa, 49 Overleaf commits) |
| `key-section-diffs/` | Diffstats for 4 milestone ranges `5e73a46→9809b8c→9ef4a07→e0ea09b→87bf139`, one selected patch |

Caveats: Chinese one-line summaries are auto-generated from subject + touched files (must verify against the patch). Author `?` = unresolvable (Overleaf anonymous or merges made by B's account). ±2h chat proximity is correlation, not causation. Chat coverage starts 09-29 11:41, so earlier commits have no chat link.

Notable find for the feedback skill: commit `9809b8c` ("hao's comments", 2026-09-29 11:35) adds a reviewing protocol to `main.tex`: `\hao{...}` = senior's notes, "resolved by Hao or the agent"; `\todo{...}` = "action items left for the student to fix; the agent must not resolve them" (`patches-msr-tpa/20260929-1135_9809b8c.patch`). Second comment drop: `0f96193` (2026-10-02 07:45); response commit `9ef4a07` ("refine methods and their figure based on hao's comments").

### `08-inventory/` (1 file)
Pointers to live repos not vendored: research repo, paper repo, Overleaf checkout, replication repo (`msr-tpa-replication` + anonymous mirror), box export, skills hub.

### `09-paper-snapshot/` (109 files, 24 images) — final paper state, HEAD `87bf139` (2026-10-03 19:38).
`main.tex` (title at line 116), `main.pdf`, `sections/01-introduction … 09-conclusion, A-terms, A-appendix`, `refs.bib`, `codebook-labels.tex`, `figures/` (incl. `study-workflow-UPDATE-PLAN.md`, `enhance_intro_failure_modes.py`), `VERSION_LIST.md` (all 105 commits one per line), copies of `REVISION-SUMMARY.md` and `BUILD.md`. Feeds notes/06 (final state of each section) and the anonymized case study.

### `10-requirements/` (12 files)
`hao/` (copies of 02), `jimmy-zhimin/{jimmy-chat,group-chat}-SUMMARY.md`, `advisor-glimpse/` (copy of 04 glimpse), `paper-refs/{REFS,SUMMARY,CHECKLIST-DRAFT}.md` (every requirement → source path/line), `venue/fse-2027-requirements.md` (page limits 18+4, acmart `acmsmall,screen,review,anonymous`, anonymization rules, Data Availability section, AI-use policy, desk-reject causes; fetched 2026-10-01 via a model extraction, items marked CONFIRM), `DECISION-HINTS.md` (U1–U5: κ numbers, RQ2 figures, Overleaf, gold, method borrow).

### `11-mining-github-issue-audit/` (585 files) — research repo audit (no data/DB).
`FILE_MANIFEST.tsv` (~13.7k files, bytes, mtime), `DIR_STATS.md`, `research-repo-commits.tsv` (research repo git log, needed to verify TIMELINE §1–§4), `remotes.txt`, `tree/` (all text files ≤1 MB: `docs/` incl. the 2026-07-08 research plan, sampling allocation, protocol, writing, partner notes, drawio, figure-generation; `prompts/`, `scripts/`, `analysis/`, `schemas/`, `sql/`, `collaboration/`). Feeds notes/04 (experiment phase) and the experiment/records design (H, G).

## 4. Citation formats to use in skills, checklists, and notes

| Source type | Format | Example |
|---|---|---|
| Paper-repo commit | `msr:<sha7>` + `07-overleaf-history/patches-msr-tpa/<file>.patch` | `msr:9809b8c` |
| Overleaf commit | `ol:<sha7>` + `07-overleaf-history/patches-overleaf/<file>.patch` | `ol:48f5713` |
| Research-repo commit | `res:<sha7>` + `11-mining-github-issue-audit/research-repo-commits.tsv` | `res:de95735` |
| Group chat message | `chat:group@YYYY-MM-DDTHH:MM` (from `messages.jsonl`) | `chat:group@2026-10-03T18:27` |
| Pre-09-29 chat | `chat:<group|1on1>-summary:<req id>` + SUMMARY path (date-level) | `C-035` |
| Comment file | `<path>:<line>` | `02-comments-hao/comments_hao.md:12` |
| Checklist item | `<ID>@<version>` | `CF-23@v2` |

In public files the source label stays (e.g. `msr:9809b8c`) but the private archive path is the resolver; no names.

## 5. Known gaps (from `GAPS.md` and this read) — write "no evidence" here

1. No raw 1:1 chat with Senior co-author A; only written comments, group messages, commits.
2. Before 09-22 chat is episodic (09-10, 09-20, 09-26 notes); 09-27/28 chat missing.
3. 09-22→09-29 chats are date-level summaries only; no automated chat↔commit links before 09-29 11:41.
4. No recalled-message audit trail; superseded tables and git history substitute.
5. Overleaf has no keystroke history; `Update on Overleaf.` can bundle many authors' edits.
6. Chinese commit summaries are auto-generated, unverified.
7. Research data/DB excluded (manifest only).
8. No reviewer reviews yet → no rebuttal evidence.
9. One paper, one field (SE/MSR). Other field profiles have no project evidence.
10. No structured record that the submission was accepted by the system, the final page count, or the final submitted PDF hash (TIMELINE_DRAFT §Gaps 9).
11. Two paper lines (Overleaf vs `msr-tpa-paper`) had diverging titles/figure sets (TIMELINE_DRAFT §7, Gaps 4).
12. Machine-generated provenance in checklist v2 has at least one misattribution (§3 above).

## 6. Inconsistencies to resolve in Phase 2

- **Deadline.** `TIMELINE.md` lists "~2026-10-12 FSE 2027 投稿锚点（群聊语境）" and the 09-20 meeting said "12 号" orally, but `10-requirements/venue/fse-2027-requirements.md` gives Fri 2 Oct 2026 AoE (= 3 Oct 19:59 China), and the paper repo's last commit `87bf139` is 2026-10-03 19:38, with the group chat on 10-03 handling PC conflicts and the abstract. Hypothesis: the real deadline was 10-03 19:59 CST; verify against transcript before stating it.
- **Title history.** Plan title → "Proof Engineering in the Wild" → "What Breaks…" (current `main.tex:116`) → "Maintaining Proof Assistants…" (per DEM-295, not in archive). Use only `main.tex` as truth.
- **Agent vs human comments.** `adams-skill-revision-comments.md` and Cursor summaries are agent-produced; the feedback table must label comment origin (human senior / relayed advisor / agent).

## 7. What feeds which Phase 2 note

| Note | Primary sources |
|---|---|
| 04 timeline & process verification | `TIMELINE*.md`, `research-repo-commits.tsv`, `msr-tpa-commits.tsv`, `overleaf-commits.tsv`, `04-comms/*/README.md` |
| 05 feedback-to-revision table | `02-comments-hao/*`, `msr:9809b8c`, `msr:0f96193`, `msr:9ef4a07`, `06-revision/REVISION-SUMMARY.md`, `past-chat-jimmy/raw/jimmy-main-pdf-comments`, group `messages.jsonl`, `*-CHAT-XREF.md` |
| 06 section evolution | `*-SECTION-EVOLUTION.md`, `key-section-diffs/`, patches, `09-paper-snapshot/sections/` |
| 07 figure iterations + checklist diffs | `05-figures-tables/**`, `01-checklist/versions/`, `FINAL-CHECKLIST-2026-10-02.md` |
| 08 process tips | `PROCESS.md` detours (verified), group chat, `20260910-*`, `20260920-*`, venue requirements |
