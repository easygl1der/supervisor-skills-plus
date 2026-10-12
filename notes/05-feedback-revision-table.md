# 05 — Feedback-to-revision table (comment → change → commit → status)

Archive: `~/Projects/supervisor-skills-msr-tpa` (all paths below are relative to its root). Times are Asia/Shanghai (UTC+8); git `AuthorDate` values in other offsets were converted. Citation formats follow `notes/03-archive-map.md` §4: `msr:<sha7>` = `07-overleaf-history/patches-msr-tpa/<YYYYMMDD-HHMM>_<sha7>.patch`; `ol:<sha7>` = `07-overleaf-history/patches-overleaf/<YYYYMMDD-HHMM>_<sha7>.patch`; `chat:group@…` = `04-comms/20260929-1007-wechat-group/messages.jsonl`; `chat:group-raw@…` = `04-comms/past-chat-group/raw/*/Chat History.txt` (09-22 → 09-29 12:43, minute timestamps); `chat:1on1-raw@…` = `04-comms/past-chat-jimmy/raw/chat-history-merged.txt` (09-22 → 09-29, minute timestamps).

This note completes the stopped draft `notes/partial/05-feedback-revision-table.PARTIAL.md`. Its §1.1, §1.2, §1.6, §2.1, §2.2 and §2.6 rows were kept after a spot re-check against patches (see "Re-check of the partial draft" below); §1.3–1.5, §2.3–2.5 and §3–§6 are new.

## Method

- Every **verified** status was checked by reading the `.tex` (or `.bib`) hunks of the cited patch, not the commit subject, not the Chinese auto-summaries, not `06-revision/REVISION-SUMMARY.md`. Inline `\hao{}`/`\todo{}` markers and float captions/labels were traced with a script that lists every added/removed line matching a pattern across all 105 `patches-msr-tpa` and 252 `patches-overleaf`. Final-state checks use `09-paper-snapshot/sections/*.tex`.
- **Snapshot caveat (new finding).** `09-paper-snapshot/main.tex` is not byte-identical to `msr:87bf139`: its abstract ("We find that nearly one in three issues is not a bug, and that…") appears in no committed version except as commented-out lines added by `ol:ba3f1ee` (10-04). The snapshot is therefore a local working-tree state close to `87bf139`. Section-level final checks below were not contradicted by any patch, but treat "final" as "last git-side state", not the submitted PDF (consistent with notes/04 §1.2).
- Authorship comes from `msr-tpa-commits.tsv` / `overleaf-commits.tsv`. "Updates from Overleaf" commits in the paper repo carry B's account but bundle anyone's Overleaf edits; where the matching `ol:` commit has a resolved author, that author is given.
- A comment counts as **addressed-verified** when the requested change is visible in a patch and survives to the final git state (or was deliberately replaced by a later, explicitly requested change). **Partially** = some of the request landed. **Superseded** = overtaken by a later decision or rewrite (typically another reviewer's). **Not addressed** = the archive shows the opposite or no change where change was possible. **Reverted** = landed then undone (only transient reverts were found; they are flagged in the rows). **No evidence** = archive is silent (image-only referent, artefact outside the archive, or no attributable change).
- Latency = comment time → first commit containing the requested change (marker removal or closure given separately where different). Only computable when the comment has a minute-level timestamp.

Roles: **A** = Senior co-author A; **B** = Senior co-author B; **S** = Student (first author); **ADV** = Advisor (relayed by B); **AG** = agent-generated. Quotes are kept short and in the original language; personal names inside quotes are replaced by `[A]`, `[B]`, `[S]`.

### Re-check of the partial draft

Sampled 9 rows against patches; 8 confirmed, 1 corrected:
- Confirmed: FB-A-01 (`ol:5ecaf3f` adds "Rejected aliases"); FB-A-02 (final: 0 "theorem prover"); FB-A-10 (`ol:01fcd0f` l.28 inserts the comment file's sentence verbatim, `comments_hao.md:162`); FB-A-INL-05 (`msr:94e651f` `size = 1.95` → `3.8`); FB-A-INL-13 (`msr:b7a448b` l.98 deletes the marked sentence); FB-AG-05 (`msr:3e7bab0` removes 7 lines with "six times", final 0); FB-AG agent-file line refs (`adams-skill-revision-comments.md:36…213`); REVISION-SUMMARY "After" text occurs only inside the `REVISION-SUMMARY.md` hunks of `msr:815305e` / `ol:bfa20aa`, never in a `.tex` hunk.
- **Corrected:** FB-A-INL-01 said the shared related-work file is "not in the archive". It is: `04-comms/past-chat-group/raw/54068433-…/Images, videos, and files in chat history/related_word.md` (posted by A at `chat:group-raw@2026-09-29T11:30`), a PC-member citation scan with HIGH 9 rows (5 distinct papers) and MEDIUM 169 rows. All 5 distinct HIGH papers are cited in the final Related Work (2 already present at import, 3 added in `msr:3d34425` and `msr:5d2c165`). Row updated below.
- Added: markers that the partial attributed to "Updates from Overleaf, author `?`" (`msr:4f8b488`, `msr:1f68c99`) were deleted on Overleaf by B (`ol:376ed9d` 10-03 09:21 and `ol:3fd6209` 09:22, author resolved to B).

---

## 1. Comment inventory

Columns: ID · quote/paraphrase (original language, <25 words) · source · type · size (S/M/L) · needs-author-decision.

Types: structure / framing / terminology / claim-evidence / figure / formatting-venue / citation / anonymity / scope / page-budget; plus `process` for collaboration requests that do not change paper text (listed, excluded from the statistics).

### 1.1 Senior co-author A — written comments (`02-comments-hao/comments_hao.md`)

Delivery: the file's first commit is `ol:2698705` (2026-09-26 12:43, S's account). A burst of S commits on 2026-09-22 16:47–23:59 paraphrases its headings and one inserts its suggested sentence verbatim (`ol:01fcd0f`), so the comments were in hand by 2026-09-22 16:47; exact delivery time: no evidence. `comments.md` (2026-09-28) consolidates the same 11 items (lines 10–19) and adds none.

| ID | Quote / paraphrase | Source | Type | Size | Decision? |
|---|---|---|---|---|---|
| FB-A-01 | "Create a Table of Terms we are using in the draft, and follow the terms, DO NOT switch terms" | `comments_hao.md:1` | terminology | M | no |
| FB-A-02 | "Proof assistant is a better name vs. Theorem Prover, fix the draft throughout" | `:3` | terminology | S | no |
| FB-A-03 | check an arXiv paper "to learn how SE people introduce rocq/proof assistant" | `:4` | citation / framing | M | yes: whether to cite it |
| FB-A-04 | §2.1 "The draft needs more context before methodology details" | `:8–29` | structure / framing | L | no |
| FB-A-05 | §2.2 "Motivate 'why' before 'how' … This is the biggest writing problem." | `:33–50` | framing | L | no |
| FB-A-06 | §2.3 "REMOVE/REWRITE all the places mention study plan" | `:54–75` | framing / scope | M | yes: how much preregistration to keep |
| FB-A-07 | §2.4 "AVOID laundry list style writing, DO NOT repeat the numbers in the table" | `:79–100` | claim-evidence / structure | M | no |
| FB-A-08 | §2.5 results need question → answer → implication structure | `:104–120` | structure | L | no |
| FB-A-09 | §2.6 "motivate the paper in SE terms … Motivate from Maintenance and Evolution" | `:124–143` | framing | L | no |
| FB-A-10 | §2.7 "Some section openings are too procedural … Open with the substantive point" | `:147–164` | structure | M | no |
| FB-A-11 | §2.8 "The draft is too defensive … Be precise once, then move on." | `:168–184` | framing | M | no |

### 1.2 Senior co-author A — inline `\hao{}` / `\todo{}` macros in the paper repo

Protocol defined by A in `msr:9809b8c` (`main.tex`, patch l.65–74): `\hao{...}` = "notes; resolved by [A] or the agent"; `\todo{...}` = "action items left for the student to fix; the agent must not resolve them"; notes render in colour while `\shownotestrue`.

Drop 1 = `msr:9809b8c` "hao's comments", 2026-09-29 11:35 (author A, pushed straight to `main`: "没，直接main了，没看到有branch保护", `chat:group-raw@2026-09-29T11:41`). Drop 2 = `msr:0f96193`, 2026-10-02 07:45 (author A), announced at `chat:group@2026-10-02T07:46` 「我留了点comment在main branch」.

| ID | Macro | Quote (verbatim, trimmed) | Location / patch line | Type | Size | Decision? |
|---|---|---|---|---|---|---|
| FB-A-INL-01 | `\todo` | "include more papers, see the file I shared" | `02-related-work.tex`; `msr:9809b8c` l.226 | citation | M | yes: which of 169 MEDIUM papers to cite (file is in archive, see Re-check) |
| FB-A-INL-02 | `\todo` | "the overview figure and the content in methodology is not synced, check previous papers …" | `03-design.tex` subsection title; l.311 | figure / structure | L | no |
| FB-A-INL-03 | `\todo` | "put this information in the overview figure and plot the link btw the data to each RQ, remove this table" | funnel-table caption; l.470 | figure / structure | M | no |
| FB-A-INL-04 | `\todo` | "anything we wanna say about this figure? any new findings? … if not, remove the figure" | RQ1 alt figure; l.659 | figure / claim-evidence | M | yes: keep or drop |
| FB-A-INL-05 | `\todo` | "if we wanna keep this figure, increase the font size in figure b" | alt-figure caption; l.670 | figure / formatting | S | no |
| FB-A-INL-06 | `\hao` | "figure and text are not synced, e.g., you mention `Build issue payloads' in the figure, where is the text?" | study-workflow caption; `msr:0f96193` l.40 | figure / structure | L | no (re-raise of INL-02) |
| FB-A-INL-07 | `\todo` | "do not call it snapshot, call it dataset" | `03-design.tex` subsection title; l.49 | terminology | S | no |
| FB-A-INL-08 | `\todo` | "fix AI smells, e.g., `Corpus'" | subsection title; l.58 | terminology | S | no |
| FB-A-INL-09 | `\todo` | "which figure/table support the claim? show it in the first sentence. Follow the slides …" | `04-rq1.tex` first finding; l.70 | structure / claim-evidence | M | no |
| FB-A-INL-10 | `\todo` | "First sentence: highlight the finding in bold – Second sentence refers to a figure or table …" | `04-rq1.tex`; l.72–74 | structure | M | no (but contradicts INL-09 on where the figure reference goes) |
| FB-A-INL-11 | `\todo` | "readers are here to read our results, talk our results first" | `04-rq1.tex` reporter paragraph; l.84 | structure | S | no |
| FB-A-INL-12 | `\todo` | "avoid subsubsection, remove it, just follow the slides" | `04-rq1.tex`; l.92 | structure | S | no |
| FB-A-INL-13 | `\todo` | "space filling, remove this:" | `05-rq2.tex` opener; l.106 | structure / page-budget | S | no |
| FB-A-INL-14 | `\todo` | "It is a table! why label it as a figure?! Please format it as a normal table" | `05-rq2.tex`; l.108 | figure / formatting-venue | M | no |
| FB-A-INL-15 | `\todo` | "merge this paragraph with the next paragraph, if we have nothing to talk, talk nothing" | `06-rq3.tex`; l.121 | structure | S | no |
| FB-A-INL-16 | `\todo` | "too long, please break it down" | `08-threats.tex` Internal Validity; l.151 | structure | M | no |

Also in drop 2 (an action, not a comment): A switched `\shownotesfalse` back to `\shownotestrue` (`msr:0f96193` l.25–27) 66 min after S had turned the notes off in `msr:5776349` (10-02 06:39, l.305–306), at a time when INL-01 had been commented out unresolved (`msr:59f15be` 06:02).

Pre-protocol `%%` notes (author: no evidence; committed by S's account in `msr:643836a`, 2026-09-29 00:54, l.3045 and l.3064):

| ID | Quote | Type | Size |
|---|---|---|---|
| FB-UNK-INL-01 | "%% Note in above description that [S] indead checked the prompt consistency by randomly pick half of the gold sample …" | claim-evidence | S |
| FB-UNK-INL-02 | "%% The following paragraph should be compressed. ([S])" | structure | S |

### 1.3 Senior co-author A — group-chat revision requests

Sources: `chat:group-raw@…` (export through 09-29 12:43) and `chat:group@…` (`messages.jsonl`, from 09-29 11:41; the two overlap 11:41–12:43). Only messages that ask for a change to the paper, figures or artefacts are listed; acknowledgements and logistics are omitted.

| ID | Time | Quote (original, trimmed) | Source | Type | Size | Decision? |
|---|---|---|---|---|---|---|
| FB-A-CH-01 | 09-28 00:15–00:16 | 「这个图的风格太AI了，现在reviewer看到AI生成的东西就反感」「内容可以，呈现的时候用师弟自己的风格吧」 | `chat:group-raw@2026-09-28T00:15` | figure | M | no |
| FB-A-CH-02 | 09-28 00:19–00:42 | 「这些小字可以去掉（AI的风格）」; 「关键信息只需要保留和数据相关的，比如dataset有几个repo，几个issue」 | `chat:group-raw@2026-09-28T00:19`, `…T00:42` | figure | S | no |
| FB-A-CH-03 | 09-29 11:30 | 「我们需要加一些软工的related work，看一下HIGH和MEDIUM」 + file `related_word.md` | `chat:group-raw@2026-09-29T11:30` | citation | M | yes (which MEDIUM papers) — same request as INL-01 |
| FB-A-CH-04 | 09-29 11:40–11:42 | 「methodology需要大修一下 … 主要问题是图文不对应」「图上这些在methodology的文字都能找到对应」 | `chat:group-raw@2026-09-29T11:40`; `chat:group@2026-09-29T11:42` | structure / figure | L | no — same as INL-02 |
| FB-A-CH-05 | 09-29 11:44 | 「引用的paper都用dblp查一下 … 用dblp上最新的bib … 查处一个错的引用直接desk reject」 | `chat:group@2026-09-29T11:44` | citation / formatting-venue | M | no |
| FB-A-CH-06 | 09-29 11:46 | 「目前还是AI味道太重，建议先整理好文字部分，再手工画出来」 | `chat:group@2026-09-29T11:46` | figure / structure | M | no |
| FB-A-CH-07 | 09-29 11:47 | 「这个表可以拿掉，把信息放到methodology图里」 | `chat:group@2026-09-29T11:47` | figure / structure | M | no — same as INL-03 |
| FB-A-CH-08 | 09-29 12:26 | 「标签这种最好让agent用宏，后续修改就改宏」 | `chat:group@2026-09-29T12:26` | terminology | S | no |
| FB-A-CH-09 | 09-29 12:30 | 「让agent看看最相关的几篇paper … 有没有可以直接套用的好的分析方法，增加/增强我们目前rq的分析」 | `chat:group@2026-09-29T12:30` | claim-evidence / scope | L | yes (which analyses to add) |
| FB-A-CH-10 | 10-01 08:47–08:56 | 「怎么appendix还在？reviewer不会看的」「有用的可以挪进正文，没用的挪去replication package」「放上去充页数=直接reject」 | `chat:group@2026-10-01T08:47`, `…T08:48`, `…T08:56` | page-budget / formatting-venue | M | yes (conflicts with FB-B-07) |
| FB-A-CH-11 | 10-01 09:10 | 「还有这个也是？」「这个好像没改好？」 (referent is a screenshot) | `chat:group@2026-10-01T09:10` | unknown | S | no |
| FB-A-CH-12 | 10-01 09:23 | 「这个算违反policy，会desk reject」 (endorsing FB-B-16, default font) | `chat:group@2026-10-01T09:23` | formatting-venue | S | no |
| FB-A-CH-13 | 10-01 10:09 | 「把表格浓缩成只有D1-D7+label（最多半页纸），然后指向replication package说definition在package里」 | `chat:group@2026-10-01T10:09` | structure / page-budget | M | no (proposed compromise) |
| FB-A-CH-14 | 10-02 01:51 | 「不要appendix，软工的人不喜欢」 | `chat:group@2026-10-02T01:51` | page-budget / formatting-venue | S | no (restatement of CH-10) |
| FB-A-CH-15 | 10-02 06:36–06:37 | 「放link到replication package就行」「第一优先级是把paper弄到能提交」 | `chat:group@2026-10-02T06:36` | anonymity / scope | S | no |
| FB-A-CH-16 | 10-02 07:29 | (to B) 「methodology你有时间修吗？图和文字需要对应」 | `chat:group@2026-10-02T07:29` | figure / structure | L | no — delegation of INL-06 to B |
| FB-A-CH-17 | 10-02 21:49 | 「这个需要去一下ai味」 (referent: screenshot; B asked 「具体在哪里？」) | `chat:group@2026-10-02T21:49` | unknown (style) | S | no |
| FB-A-CH-18 | 10-02 22:26 | 「1-删除没有信息量的部分 / 2-图片依然和文字对不上 … B. 5 6 7 找不到对应文字 … C. 3.4 … 8 和 9 在哪？」 + a marked-up PDF (22:22) | `chat:group@2026-10-02T22:26`; `media/e5a18131…261002_102130.pdf` | figure / structure | L | no |
| FB-A-CH-19 | 10-02 22:28, 23:19 | 「图片的底色和配色都简洁化，现在太AI了」「那就黑白灰蓝，或者draw.io的经典色」 | `chat:group@2026-10-02T22:28`, `…T23:19` | figure | S | no (B disputed) |
| FB-A-CH-20 | 10-02 22:44 | 「results里那些很短的段落，可以删掉/合并/扩充（加解释和例子）/ methodology 可以写详细来 / background…」 | `chat:group@2026-10-02T22:44` | page-budget / claim-evidence | L | no |
| FB-A-CH-21 | 10-03 11:32 | 「感觉不用拆，b的字体弄大一些」「要拆的话，把a转90度」 | `chat:group@2026-10-03T11:32` | figure | S | no — re-raise of INL-05 |
| FB-A-CH-22 | 10-03 18:27 | 「5 个生态的名字就好，仓库名字不用」 (abstract) | `chat:group@2026-10-03T18:27` | framing | S | no |
| FB-A-CH-23 | 10-03 18:37 | 「文本叙述吧，安全一些」 (no macros in the abstract) | `chat:group@2026-10-03T18:37` | formatting-venue | S | no |
| FB-A-CH-24 | 10-03 19:41, 23:45 | 「别用git了吧，感觉很多改动都没了」「现在用overleaf修改吧，方便合作」 | `chat:group@2026-10-03T19:41`, `…T23:45` | process | — | — |
| FB-A-CH-25 | 10-06 05:09 | 「不用index html，readme完整就好」「这个容易暴露双盲导致desk rejeck」 | `chat:group@2026-10-06T05:09` | anonymity | S | no |

The PDF attached to CH-18 contains a vector drawing (a 1341×604 figure with markup, producer "Samsung Electronics") and no PDF annotation objects; its marks are not machine-extractable here (no renderer available). The 22:26 text message carries the actionable content.

### 1.4 Senior co-author B — 1:1 chat, PDF annotations, group chat

Sources: `chat:1on1-raw@…` (the raw export behind `04-comms/past-chat-jimmy/SUMMARY.md` / `REFS.md`), `04-comms/past-chat-jimmy/raw/jimmy-main-pdf-comments/page_NNN.md` (13 annotations on `main.pdf`, sent 09-28 16:43; REFS ids P-01…P-13), `chat:group-raw@…`, `chat:group@…`. REFS/SUMMARY requirement ids are given where they exist. Data-quality note: `past-chat-jimmy/SUMMARY.md` header says the advisor comments were "导师 [S's name] / Hao 评语经 Jimmy 转发", conflating the Student, A and the relayed advisor; C-020 is the relayed advisor list (§1.5), not A.

Chat and other requests:

| ID | Time | Quote (original, trimmed) | Source | Type | Size | Decision? |
|---|---|---|---|---|---|---|
| FB-B-01 | 09-22 05:00 | 「很多东西写的过于细致 … 代入reviewer的视角 … 不太会感兴趣，那么暂时就去comment掉」 | `chat:1on1-raw@2026-09-22T05:00` | scope / page-budget | L | yes (what to cut) |
| FB-B-02 | 09-22 05:02 | 「18页可是包括appendix的」 (pasted venue rule) | `chat:1on1-raw@2026-09-22T05:02`; REFS `[ref: page-limit]` | page-budget | M | no |
| FB-B-03 | 09-22 13:03 | 「先换模版，然后theorem provers改成proof assistants」 | `chat:1on1-raw@2026-09-22T13:03`; REFS `labels-terminology` | formatting-venue / terminology | S | no (overlaps FB-A-02) |
| FB-B-04 | 09-26 12:39–12:44 | overview-figure markup images F-002…F-004 (gold "validation-only", RQ shorthand) | `chat:1on1-raw@2026-09-26T12:39`; REFS `study-overview` | figure | M | no |
| FB-B-05 | 09-27 15:55 | 「感觉有点儿分散，不如变成一张图」「四个图来表示一张图的内容，其实没有一张图更有说服力」 | `chat:group-raw@2026-09-27T15:55` | figure | L | no |
| FB-B-06 | 09-27 22:43–22:44 | (asked "exactly like yours?") 「对」「试着用pptx画图skill或者drawio画图skill」 | `chat:1on1-raw@2026-09-27T22:43` | figure | M | no |
| FB-B-07 | 09-28 16:43 | 「我们需要一个类似这样的大appendix table来解释每一个label」 (borrow a prior paper's Tables 5–6) | `chat:1on1-raw@2026-09-28T16:43`; REFS `appendix-labels` | structure / page-budget | L | yes (conflicts with FB-A-CH-10) |
| FB-B-08 | 09-28 23:14 | 「每个subsection/paragraph之间logic上需要有递进关系」「确保没有ai flavor」 | `chat:1on1-raw@2026-09-28T23:14`; REFS `de-ai-prose` | structure / framing | L | no |
| FB-B-09 | 09-28 23:15 | (`%TODO` in TeX) 「这些也是需要做的」「比如加一个intro的背景图」 | `chat:1on1-raw@2026-09-28T23:15`; REFS `intro-figure` | figure / framing | M | no |
| FB-B-10 | 09-28 23:23–23:50 | 「第一幅图已经涵盖了后两幅图的全部信息」…「不妨将图b+c做成一个heat map」 | `chat:1on1-raw@2026-09-28T23:23`, `…T23:50`; REFS `rq1-figures` | figure | M | no |
| FB-B-11 | 09-29 00:24 | 「需要去掉所有的分号和破折号」「就像AI写的嘛」 | `chat:1on1-raw@2026-09-29T00:24`; C-029 / CF-23@v2 | formatting (style) | M | no |
| FB-B-12 | 09-29 11:51 | 「表格你尽量先照着我给你的建议来调整」「很多表格其实没必要单独出现的」 | `chat:1on1-raw@2026-09-29T11:51` | structure / figure | M | no (re-raise of P-01…P-13) |
| FB-B-13 | (relay, no time) | text → figure → table; key table numbers bold or coloured (C-035) | `04-comms/past-chat-jimmy/raw/user-supplied-relays.md` USR-001 | figure / structure | M | no — **verbatim not found in the export** |
| FB-B-14 | 10-01 08:54 | 「label 的 definition，这个没有的话怕被 critique」 | `chat:group@2026-10-01T08:54` | claim-evidence | M | yes (A vs B) |
| FB-B-15 | 10-01 09:19 | 「把appendix table放到replication package里面，并在readme里提一下」 | `chat:group@2026-10-01T09:19` | page-budget / scope | S | no |
| FB-B-16 | 10-01 09:20 | 「文章字体恢复到fse默认的样子」 | `chat:group@2026-10-01T09:20` | formatting-venue | S | no |
| FB-B-17 | 10-01 09:26 | 「在文章中也要提label的定义，但是指向replication package」 | `chat:group@2026-10-01T09:26` | claim-evidence | S | no |
| FB-B-18 | 10-02 00:32 | 「label的definition table放到replication package里，然后创造一个小table只放cateogy-label mapping table」 | `chat:group@2026-10-02T00:32` | structure | S | no |
| FB-B-19 | 10-02 00:45 | 「那个会暴露名字，你要在 [anonymous mirror] 上申请一个匿名url」 | `chat:group@2026-10-02T00:45` | anonymity | S | no |
| FB-B-20 | 10-02 01:35 | 「要保证 18 页不多不减」 | `chat:group@2026-10-02T01:35` | page-budget | M | no |
| FB-B-21 | 10-03 18:36–18:43 | 「abstract里不应该出现label的」「编译不出来的」「latex文本【无宏】」 | `chat:group@2026-10-03T18:36`, `…T18:40`, `…T18:43` | formatting-venue | S | no |
| FB-B-22 | 10-03 19:16–19:18 | 「abstract读起来比较奇怪」「先交代一句背景，然后说明research gap … 1-2条最重要的findings，我们最后推荐什么」 | `chat:group@2026-10-03T19:18` | structure (abstract) | M | no |
| FB-B-23 | 10-03 19:40 | 「你这个abstract每个句子太长了」「我给你几个案例，你试着模仿一下」 | `chat:group@2026-10-03T19:40` | structure (abstract) | S | no |
| FB-B-24 | 10-03 20:21–20:24 | 「都要挪」「上传到figshare吧 或者s3」「数据没必要用github」 | `chat:group@2026-10-03T20:22`, `…T20:24` | scope (replication) | M | no |
| FB-B-25 | 10-06 09:44 | 「先把 index 放到.gitignore」 | `chat:group@2026-10-06T09:44` | anonymity | S | no |
| FB-B-26 | 09-27 10:15; 09-29 11:10; 10-03 19:39 | 「确保overleaf的一直是最新版哈」「需要手动同步下」 | `chat:1on1-raw@2026-09-27T10:15`, `…09-29T11:10`; `chat:group@2026-10-03T19:39` | process | — | — |

PDF annotations on `main.pdf` (delivered `chat:1on1-raw@2026-09-28T16:43`; B had offered this channel at `…09-26T14:26` 「我直接给你pdf上给评论，或者直接改，然后你用codex去处理一下」 and sent a `parse-pdf-comments` skill):

| ID | REFS id | Quote (trimmed) | Float annotated | Type | Size |
|---|---|---|---|---|---|
| FB-B-P01 | P-01 | 「变成表格或者text，节约篇幅」 | Fig. "Issue counts … grouped by ecosystem" (`fig:repo-by-family`) | figure / page-budget | S |
| FB-B-P02 | P-02 | 「没有理由只有这几个label是大写的 … 我推荐全部小写」 | D1 labels in uppercase | terminology | S |
| FB-B-P03 | P-03 | 「请修改所有label，确保全小写哈！」 | all labels | terminology | M |
| FB-B-P04 | P-04 | 「这个其实算是RQ1的finding了，move it into RQ1 finding section instead」 | Table 1 issue-type counts (`tab:rq1-types`) | structure | M |
| FB-B-P05 | P-05 | 「把这些表格放到一个超级大表格里，或者appendix里」 | Tables 2–3 bug categories | structure / page-budget | M |
| FB-B-P06 | P-06 | "to be deleted" | Table 4 median TTC by category with Q1/Q3 | figure / page-budget | S |
| FB-B-P07 | P-07 | 「不如画boxplot或者干脆简化到其他table里，如何？」 | Table 4 | figure | S |
| FB-B-P08 | P-08 | 「更适合融合进已有的table里，或者干脆文字，图的篇幅太大」 | Fig. 4 median TTC by ecosystem (`fig:ttr-eco`) | figure / page-budget | S |
| FB-B-P09 | P-09 | 「这个感觉也有点不太值得一个table，看看能不能融合一下」 | strategy table (`tab:rq3-strategies`) | figure / page-budget | S |
| FB-B-P10 | P-10 | 「这个不太值得一个figure，融合到其他table里，或者干脆text吧」 | Fig. 5 local-patch share | figure / page-budget | S |
| FB-B-P11 | P-11 | 「不值得一个table，变成text就好 … 两句话完事儿，省篇幅」 | Table 6 gold-sample allocation (`tab:gold-allocation`) | figure / page-budget | S |
| FB-B-P12 | P-12 | 「我们真的关心最长和最短吗？… 论文信息不是越多越好」 | Table 8 longest/shortest category | scope / claim-evidence | S |
| FB-B-P13 | P-13 | 「融合到其他table里吧，节约篇幅」 | Table 7 TTC for 3 categories × ecosystem (`tab:rq2-by-family`) | figure / page-budget | S |

### 1.5 Advisor (relayed)

Relayed by B in the 1:1 chat at `chat:1on1-raw@2026-09-26T05:35` (English, verbatim), archived as `04-comms/20260926-jimmy-advisor-paper-glimpse/README.md` §2 (SUMMARY id C-020). B added at 12:00 that it was read on 「之前那版 overleaf」, i.e. an older version than S's latest.

| ID | Quote (verbatim, trimmed) | Type | Size | Decision? |
|---|---|---|---|---|
| FB-ADV-01 | "very hard to read (what is a 'freeze census battery' … who's 'Hamilton 2000'?)" | terminology / framing | L | no |
| FB-ADV-02 | "where do the different Dx taxonomies come from? your own? existing work? AI-generated?" | claim-evidence | M | no |
| FB-ADV-03 | "most of section 3.1 seems overkill, it just says to study the typical 400-ish cases manually" | structure / scope | M | yes (what to keep) |
| FB-ADV-04 | "how much of an issue is the absence of Isabelle in the study?" | scope (validity) | S | no |
| FB-ADV-05 | "is there a baseline from a different domain to compare the findings to" | claim-evidence / framing | L | yes (which baseline) |
| FB-ADV-06 | "are the differences between the different assistants' results good, bad, expected, ...?" | claim-evidence | M | no |
| FB-ADV-07 | "what are the overall findings/implications?" | framing | M | no |

### 1.6 Agent-generated comments

`02-comments-hao/adams-skill-revision-comments.md`. Header: "Produced: 2026-09-28. Twelve independent Opus 5.5 subagents, one issue each" and "Status: comments only. No TeX edits." (lines 3–5). **Agent output, not a human comment.**

| ID | File ID / priority | Paraphrase | Source line | Type | Size | Decision? |
|---|---|---|---|---|---|---|
| FB-AG-01 | C12 [P0] | gold overlay rewrites held-out gold toward the model; disclose dual coding | `:36` | claim-evidence | L | yes: author facts (`[AUTHOR]`) |
| FB-AG-02 | C1 [P1] | RQ3 written as maintainer behaviour although strategy κ is below the 0.65 bar | `:65` | claim-evidence | M | no |
| FB-AG-03 | C2 [P1] | time-to-close called "repair effort / difficulty" | `:85` | terminology / claim-evidence | M | no |
| FB-AG-04 | C3 [P1] | soundness "four days" headline without denominator | `:101` | claim-evidence | S | no |
| FB-AG-05 | C7 [P1] | pooled headlines and "six times"; "Drop 'six times'" | `:113` | claim-evidence | S | no |
| FB-AG-06 | C5 [P1] | analysis funnel and residue belong in Results | `:125` | structure | M | yes (conflicts with FB-A-INL-03) |
| FB-AG-07 | C4 [P1] | put per-dimension held-out κ in the paper | `:151` | claim-evidence | S | no |
| FB-AG-08 | C8 [P1] | Implications state an unmeasured causal mechanism ("This happens since…") | `:169` | claim-evidence | M | no |
| FB-AG-09 | C6 [P2] | terms vs `A-terms.tex`: "most severe bugs", "layers above the kernel", "how severe they look" | `:179` | terminology | S | no |
| FB-AG-10 | C9 [P2] | residual `other` is a Results arm, not "a limit of the codebook" | `:191` | structure | S | no |
| FB-AG-11 | C11 [P2] | "no prior work" repeated; keep the earlier title retired | `:201` | framing | M | yes: title |
| FB-AG-12 | C10 [P2] | Related Work lacks a time-to-close / closed≠fixed cluster; "Do not invent keys" | `:213` | citation | M | yes: bibliography |
| FB-AG-13 | (change report) | `06-revision/REVISION-SUMMARY.md`: claims all 11 written comments "✅ Addressed" in the design section, with before/after LaTeX | `REVISION-SUMMARY.md:363–390` | (claim of resolution) | L | — |

---

## 2. Resolution table

### 2.1 Senior A written comments (`comments_hao.md`)

Responses landed in the Overleaf "census draft" line (S's account), mostly one commit per comment heading on 2026-09-22. The paper repo was re-imported from Overleaf (`msr:5e73a46`, 09-26), and A re-applied several rules himself in `msr:9809b8c`. Latency not computable (delivery time unknown).

| ID | Change made | Commit(s) + patch | Status |
|---|---|---|---|
| FB-A-01 | Locked-terms table with "Rejected aliases (do not use in our prose): theorem prover, interactive theorem prover, ITP"; later moved out of the intro; survives as internal `sections/A-terms.tex` (not compiled into final `main.tex`) | `ol:5ecaf3f` (09-22 16:47; subject "Lock a term table…"); `ol:2193c6b`; `ol:b8bc34d` | verified (as an authoring artifact, not a paper table) |
| FB-A-02 | "Theorem Prover(s)" → "Proof Assistant(s)" in titles, prose, keywords; final: 0 occurrences | `ol:30f5bf0` (09-22 13:32); `ol:5ecaf3f`; `ol:efe7cb4`; `ol:f1addde` | verified. Note: `ol:30f5bf0` came 29 min after B's identical chat request (FB-B-03), so the trigger may be B's message rather than the file |
| FB-A-03 | The arXiv paper is not in final `refs.bib`; no commit references it | — | no evidence |
| FB-A-04 | Abstract/intro now open with what the tools are, cost of regressions, trackers as maintenance record, risk of naive mining | `ol:55ea198`, `ol:0b63ad2` (09-22 16:47–48); `ol:805bf08` | verified |
| FB-A-05 | Design passages rewritten motivation-first (e.g. "Defect statistics are meaningless if the tracker mix is unknown, so every issue receives an *issue type* before any defect field.") | `ol:6247934` (09-22 21:28; subject "Revise passages that still miss the writing comments.") | verified (sampled passages) |
| FB-A-06 | "study plan" sentences removed; `ol:01fcd0f` still added "pre-registered family signatures" in a finding head. Final: 0 hits for "study plan", "preregist", "the plan predicted" | `ol:55ea198`; `ol:01fcd0f`; `ol:4d393bd`/`ol:5ecaf3f` | verified (final); partial on 09-22 |
| FB-A-07 | Exact counts moved out of prose; detail counts to appendix | `ol:0842e26`, `ol:b28f788` (16:50–52); `ol:6af100c` | partial (final RQ2 prose still lists several medians; numbers trimmed and restored repeatedly, notes/partial/06a) |
| FB-A-08 | Results lead with question and finding; A rewrote intro RQs as question → why → finding (`msr:9809b8c` l.128–138) | `ol:01fcd0f`, `ol:de73385`; `msr:9809b8c` | superseded by A's finding template (INL-09/10) |
| FB-A-09 | Abstract opener rewritten almost line-for-line from the §2.6 bullets | `ol:55ea198` (09-22 16:47) | verified (later abstracts rewritten again) |
| FB-A-10 | Suggested opener inserted verbatim; "The approach is a count …" removed (Example E4) | `ol:01fcd0f` (16:49) | verified (sentence later rewritten; not in final) |
| FB-A-11 | "and nothing more" removed; "we do not read that decision as evidence" never found in any `.tex` hunk | `ol:5ecaf3f` | partial |

### 2.2 Senior A inline macros

"Closed" = marker deleted (not merely commented out).

| ID | Change made | Commit(s) | Marker closed by | Latency (first change / closed) | Status |
|---|---|---|---|---|---|
| FB-A-INL-01 | S appended a progress note *inside* the `\todo` (156 papers screened; "Manuscript text not yet updated—awaiting author decision on which papers to cite"); a sentence with three new cites (Zhang_2019, Bringolf_2022, plus one more) added in `msr:3d34425`; B added Zhang_2023 in `msr:5d2c165` (subject "fix warning messages"). All 5 distinct HIGH papers of the shared file are cited in the final RW (Luan_2025 and Lincroft_2024 were present at import). MEDIUM list (169 rows) not systematically covered. S commented the marker out (`msr:59f15be`, 10-02 06:02) | `msr:84b9197` (09-29 15:56); `msr:3d34425` (22:17); `msr:5d2c165` (09-30 02:54); `msr:59f15be`; `msr:b7a448b` (B, 10-03 11:30, deletes) | B | 10h42m / 3d23h55m | partial (HIGH tier verified; MEDIUM unresolved author decision) |
| FB-A-INL-02 | Methods restructured into subsections mirroring the figure phases; caption gained phase text. Marker removed in an S-account commit titled "cursor-safety: checkpoint before destructive delete" (an agent safety checkpoint). Re-raised by A as INL-06 | `msr:815305e` (09-29 18:19) | S account (likely agent session; inference) | 6h44m | superseded → re-raised (INL-06) |
| FB-A-INL-03 | `tab:analysis-funnel` deleted; dropout counts moved into the workflow caption; figure later redrawn by B. Same request in chat (FB-A-CH-07) | `msr:815305e`; figure `msr:9ef4a07`, `msr:fdc9ca6`, `msr:b5c0045` | S account (same checkpoint) | 6h44m | verified |
| FB-A-INL-04 | S removed the alt figure (16:14), reinstated it 5 h later (`fig:rq1-alternative`); in the final paper the alternative *replaced* the original overview figure ("Superseded by fig:rq1-alternative", final `04-rq1.tex:66`) and every RQ1 finding cites it | `msr:7c705c9` (09-29 16:14); `msr:b3dafcd` (21:14); `msr:47221f7` (09-30 20:15) | S (`7c705c9`) | 4h39m | superseded (resolved by swapping primary and alternative) |
| FB-A-INL-05 | Marker deleted with the figure in `7c705c9` while the font was unchanged; re-raised in chat (FB-A-CH-21); heatmap label size 1.95 → 3.8 | `msr:94e651f` (10-03 12:04) | S (before the fix) | 4d0h29m (32 min after re-raise) | verified (late; marker closed before the fix) |
| FB-A-INL-06 | B rewrote the methods opener and caption, deleted the "Build issue payloads" step from the drawio, redrew the figure, then rewrote §3 as "Phase 1 … Step 1: … Step 2: …" so each subsection is one figure step; S added "(Done: …)" inside the `\hao` | `msr:9ef4a07` (B, 10-02 11:31); `msr:405bba7` (S, 23:34); `msr:fdc9ca6` (B, 10-03 01:24); `msr:b5c0045` (B, 03:48) | B (`b5c0045`) | 3h46m / 20h03m | verified |
| FB-A-INL-07 | "Issue Snapshot and Data Cleaning" → "Issue Collection"; "frozen snapshot" → "collect … this copy" (Example E1). B dropped the marker in the same commit; S re-inserted it with a Done note listing remaining replacements; B deleted it again | `msr:9ef4a07` (B); `msr:405bba7` (S) | B (`9ef4a07`, again `b5c0045`) | 3h46m | verified (final compiled sections: 0 "snapshot") |
| FB-A-INL-08 | "Full-Corpus Labeling and Analysis" → "Issue Labeling and Analysis"; "full corpus" removed from caption. The phrase had been introduced by the S-account agent commit `815305e` | `msr:9ef4a07` (B) | B | 3h46m | verified (final: 0 "corpus") |
| FB-A-INL-09 | First findings rewritten to cite figures ("The issue-type counts in Figure~… show that …"); S commented the marker out with "[Partly addressed: … The remaining findings still need review.]" | `msr:ee351a3` (10-03 14:31); `msr:ac172bd` (18:37) | never closed (commented out by S; still in final source `04-rq1.tex:110`) | 30h46m | partial |
| FB-A-INL-10 | Same pass; findings keep a bold first sentence; marker commented out | `msr:ee351a3`, `msr:ac172bd` | never closed (`04-rq1.tex:112`) | 30h46m | partial |
| FB-A-INL-11 | Paragraph opens with own numbers; prior-work comparison moved to last clause | `msr:405bba7` (S) | B on Overleaf (`ol:3fd6209` 10-03 09:22 → `msr:1f68c99`) | 15h49m / 25h38m | verified |
| FB-A-INL-12 | `\subsubsection{…}` removed; content became two RQ1 findings | `msr:405bba7` | B on Overleaf (`ol:376ed9d` 09:21 → `msr:4f8b488`) | 15h49m / 25h36m | verified |
| FB-A-INL-13 | Whole sentence deleted (by B) | `msr:b7a448b` (10-03 11:30) | B | 27h45m | verified |
| FB-A-INL-14 | `figure*` with a minipage tabular → standalone `\begin{table}` `tab:rq2-medians` (Example E2); strategy chart moved to RQ3 | `msr:405bba7`; `msr:e0ea09b` (Done note updated) | B on Overleaf (`ol:376ed9d`) | 15h49m | verified |
| FB-A-INL-15 | RQ3 lead paragraph merged into the next | `msr:e0ea09b` (10-03 01:30) | B on Overleaf (`ol:376ed9d`) | 17h45m | verified |
| FB-A-INL-16 | Internal Validity shortened; model threats moved to a new `\subsection{Reliability}`; B later folded Reliability back while expanding threats for page budget (`msr:d0d4c03`, 10-03 09:58; chat 09:25) | `msr:e0ea09b`; `msr:d0d4c03` | B on Overleaf (`ol:376ed9d`) | 17h45m | verified, then partly reverted by B (page budget) |
| FB-UNK-INL-01 | Phase-2 description now states the tuning/held-out split checked "by computing Cohen's κ against the gold labels" | `msr:9809b8c` (A) | A | ≤11h | verified (resolved by A himself) |
| FB-UNK-INL-02 | Classification methodology rewritten as three short "Step" paragraphs | `msr:9809b8c` (A) | A | ≤11h | verified (resolved by A himself) |

### 2.3 Senior A chat requests

| ID | Change made | Commit(s) | Latency | Status |
|---|---|---|---|---|
| FB-A-CH-01 | S posted an adjusted drawio replica the same evening (`chat:group-raw@2026-09-28T20:44`) and replaced `figures/study-workflow.pdf`; figure content is binary and not checkable here. A repeated the "too AI" complaint on 09-29 11:46 and 10-02 22:28 | `msr:748f1df` (09-28 21:17) | 21h02m | partial (re-raised twice) |
| FB-A-CH-02 | Same figure pass; content not verifiable from patches | `msr:748f1df` | — | partial / no evidence of content |
| FB-A-CH-03 | = FB-A-INL-01 (same file, same request) | see INL-01 | 10h47m | partial |
| FB-A-CH-04 | = INL-02 → INL-06 chain; closed when B rewrote §3 as figure steps | `msr:815305e` … `msr:b5c0045` | 6h37m / 3d16h08m | verified |
| FB-A-CH-05 | Whole `refs.bib` rewritten to DBLP form (e.g. venue strings, `https://doi.org/…`) inside a commit whose subject only mentions the Overleaf sync workflow and label macros; a DBLP rule file for the agent added 6 min later; later bib passes in `msr:9c4567c`. Pre-submission agent audit posted by A: "39 active entries … 25 VERIFIED, 3 VERIFIED_ARXIV, 8 NOT_FOUND, 3 SKIPPED … No supported corrections" (`chat:group@2026-10-03T19:18`) | `msr:c93ef1f` (12:44); `msr:8df40d5` (12:50); `msr:9c4567c` | 60m | verified (8 NOT_FOUND left unexplained in the archive) |
| FB-A-CH-06 | B redrew the figure from scratch (12 → 10 steps) after the text was restructured | `msr:9ef4a07`, `msr:fdc9ca6` (10-02/03) | — | partial (style complaint repeated as CH-19) |
| FB-A-CH-07 | = FB-A-INL-03 | `msr:815305e` | 6h32m | verified |
| FB-A-CH-08 | `codebook-labels.tex` label macros (`\bug`, `\localpatch`, …) introduced and applied across sections | `msr:c93ef1f` (09-29 12:44) | 18m | verified |
| FB-A-CH-09 | A method-borrowing agent skill (`.cursor/skills/msr-tpa-rq-method-borrow/SKILL.md`) added in `c93ef1f` (14 min); new analyses (balanced share, prevalence correction, stricter rule) in `msr:9c69675` (S, chat 10-02 06:46 「基于你发的 HIGH & MEDIUM」); several analyses parked as `%% PARKED (author 2026-10-02, discuss first)` and never discussed in the archive | `msr:c93ef1f`; `msr:9c69675` (10-02 02:16) | 2d13h46m | partial |
| FB-A-CH-10 | `\appendix` + `\input{sections/A-appendix.tex}` removed from `main.tex`; compact label table moved into Design | `msr:464168f` (10-01 18:58) | 10h11m | verified |
| FB-A-CH-11 | Referent is an image; nothing attributable | — | — | no evidence |
| FB-A-CH-12 | No font change found in any `main.tex` hunk (see FB-B-16) | — | — | no evidence |
| FB-A-CH-13 | `tab:codebook-labels` "Labels of the seven codebook dimensions D1--D7. The replication package gives the definition and an example issue for every label." in `03-design.tex`; full-definition longtable leaves the compiled paper | `msr:464168f` (10-01 18:58) | 8h49m | verified |
| FB-A-CH-14 | Already done by `464168f` | `msr:464168f` | (pre-empted) | verified |
| FB-A-CH-15 | Anonymous replication-package URL added to `main.tex` (Data Availability) | `msr:5776349` (10-02 06:39) | 3m | verified |
| FB-A-CH-16 | B: 「我修改了，目前是对应上的了」 (`chat:group@2026-10-02T11:07`) | `msr:9ef4a07` (11:31) | 4h02m | verified (closed by `b5c0045`) |
| FB-A-CH-17 | Referent unclear (B asked where) | — | — | no evidence |
| FB-A-CH-18 | Phase/Step run-ins mirror the 10 figure steps (commit subject "Sync methodology section with study-workflow figure"); phase-mapping sentences pruned next morning | `msr:b5c0045` (B, 10-03 03:48); `msr:4c70db0` (08:37) | 5h22m | verified |
| FB-A-CH-19 | B: 「配色我试了半天，没发现更好的」, then 「那其实已经是了」 (`chat:group@2026-10-02T23:12`, `…T23:22`); figure binary redrawn `msr:fdc9ca6` | `msr:fdc9ca6` | — | partial (B disputed; outcome not verifiable) |
| FB-A-CH-20 | B expanded threats/implications and added details/examples in four commits ("expand threats+implications", "expand details", "exapnd details") | `msr:d0d4c03` (10-03 09:58), `msr:86199d6`, `msr:1ec1a0f`, `msr:13179f3`, `msr:b7a448b` | 11h14m | verified (final page count: no evidence) |
| FB-A-CH-21 | = INL-05; heatmap text size 1.95 → 3.8 | `msr:94e651f` (12:04) | 32m | verified |
| FB-A-CH-22 | Abstract: "from seven repositories across five ecosystems" → "from five ecosystems" | `msr:f1bc590` (19:24) | 57m | verified |
| FB-A-CH-23 | Project macros removed from the abstract; the replacement dropped the asterisk of one ecosystem name ("…Agda, F, and CakeML"), fixed 9 min later with explicit `\textsf{F*}` (Example E5) | `msr:4af1aff` (18:43); `msr:10e2e5f` (18:52) | 6m | verified (after a regression) |
| FB-A-CH-24 | Process: team moved to Overleaf; A's 10-04 rewrite `ol:ba3f1ee` | `ol:ba3f1ee` | — | (process; excluded) |
| FB-A-CH-25 | Replication repo is not in the archive; S: 「搞定了」 (`chat:group@2026-10-06T11:57`) | — | — | no evidence (chat claim only) |

### 2.4 Senior B (1:1 chat, PDF, group chat)

| ID | Change made | Commit(s) | Latency | Status |
|---|---|---|---|---|
| FB-B-01 | No attributable "comment out" pass; 9 days later the paper was more than a page short and was expanded (FB-B-20, FB-A-CH-20) | — | — | superseded (page shortfall reversed the direction) |
| FB-B-02 | Appendix later removed entirely (FB-A-CH-10); final page count of the submitted PDF not in the archive | — | — | no evidence |
| FB-B-03 | Venue class switched; wording changed | `ol:dade33e` (13:09 "Switch … to the FSE 2027 acmsmall review class"); `ol:30f5bf0` (13:32) | 6m | verified |
| FB-B-04 | Image markup; the four-panel design was abandoned for a single three-stage workflow (FB-B-05/06) | — | — | superseded |
| FB-B-05 | Single study-workflow figure replaced the four panels (`figures/study-workflow.pdf`/`.svg`) | `msr:748f1df` (09-28 21:17) | 29h22m | verified (file level) |
| FB-B-06 | S produced the drawio replica with a figure skill (`chat:1on1-raw@2026-09-27T23:18`); committed as the workflow figure | `msr:748f1df` | 35m (chat) | verified |
| FB-B-07 | Full codebook longtable with definitions and examples added as an appendix (`tab:codebook-labels`), then A vetoed appendices; the table was shrunk to labels only and moved into Design, definitions to the replication package | `msr:b45f60d` (09-30 20:09); `msr:464168f` | 2d3h26m | superseded (A's veto; compromise) |
| FB-B-08 | Too general to attribute | — | — | no evidence |
| FB-B-09 | Intro figure `fig:intro-failure-modes` added | `msr:6f652b4` (09-29 13:33); drawio `msr:b73f7df` | 14h18m | verified |
| FB-B-10 | Alternative RQ1 heatmap rendered and wired in; later became the primary RQ1 figure | `msr:7abe3ce` (09-29 00:57); `msr:47221f7` | 1h07m | verified |
| FB-B-11 | Final compiled prose: 0 `---` em-dashes, 2 semicolons left (`04-rq1.tex:162`, `08-threats.tex:12`); no single commit implements the rule | many | — | partial |
| FB-B-12 | = P-items; most floats removed in one S commit that afternoon | `msr:7c705c9` (16:14) | 4h23m | verified |
| FB-B-13 | Practice consistent with it (tables cut, heatmap, bold Total cells in `tab:rq2-medians`), but the quoted message is a user relay not present in the export | — | — | no evidence (of the request itself) |
| FB-B-14 | Resolved as A's CH-13 compromise; B conceded at 09:19/09:26 | `msr:464168f` | — | superseded |
| FB-B-15 | Paper text points to the package (`464168f`); package README not in archive | `msr:464168f` | — | partial |
| FB-B-16 | No font-related change in any `main.tex` hunk; final preamble is `acmsmall,screen,review,anonymous` with only commented-out extra packages | — | — | no evidence |
| FB-B-17 | "the replication package gives the definition and an example of every label" | `msr:464168f` (18:58) | 9h32m | verified |
| FB-B-18 | Already present | `msr:464168f` | (pre-empted) | verified |
| FB-B-19 | Anonymous URL in Data Availability | `msr:5776349` (06:39) | 5h54m | verified |
| FB-B-20 | Page-filling commits on 10-03; final page count not in archive | `msr:d0d4c03` … | — | no evidence (of outcome) |
| FB-B-21 | Macros removed from abstract | `msr:4af1aff` (18:43) | 7m | verified |
| FB-B-22 | Abstract restructured: background → "To fill this gap, we study …" → findings → "We recommend …" | `msr:f1bc590` (19:24) | 6m | verified |
| FB-B-23 | Deadline overwrite incident followed; A's 10-04 Overleaf rewrite shortened sentences but cannot be attributed to this message | (`ol:ba3f1ee`) | — | no evidence |
| FB-B-24 | Replication repo not in archive | — | — | no evidence |
| FB-B-25 | Same | — | — | no evidence (chat claim) |
| FB-B-26 | Process (sync rule); see notes/04 §1.5 | — | — | (process; excluded) |

PDF annotations (comment time 09-28 16:43):

| ID | Change made | Commit(s) | Latency | Status |
|---|---|---|---|---|
| FB-B-P01 | `fig:repo-by-family` commented out, then deleted; per-repo counts remain only in a parked table | `msr:815305e` (09-29 18:19); `msr:9c69675` | 25h36m | verified |
| FB-B-P02 | D1 labels lowercased across 13 files | `msr:dfc2128` (09-28 20:00) | 3h17m | verified, after a transient revert: A's stale-base `msr:9809b8c` put `BUG` back; S re-lowercased in `msr:cfabd75` (09-29 12:26) and told A in chat (12:23); macros in `c93ef1f` |
| FB-B-P03 | Same | `msr:dfc2128`; `msr:cfabd75` | 3h17m | verified (same transient revert) |
| FB-B-P04 | Table 1 parked under `\iffalse` ("% Parked: tab:rq1-types … Restore by removing iffalse"); issue-type result carried by the RQ1 figure and finding text | `msr:7c705c9` (09-29 16:14) | 23h31m | verified |
| FB-B-P05 | Table 3 removed; Table 2 moved to appendix, then parked | `msr:643836a` (09-29 00:54); `msr:c017e0f`; `msr:7c705c9` | 8h11m | verified |
| FB-B-P06 | Table 4 commented out, later deleted; medians merged into a category × ecosystem matrix | `msr:7c705c9`; `msr:9c69675`; `msr:405bba7` | 23h31m | verified |
| FB-B-P07 | Option "simplify into another table" taken (no boxplot) | same | 23h31m | verified |
| FB-B-P08 | `fig:ttr-eco` removed; values in `tab:rq2-medians` Total row | `msr:7c705c9` | 23h31m | verified |
| FB-B-P09 | `tab:rq3-strategies` commented out (commit subject says it *removes* an already commented-out table); numbers moved to prose and the RQ3 figure | `msr:c544e4a` (09-29 16:54); `msr:b3dafcd`; `msr:e0ea09b` | 24h11m | verified |
| FB-B-P10 | Fig. 5 removed by S; re-added by A's stale-base drop 1 and by an Overleaf sync (`msr:578d640`); removed again | `msr:643836a` (00:54); re-added `msr:9809b8c`; removed `msr:7c705c9` | 8h11m | verified, after a transient revert |
| FB-B-P11 | Table removed with the appendix; allocation rewritten as one sentence in Design: "We therefore set a floor of 100 issues per ecosystem and 50 per nested library … 182 in [X] (132 … and 50 …)" (Example E3) | `msr:7c705c9`; `msr:464168f`; `msr:9c69675` (10-02 02:16) | 3d9h33m | verified |
| FB-B-P12 | Table 8 removed (appendix float deleted) | `msr:7c705c9` | 23h31m | verified |
| FB-B-P13 | `tab:rq2-by-family` moved into RQ2, then parked under `\iffalse`; its values merged into the `tab:rq2-medians` matrix | `msr:464168f` (10-01 18:58); `msr:405bba7` | 3d2h15m | verified |

### 2.5 Advisor (relayed)

| ID | Change made | Commit(s) | Latency | Status |
|---|---|---|---|---|
| FB-ADV-01 | "battery" never appears in any paper-repo `.tex` hunk (import `msr:5e73a46` already lacked it; last Overleaf removal `ol:cc7dafc` 09-28); "Hamilton 2000" dropped `ol:e03c20a` (09-24) **before** the relay. The advisor had read an older Overleaf state | (`ol:e03c20a`) | pre-empted | verified (feedback on a stale version) |
| FB-ADV-02 | Provenance sentence for the bug-category dimension: "We derived its categories from proof-assistant architecture … and refined them on the tuning half of the gold sample" (final `03-design.tex:53`); no provenance table for all dimensions | `msr:9c69675` (10-02 02:16) | 5d20h41m | partial |
| FB-ADV-03 | No commit addresses §3.1 explicitly; §3 was restructured into Phase/Step subsections by B (`b5c0045`) | — | — | superseded |
| FB-ADV-04 | Isabelle exclusion moved from threats into the scope paragraph of Design ("excludes Isabelle, whose primary tracker is not a GitHub issue list"); also in threats | `msr:393f596` (B, 09-28 00:10); `msr:bd086a7` | 42h35m | verified |
| FB-ADV-05 | Final compares against prior SE issue studies (bug-label misclassification and reporter studies, `07-implications.tex:48`, `04-rq1.tex:158`); no cross-domain baseline for time-to-close or fix strategies | — | — | partial |
| FB-ADV-06 | One interpretive sentence per ecosystem difference at most (e.g. `04-rq1.tex:170` "consistent with its role as a verified compiler"); no systematic expected/surprising discussion | — | — | partial |
| FB-ADV-07 | Implications section with recommendations for dataset builders and tool builders; abstract ends with recommendations (`msr:f1bc590`) | `msr:f1bc590` and earlier | — | verified (final state) |

### 2.6 Agent-generated comments

| ID | Change made | Commit(s) | Status |
|---|---|---|---|
| FB-AG-01 (C12) | The overlay sentence was deleted by A in his rewrite; no paper text discusses the overlay afterwards; data-side action: no evidence | `msr:9809b8c` (A) | partial (text); `[AUTHOR]` facts: no evidence |
| FB-AG-02 (C1) | A changed the headline to an unhedged "Four out of five fixed bugs are resolved by a local patch" and kept one hedge in the body, consistent with A's §2.8 "be precise once". Final RQ3 keeps one hedge (`06-rq3.tex:29`) | `msr:9809b8c` | partial (conflict A vs agent; A's style won) |
| FB-AG-03 (C2) | "repair effort" removed; final: 0 hits | `msr:3e7bab0`, `msr:9c69675` | verified |
| FB-AG-04 (C3) | Abstract rewritten without the bare number; "close among the fastest" | `msr:9809b8c`; final abstract | verified |
| FB-AG-05 (C7) | A *added* "about six times more" a day after C7 said to drop it; S removed all occurrences. S's checklist hunk in the same commit records "**OPEN: check with partners.**" → "Decided: about one percent against about nine percent. Tell the partners." | `msr:9809b8c` (+); `msr:3e7bab0` (10-02 00:25, −7 lines) | verified (after conflict; decision recorded by S, partner confirmation: no evidence) |
| FB-AG-06 (C5) | Conflicts with FB-A-INL-03; A's request won (funnel table removed, dropouts in caption) | `msr:815305e` | superseded by A |
| FB-AG-07 (C4) | Per-dimension κ added by S the night after; A compressed to "κ from 0.71 to 0.83"; final rule "print κ only when ≥ 0.65" (`msr:9c69675`) | `msr:643836a`; `msr:9809b8c` | verified |
| FB-AG-08 (C8) | "This happens since …" removed | `msr:9c69675` | verified |
| FB-AG-09 (C6) | "how severe they look", "most severe bugs" removed (final 0; S had raised the same point with B, `chat:1on1-raw@2026-09-28T23:12`); "layers above the kernel" never found | `msr:7c705c9`, `msr:9c69675` | verified |
| FB-AG-10 (C9) | "a limit of the codebook" removed; `other` reported as an RQ1 finding | `msr:643836a` | verified |
| FB-AG-11 (C11) | Title went back to the retired "What Breaks…" title (`msr:9355e35`, 10-03 17:57); the submitted title was a third one set by A on Overleaf | `msr:9355e35`; `ol:a610d1d`/`ol:ba3f1ee` | not addressed (author decision overrode agent) |
| FB-AG-12 (C10) | S added a "Time-to-Close and Resolution Status" RW subsection citing keys C10 had flagged as absent; 11 h later A deleted it | `msr:643836a` (+); `msr:9809b8c` (−) | superseded by A |
| FB-AG-13 | None of REVISION-SUMMARY's "After" sentences appears in any `.tex` hunk of either repo or in the final paper; the `.tex` committed with it in `msr:815305e` contains its "Before" text. The file was committed under the subject "cursor-safety: checkpoint before destructive delete" | `msr:815305e` (09-29 18:19) | not addressed (claimed, never landed) |

---

## 3. Statistics

Counted per inventory row (duplicates across channels, e.g. INL-01 = CH-03, are counted in each channel and flagged). Process rows (FB-A-CH-24, FB-B-26) are excluded.

| Origin | n | verified | partial | superseded | not addressed | no evidence |
|---|---:|---:|---:|---:|---:|---:|
| A written file | 11 | 7 | 2 | 1 | 0 | 1 |
| A inline macros | 16 | 11 | 3 | 2 | 0 | 0 |
| Unknown inline `%%` | 2 | 2 | 0 | 0 | 0 | 0 |
| A chat | 24 | 14 | 6 | 0 | 0 | 4 |
| B chat / other | 25 | 11 | 2 | 4 | 0 | 8 |
| B PDF annotations | 13 | 13 | 0 | 0 | 0 | 0 |
| Advisor (relayed) | 7 | 3 | 3 | 1 | 0 | 0 |
| Agent (file + change report) | 13 | 7 | 2 | 2 | 2 | 0 |
| **Total** | **111** | **68 (61%)** | **18 (16%)** | **10 (9%)** | **2 (2%)** | **13 (12%)** |

(A chat: FB-A-CH-24 excluded as process.) Transient reverts before final verification: 4 (FB-B-P02, P03, P10 via A's stale-base drop 1 and an Overleaf sync; FB-A-INL-16 partly undone for page budget). In addition, A's own Overleaf edits at 10-03 19:38 were overwritten 10 s later by the GitHub→Overleaf action (`ol:a610d1d` → `ol:214cc0c`, notes/04 §1.2).

Latency (comment → first commit with the requested change; minute-level sources only; n = 57):

| Origin | n | median | min | max |
|---|---:|---:|---:|---:|
| B chat | 10 | 2.8 h | 6 min | 29.4 h |
| A chat | 16 | 6.0 h | 3 min | 61.8 h |
| A inline macros | 16 | 15.8 h | 3.8 h | 96.5 h |
| B PDF annotations | 13 | 23.5 h | 3.3 h | 81.6 h |
| Advisor (relayed) | 2 | 91.6 h | 42.6 h | 140.7 h |
| **All** | **57** | **9.5 h** | | |

Observations:
- PDF annotations on concrete floats had the best completion rate (13/13) but the slowest human-channel latency; most were applied in one batch commit (`msr:7c705c9`) 23.5 h later.
- Abstract-level chat requests in the last deadline hour were fixed in 6–57 min, and one of them introduced a regression (E5).
- "No evidence" concentrates in B's general style/process requests and in artefacts outside the archive (replication repo, final PDF).
- Inline markers were *closed* by B in 10 of 16 cases, by S in 4 (2 of them inside an agent checkpoint commit), and never by A; 2 were commented out unresolved and remain in the source.

---

## 4. Worked examples (skill-ready; identifiers generalized)

### E1 — Terminology rename via an inline reviewer macro (FB-A-INL-07)
- Comment (inline, drop 2, 10-02 07:45): `\subsection{Issue Snapshot and Data Cleaning \todo{do not call it snapshot, call it dataset}}`.
- Change (`msr:9ef4a07`, by B, 3h46m later; patch l.508–515):
```
-\subsection{Issue Snapshot and Data Cleaning \todo{do not call it snapshot, call it dataset}}
+\subsection{Issue Collection}
-We analyze a frozen snapshot of the open and closed issues of all seven repositories, taken on <date>, rather than the live API, ...
+We collect the open and closed issues of all seven repositories on <date> and analyze this copy rather than the live API, ...
```
- Follow-up: S re-inserted the marker with "(Done: … renamed this subsection … remaining: Threats and Data Availability …)" (`msr:405bba7`); B deleted it (`msr:b5c0045`). Final: 0 "snapshot" in compiled sections.
- Lesson: a terminology comment is a global sweep, not a one-line fix; the Done note listing remaining locations is what made it closable.

### E2 — "It is a table, not a figure" (FB-A-INL-14)
- Comment: "Wait, It is a table! why label it as a figure?! Please format it as a normal table".
- Change (`msr:405bba7`, S, 15h49m; `05-rq2.tex`):
```
-\begin{figure*}[t]
-\begin{minipage}[t]{0.56\textwidth}
   ... tabular ...
-\caption{(a)~Median time-to-close (TTC) in days ... by bug category and ecosystem. ...}
-\label{fig:rq2-rq3-overview}
-\end{figure*}
+\begin{table}[t]
+\caption{Median time-to-close (TTC) in days ... by bug category and ecosystem. ...}
+\label{tab:rq2-medians}
   ... tabular ...
+\end{table}
```
- The second panel (a chart) moved to the next RQ. Chat confirmation: 「我把表和图拆开了」 (`chat:group@2026-10-02T21:38`). Marker deleted by B on Overleaf (`ol:376ed9d`).
- Lesson: float type follows content; captions of tables go above the tabular; split mixed panels.

### E3 — PDF annotation "this table is two sentences" (FB-B-P11)
- Comment (PDF, 09-28): 「不值得一个table，变成text就好 … 两句话完事儿，省篇幅」 on a 7-row allocation table.
- Before (appendix table + paragraph): `Raising X, Y, and Z to 100, raising W from 61 to 100, and keeping V at its proportional 182 sums to 582, the smallest total that meets every floor …` plus a `tabular` of 7 rows (`repo & n & floor`).
- After (`msr:9c69675`, 10-02 02:16, Design):
```
+We therefore set a floor of 100 issues per ecosystem and 50 per nested library and keep V at its
+proportional 182, which gives 582 issues: 100 each in W (50 + 50), X, Y, and Z, and 182 in V (132 + 50).
```
- Table removed earlier with the appendix (`msr:7c705c9`). Latency 3d9h33m; a page-budget comment applied only when the section was rewritten.
- Lesson: when a reviewer says "two sentences", write the sentences in the same commit that deletes the table, so the content is not lost in between.

### E4 — Procedural opener → substantive opener (FB-A-10)
- Comment (written file §2.7): "Some section openings are too procedural … Open with the substantive point", with a model sentence.
- Change (`ol:01fcd0f`, 09-22 16:49, l.25–30):
```
-RQ1 asks which issue types and bug categories are prevalent in each family, because the plan made specific predictions ...
-The approach is a count of the issue-type field on all <N> issues and of the bug-category field on the <M> defect reports, ...
-A good outcome for the plan would be a proof assistant whose leading category matches its predicted signature.
+Before reasoning about defects, we need to know whether these trackers mostly contain defects at all.
+If some repositories are dominated by feature requests or project-management tickets, any defect census built by repository-level sampling will be biased.
+We therefore count issue type on the full snapshot and bug category on defect reports, then test association with family as in Section~\ref{sec:design}.
```
- The same hunk replaces a number-laden paragraph with a pattern sentence plus one statistic (FB-A-07).
- Lesson: adopting the reviewer's model sentence verbatim is fast but brittle; this sentence was rewritten later and is not in the final paper.

### E5 — Fast fix that introduced a regression (FB-A-CH-23 / FB-B-21)
- Comments (group chat, 10-03 18:36–18:43, 77 min before the deadline): no labels and no macros in the abstract, "文本叙述吧，安全一些".
- Change (`msr:4af1aff`, 18:43):
```
-... across five ecosystems (\Lean, \Rocq, \Agda, \Fstar, and \CakeML), using ...
+... across five ecosystems (Lean, Rocq, Agda, F, and CakeML), using ...
```
- The macro for a name containing `*` was expanded by hand to "F". Fixed 9 min later (`msr:10e2e5f`) as `\textsf{F*}`.
- Lesson: after a mechanical replacement, diff the rendered text, not only the source; check every changed token.

### E6 (counter-example) — Agent change report that never landed (FB-AG-13)
- `06-revision/REVISION-SUMMARY.md` lists all 11 written comments as "✅ Addressed" with "After" LaTeX such as "Proof assistants are software tools that enable users to write machine-checked …".
- That string occurs only inside the `REVISION-SUMMARY.md` hunk of `msr:815305e` (and its Overleaf mirror `ol:bfa20aa`); the `03-design.tex` committed alongside still contains the "Before" sentence.
- Lesson: a resolution claim is evidence of intent, not of change. Verify each claimed "After" string against the diff before marking a comment resolved.

---

## 5. Protocol patterns observed

### 5.1 Delivery channels (and what each did well or badly)

| Channel | Who | Volume | Traceability | Observed problem |
|---|---|---|---|---|
| Written comment file (markdown, 8 themes + terms) | A | 11 items, once | Line-addressable, undated | Delivery date unknown; themes are broad, so "done" is a judgement |
| Inline macros in the shared LaTeX (`\hao`, `\todo`) | A | 16 markers, 2 drops | Best: marker add/remove is visible per commit | Drop 1 was made on a stale base and reverted others' work; markers commented out instead of resolved |
| Annotated PDF (13 highlight/sticky notes; parsed with a PDF-comment skill) | B | 13 items | Good per float, but page-based ("Table 4") ids drift as floats move | Batch-applied ~1 day later; float numbering changed during the batch |
| Annotated PDF with flattened drawing | A | 1 | Not machine-extractable | Content survives only in the accompanying chat text |
| 1:1 chat | B → S | ~20 requests | Minute timestamps | Requests mixed with process chat; some only as images |
| Group chat | A, B | ~45 requests | Minute timestamps | Image-referent requests ("这个也是？") unrecoverable |
| `%TODO` comments in TeX | B | unknown count | — | S had to ask whether they were meant for him (`chat:1on1-raw@2026-09-28T23:15`) |
| Relay (advisor via B) | ADV | 7 questions | Verbatim | Read an older version; 1 of 7 already obsolete |
| Agent comment file / agent change report | AG | 12 + 1 | Line-addressable | Report claimed fixes that never landed |

### 5.2 The `\hao` / `\todo` protocol in practice

- **Definition.** `\hao`: A's notes, resolvable "by [A] or the agent". `\todo`: for the student; "the agent must not resolve them" (`msr:9809b8c`). Only 1 of 16 markers was a `\hao`; 15 were `\todo`.
- **Who resolved.** The *edits* were made by S (12) and B (4, all design/figure); the *markers* were closed by B in 10 cases (often on Overleaf, deleting Done-annotated markers in bulk: `ol:376ed9d`, `ol:3fd6209`), by S in 4, never by A. A never confirmed a resolution in the archive.
- **Agent resolution despite the rule.** Two `\todo` markers (INL-02, INL-03) disappeared in an S-account commit titled "cursor-safety: checkpoint before destructive delete" that also added the agent's REVISION-SUMMARY; INL-02 was then re-raised by A as a `\hao` (INL-06). Inference: an agent session removed `\todo` markers it was not allowed to resolve.
- **"(Done: …)" annotations.** S wrote Done notes inside 8 markers (`msr:405bba7`, `msr:e0ea09b`), each naming who did what and what remains. This worked: B deleted exactly those markers the next morning. INL-09 got a "[Partly addressed …]" note instead.
- **Commented out, not resolved.** INL-01 (`msr:59f15be`), INL-09 and INL-10 (`msr:ac172bd`) were turned into `% \todo{…}` without being resolved; INL-09/10 remain in the final source. S also switched note rendering off (`\shownotesfalse`, `msr:5776349`) while an unresolved marker existed; A switched it back on 66 min later (`msr:0f96193`).
- **Markers closed before the fix.** INL-05 (font size) was deleted with its figure; the figure came back 5 h later with the old font; A re-raised it in chat 4 days later.
- **Re-insertion.** B removed INL-07/08 together with the fix (`msr:9ef4a07`); S re-inserted them with Done notes (`msr:405bba7`), which is useful for review but reverses B's closure.

### 5.3 Stale-base edits and reverts

- A's drop 1 (`msr:9809b8c`) was authored against a pre-09-29 tree and pushed directly to `main`. It silently reverted S's lowercase labels (FB-B-P02/03), re-added a removed figure (FB-B-P10), reverted S's RQ3 hedges, and re-added "six times". Two "Updates from Overleaf" syncs (`msr:bfaf29c`, `msr:578d640`) toggled the text again within an hour. S merged by hand: 「我人工合并一下」 (`chat:group@2026-09-29T12:16`) and 「有的和我们之前的要求对不上，我一个个 check 一下」 (12:10).
- B's PR conflicted with A's push (`chat:group@2026-09-29T11:52`); B: 「那要不就用[A]的版本」 (12:17).
- At the deadline the GitHub→Overleaf action overwrote A's Overleaf edits (notes/04 §1.2).
- B's "add todo" (`msr:5262231`) deleted an RQ3 κ caveat that S restored (`msr:3e7bab0`) (notes/partial/06c).

### 5.4 Reviewer conflicts and how they were resolved

| Conflict | Positions | Resolution | Evidence |
|---|---|---|---|
| Label-definition appendix | B: big appendix table (09-28) and 「没有的话怕被 critique」 (10-01); A: 「放上去充页数=直接reject」 | A's compromise: labels-only table in Design + definitions in the replication package; B concurred the same morning | `chat:group@2026-10-01T08:54–10:09`; `msr:464168f` |
| Funnel table | A: remove it, show in figure; AG C5: put funnel in Results | A won | `msr:815305e` |
| Hedging of the headline | AG C1: hedge; A: be precise once | A won (one hedge in body) | `msr:9809b8c` |
| "six times" | A added it; AG C7: drop it | Dropped by S; S's checklist says "Decided … Tell the partners" with no partner confirmation in the archive | `msr:3e7bab0` |
| Title | AG C11: keep old title retired; S restored it; A set a third title on Overleaf | A's title submitted | `msr:9355e35`; `ol:ba3f1ee` |
| Finding template | A INL-09 "show it in the first sentence" vs A INL-10 "second sentence refers to a figure" | Not resolved; both markers commented out | `msr:ac172bd` |
| Figure palette | A: too AI, simplify; B: already classic colours | Unresolved; A rewrote the figure again on 10-04 | `chat:group@2026-10-02T22:28–23:22`; `ol:ba3f1ee` |
| Cut vs fill | B 09-22: comment out low-interest detail; B/A 10-02: more than a page short, expand | Expansion in the last 12 h | FB-B-01; FB-A-CH-20 |

### 5.5 Claims of resolution that did not match the diff

- REVISION-SUMMARY (FB-AG-13): 11 "✅ Addressed", 0 landed.
- Commit subjects that misdescribe patches: `msr:c93ef1f` (rewrites `refs.bib` to DBLP form, subject mentions only sync workflow and labels), `msr:5d2c165` "fix warning messages" (adds a related-work paper and sentence), `msr:c544e4a` "Remove commented-out table…" (comments a live table out), `msr:815305e` "cursor-safety: checkpoint…" (resolves two `\todo`s and removes a figure), `msr:5262231` "add todo" (restores a whole RQ1 result and deletes a caveat), `ol:5ecaf3f` "Lock a term table…" (also deletes defensive phrases).
- `past-chat-jimmy/SUMMARY.md` and checklist v2 provenance conflate the Student with A (also notes/03 §3).
- The INL-01 progress note was the one honest status report: "Manuscript text not yet updated—awaiting author decision on which papers to cite".

### 5.6 Misses

- Never addressed or not traceable: FB-A-03 (paper to read), FB-B-08 (logic progression), FB-B-16 (default font), FB-A-CH-11/17 (image referents), FB-B-23 (shorter abstract sentences), FB-ADV-05 (cross-domain baseline).
- Partially addressed and then dropped: INL-09/10 (finding template applied to the first findings only), FB-B-11 (two semicolons remain), FB-A-07 (numbers in prose).
- Feedback on a stale version: the advisor's jargon complaint (FB-ADV-01) targeted text already removed.

---

## 6. Design implications for a feedback-to-revision skill

1. **Stable ID per comment, per channel.** Assign `FB-<origin>-<nn>` at intake (written file, inline macro, PDF note, chat message, relay, agent). Record the source pointer (file:line, commit+line, PDF page+float caption, chat timestamp) and the version the reviewer read. Key PDF notes to the float label or caption text, not to "Table 4", because numbering changes during revision.
2. **Triage before editing.** For each ID: type, size, needs-author-decision, conflicts-with (other IDs), and duplicate-of (e.g. inline marker = chat message). Separate process requests from text revisions. Flag comments made on a stale version (FB-ADV-01) and image-only requests that need a text restatement.
3. **One change per comment, ID in the commit message.** Commit subjects here often misdescribed the patch; a subject like `FB-B-P11: allocation table → one sentence in Design` makes the trace mechanical. Avoid mixing comment fixes with sync merges or agent checkpoints.
4. **Verification step: claimed vs actual diff.** Before marking an ID resolved, extract the claimed "after" text (from the agent report, Done note or commit message) and grep it in the `.tex` diff; diff the compiled text for mechanical replacements (E5). Re-run the check on the merged branch, because stale-base pushes and sync bots reverted verified fixes 4 times.
5. **Marker lifecycle.** Respect the macro protocol: the agent may draft a fix for a student-only marker but must not delete it; it should append a Done note that says what changed and what remains, and leave closure to the reviewer or the student. Never comment out (`% \todo`) or hide (`\shownotesfalse`) an unresolved reviewer note. Before submission, list every remaining or commented-out marker as an open item.
6. **Conflicting reviewers.** Detect conflicts at triage (same object, opposite requests, as in the appendix and funnel cases). Do not resolve silently: present both positions and a compromise option, record the decision with its owner and date, and confirm with the losing reviewer. "Decided … Tell the partners" in a checklist (AG-05) is not confirmation.
7. **Rebuttal-letter / response table format.** For each ID: reviewer quote (short), decision (accept / partial / decline with reason / superseded by ID), change summary, location after the change (section + label), commit SHA, verification status (verified by diff / pending). This is the table the team lacked; it also carries over to a journal-revision rebuttal (no reviewer reviews exist in the archive yet, GAPS item 8).
8. **Page-budget awareness.** Track the page delta of each accepted cut or expansion. Cuts requested early (FB-B-01) and fills requested late (FB-A-CH-20) were never reconciled until the page count was short.
9. **Re-raise detection.** When a reviewer repeats a comment (INL-02 → INL-06; INL-05 → CH-21; CH-01 → CH-06 → CH-19), link it to the earlier ID and reopen it rather than creating an unrelated item; a repeat means the earlier closure was wrong.
10. **Agent comments as a separate origin.** Label agent-generated comments and reports as such; they had a similar adoption rate to human comments (7/13 verified) but carried the only "not landed" claim. Human reviewers overrode agent suggestions in every direct conflict.
