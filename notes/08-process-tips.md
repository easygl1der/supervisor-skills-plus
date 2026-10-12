# 08 — Process tips: collaboration, experiments, venue hardening, records

Phase 2 mining note. Evidence archive: `~/Projects/supervisor-skills-msr-tpa` (HEAD `669b29a`). All times Asia/Shanghai (UTC+8). Citation formats follow `03-archive-map.md` §4: `msr:<sha>` (paper repo, `07-overleaf-history/patches-msr-tpa/`), `ol:<sha>` (Overleaf git, `07-overleaf-history/patches-overleaf/`), `res:<sha>` (research repo, `11-mining-github-issue-audit/research-repo-commits.tsv`), `chat:group@YYYY-MM-DDTHH:MM` (`04-comms/20260929-1007-wechat-group/messages.jsonl`), `chat:1on1@YYYY-MM-DDTHH:MM` (`04-comms/past-chat-jimmy/raw/chat-history-merged.txt`), `<path>:<line>`.

Roles are used throughout, also in §1–§4: **Student** (first author), **Senior A** (writing organization, desk-reject red lines), **Senior B** (methods figure, page budget, owner of the paper repo and the Overleaf project), **Advisor (relayed)**. Repos are named by role: *research repo* (corpus, annotation, analysis), *paper repo* (GitHub LaTeX, created 09-26), *Overleaf project*, *replication repo* (+ anonymous mirror). Chat quotes are short and in the original language. `TIMELINE_DRAFT.md` is secondary; where it disagrees with primary sources, this note says so.

---

## 1. Collaboration and source of truth (SoT)

### 1.1 Topology that actually existed

| Channel | What it was | Evidence |
|---|---|---|
| Overleaf project | Created by Senior B 2026-08-01, template only until mid-Sept; 252 commits to 10-04 | `ol:48f5713`; `11-*/tree/docs/notes/20260814-overleaf-paper-backup.md` ("still the ACM template … no paper prose") |
| Local Overleaf clone | Nested independent git repo inside the research repo, pulled with `--ff-only`, private GitHub backup; rule "Do not `git push --force` to Overleaf" | same note; `ol:c5de1ea` (09-06, pull helper restored) |
| Overleaf MCP (agent writes) | 74 Overleaf commits authored `Overleaf MCP`, 09-09 → 09-21 only | `07-overleaf-history/overleaf-commits.tsv` (author counts) |
| Paper repo (GitHub) | Senior B's "Initial Overleaf Import" 09-26 19:37; 105 commits to 10-03 19:38 | `msr:5e73a46` … `msr:87bf139` |
| Overleaf ↔ GitHub via Overleaf's own GitHub integration (Senior B's account) | Pairs `Updates from Overleaf` + `Merge overleaf-YYYY-MM-DD-HHMM into main`, 8 pairs 09-29 → 10-03 | e.g. `msr:8fc36d3`+`msr:01d66a2` (09-29 19:32); timestamps match `ol:bfa20aa` (Anonymous "Update on Overleaf", 19:32:41). The link between the two is **inferred** from timestamps |
| GitHub → Overleaf one-way mirror (Actions) | `.github/workflows/sync-overleaf.yml` on every push to `main` runs `scripts/sync-to-overleaf.sh`; 43 Overleaf commits `Sync GitHub main @ <sha>` by `github-actions[bot]`, first at 09-29 13:34 | `msr:c93ef1f` (09-29 12:44, workflow + script), `msr:c3d1e70` (12:57, secret fix), `ol:26eb2dc` (12:59 test), `ol:b0123f2` (13:34 first bot sync) |
| Overleaf web edits | 24 `Update on Overleaf.` commits, 13 authored `Anonymous` (author unresolvable) | `overleaf-commits.tsv`; `07-overleaf-history/README.md` caveat |

The sync script is a **copy-over, not a merge**: it clones Overleaf, copies a filtered file list from the GitHub checkout on top, commits, and pushes (`msr:c93ef1f`, `scripts/sync-to-overleaf.sh`: "Mirror the GitHub checkout to Overleaf Git (one-way: this repo -> Overleaf)"). Any Overleaf-side edit not yet merged into GitHub `main` is silently overwritten by the next push from anyone. A later fix added only a token-format check (`olp_` prefix) (`msr:e4ebb61`).

### 1.2 Which side was authoritative, and when it changed

| When | Rule | Who / evidence |
|---|---|---|
| 08-14 | Overleaf = paper; GitHub only a disaster backup | `20260814-overleaf-paper-backup.md` |
| 09-20 | Use Senior B's Overleaf; free plan allows only two collaborators; sync every 2–3 days | `04-comms/20260920-msritp-meeting/README.md` §1.6 |
| 09-27 | Overleaf must always be latest: "确保overleaf的一直是最新版哈" | Senior B, `chat:1on1@2026-09-27T10:15` |
| 09-27 22:33 | Senior B refactors on Overleaf/paper repo, asks Student to pull | `chat:1on1@2026-09-27T22:33`; `msr:33e0af9` (22:32) |
| 09-29 11:10 | "需要手动同步下" (push ≠ Overleaf update) | Senior B, `chat:1on1@2026-09-29T11:10` |
| 09-29 11:52–12:16 | PR #2 conflict; Student: submitted while "overleaf 版本和 git 版本当时没对上"; Senior B's PR predates Senior A's big edit; Student merges by hand | `chat:group@2026-09-29T11:52`, `…T12:16` |
| 09-29 12:25 | Senior A: "目前规则是保证overleaf是最新的？还是git main是最新的？" | `chat:group@2026-09-29T12:25` |
| 09-29 12:40 | Student: "我是保持 Git main最新"; Cursor thread records "GitHub main is canonical … default rule for all future paper repos"; PR #2 closed unmerged | `chat:group@2026-09-29T12:40`; `04-comms/cursor-history-chat/20562bcb/SUMMARY.md` turns 15–17; `past-chat-group/SUMMARY.md` "Outdated/superseded" row |
| 10-03 04:53 | Senior A: "都弄好了sync到overleaf吧，方便修改和协作" | `chat:group@2026-10-03T04:53` |
| 10-03 19:41–19:44 | After the revert incident (§1.3) Senior A: "别用git了吧"; Student: "我直接 overleaf 改了" | `chat:group@2026-10-03T19:41`, `…T19:44` |
| 10-03 23:45 | Senior A: "现在用overleaf修改吧，方便合作"; Student agrees | `chat:group@2026-10-03T23:45`, `…T23:55` |
| after 10-03 19:38 | Paper repo gets **no further commits**; Overleaf gets 4 edits on 10-04, incl. Senior A's +468/−453 rewrite with a **new title** | `msr-tpa-commits.tsv` (last `msr:87bf139`); `ol:ba3f1ee` (10-04 13:16) |

So the SoT flipped three times in eight days (Overleaf → GitHub `main` → Overleaf), and the last flip was never written into the repo docs: `BUILD.md` in the final paper repo still says "GitHub is source of truth" (`09-paper-snapshot/BUILD.md`, "Overleaf sync" section). Consequence for the archive: `09-paper-snapshot` (`msr:87bf139`) is **not** the submitted version; the title, intro, related work and RQ2 robustness text in `ol:ba3f1ee` differ. This is the mechanism behind archive gap 11 (two diverging paper lines).

### 1.3 Incidents

1. **Sync bot reverted a co-author's Overleaf edits, 10-03 19:39, 20 minutes before the deadline.** Senior A edited 7 files on Overleaf at 19:38:54 (`ol:a610d1d`: new title, intro architecture paragraph, related work, RQ2 filing-period robustness). Ten seconds later the Action mirrored Student's push `msr:87bf139` (`ol:214cc0c`, 19:39:04), whose patch is the exact inverse of those hunks (title back to the old one, the robustness paragraph deleted). Chat: Senior A "我改了半天的东西都没了" and "页数越写越少" (`chat:group@2026-10-03T19:41–19:42`); Student offers to roll back, Senior A does it himself (`…T19:45–19:47`). The new title reappears only in `ol:ba3f1ee` on 10-04. Root cause: one-way copy-over sync plus two people editing different channels in the same minutes, with no lock or "who has the pen" rule.
2. **Overleaf MCP whole-file writes truncated `paper.tex` twice.** 09-09: an author-block update via MCP was +21/−379 lines, followed by two "Restore full paper.tex" commits (`ol:b2ad042`, `ol:030783c`, `ol:f77d894`). 09-16: a remark insertion deleted 119 lines (codebook + sampling-frame tables), restored 2 minutes later "after accidental placeholder" (`ol:3ae9fd3`, `ol:6cca5e3`, `ol:c128ade`, `ol:1ba123a`). No MCP commits after 09-21.
3. **Merge-conflict markers committed** into the Overleaf preamble and fixed by hand (`ol:2f275a8`, 09-15).
4. **Merge storm on submission day.** On 10-03 the paper repo has 6 merge commits (`msr:55e1878` 01:36, `msr:3c6bbad` 08:53, `msr:bbbf4cd` 09:01, `msr:4c69816` 10:05, `msr:1c44749` 11:32, `msr:5fb7817` 17:00) and 2 lone `Updates from Overleaf` (`msr:4f8b488`, `msr:1f68c99`), interleaved with 11 Anonymous/Senior-B Overleaf edits and 15 bot syncs (`overleaf-commits.tsv`). Questions "是最新的吗" recur: `chat:group@2026-09-29T11:52`, `…10-03T12:23`, `…10-03T18:27`.
5. **Private material pushed to the shared repo for 21 h.** `msr:f1c7df8` (10-01 00:51) tracked `local-refs/` (chats, PDFs, skills) "for co-authors"; `msr:c8adb43` (10-01 22:07) untracked it again. The research repo later did the same for chat archives and the literature workbench (`res:7b81393`, `res:7c7abc1`, `res:e66ba6d`, 10-10).

### 1.4 What worked

- Filtered file list in the sync script kept R/Python/CSV/drawio/PNG out of Overleaf (`msr:c93ef1f`; checklist `CO-04@v2`).
- Safety checkpoints before agent-driven destructive edits: commits titled `cursor-safety: checkpoint before destructive delete` (`ol:5eecfa5`, `ol:1f99dde`, `msr:815305e`, `res:43a6245`) and `Baseline: snapshot of uncommitted main working tree before methodology/RQ revision` (`msr:3e7bab0`).
- Senior A's comment protocol in `main.tex`: `\hao{}` notes may be resolved by him or the agent; `\todo{}` items are for the Student, and "the agent must not resolve them" (`msr:9809b8c`, 09-29 11:35; second drop `msr:0f96193`, 10-02 07:45, announced at `chat:group@2026-10-02T07:46`).
- Time-zone relay: Senior A in Canada asks for handoff ("我睡一觉起来接手？", `chat:group@2026-10-03T12:20`); Senior B checks "全push" before the handoff (`…T12:23`).

### 1.5 Lessons (collaboration)

- Pick one writable SoT per phase, write it into `BUILD.md`/`STATUS.md`, and re-write it when it changes. Here the final switch to Overleaf exists only in chat.
- A one-way mirror must refuse to push when the target has commits not in the source (fast-forward check), or at least warn. A copy-over mirror and a second bidirectional bridge on the same Overleaf project is the setup that lost edits.
- In the last hours, freeze to one channel and one editor at a time ("pen" token in chat).
- After any agent write to a shared document, check the diffstat; a large deletion from a small intended change means a whole-file overwrite.

---

## 2. Experiments and data

### 2.1 Corpus freeze and sampling

- Snapshot of seven repositories / five ecosystems taken 2026-07-12; frozen analysis corpus N = 23,671 (`01-checklist/CHECKLIST-UPDATE-SUMMARY.md` RP-07; `09-paper-snapshot/main.tex:123`). Earlier run `seven-repo-700-20260712` superseded by the 582 run (`11-*/tree/docs/notes/20260812-review-status-199-vs-582.md`).
- Constrained stratified sampling documented before annotation (`res:4c60e71`, 07-13; `tree/docs/msr4itp_constrained_stratified_sampling_allocation_20260713.md`); gold id `seven-repo-582-20260714`, seed 42; held-out split `split_seed42_stratified7.json` (291 held-out) (`tree/prompts/llm-annotation-v1/README.md`).
- Repository-selection star date (20 Sept) differs from the snapshot date (12 July); recorded as an accepted author decision in the final check (`01-checklist/FINAL-CHECKLIST-2026-10-02.md`, header).

### 2.2 Gold labels and who produced them

- Collaborative annotation app on a VPS with a git-synced state file: `collaboration/research_state.json` (export/import scripts; importer stops on conflicting primary keys) (`tree/collaboration/README.md`; `res:d3caaf2`, `res:02eefe9`).
- **VPS UI vs local DB.** On 08-12 the live queue showed 199/383 while local SQLite and the git state file had 582/582; `origin/main` had a third state (99/483). Root cause: the VPS SQLite was never re-imported (`tree/docs/notes/20260812-review-status-199-vs-582.md`). Resolution recorded there: trust local SQLite + state file, not the live UI. The Overleaf draft carried this as an explicit disclaimer ("not the production UI slice of 199/383 submitted rows", context lines of `ol:3ae9fd3`).
- Gold review log with an update protocol: every relabel, KEEP, or open ambiguity is logged in the same agent turn; each new classifier trap gets an `L###` id and a one-line prompt rule (`tree/docs/notes/gold-review/CHANGELOG.md` lines 1–30; L001–L025, e.g. "L001 COMPLETED ≠ fixed", "L002 禁止为清 unknown 猜 local-patch", "L019 「closing, see comment above」不是 fixed"). Machine-readable `prompt-lessons.jsonl` is referenced but **kept local-only** (`res:7e4a35c`, 09-12); not in the archive.
- **Agent relabeling of gold.** A Cursor Goal authorized the agent to rewrite gold codes in SQLite from LLM-visible payloads without per-issue human naming (`tree/docs/notes/gold-review/GOAL.md`, DEM-21 → DEM-53, 09-16). The 10-02 final check found the annotation app entries mostly by `codex` (3,503 entries over 571 issues; 471 later superseded by the Student) and no data supporting "two authors independently annotate all 582 issues … κ = 0.74" (`FINAL-CHECKLIST-2026-10-02.md` B1). The claim is still in the 10-03 snapshot (`09-paper-snapshot/sections/03-design.tex:97`) and the post-deadline Overleaf rewrite does not touch that line (`ol:ba3f1ee`). Whether the submitted PDF changed it: **no evidence** (gap 10).
- **Held-out gold edited after seeing model output.** On 09-20 the user accepted 14 agent-proposed D6/D7 gold changes ("overlay-high14", built from gold-vs-LLM pages for v1.4.13) and set the opening bar to Cohen 0.65 in the same step; the note says rejecting any one D7 cell "could drop D7 below 0.65" (`tree/docs/notes/gold-review/overlay-high14-review.md` lines 1–9, 28–29). The prompt pack README had a user bar of "≈≥0.7" that v1.4.13 did not pass (`tree/prompts/llm-annotation-v1/README.md`, v1.4.13 entry). No mention of the overlay in the 10-03 paper body (only a TeX comment, `03-design.tex:6`). The decision was recorded (good); disclosure is the open risk.

### 2.3 LLM annotation and prompt versioning

- Prompt pack `llm-annotation-v1.x` in the research repo with an in-README version log: each version lists held-out κ per dimension for two runs and whether it was kept or rolled back (v1.4.4, v1.4.10, v1.4.12 rolled back; v1.4.13 shipped 09-20, `res:ffbf63a`) (`tree/prompts/llm-annotation-v1/README.md`).
- System-level decisions are coded, not prompted: gate enforcement, existence check for `fixed`, signals, truncation caps, retries, Gwet AC1, two-run self-consistency (`compare_two_runs.py`), adjudication script (README "DEM-6 decisions A1–A8, 2026-09-19").
- Model lock recorded as a ticket: DEM-98 (09-18) `deepseek-v4.1-flash` via Ollama Cloud, temperature 0, JSON object (README "Live cloud lock"); the paper reports the same (`03-design.tex:104`).
- Run gating in the script: the large audit run "refuses until `GOLD_BAR_OK=1` after held-out κ is near ≥0.7 on two runs"; jobs run as systemd units on the VPS so the laptop can sleep; scripts "Never print API keys" (`tree/scripts/vps-hk-llm-annotate.sh`, `vps-freeze-health.sh`, `vps-freeze-drain-watch.sh`).
- Partner bundle with sha256 manifest for the co-author (`res:44b01cb`; `tree/scripts/package_partner_llm_annotation_bundle.py`).
- Prompt-vs-RQ confusion resolved at the 09-20 meeting: the prompt/κ is method, RQ2 is a plain statistics script, RQ3 reuses the seven dimensions with no second prompt (`04-comms/20260920-msritp-meeting/README.md` §1.3–1.4, §3).
- Reporting rule conflict left open at the final check: an author rule "report only the first validation run" vs Design printing 0.81 and 0.82 and Data Availability promising "both held-out runs" (`FINAL-CHECKLIST-2026-10-02.md` H1); the 10-03 snapshot still prints both (`03-design.tex:112`, `main.tex:171`).

### 2.4 Coverage wall → threats (method decision)

On 09-10 the Student reported >16% closed issues without a PR/commit; Senior B: put it in threats and move to RQ2; Senior A: give the mechanism (deleted branches, squashed commits) and decide by label purpose (unknown vs out of scope) (`04-comms/20260910-zhimin-d4d5-threats/README.md` §1–2; recorded in the research repo `res:7998b24`, `res:8fe17c3`). The README also records the "do not" list (no time-window commit matching as a main method, no guessing `local-patch`). Good example of a decision captured with rejected alternatives.

### 2.5 Where large data lived

- Research repo is 4.5 GB on disk; `research.sqlite`, crawled data, `analysis/`, `dist/`, `outputs/` are listed only in `11-*/FILE_MANIFEST.tsv` and excluded from the archive (`11-*/README.md`; `GAPS.md`). SQLite backups taken before VPS imports (`FILE_MANIFEST.tsv`: `research.sqlite.before-vps-import-20260801T…bak`).
- Paper repo: no data; `.gitattributes` only marks `*.pdf binary` (`msr:643836a`); RP-04 "No freeze jsonl copied into paper repo" (`CHECKLIST-UPDATE-SUMMARY.md`). Git LFS: **no evidence** of LFS in the paper or research repos (only the evidence archive itself uses LFS for media).
- Replication: labels as jsonl in the repo; issue bodies about 1 GB; Senior B: "上传到figshare吧 … 数据没必要用github" (`chat:group@2026-10-03T20:22–20:24`); earlier "太大的话用 s3 或者 Google drive" (`…10-02T00:47`). Where the bodies finally went: **no evidence**.

### 2.6 How results reached the paper

- Writing order fixed at the 09-20 meeting: put RQ tables, figures and *copyable text numbers* into Overleaf first, then generate a draft with a writing skill, then human edits (`20260920-msritp-meeting/README.md` §1.5).
- RQ2 median matrix is hard-coded in TeX from `compute_rq2_median_matrix.py`, which reads freeze jsonl in the sibling research repo (`09-paper-snapshot/BUILD.md`, "Figure PDFs").
- Verification: RP-11 "RQ2 median matrix verified – EXACT MATCH (all 42 cells)" (`CHECKLIST-UPDATE-SUMMARY.md:36, 85–99`). RP-12 (record the research-repo SHA used) left as "recommended, not blocking", placeholder `[INSERT SHA HERE …]` (same file, ~line 80).
- The final check found a number audit listing 28 printed numbers not reproduced by replication outputs (D3/D6/D7 shares, heatmap cells, gold-design arithmetic, κ 0.74) and flagged the Data Availability sentence "scripts that recompute every number" as an overclaim (`FINAL-CHECKLIST-2026-10-02.md` H9). The audit file itself (`NUMBER-AUDIT-2026-10-02.md`) is **not in the archive**.
- After submission the Student reports that analysis code added while revising RQ findings was not moved to the replication repo; Senior B: "都要挪" (`chat:group@2026-10-03T20:20–20:22`).

### 2.7 Replication package and anonymous mirror (steps as they happened)

1. 10-01: appendix tables move to the replication package with a README pointer; paper keeps a condensed D1–D7 label table (`chat:group@2026-10-01T09:19`, `…T10:09`; glossary of 66 labels moved to the replication repo, `msr:464168f` checklist text).
2. 10-02 00:45: do not cite the project page, "那个会暴露名字"; apply for an anonymous.4open.science URL (`chat:group@2026-10-02T00:45`); mirror URL created 01:44.
3. 10-02 06:36–06:37: Senior A: link only the package; the package README can be completed after the deadline; first priority is a submittable paper (`chat:group@2026-10-02T06:36–06:37`).
4. 10-02 final check: replication repo had been public under an author-identifying account (`01-checklist/checklist.md:310`), later private (`FINAL-CHECKLIST` AT1); pushed `index.html` contains all author names, affiliations and lab links; mirror currently serves an older clean page, so the leak is latent; mirror also stale vs paper numbers (B2, H8, AT2, AT6).
5. 10-03 23:16: Senior A: the repo must not be empty on the first day after the deadline (`chat:group@2026-10-03T23:16`).
6. 10-05/06: Student asks why the anonymous `index.html` does not render; Senior A: "不用index html，readme完整就好 … 这个容易暴露双盲导致desk rejeck"; Senior B: put `index` in `.gitignore`; done 11:57 (`chat:group@2026-10-05T22:46` → `…10-06T11:57`). This is the same leak the 10-02 check predicted.
7. 10-07: Senior A shares a public post by another SE author about a desk reject issued months into review for an identity-revealing artifact (`chat:group@2026-10-07T07:42`, media `Weixin Image_202610070742_10.jpg`).

`TIMELINE_DRAFT.md` §7 adds "DEM-295 Done: intern 实跑 headline MATCH" on 10-05; the Linear issue is not in the archive, so treat as secondary.

### 2.8 Tooling evidence

| Tool | Evidence | Verdict |
|---|---|---|
| Overleaf MCP | 74 Overleaf commits 09-09 → 09-21, two truncation incidents (§1.3); MCP config paths in Cursor thread `20562bcb` | Used; risky for whole-file writes |
| Cursor agents | `Cursor Agent`-authored research commits 09-07 (`res:56b9084`…`res:5f15595`); Cursor Goal for gold relabel (`GOAL.md`); 42 Cursor threads 09-27 → 09-29 incl. read-only reviewer subagents C1–C12 (`cursor-history-chat/INDEX.md`) | Used heavily; summaries are agent-written |
| Codex / Claude Code | Senior A uses "codex+claude code" (`chat:group@2026-09-30T21:52`); Codex citation audit on submission day (`…10-03T19:03`, `…T19:18`); `codex` as annotator in gold (FINAL B1) | Used |
| Academic MCP / DBLP | DBLP verification worker threads (`cursor-history-chat/MERGED-SUMMARY.md` §4) | Used |
| draw.io MCP | "效果一般，不推荐单独依赖" (`past-chat-group/SUMMARY.md`, tools table) | Tried, weak |
| Wispr Flow (meeting voice notes) | 09-20 meeting; "Flow Summary 会丢细节，以转写为准" (`20260920-msritp-meeting/README.md` header) | Used; summaries lossy |
| Linear | Ticket ids cited in code, notes and TeX comments: DEM-6, 14, 15, 17, 21, 47, 48, 49, 53, 57, 69, 70, 92, 98, 113–116, 295 (grep across archive); e.g. TeX comment "Linear lock (DEM-92 tail, 2026-09-17)" (`msr:33e0af9` removed lines); one issue URL in `GOAL.md`. Ticket bodies are **not** in the archive | IDs only; content lost |
| GitHub Actions | Overleaf sync workflow (§1.1) | Used |
| Google Colab | **No evidence** (only in prompt files for this extraction) | — |
| Git LFS | **No evidence** in project repos | — |

---

## 3. Venue hardening (FSE 2027, double-anonymous)

Venue facts: `10-requirements/venue/fse-2027-requirements.md` (fetched 10-01 via model extraction; "CONFIRM" items). Deadline Fri 2 Oct AoE = 3 Oct 19:59 China; 18 pages + 4 references; `acmsmall,screen,review,anonymous`; desk reject for format violations, fabricated citations, anonymity breaks.

| Topic | What happened | Evidence | Status at 10-03 |
|---|---|---|---|
| Deadline confusion | 09-20 meeting said "12 号"; venue page says 10-02 AoE | `20260920-msritp-meeting/README.md` §1.5 vs venue file | Resolved by 10-01 fetch. The archive map hypothesis (real deadline 10-03 19:59 CST) is confirmed by chat: PDF uploaded 19:55–19:56, system down at 19:59 (`chat:group@2026-10-03T19:55–19:59`) |
| Submission-site outage and reopening | Screenshot of conference posts: site unavailable, will "reopen/extend"; Senior B: use the reopening to polish; "还有18小时" at 10-04 02:06; new versions submitted 10-04 08:46 (A) and 18:04 (B) | `chat:group@2026-10-03T23:18` (media `…202610032318_9.jpg`), `…T23:19`, `…10-04T02:06`, `…T08:46`, `…T18:04` | Done |
| Early upload | Senior B: start uploading at :50, again at :55, "不然overleaf崩了就遭了"; Senior A: "pdf对就行" when form errors appeared | `chat:group@2026-10-03T19:45`, `…T19:58` | Good practice |
| Double-blind: project page / index.html | See §2.7; predicted by the 10-02 check (B2), happened 10-05/06 | `FINAL-CHECKLIST` B2; `chat:group@2026-10-06T05:09` | Fixed by `.gitignore` |
| Double-blind: author-revealing URLs and repo account | Project page "会暴露名字"; replication repo public under an author account; mirror is the only link in the PDF | `chat:group@2026-10-02T00:45`; `checklist.md:310`; `FINAL-CHECKLIST` AT1–AT3 (PDF metadata `dc:creator` = "Anonymous Author(s)") | PDF PASS, repo PARTIAL |
| DBLP-only bib | Senior A: check all cites on DBLP, "现在查处一个错的引用直接desk reject"; earlier per-entry "Correct BibTeX … from the verified record" commits (09-22); DBLP rule file; Codex audit 39 entries: 25 verified, 3 arXiv, 8 not found, 3 skipped; Senior A: "这个没事" | `chat:group@2026-09-29T11:44`; `ol:8ab3546`…`ol:a739ae5`; `msr:8df40d5`; `chat:group@2026-10-03T19:18` | G4 PARTIAL at 10-02 (7 DBLP keys unchecked, `FINAL-CHECKLIST`) |
| Fonts / template | Senior B: restore FSE default font; Senior A: "这个算违反policy，会desk reject"; local shrinking removed 10-01 and written as an author rule; regression found 10-02 (`\footnotesize`, `\tabcolsep` in `05-rq2.tex`) | `chat:group@2026-10-01T09:20–09:23`; `msr:464168f`, `msr:ff0108e` (checklist text); `FINAL-CHECKLIST` G3 | Body sections clean in `09-paper-snapshot` (only non-input appendix files still shrink) |
| Abstract in submission form | No LaTeX macros in the HotCRP abstract: "latex文本【无宏】"; Senior A: plain text "安全一些" | `chat:group@2026-10-03T18:32–18:43`; `msr:4af1aff` | Done |
| Appendix | Senior A: reviewers will not read it; filling pages with it = reject; "不要appendix，软工的人不喜欢" | `chat:group@2026-10-01T08:47–08:56`, `…10-02T01:51` | Appendix removed; 20 → 17 pages (`msr:464168f` text); `FINAL-CHECKLIST` G7 PASS |
| Page budget and end-game fill | 18 pages incl. appendix (`chat:1on1@2026-09-22T05:02`); team target "18 页不多不减" (`chat:group@2026-10-02T01:35`); 10-02 22:36 "还差一页多"; Senior A's priority list: merge/expand short results paragraphs, more methodology detail, background gaps (`…T22:44`); Senior B expands implications and threats (`chat:group@2026-10-03T09:25`; `msr:d0d4c03`, `msr:86199d6`, `msr:1ec1a0f`, `msr:13179f3`, `msr:b7a448b`) | as cited; screenshot `…202610022236_8.jpg` shows conclusion ending on p.17 of 19 | Final page count of the submitted PDF: **no evidence** (gap 10) |
| PC conflicts | Form kept warning; Senior B: every PC member related to author 1 must be marked; Senior A takes over (same-institution cases) and sets corresponding author | `chat:group@2026-10-03T17:28–17:56`, `…T18:32` | Done by Senior A, 2.5 h before deadline |
| Topic | "Software Analytics, Maintenance and Evolution"; SE4AI judged a stretch | `chat:group@2026-10-01T21:05` | Done |
| Data Availability | Unnumbered section after Conclusion with the anonymous URL; content overclaims (H1, H9) | `09-paper-snapshot/main.tex:169–171`; `FINAL-CHECKLIST` G8 | Present |
| AI-use policy | Classifier use described (model, temperature, prompt, demos, split, validation); gold construction appears AI-assisted but is described as purely human (B1) | `03-design.tex:104–112`; `FINAL-CHECKLIST` G9 | Open risk (§2.2) |

---

## 4. Records: where decisions lived, and how well that worked

| Record | Content | Worked? |
|---|---|---|
| Episodic comms READMEs (`04-comms/2026091…`, `…0920…`, `…0926…`) | Verbatim quotes + "what changed" + do/don't list; written by Student with an agent after the event | Good: the 09-10 README is a usable ADR (context, decision, rejected options, consequences). Coverage is episodic (gaps 2–3) |
| Group chat full export (`20260929-1007-wechat-group`) | 384 msgs with minute timestamps, media | Best primary source; only from 09-29 11:41 |
| Chat SUMMARY files with "Outdated / superseded" tables (`past-chat-group/SUMMARY.md`, `past-chat-jimmy/SUMMARY.md`) | Latest requirements override older ones | Useful pattern; date-level only; contains a role error (the 1:1 SUMMARY header calls the Student's name a "导师") |
| Cursor `MERGED-SUMMARY.md` ("later timestamp wins") | Agent-written requirement ledger, tags `[LATEST]/[OUTDATED]` | Useful; agent-written, verify |
| Research repo dated notes `docs/notes/YYYYMMDD-*.md` | Incidents (199 vs 582), plans, audits | Good; partly untracked later (`res:e66ba6d`) |
| Gold review `CHANGELOG.md` + `L###` lessons | Per-relabel log, KEEP reasons, prompt rules | Strong design; `prompt-lessons.jsonl` kept local-only |
| Prompt pack README version log | κ per version, rollbacks | Strong |
| Linear (DEM-xx) | Locks (model, gates, structure) referenced by id | IDs survive in code/TeX comments; ticket text lost from the archive |
| TeX comments | "Linear lock …", "Kappa printing rule …", `\hao{}`/`\todo{}` protocol | Close to the text; deleted with refactors (`msr:33e0af9`) |
| Paper-repo `checklist.md` (10-01) + v2 140-item checklist + `FINAL-CHECKLIST-2026-10-02.md` + `CHECKLIST-UPDATE-SUMMARY.md` | Author rules, decided items, open decisions, verification results | The final read-only check found real blockers (B1, B2) a day early; B2 was still acted on only after the senior's warning on 10-06; B1 has no evidence of resolution |
| `DECISION-HINTS.md` (U1–U5) | Open policy questions with repo facts | Good "open decision" register |
| Repo docs (`BUILD.md`) | SoT policy | **Stale**: never updated after the switch back to Overleaf |
| ADR folder / `STATUS.md` | — | **No evidence** in any repo |

What was lost (beyond `GAPS.md`): Linear ticket bodies; `prompt-lessons.jsonl`; `NUMBER-AUDIT-2026-10-02.md` and `DBLP-CHECK-2026-10-02.md`; the submitted PDF and its page count; who did what inside `Anonymous` Overleaf commits; the reason the κ bar moved from ≈0.7 to 0.65 beyond the overlay note; 09-27/28 group chat. `TIMELINE_DRAFT.md` errors found while verifying: it dates `hao's comments` to 10-01 (actual `msr:9809b8c` 09-29 and `msr:0f96193` 10-02).

---

## 5. Candidate supervisor lessons

Roles only. Confidence: high = direct primary evidence of both problem and outcome; med = primary evidence of the problem, outcome or generality partly inferred; low = single weak signal. Scope: G = general, SE = SE/MSR, P = project-specific. Target skill/checklist: **F2R** feedback-to-revision; **PSR-T / PSR-DB / PSR-A** pre-submission-reviewer threats / double-blind / artifact sub-checklists; **REC** records (`docs/STATUS.md` + ADR); **EXP** experiment workflow; **POL** paper-polish; **FIG** figure-designer.

| # | Rule | Evidence | Conf. | Scope | Target |
|---|---|---|---|---|---|
| 1 | Name one writable source of truth per phase in `STATUS.md`; announce and record every switch. | §1.2 (three flips; `BUILD.md` stale) | high | G | REC |
| 2 | A mirror into a co-edited document must fast-forward-check or abort; never copy-over into Overleaf. | `ol:a610d1d` → `ol:214cc0c`; `chat:group@2026-10-03T19:42` | high | G | REC |
| 3 | In the final 24 h, one channel and one editor at a time; pass the pen explicitly in chat. | 10-03 19:38–19:47 incident; merge storm §1.3(4) | high | G | PSR-A / REC |
| 4 | Upload a complete PDF well before the deadline, then replace it. | `chat:group@2026-10-03T19:45`, `…T19:59` outage | high | G | PSR (submission) |
| 5 | After any agent write to a shared doc, read the diffstat; large deletions mean a whole-file overwrite. | `ol:b2ad042` (−379), `ol:3ae9fd3` (−119) | high | G | REC / EXP |
| 6 | Checkpoint-commit before agent-driven destructive edits. | `ol:5eecfa5`, `msr:815305e`, `msr:3e7bab0` | med | G | REC |
| 7 | Mark comments the agent may resolve vs those only the student may resolve. | `msr:9809b8c` (`\hao{}` vs `\todo{}`) | med | G | F2R |
| 8 | Keep private chats, PDFs and notes out of the shared paper repo (gitignore from day one). | `msr:f1c7df8` → `msr:c8adb43`; `res:e66ba6d` | med | G | REC / PSR-DB |
| 9 | Verify every reference against DBLP (or the publisher) and keep the audit output. | `chat:group@2026-09-29T11:44`; `…10-03T19:18`; FINAL G4 | high | SE | PSR (citations) |
| 10 | Never change the template font, margins or local font size; check again after each late edit. | `chat:group@2026-10-01T09:20–09:23`; FINAL G3 regression | high | SE | PSR / POL |
| 11 | No appendix at SE venues with an all-in page limit; move tables to the replication package and point to it. | `chat:group@2026-10-01T08:47–08:56`, `…10-02T01:51`; `msr:464168f` | high | SE | POL / PSR-A |
| 12 | Grep the artifact (README, index.html, LICENSE, repo description, account name, metadata) for identity before refreshing the anonymous mirror. | FINAL B2/AT1–AT3; `chat:group@2026-10-06T05:09` | high | SE | PSR-DB |
| 13 | Prefer a complete README over a project web page in the anonymous artifact. | `chat:group@2026-10-06T05:09`, `…T09:44` | high | SE | PSR-DB |
| 14 | Link only the anonymous mirror in the PDF; never the author-named page or repo. | `chat:group@2026-10-02T00:45`; FINAL AT2 | high | SE | PSR-DB |
| 15 | The artifact must be non-empty on day one after the deadline; README directory guide can follow. | `chat:group@2026-10-02T06:36–06:37`, `…10-03T23:16` | med | SE | PSR-A |
| 16 | Move all analysis code used for printed numbers into the replication repo before claiming "recomputes every number". | `chat:group@2026-10-03T20:20–20:22`; FINAL H9 | high | SE | PSR-A |
| 17 | Every printed number needs a generating script and a recorded data/code SHA; diff script output against TeX. | RP-11 (42 cells exact match), RP-12 placeholder | high | SE | EXP / PSR-A |
| 18 | Every human-agreement number needs the raw independent label sets in the package; otherwise rewrite the method. | FINAL B1; `03-design.tex:97` | high | SE | PSR-T / EXP |
| 19 | Disclose AI assistance in gold construction, not only in the classifier. | FINAL G9, B1; venue AI-use row | high | SE | PSR-T |
| 20 | Freeze held-out gold before looking at model output; log and disclose any later gold correction and threshold choice. | `overlay-high14-review.md` | med | SE | EXP / PSR-T |
| 21 | Write the acceptance bar before the run and enforce it in the run script. | `vps-hk-llm-annotate.sh` (`GOLD_BAR_OK=1`) | med | SE | EXP |
| 22 | Version the prompt with per-version agreement, rollbacks and a one-line reason. | prompt pack README v1.4.x log | high | SE | EXP |
| 23 | Turn each annotation disagreement into a numbered rule (trap → prompt rule) and keep the rule file in the repo. | gold `CHANGELOG.md` L001–L025; `res:7e4a35c` (kept local) | med | SE | EXP / REC |
| 24 | Treat dashboards as views; the authoritative state is the file you can diff (DB export / state JSON). | `20260812-review-status-199-vs-582.md` | high | G | EXP |
| 25 | When a data gap cannot be closed by more crawling, move it to threats with its mechanism and stop chasing it. | `20260910-zhimin-d4d5-threats/README.md` | high | SE | PSR-T / F2R |
| 26 | Decide unknown-vs-out-of-scope coding by the label's purpose, and write that rule in the approach. | same README §1.4 | med | SE | EXP |
| 27 | Keep method (prompt, κ) separate from RQ numbering; an RQ needing only statistics gets a script, not an LLM. | `20260920-msritp-meeting/README.md` §1.3–1.4 | med | SE | EXP |
| 28 | Put copyable numbers and tables into the manuscript before drafting prose with a writing skill. | same README §1.5 | med | G | EXP / POL |
| 29 | Fill a short page budget by priority: expand thin results with explanation and examples, then methodology detail, then background, then implications and threats; never with appendix. | `chat:group@2026-10-02T22:44`, `…10-03T09:25`; `msr:d0d4c03` | med | SE | POL |
| 30 | Type the submission-form abstract as plain text with no macros or labels. | `chat:group@2026-10-03T18:36–18:43` | high | G | PSR (submission) |
| 31 | Do PC conflicts, topics and author metadata a day early; the senior with the institutional knowledge enters conflicts. | `chat:group@2026-10-01T21:05`, `…10-03T17:28–18:32` | med | SE | PSR (submission) |
| 32 | Re-fetch the venue call into a dated requirements file; do not trust a deadline heard in a meeting. | `20260920-msritp-meeting` "12 号" vs `fse-2027-requirements.md` | med | G | PSR / REC |
| 33 | Record each decision with rejected alternatives and a "do not" list, close to where it is used. | `20260910-…/README.md` §5; ADR folder: no evidence | med | G | REC (ADR) |
| 34 | Keep requirement summaries with an explicit "superseded by" table; latest wins. | `past-chat-group/SUMMARY.md`, `past-chat-jimmy/SUMMARY.md` | med | G | F2R / REC |
| 35 | Do not cite ticket ids alone; copy the decision text into the repo, since tracker content may be lost. | DEM-xx ids in code/TeX, bodies absent | med | G | REC |
| 36 | Use labels via macros so one edit propagates; then check spacing in the PDF. | `chat:group@2026-09-29T12:26`; Cursor `085dba30` (`\xspace` bug) | med | G | POL |
| 37 | Run a read-only pre-submission check one day early and act on its blockers immediately. | FINAL B2 predicted the 10-05/06 index.html issue | high | G | PSR |
| 38 | Use meeting transcripts, not tool-generated summaries, as the record. | `20260920-msritp-meeting/README.md` header | low | G | REC |
| 39 | Keep large raw data out of GitHub; use a data host and list it in a manifest. | `chat:group@2026-10-03T20:24`; `11-*/README.md` | med | SE | PSR-A / EXP |
| 40 | After the deadline, sync the final submitted version back into the repo and tag it. | §1.2 (paper repo ends at `msr:87bf139`, Overleaf continues `ol:ba3f1ee`); gap 10 | med | G | REC |
