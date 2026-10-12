# 04 — Verified timeline and reconstructed research process

Phase 2 evidence note. Archive: `~/Projects/supervisor-skills-msr-tpa` (HEAD `669b29a`). All paths below are relative to the archive root. Citation formats follow `03-archive-map.md` §4: `msr:<sha>` (paper repo), `ol:<sha>` (Overleaf git), `res:<sha>` (research repo), `chat:group@YYYY-MM-DDTHH:MM` (from `04-comms/20260929-1007-wechat-group/messages.jsonl`), `chat:group-raw@…` / `chat:1on1-raw@…` (timestamped raw exports under `04-comms/past-chat-group/raw/*/Chat History.txt` and `04-comms/past-chat-jimmy/raw/chat-history-merged.txt`).

Roles: **Student** (first author), **Senior A** (writing organization, desk-reject red lines), **Senior B** (methods figure, page budget, paper-repo and Overleaf owner, advisor relay), **Advisor (relayed)**. Sections 1 to 4 (verification) may show commit author strings, because they are needed to check authorship. Sections 5 to 7 use roles only.

Status labels: **VERIFIED** (primary source cited), **PARTIAL** (true with a correction, or only part is supported), **CONTRADICTED** (a primary source disagrees; both are shown), **NO EVIDENCE** (the cited source is outside this archive, or the archive is silent).

Time conventions. The tsvs give commit times converted to UTC+8. The raw patches keep each author's own offset: Senior A's commits are authored in UTC−4, so `msr:9809b8c` is 2026-09-28 23:35 −0400 = 09-29 11:35 +0800, and `msr:0f96193` is 10-01 19:45 −0400 = 10-02 07:45 +0800. Some TIMELINE_DRAFT dates differ from the tsv for this reason only. The research-repo tsv does not state its offset.

---

## 1. Headline resolutions

### 1.1 Submission deadline: 2026-10-03 19:59 China time (Fri 2 Oct AoE), then a reopening after a site outage. Not ~10-12.

| Evidence | What it shows |
|---|---|
| `10-requirements/venue/fse-2027-requirements.md` (Deadline row) | "Fri 2 Oct 2026, AoE … 3 Oct 19:59 in China". It is a model extraction made 2026-10-01 |
| `04-comms/20260929-1007-wechat-group/media/Weixin Image_202610031956_3.jpg` (screenshot of the submission site's edit page, shared 10-03 19:56) | "The submission deadline is Friday Oct 2, 2026, 11:59 PM AoE (Oct 3 7:59 PM your time)". The header reads "Submission deadline in 138 seconds", and the PDF upload is stamped "Oct 2, 2026, 11:56:38 PM AoE" (= 10-03 19:56:38 +0800). This is a primary source and agrees with the venue file |
| `chat:group@2026-10-03T19:45` Senior B | 「50就开始提交pdf了」, then 「等55再交一版」 |
| `chat:group@2026-10-03T19:55`–`19:56` | Senior B: 「提交」「赶紧」; Student: 「交了」 |
| `chat:group@2026-10-03T19:59` Senior A | 「估计崩了」「我登不上fse的系统了」 |
| `media/Weixin Image_202610032318_9.jpg` (posted by Senior A at 23:18) | Screenshot of the conference's social-media posts: the submission site is unavailable and the organizers "will reopen/extend the submission site" |
| `chat:group@2026-10-03T23:19` Senior B | 「感觉可以趁着再次开放微调一下的」 |
| `chat:group@2026-10-04T02:06` Senior A | 「还有18小时，可以小修小补一下」, which puts the reopened deadline at about 10-04 20:00 +0800. That is an inference from one message. The new deadline was never stated exactly |
| `chat:group@2026-10-04T08:46` Senior A; `chat:group@2026-10-04T18:04` Senior B | 「我修改了一下稿子，提交了一个新版本」 / 「我提交了」. Ambiguous: "提交" may mean an Overleaf edit or an upload to the submission site |

Verdict on `TIMELINE.md` "~2026-10-12 FSE 2027 投稿锚点": **CONTRADICTED**. Its only basis is the TIMELINE_DRAFT header ("群聊语境 deadline 约 10/12") and the 09-20 meeting note (「Deadline **12 号**」, `04-comms/20260920-msritp-meeting/README.md` §1.5). That note itself says the month and year were not in the transcript. No message in `messages.jsonl` mentions a 10-12 deadline. Note also that `chat:group@2026-10-03T23:16` (「大概deadline后两三天吧」) answers a question about some other deadline, apparently the replication package. It is not about the paper.

### 1.2 The paper the team submitted is not the git snapshot `87bf139`

- `msr:87bf139` (10-03 19:38, last paper-repo commit) is HEAD of `09-paper-snapshot/`. Its title is "What Breaks in Proof Assistants, and How Maintainers Fix It…" (`09-paper-snapshot/main.tex:116`).
- `ol:a610d1d` (10-03 19:38, author string `leo-lihao` = Senior A, made on Overleaf): changes the title to "Maintaining Proof Assistants: An Empirical Study of Reported Bugs and Resolution Patterns" (`07-overleaf-history/patches-overleaf/20261003-1938_a610d1d.patch`).
- `ol:214cc0c` (10-03 19:39, `github-actions[bot]`, "Sync GitHub main @ 87bf139"): one minute later it reverts the title and removes Overleaf-side text from related work, RQ2 and RQ3 (+9/−29; `patches-overleaf/20261003-1939_214cc0c.patch`).
- `chat:group@2026-10-03T19:41`–`19:42` Senior A: 「别用git了吧，感觉很多改动都没了」, 「页数越写越少」, 「我改了半天的东西都没了」. Then a rollback on Overleaf at 19:45–19:47.
- The submission-site screenshot at 19:56 already shows the "Maintaining Proof Assistants…" title.
- `ol:ba3f1ee` (10-04 13:16, Senior A on Overleaf, 14 files, +468/−453): restores the "Maintaining…" title and reworks every section and the study-workflow figure. `ol:1499336` and `ol:3410f5e` (10-04 13:28 and 13:31, Senior B) and `ol:5661971` (10-04 15:51, Student, empty diff) follow it.
- Consequence: **the final submitted text lives on the Overleaf line after 10-04, which the paper repo never received.** `09-paper-snapshot/` is the git state before the final Overleaf pass. `03-archive-map.md` §6 says "use only `main.tex` as truth" for the title. That rule is wrong for the submitted version; use `ol:ba3f1ee` instead. No final PDF or hash of the submission is in the archive (GAPS item 10 stands).

### 1.3 When the repositories were created

| Repo | First commit | Status |
|---|---|---|
| Research repo | `res:de95735` "Initial project snapshot", tsv time 2026-06-19 00:06 (offset not stated). TIMELINE_DRAFT §1 says 06-18 | **PARTIAL**: 06-18 holds only if the tsv time is UTC+8 and the claim uses UTC (that would be 06-18 16:06 UTC). The archive does not settle the offset |
| Overleaf project | `ol:48f5713`, authored 2026-08-01 23:11 +0800 by `Zhimin Zhao` (= Senior B), ACM sample template. The git bridge committed it on 08-14 | **VERIFIED** as an empty shell: `11-mining-github-issue-audit/tree/docs/notes/20260814-overleaf-paper-backup.md` says it "currently holds the ACM `acmart` / sigconf sample template, not the paper text" |
| First paper text on Overleaf | `ol:20a6d25` 08-14 13:29 (Student: "Add paper.tex skeleton … leave ACM templates untouched"); `ol:26ed99e` 08-17 | VERIFIED |
| Paper collaboration repo | `msr:5e73a46` "Initial Overleaf Import", 2026-09-26 19:37:05 +0800, author `Zhmin Zhao` (= Senior B). Link posted at `chat:group-raw@2026-09-26T19:43` (「overleaf的github：…」「大家注意查收邮箱」) | **VERIFIED** |
| Overleaf→GitHub automation | `msr:c93ef1f` 09-29 12:44 "Add Overleaf sync workflow…", fixed by `msr:c3d1e70` 12:57. First bot push `ol:b0123f2` at 13:34 | VERIFIED |

### 1.4 Peak activity (computed from the tsvs)

Paper repo (`07-overleaf-history/msr-tpa-commits.tsv`, 105 commits):

| 09-26 | 09-27 | 09-28 | 09-29 | 09-30 | 10-01 | 10-02 | 10-03 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 10 | **25** | 14 | 7 | 11 | **33** |

On 10-03 commits came in two waves, 08:00–11:59 (18 commits, mostly Senior B's "expand details" + Overleaf merges) and 17:00–19:59 (8 commits, the Student's abstract passes).

Overleaf git (`07-overleaf-history/overleaf-commits.tsv`, 252 commits; days with ≥4):

| 09-09 | 09-15 | 09-16 | 09-18 | 09-20 | **09-21** | **09-22** | 09-23 | 09-24 | 09-26 | 09-29 | 09-30 | 10-02 | 10-03 | 10-04 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 4 | 8 | 4 | 18 | **48** | **69** | 4 | 5 | 5 | 19 | 8 | 8 | 26 | 4 |

Research repo (`11-mining-github-issue-audit/research-repo-commits.tsv`, 71 commits): by month 06:2, 07:18, 08:16, 09:32, 10:3. The busiest days are 08-01 (9) and 09-07 (6). No commits fall between 09-25 and 10-10.

Group chat (`messages.jsonl`, 384 messages): 09-29 54, 09-30 13, 10-01 32, 10-02 84, **10-03 175**, 10-04 8, 10-05 1, 10-06 5, 10-07 12.

Verdict on `TIMELINE.md` "Peak: 2026-09-29 → 10-03": **PARTIAL**. It holds for the paper repo and the chat. The largest burst in the archive, however, is on Overleaf on **09-21/22** (117 commits): 74 of the 252 Overleaf commits carry the agent author string `Overleaf MCP`, and most of them fall on 09-20/21. That burst is the census-retarget plus writing-comment pass (detour D6). The timeline does not mention it.

### 1.5 The source of truth for the paper changed during submission week

- `chat:group-raw@2026-09-28T22:08`: Senior A asks whether Overleaf is the latest; Senior B says it is.
- `chat:group@2026-09-29T12:25` Senior A: 「目前规则是保证overleaf是最新的？还是git main是最新的？」. At `12:40` the Student answers 「我是保持 Git main最新」. This is the Student's own practice, acknowledged by Senior A (「了解」). It was never a group decision. The 09-29 Cursor summary (`04-comms/cursor-history-chat/MERGED-SUMMARY.md` §1) records "GitHub `main` is canonical" as an agent-session rule.
- `chat:group@2026-10-03T04:53` Senior A: 「都弄好了sync到overleaf吧，方便修改和协作」.
- `chat:group@2026-10-03T19:41` (after the overwrite) Senior A: 「别用git了吧」, and at `23:45`: 「现在用overleaf修改吧，方便合作」. The Student agrees at `23:55`.
- Verdict on PROCESS.md "Git `main` SoT + Overleaf sync": **CONTRADICTED for the end state**. Git main was the Student's working rule from 09-29 to 10-03. After the 19:39 overwrite the team moved explicitly to Overleaf as the source of truth.

### 1.6 Where the human-agreement number came from: no evidence in the archive

The final paper says two authors independently annotated all 582 gold issues with Cohen's κ = 0.74 (`09-paper-snapshot/sections/03-design.tex:97`, intro `:53`). In this archive:
- The research-repo notes record one main annotator plus a sparse second one: "`codex` 576 issues; `yitwah` 24; overlap 18 (not an IRR sample)" (`11-*/tree/docs/notes/20260813-rq1-rq3-answer-plan.md:18`, `20260814-paper-writing-frame.md:19`). The formal IRR item is still "open" (`20260901-xuezhang-gap-and-d5.md:15`).
- The 09-22 devil's-advocate critique lists the missing perspective "A second annotator. There is one gold file…" (`11-*/tree/docs/partner/zhimin-msr-tpa-paper/snapshot/notes/CRITIQUE-2026-09-22.md:59`).
- The sentence with κ = 0.74 first enters the paper repo in `msr:393f596` (09-28 00:10 +0800, author `zhimin-z`, message "add").
- `chat:1on1-raw@2026-09-28T20:16`: the Student asks whether the two-human κ was ever computed (「那个数据好像我们没比较？」). Senior B replies at `20:17`: 「我这边儿对了，没事儿」.
- The research-repo tsv has no commit for a second-annotator pass or a κ computation. The value appears in the research tree only in figure sources (`tree/docs/drawio/overview-variants/variants.yaml:16`).
- Status: **NO EVIDENCE IN ARCHIVE** for the annotation pass or the computation. The only support is a chat assurance from Senior B. Before the case study cites "two-author κ" as an example of good practice, check it against the research repo or ask the user.

---

## 2. TIMELINE.md: row-by-row verification

| TIMELINE.md claim | Status | Primary evidence / correction |
|---|---|---|
| 06-18 → 07-14 project start and sampling: freeze of seven repos, stratified sample of 582 | VERIFIED (start date PARTIAL, see §1.3) | `res:de95735` (06-19 00:06); `res:4c60e71` 07-13 21:47 "Add constrained stratified sampling methodology"; `res:2700d27` 07-14 18:55 "Switch annotation queue to 582 issue sample"; `11-*/tree/docs/msr4itp_constrained_stratified_sampling_allocation_20260713.md` (N = 23,671; run `seven-repo-582-20260714`, seed 42, line 202; supersedes the 700-issue queue, line 5) |
| 07-14 → 08-17 gold sample and annotation workbench; prompt locked | VERIFIED | `res:d3caaf2` 07-18 "Complete collaborative annotation workflow"; `res:43d9c10` 08-01 queue dashboard; `res:6bed599` 08-17 01:29 "Publish the locked LLM annotation prompt…" |
| 08-01 empty Overleaf shell | VERIFIED | `ol:48f5713` (template); `tree/docs/notes/20260814-overleaf-paper-backup.md` |
| 08-13 → 09-11 D4/D5 coverage wall → threats pivot | VERIFIED | `res:1549c50` 08-13 "…before PR-body backfill"; `res:7e707ad` 09-06 gap audit; `04-comms/20260910-zhimin-d4d5-threats/README.md` (screenshots 01–04 timed 09-10 22:19 to 09-11 00:24); `res:7998b24` 09-11 00:25 "Record advisor Threats decisions"; `res:8fe17c3` 09-11 22:35 "Record Li Hao's label-purpose rule" |
| 09-09 author block / corresponding author changed (Overleaf MCP) | VERIFIED | `ol:b2ad042`…`ol:0cab5cb` (7 commits, 13:58–14:39, author string `Overleaf MCP`), e.g. `ol:8bb3f44` "Mark … as corresponding author" |
| 09-16 gold D4/D5 unknown standards; placeholder restore incident | VERIFIED | `ol:7b0c955` 00:20 "Gold D4: issue-local evidence only"; `ol:3ae9fd3` 00:35 swaps 119 lines for the literal `PLACEHOLDER` (`patches-overleaf/20260916-0035_3ae9fd3.patch:139`); restored by `ol:6cca5e3`, `ol:1ba123a`, `ol:c128ade` within 2 minutes |
| 09-20 group meeting | VERIFIED | `04-comms/20260920-msritp-meeting/README.md` (22:29–23:07). Its outcome is visible in git the next day (`ol:8cf91a2` 09-21 15:51 "Retarget analysis plan: paper conclusions use freeze census N=23671") |
| 09-22 page limit 18+4, pruning, "proof assistants" term | VERIFIED | `chat:1on1-raw@2026-09-22T05:02` (Senior B pastes the 18-page rule; 「18页可是包括appendix的」); `@13:03` 「先换模版，然后theorem provers改成proof assistants」. Executed the same day: `ol:dade33e` 13:09 "Switch the census draft to the FSE 2027 acmsmall review class", `ol:30f5bf0` 13:32 "Use proof assistant for our own wording" |
| 09-26 paper repo "Initial Overleaf Import"; advisor glimpse | VERIFIED | `msr:5e73a46`; `chat:1on1-raw@2026-09-26T05:35` (Senior B relays the advisor's English notes verbatim; also `04-comms/20260926-jimmy-advisor-paper-glimpse/README.md` §2) |
| 09-27 → 29 overview figure four panels → one; methodology rewrite; senior comments | VERIFIED | `chat:group-raw@2026-09-27T15:55` Senior B 「不如变成一张图」「四个图来表示一张图的内容…」; `chat:group-raw@2026-09-28T00:15` Senior A 「这个图的风格太AI了」; `msr:9809b8c` 09-29 11:35 "hao's comments" (12 files, +356/−414) |
| 09-29 → 10-07 three-person revision week (384 msgs) | VERIFIED | `messages.jsonl` counts: 384; Student 170, Senior B 120, Senior A 94 |
| 10-01 → 03 checklist, study-workflow final, RQ polish, abstract | VERIFIED | `msr:0c0dae0` 10-01 00:41 "Add writing checklist for FSE 2027 submission" … `msr:87bf139`; study-workflow: `msr:fd283fd`, `msr:9ef4a07`, `msr:55e1878`, `msr:b5c0045`, `msr:4c70db0` |
| 10-04 late Overleaf updates; "⚠ no matching discussion in chat" | Commits VERIFIED; the "no chat" note is **CONTRADICTED** | `ol:ba3f1ee`, `ol:1499336`, `ol:3410f5e`, `ol:5661971` exist. Chat on 10-04: `02:06` 「还有18小时」, `08:46` 「我修改了一下稿子，提交了一个新版本」, `18:04` 「我提交了」. The ±2h cross-reference misses them because an `Update on Overleaf.` commit appears when the bridge is pulled and can bundle earlier edits |
| ~10-12 FSE 2027 submission anchor | **CONTRADICTED** | §1.1 |
| Commit density peak 09-29 → 10-03 | PARTIAL | §1.4 (Overleaf peak 09-21/22) |
| Bridge "Hao methodology comments → `9809b8c`, `0f96193`, `9ef4a07`" | VERIFIED | `0f96193` adds 11 `\hao{}`/`\todo{}` lines (e.g. 「figure and text are not synced」 in 03-design); `chat:group@2026-10-02T07:46` Senior A 「我留了点comment在main branch」; `9ef4a07` 11:31 "refine methods and their figure based on hao's comments"; `chat:group@2026-10-02T11:07` Senior B 「我修改了，目前是对应上的了」 |
| Bridge "DBLP / desk reject" | VERIFIED | `chat:group@2026-09-29T11:44` Senior A (DBLP; 「查处一个错的引用直接desk reject」) → `msr:8df40d5` 12:50 "Add DBLP citation rules…". Earlier: 21 `ol:` "Correct BibTeX for … from the verified … record" commits on 09-22 13:17–13:29 |
| Bridge "Git main is authoritative (group SUMMARY 09-29)" | PARTIAL / reversed | §1.5 |

---

## 3. TIMELINE_DRAFT §1–§9: key claims

| § | Claim | Status | Evidence / correction |
|---|---|---|---|
| §1 | Frozen window `seven-repo-20260712`, cutoff 2026-07-12T23:59:59Z, N = 23,671 | VERIFIED | `11-*/tree/README.md:38`; `tree/tasks/build_gold_review_batch.py:21`; allocation doc line 19 |
| §1 | A single proportion n ≈ 385 does not cover ecosystem floors (≥100 each) and library floors (≥50) | VERIFIED | allocation doc §"Why 385 Is Not Enough", lines 34–56, 70–85 |
| §1 | "Optimal" is banned as a slogan | VERIFIED | allocation doc line 15, line 184 |
| §1 | RQ1–RQ3 framework set by the 07-08 plan | PARTIAL | `11-*/tree/docs/Mining GitHub Issues in Theorem Prover Ecosystems - 2026-07-08.md` (RQ1 line 43, RQ2 47, RQ3 51). The document's own header says "May 2026"; `res:fba39cd` 07-08 "Update MSR4ITP schema and planning artifacts" matches the filename date |
| §1 | Fourteen-repo v4 taxonomy dropped in favour of seven repos / 582 | VERIFIED | `res:6cae113` 07-06 "Add v4 fourteen-repo taxonomy report" → `res:4c60e71`; 700-issue run kept as `superseded` (allocation doc line 202) |
| §2 | Live UI showed 199/383 while 582 were done; local SQLite + `research_state.json` made authoritative | VERIFIED | `11-*/tree/docs/notes/20260812-review-status-199-vs-582.md` (root cause: the production SQLite was never updated) |
| §2 | Annotators: `codex` 576, `yitwah` 24, overlap 18 | VERIFIED | `tree/docs/ui-annotation-codebook-zh.md:23`; `notes/20260813-rq1-rq3-answer-plan.md:18` |
| §2 | Reopen timeline is 0 in the whole corpus, so no reopen proxy | **PARTIAL / later corrected** | `notes/20260814-paper-writing-frame.md:856` (0 reopens at the time). But `res:300d3a6` 09-14 "Record gold-sample reopen events that the original crawl omitted", and `ol:f54f954` 09-22 "Put reopen rate … in the appendix". The zero was a crawl gap |
| §2 | Push main only to `origin` | VERIFIED | `res:a6672d7` 08-27; `11-*/remotes.txt` (two remotes) |
| §2 | Prompt v1.0 → … → v1.4.13 | VERIFIED (endpoints) | `res:11aa5d9` v1.1.0 (09-06), `res:25ecb0d` v1.3.0 (09-18), `res:ffbf63a` v1.4.13 (09-20) |
| §3 | 09-10 decision: coverage gap goes to threats; pivot to RQ2 | VERIFIED (via README transcription of screenshots) | `04-comms/20260910-zhimin-d4d5-threats/README.md` §1.2 (Senior B 22:37: 「就只能放到 threat of validity 里面吧」); §1.4 label-purpose rule (Senior A 00:24) |
| §3 | Cursor-Agent backfills on "09-05～06" | PARTIAL | The `Cursor Agent` commits are `res:56b9084`…`res:5f15595`, 09-07 01:48–02:31 |
| §3 | Rejected paths (time-window commit matching, guessing `fixed`/`local-patch`, a dedicated solution prompt, new taxonomy classes, GraphQL re-crawl as review) | VERIFIED for 1, 2, 3, 5; NO EVIDENCE for 4 | (1, 2) 09-10 README §5 "不做"; (3) 09-20 meeting README §1.3; (5) `tree/docs/notes/gold-review/README.md:20` (browser page opens required, no GraphQL); (4) "use `other`, don't add a math subclass" has no primary source in the archive |
| §3 | lean4#14576 post-freeze narrative; "Memory `memory/log/2026-09.md`" | NO EVIDENCE | memory files are not in the archive |
| §4 | 09-12 hard goal: 582/582 pages opened in browser, wall clock ~4h38m; CHANGELOG local-only | VERIFIED | `res:1dc5006` 09-12; `gold-review/README.md:24,28` ("4h 38m 46s"); `res:7e4a35c` 09-12 |
| §4 | DEM-53: 66 red + 59 yellow worked through, not "zero unknown" | VERIFIED | `gold-review/GOAL.md` (acceptance criterion 1) |
| §4 | 09-20 meeting: ~2,000 labelled → ~20k; RQ numbering fixed; write order numbers → skill → human edit | VERIFIED | meeting README §1 |
| §4 | Hamilton 2000 dropped on 09-24 | VERIFIED | `ol:e03c20a` 09-24 17:20 "Drop Hamilton 2000 due-diligence from Design and Implications" |
| §5.1 | Senior A's writing comments dated 09-22 | PARTIAL | The source cited (`memory/writing/…`) is not in the archive. `02-comments-hao/comments_hao.md` is undated. Edits matching it (term table, "motivate before mechanics", "lead results with the question", "leave exact counts in tables") appear as paired `ol:` commits on 09-22 16:47–16:52, and `ol:6247934` 21:28 says "Revise passages that still miss the writing comments", so the comments existed by 09-22 afternoon |
| §5.2 | Advisor glimpse 09-26 (relay) | VERIFIED | §2 row 09-26 |
| §5.3 | 09-27/28 Senior A comments `9809b8c` land | PARTIAL | 09-28 23:35 in the author's offset, 09-29 11:35 +0800 |
| §6 | 09-29: figure–text correspondence, DBLP, de-AI, merge table into figure; Overleaf vs git conflict | VERIFIED | `chat:group@2026-09-29T11:42–11:52` |
| §6 | 10-01: checklist; appendix → replication; default font (else desk reject); compact D1–D7 table pointing to package | VERIFIED | `chat:group@2026-10-01T00:58`, `08:47`/`08:56` (「放上去充页数=直接reject」), `09:19`, `09:20`/`09:23`, `10:09` |
| §6 | "10-01: Senior A commit `hao's comments`" | PARTIAL | `msr:0f96193` is 10-01 19:45 −0400 = 10-02 07:45 +0800 |
| §6 | "10-01: Student methodology/RQ overhaul; stop tracking `local-refs`" | PARTIAL | `msr:c8adb43` 10-01 22:07 (untrack) VERIFIED; the overhaul `msr:9c69675` is 10-02 02:16 |
| §6 | 10-02: anonymous mirror, page budget 18, "paper first, replication later", Senior B refines methods figure, Student merges B's figure | VERIFIED; merge date PARTIAL | `chat:group@2026-10-02T00:45`, `01:35` 「要保证 18 页不多不减」, `06:37`, `11:07`; merge is `msr:55e1878` 10-03 01:36 |
| §6 | 10-03 densest day; one page short → expand implications/threats; "pages keep shrinking"; site login problem | VERIFIED | 175 msgs; `chat:group@2026-10-03T09:25` Senior B 「页数还是差一页，我打算扩写一下implication和threats」 → `msr:d0d4c03` 09:58 "expand threats+implications"; `19:41`; `19:59` |
| §6 | 10-04/05 replication page published; DEM-295 | Page VERIFIED; DEM-295 NO EVIDENCE | `chat:group@2026-10-05T22:46`; Linear is not in the archive |
| §6 | 10-06 index.html risks double-blind → .gitignore | VERIFIED | `chat:group@2026-10-06T05:09` 「这个容易暴露双盲导致desk rejeck」; `09:44`; `11:57` |
| §6 | 10-07 another venue's "accident" screenshot; anonymous page rendering OK | VERIFIED | `chat:group@2026-10-07T07:42`, `11:56` |
| §6 | Title history ending at "Maintaining Proof Assistants…" "per DEM-295" | VERIFIED from git, not from DEM-295 | full chain in §4 row "title"; final title per `ol:a610d1d` / `ol:ba3f1ee` and the submission screenshot |
| §7 | Replication repo filled from 10-01; 10-05 DEM-295 done; 10-06 cleanup | PARTIAL | Chat confirms the 10-03 20:17–20:24 gap ("analysis code not all moved", 「数据没必要用github」→ figshare/S3) and the 10-06 cleanup. The replication repo itself is not in the archive (NO EVIDENCE for its commit dates) |
| §9A | Research repo pushes almost all by the Student / Cursor Agent | VERIFIED | 71 commits: `yitwah` 65, `Yue Yihua` 1, `Cursor Agent` 5 |
| §9A | origin/main stopped at 09-21 `b449e2c`, local ahead | NO EVIDENCE / PARTIAL | `b449e2c` is 09-22 03:13 in the tsv; there are no remote refs in the archive |
| §9B | Contributors: yitwah ≈56, zhimin-z ≈52, Leo-LiHao ≈2 | PARTIAL | Local tsv: `yitwah` 56; `zhimin-z` 25 + `Zhmin Zhao` 22 = 47 (the 22 are mostly Overleaf merges carrying anyone's edits); `Hao Li` 2. On Overleaf `leo-lihao` has 2 commits, but one (`ol:ba3f1ee`) is the largest late rewrite |
| §9C | `main` is ~67 commits ahead of `overleaf-main` | NO EVIDENCE | no branch refs in the archive |

---

## 4. PROCESS.md: decision log and detours

### Decision log

| PROCESS.md decision | Status | Evidence |
|---|---|---|
| Seven repos / 582 stratified, not a larger cohort / fourteen-repo taxonomy | VERIFIED | §3 rows §1 |
| Issue-local D4/D5 evidence instead of re-crawling to zero | VERIFIED | `ol:7b0c955` 09-16; 09-10 README |
| Gold used for validation only, not wired to RQ outputs; attributed to "Jimmy/Hao" | PARTIAL | The shift happened on Overleaf: `ol:b805c55` 09-20 "gold 582 is the quota contrast", `ol:1d20ee1` 09-21 "census, not gold", `ol:edafe5e` 09-21 "keep gold 582 as quota/kappa". Nothing in the archive attributes it to either senior |
| Single three-stage study-workflow, not four panels | VERIFIED | `chat:group-raw@2026-09-27T15:55` (Senior B), `chat:group-raw@2026-09-28T00:15` (Senior A, "too AI") |
| Text → figure → table (C-035) | PARTIAL | The verbatim C-035 quote is a user relay **not found** in the export (`04-comms/past-chat-jimmy/raw/user-supplied-relays.md`, USR-001). Closest real message: `chat:1on1-raw@2026-09-29T11:51` Senior B 「很多表格其实没必要单独出现的」 |
| DBLP-only bib | VERIFIED | §2 bridge row; plus `chat:group@2026-10-03T19:18` (Senior A runs an agent citation audit before submission) |
| Git `main` as SoT + Overleaf sync | CONTRADICTED (end state) | §1.5 |
| κ played down into related work / threats instead of IRR as the main selling point | PARTIAL / CONTRADICTED | `ol:ee75959` 09-22 (held-out κ table replaced), `ol:ac81b3a` 09-24 (κ dropped from the related-work gold-check sentence). But the final paper reports two-author κ = 0.74 in Design and classifier κ in Threats (`09-paper-snapshot/sections/03-design.tex:97,110`, `08-threats.tex:12,20`); see §1.6 |

### Detours

| PROCESS.md detour | Status | Evidence / correction |
|---|---|---|
| 1. VPS UI progress lie (199/383 vs 582) | VERIFIED | `notes/20260812-review-status-199-vs-582.md` |
| 2. Overleaf placeholder wipe 09-16 | VERIFIED, with a correction | It was an agent commit (`Overleaf MCP`, `ol:3ae9fd3`), restored by agent commits within 2 min |
| 3. Merge storms 10-02–10-03 | PARTIAL | They started 09-29: 43 `github-actions[bot]` syncs from 09-29 13:34 and 8 "Merge overleaf-…-into main" commits in the paper repo from 09-29 19:32. The climax is the 10-03 19:39 overwrite (§1.2). The fix the team actually adopted was "edit on Overleaf". PROCESS.md says "main is authoritative", which is the reverse |
| 4. Figures redrawn repeatedly (AI sketch → reference replica → preview) | VERIFIED | `05-figures-tables/sources/drawio/` iterations; `msr:748f1df` 09-28, `msr:fd283fd` 10-02, `msr:9ef4a07`, `msr:4c70db0` 10-03; `ol:ba3f1ee` 10-04 still edits `study-workflow.drawio` (371 lines) |
| 5. Formal IRR (~200 double-coded) stayed open → narrative shift | PARTIAL / unresolved | Open per `notes/20260901-xuezhang-gap-and-d5.md:15`; the final paper nonetheless claims a full two-author pass (§1.6) |

---

## 5. Reconstructed research process (roles only)

Each stage lists entry and exit criteria, artifacts, who did the work, and decisions with the alternatives that were rejected. "Agent" means coding/writing agents run by the Student (Cursor Agent, the Overleaf MCP, Codex/Claude).

### S1. Frame the questions and freeze the corpus (≈06-19 → 07-12)
- **Entry:** a research-proposal draft with three RQs (prevalence, difficulty, resolution strategy) and a candidate repository list.
- **Work:** crawl the issue trackers; compare taxonomies (v3, v4 on fourteen repos); narrow to seven repos in five ecosystems; fix a cutoff timestamp.
- **Artifacts:** proposal doc (`11-*/tree/docs/…2026-07-08.md`); snapshot commits `res:e9858f8`/`res:6b41bb1`/`res:f1bc4d9` (07-09); freeze id and cutoff (`tree/README.md:38`).
- **Who:** Student (implementation). The proposal is aligned with Senior B's lab, but meetings before 09-10 are not archived.
- **Decisions:** seven repos / five ecosystems rather than fourteen repos; one frozen snapshot rather than a moving corpus. The target population is the snapshot, not "all proof assistants".
- **Exit:** frozen N = 23,671 issues with a recorded cutoff.

### S2. Probability sample and codebook (07-13 → 07-14)
- **Entry:** frozen corpus, RQs, dimensions to code.
- **Work:** derive the sample size from estimand plus constraints; write the methodological decision record; draw with a recorded seed.
- **Artifacts:** `msr4itp_constrained_stratified_sampling_allocation_20260713.md`; run `seven-repo-582-20260714` (seed 42); `res:4c60e71`, `res:2700d27`.
- **Who:** Student.
- **Decisions:** constrained Neyman allocation with ecosystem floors (≥100) and library floors (≥50), N = 582. Rejected: SRS n = 385 (misses the floors) and the earlier 700 queue (kept as `superseded` for audit). Severity/Impact dimensions were cut later in favour of D1–D7.
- **Exit:** a reproducible sampling run with inclusion probabilities.

### S3. Annotation workbench and gold sample (07-14 → 08-17)
- **Entry:** sample drawn; codebook v0.3.
- **Work:** web annotation workbench; collaborative state export; LLM-assisted first pass plus human review; lock the annotation prompt.
- **Artifacts:** `res:d3caaf2`, `res:43d9c10`, `res:6bed599`; `collaboration/research_state.json`.
- **Who:** Student plus agents.
- **Decisions:** the local DB and exported state are authoritative, not the live UI (detour D1). The prompt is locked before scale-up.
- **Exit:** 582/582 submitted; prompt locked. Known debt: no designed second-annotator sample (overlap 18).

### S4. Evidence backfill and the coverage wall (08-13 → 09-11)
- **Entry:** RQ3 needs fix evidence (PR/commit) for closed issues.
- **Work:** PR-body backfill, mention / multi-source / bare-SHA backfill, gap audit, a 50-item adversarial review of D4-unknowns.
- **Artifacts:** `res:1549c50`, `res:a387f2c`, `res:7e707ad`, `res:56b9084`…`res:5f15595`, notes `20260901-*`, `20260906-pr-link-gap-audit.md`.
- **Who:** Student plus agents; decision by Senior B with mechanism and labeling rule from Senior A (09-10/11).
- **Decisions:** treat the residual gap as a validity threat and pivot effort to the RQ that does not need PRs (RQ2). Rejected: time-window commit matching as main method, guessing `fixed`/`local-patch`, more re-crawling. Labeling contract: what you label depends on the RQ's purpose (problem-only → `unknown`; problem + solution → out of scope).
- **Exit:** threats wording drafted; D4/D5 rules written (`ol:7b0c955` 09-16).

### S5. Gold review, scale-up, and locking the RQ denominators (09-12 → 09-21)
- **Entry:** gold rules fixed; prompt near final.
- **Work:** open every gold issue page in a browser and record it; work the red/yellow residuals; ship prompt v1.4.13; group meeting; label the whole corpus.
- **Artifacts:** `gold-review/{GOAL,README,CHANGELOG}.md`; `res:1dc5006`, `res:ffbf63a`, `res:44b01cb` (partner bundle); `ol:8cf91a2` and the 09-21 census commits.
- **Who:** Student plus agents; Senior B at the 09-20 meeting.
- **Decisions:** "done" means every residual processed, not zero unknowns. RQ numbering is frozen: RQ2 is a statistics script with no LLM; RQ3 reuses the seven-dimension labels with no second prompt. The paper reports on the full corpus (machine-labelled) with gold as validation. Rejected: answering the RQs on the 2,000-issue intermediate sample (`ol:b805c55` → `ol:8cf91a2` → `ol:e03c20a`).
- **Exit:** corpus labelled; analysis plan retargeted to N = 23,671.

### S6. First full draft by agents on Overleaf (09-14 → 09-25)
- **Entry:** tables/figures/numbers available. The meeting's write order: put numbers into the manuscript, run a paper-writing skill, then edit by hand.
- **Work:** agent-driven drafting on Overleaf (74 `Overleaf MCP` commits); switch to the venue template; split into section files; verify every BibTeX entry; apply the senior's writing comments one commit per rule.
- **Artifacts:** `ol:dade33e`, `ol:4e96421`, 21 "Correct BibTeX…" commits, the 09-22 16:47–23:59 comment-response commits, the DA critique (`CRITIQUE-2026-09-22.md`).
- **Who:** Student plus agents; comments from Senior A; page and terminology rules from Senior B (09-22).
- **Decisions:** "proof assistant" as the only term (rejected "theorem prover"/"interactive"); why-before-how; counts in tables, patterns in prose; internal codenames removed.
- **Exit:** a complete draft on the venue template.

### S7. External readability check (09-26)
- **Entry:** a draft a senior outsider can skim.
- **Work:** the Advisor (relayed) reads for a few minutes and returns questions on jargon, codebook provenance, an overlong §3.1, a missing ecosystem, a cross-domain baseline, and overall implications.
- **Artifacts:** `04-comms/20260926-jimmy-advisor-paper-glimpse/README.md`.
- **Who:** Advisor via Senior B.
- **Exit:** list of reader-facing fixes (no new analysis demanded).

### S8. Collaborative revision in the paper repo (09-26 → 10-02)
- **Entry:** Senior B imports the Overleaf project into a shared GitHub repo (`msr:5e73a46`).
- **Work:** Senior B cleans the repo and rewrites framing; Senior A leaves inline `\hao{}`/`\todo{}` comment drops (`msr:9809b8c`, `msr:0f96193`) under a stated protocol; the Student merges, redraws figures, builds a checklist from chat history (`msr:0c0dae0`), and revises methods/RQs (`msr:9c69675`).
- **Who:** all three. Senior A reviews in their evening, which is the Student's morning.
- **Decisions:** one study-workflow figure whose boxes map 1:1 to methodology subsections (rejected: four panels, decorative AI styling). DBLP-verified references. No appendix (rejected: an appendix of label definitions, which Senior B had asked for on 09-28 and Senior A rejected on 10-01 as page-padding); a compact label table plus definitions in the replication package. Default venue fonts. Anonymous mirror instead of a personal project page.
- **Exit:** figure–text correspondence confirmed by Senior B (`chat:group@2026-10-02T11:07`).

### S9. Page-budget and submission sprint (10-02 22:00 → 10-03 19:56)
- **Entry:** content complete but more than one page short of 18 (`chat:group@2026-10-02T22:36`).
- **Work:** Senior A sets priorities: expand short results paragraphs with explanation and examples, more methodology detail, missing background (`22:44`). Senior B expands threats and implications (`msr:d0d4c03`…`msr:b7a448b`). The Student rewrites the abstract repeatedly. Senior A handles PC conflicts and the corresponding author on the submission site and runs an agent citation audit. Senior B gives an abstract template (`19:18`: background → gap → study → 1–2 findings → recommendation).
- **Decisions:** abstract names the five ecosystems but not the repos, and uses plain text with no LaTeX macros (`18:27`–`18:43`). Upload a safe PDF before the deadline and keep revising.
- **Failure:** pushes to git triggered the GitHub→Overleaf action and overwrote Senior A's Overleaf edits at 19:39 (§1.2).
- **Exit:** PDF uploaded 10-03 19:56 (2.5 min before the deadline).

### S10. Post-deadline window and replication hardening (10-03 20:00 → 10-07)
- **Entry:** the site went down at the deadline; organizers reopened it.
- **Work:** Overleaf becomes the source of truth; Senior A rewrites on 10-04 (`ol:ba3f1ee`); Senior B makes small edits; re-uploads during the reopened window. The Student moves all analysis code into the replication repo (big data to an external store, not GitHub) and removes `index.html` and other author-revealing material.
- **Decisions:** README-only anonymous package (rejected: a rendered project page). The repo must not be empty on the day after the deadline (`chat:group@2026-10-03T23:16`).
- **Exit:** no evidence of the final submitted PDF or a confirmation record.

---

## 6. Detours and failed paths (verified), with what was learned

| # | Detour | Evidence | Lesson |
|---|---|---|---|
| D1 | The live annotation UI under-reported progress (199/383 vs 582) because the server DB was never refreshed | `notes/20260812-review-status-199-vs-582.md` | Name one authoritative store for research state; a dashboard is a view, not the record |
| D2 | Trying to recover fix evidence for every closed issue (time windows, mentions, multi-source backfill) | `res:7e707ad`, `res:b77e017`, 09-10 README §4 (≈14,062/18,091 closed issues without closing PR) | When a measurement ceiling is structural, write it as a threat and move effort to RQs that don't depend on it. Decide labeling by the RQ's purpose |
| D3 | An agent replaced 119 lines of the codebook/sampling sections with `PLACEHOLDER` on Overleaf | `ol:3ae9fd3` → `ol:6cca5e3`/`1ba123a`/`c128ade` | Agents editing the shared manuscript need diffs reviewed before sync. Small commits made the restore trivial |
| D4 | A writing-skill pass degraded the RQ1 draft; 7 identical agent commits, then a manual restore | `ol:ededfb8`…`ol:c8ef96a` (09-21 18:19–18:26, "remarks cleaned to 8 codebook notes") → `ol:aea22c2` 18:30 "Restore … from pre-skill complete RQ1" (+126/−500) | Snapshot before running a rewrite skill; compare content, not only style |
| D5 | Answering RQs on the 2,000-issue intermediate sample, with internal codenames in the prose | `ol:b805c55` 09-20 21:33 → meeting 22:29 → `ol:8cf91a2` 09-21 15:51 → `ol:e03c20a` 09-24; advisor relay 09-26 ("who's 'Hamilton 2000'?") | Fix the reporting population before writing; internal codenames must never reach the manuscript |
| D6 | Reopen data assumed absent (0 events) and a proxy dropped | `notes/20260814-paper-writing-frame.md:856` vs `res:300d3a6` 09-14 | Treat "zero" in mined data as a possible crawl gap until checked against the source |
| D7 | Overview drawn as four AI-styled panels | `chat:group-raw@2026-09-27T15:55`, `@2026-09-28T00:15`; `05-figures-tables/sources/drawio/` | One figure whose numbered boxes equal the methodology subsections; draft with AI, finish by hand |
| D8 | Appendix of label definitions to defend the codebook | `chat:1on1-raw@2026-09-28T16:43` (asked for) vs `chat:group@2026-10-01T08:47`/`08:56` (removed as padding) | In page-limited SE venues, put definitions in the replication package and keep a compact table in the paper |
| D9 | After removing the appendix the paper was more than a page short of 18 | `chat:group@2026-10-02T22:36`; `msr:d0d4c03` | Cutting and filling were done in the last 24 h. Check the page budget when cutting, not after |
| D10 | Two sync channels (Overleaf→GitHub merges by the owner's account, GitHub→Overleaf by a CI action) with people editing in both places in the final hour | §1.2; `msr:c93ef1f`; `chat:group@2026-10-03T18:43` (Student: 「我们去 Overleaf 上面改吧」, then pushed to git at 18:52, 19:24, 19:38) | Declare one editing surface for the last 24 h and switch off the other direction's automation |
| D11 | Private reference material tracked on main and synced into the shared Overleaf | `msr:f1c7df8` 10-01 00:51 (tracks `local-refs`, including another paper's template) → `ol:8e0551e` 08:45 → `msr:c8adb43` 22:07 untrack → `ol:5ac0aa5` 10-03 removes it | Keep author-only materials out of the manuscript repo; anything there reaches every collaborator surface |
| D12 | Analysis code written during writing was not in the replication repo at the deadline | `chat:group@2026-10-03T20:20`–`20:24` | Analysis scripts added while revising must land in the replication package on the same day |
| D13 | A reliability number entered the paper without a computation record in the research repo | §1.6 | Every reported agreement statistic needs a script and data path that a co-author can rerun |

---

## 7. Process-tip candidates

One line each, then citation and confidence (High = several primary sources agree; Med = one primary source or an inference; Low = secondary or relayed).

| # | Tip | Citation | Confidence |
|---|---|---|---|
| T1 | Freeze the corpus with a recorded cutoff and id; never ingest post-freeze items into the analysis | `tree/README.md:38`; 09-10 README §4 | High |
| T2 | Derive the sample size from estimand + floors + cost, record seed and superseded runs, and never call it "optimal" without the objective | allocation doc lines 15, 56, 184, 202 | High |
| T3 | Keep one authoritative store for annotation state; dashboards are views | `notes/20260812-review-status-199-vs-582.md` | High |
| T4 | When the evidence gap is structural, move it to threats and refocus on the RQ that does not depend on it | 09-10 README §1.2 | High |
| T5 | Choose how to label missing evidence by the purpose of each RQ, not by a global rule | 09-10 README §1.4 | High |
| T6 | "Done" for gold review means every residual worked with a reason, not zero unknowns | `gold-review/GOAL.md` criterion 1 | High |
| T7 | Fix RQ numbering and the reporting population at one meeting and write them down that night | 09-20 README §1.3; `ol:8cf91a2` | Med |
| T8 | Before a writing skill or agent rewrites the manuscript, snapshot; after, diff for lost content | `ol:aea22c2`; `ol:3ae9fd3` | High |
| T9 | One manuscript editing surface at a time; in the final 24 h, disable the opposite sync direction | §1.2, §1.5 | High |
| T10 | Announce source-of-truth switches in the group and confirm the other side is current before editing | `chat:group@2026-10-03T18:27`–`18:28`; `19:41` | High |
| T11 | Upload a complete PDF well before the deadline, then iterate | `chat:group@2026-10-03T19:45`, `19:59` | High |
| T12 | Know the deadline in the venue's timezone and your own; quote the submission system, not memory | screenshot `…202610031956_3.jpg`; §1.1 | High |
| T13 | Verify every reference against DBLP and run a citation audit before submission | `chat:group@2026-09-29T11:44`; `msr:8df40d5`; `chat:group@2026-10-03T19:18` | High |
| T14 | Use the venue's default template and fonts and keep the page budget exact; formatting violations are desk rejects | `chat:group@2026-10-01T09:20`/`09:23`; `chat:group@2026-10-02T01:35` | High |
| T15 | No appendix as page filler; a compact label table in the paper, full definitions in the replication package | `chat:group@2026-10-01T08:56`, `10:09`; `@2026-10-02T00:32` | High |
| T16 | Each methodology figure box gets a same-named subsection, in order | `chat:group@2026-09-29T11:42`; `@2026-10-02T22:26` | High |
| T17 | One integrated workflow figure, drafted with AI and finished by hand; plain palette | `chat:group-raw@2026-09-27T15:55`; `@2026-09-28T00:15`; `chat:group@2026-10-02T23:19` | High |
| T18 | Lock a term table early and never switch names | `comments_hao.md` §1; `ol:4d393bd` 09-22 | High |
| T19 | Give the draft to an outside senior for a few-minute read and fix whatever they can't parse | advisor glimpse README §2 | Med |
| T20 | Inline review protocol: senior comments as one macro, student actions as another that agents may not resolve | `msr:9809b8c` (`main.tex`) | Med |
| T21 | Abstract shape: background, gap, study, 1–2 findings, recommendation, one sentence each, no macros | `chat:group@2026-10-03T19:18`, `18:36`–`18:43` | Med |
| T22 | Use an anonymous mirror with a complete README, no rendered index page or personal URLs | `chat:group@2026-10-02T00:45`; `@2026-10-06T05:09` | High |
| T23 | The replication repo must not be empty after the deadline; move all analysis code and keep big data off GitHub | `chat:group@2026-10-03T20:22`–`20:24`, `23:16` | High |
| T24 | Every reported reliability number must point to a rerunnable script and its input | §1.6 | Med (derived from a gap, not a stated team rule) |
| T25 | Keep author-only materials (chat exports, other papers) out of the manuscript repo | `msr:f1c7df8` → `msr:c8adb43` | Med |
| T26 | Treat a mined "zero" as a possible crawl gap | `res:300d3a6` | Med |
| T27 | When cutting content, recount pages at the same time; plan where to expand | `chat:group@2026-10-02T22:36`, `22:44` | Med |

---

## 8. Remaining "no evidence" items relevant to this note

- Meetings and chats before 09-10, and on 09-27/28 apart from the group export through 09-29 12:43. The 06–08 work is visible only in research-repo commits and notes.
- Linear tickets (DEM-14/21/48/53/57/295) beyond what `gold-review/GOAL.md` quotes.
- Replication-repo history and the anonymous mirror contents.
- The final uploaded PDF, its page count, and any submission confirmation.
- The computation behind two-author κ = 0.74 (§1.6).
- Research-repo remote state (origin vs local), and the exact reopened deadline (inferred ≈ 10-04 20:00 +0800 from one message).
