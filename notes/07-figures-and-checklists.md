# 07 — Figure iterations and checklist evolution

Phase 2 evidence note. Archive: `~/Projects/supervisor-skills-msr-tpa` (HEAD `669b29a`). All paths are relative to the archive root; all times Asia/Shanghai (UTC+8). Citation formats follow `03-archive-map.md` §4: `msr:<sha>` (paper repo, `07-overleaf-history/patches-msr-tpa/`), `ol:<sha>` (Overleaf git, `07-overleaf-history/patches-overleaf/`), `res:` (research repo), `chat:group@…` (`04-comms/20260929-1007-wechat-group/messages.jsonl`), `chat:group-raw@…` (`04-comms/past-chat-group/raw/*/Chat History.txt`, 09-22 → 09-29), `chat:1on1@…` (`04-comms/past-chat-jimmy/raw/chat-history-merged.txt`, ends 09-29 12:53), `<path>:<line>`.

Roles only: **Student** (first author), **Senior A** (writing organization, desk-reject red lines), **Senior B** (methods figure, page budget, repo owner), **Advisor (relayed)**. "Agent" = a coding/writing agent run by a human (Cursor, Codex, Claude); agent output is labelled as such. Private note: it contains dataset sizes and paper-identifying numbers; strip them before anything goes public.

Status words: **VERIFIED** (primary source read), **PARTIAL**, **CONTRADICTED**, **NO EVIDENCE**, **INFERRED** (my reading of several sources, not stated anywhere).

Images were inspected directly (chat media, `final/*.png`, PDFs rendered locally); `.drawio` files were compared only through the label text and style attributes in commit diffs.

---

# PART A — Figure iterations

## A.0 Overview

| Figure (final label) | Final form | Versions seen | Span | Main drivers | Tools |
|---|---|---:|---|---|---|
| Study workflow (`fig:study-workflow`) | 3 phases, 10 numbered steps, pastel phase frames, icons; caption cut to one line on 10-04 | ≥ 11 | 09-26 → 10-04 | Senior B (layout, redraws), Senior A (redline, figure↔text sync, "too AI"), Student + agents (replica builds) | AI image → agent-built native draw.io replica (Python generator) → redline revision script → hand edits in draw.io desktop |
| Intro failure modes (`fig:intro-failure-modes`) | Native draw.io diagram: proof scripts → elaborator & tactics / trusted kernel → regression vs soundness panels | 4 | 09-28 → 10-04 | Senior B (asked for it, "convention"), Student | ChatGPT-style raster reference → Python upscaling script (abandoned) → hand-drawn draw.io |
| RQ1 (`fig:rq1-alternative`) | (a) bars, one bar per issue type, repository shares inside; (b) bug-category × ecosystem heatmap with All and Balanced columns | ≥ 6 | 09-28 → 10-04 | Senior B (invert bars, merge b+c into heatmap), Senior A (keep only if it adds info; font size) | R/ggplot2 |
| RQ1 D6/D7 (`fig:rq1-d6-d7`) | Two donuts, every codebook level, N/A excluded | 8 drafts | 09-29 → 10-02 | Student (user judged earlier figures "unattractive"), Senior A (no appendix) | R |
| RQ2 | **No figure**: one booktabs table `tab:rq2-medians` (bold Total row) | ≥ 5 | 09-26 → 10-02 | Senior B (cut figures/tables), Senior A ("It is a table! why label it as a figure?!") | R, Python (matrix), LaTeX |
| RQ3 (`fig:rq3-resolution`) | Triptych: (a) strategy mix, (b) fix size median/IQR by category, (c) time-to-close by strategy | ≥ 3 + 5 drafts | 09-26 → 10-04 | Senior A (split table from figure), Student | R/ggplot2 (Helvetica, 6–6.5 pt) |
| Appendix D3/D6/D7 plots | Removed with the appendix; D3 figure parked | 2 | 09-29 → 10-02 | Senior A ("不要appendix，软工的人不喜欢") | R |

## A.1 Study-workflow (overview) figure

### Iteration chain

| # | When | Artifact / commit | Who | What changed | Driving feedback |
|---|---|---|---|---|---|
| 0 | 09-22 23:41–23:42 | chat only | Student, Senior B | Student: draw.io MCP "画起来不咋行"; B: "先让 ai 帮你生成草图，然后你来手动实现" | Tool choice (`chat:group-raw@2026-09-22T23:41`) |
| 1 | 09-26 00:04 / 01:34 | `05-figures-tables/sources/briefs/overview-figure-prompt.md` (665 lines, for "PaperBanana, SciFig, AutoFigure … Draw.io agents"); `drawio-overview-brief.md` (4 panels A–D, palette, "do not add Severity, Impact, 502") | Student + agent (file mtimes in `11-*/FILE_MANIFEST.tsv`) | Structure-first figure contract: gates, RQ lanes, acceptance checklist, negative prompt | None recorded; self-initiated |
| 2 | 09-26 12:04 | AI-generated overview image (`chat:1on1@2026-09-26T12:04`, "我让AI生成的 … 到时候自己手绘一下") | Student | First visual | — |
| 3 | 09-27 15:48 | `sources/drawio/Overview - GitHub issue mining.drawio` (6 pages: A, B, C, D, overview, modified); posted in group | Student (hand-drawn) | Four panels: data card; sample → "κ = 0.76" → "κ = 0.65" → LLM prompt; gated codebook; RQ ← dimension sums | Student: "还没有那种学术的感觉" |
| 4 | 09-27 15:55–17:36 | B's reference image (`raw/C204…/Weixin Image_202609271736_2.jpg`) | Senior B | Three phases, 12 numbered steps, icons in pastel disks, detail line under each step, incl. "two first authors · Cohen's κ = 0.74" and "291 held out · Cohen's κ = 0.81" | B: "四个图来表示一张图的内容，其实没有一张图更有说服力"; "我给你生成一个样子" (`chat:group-raw@2026-09-27T15:55–15:56`) |
| 5 | 09-27 22:43–23:21 | `overview-reference-replica/` (LAYOUT_FINGERPRINT 22:49, QA phases 22:54–22:58, 11 SVG icons 23:09); `build_replica.py` | Student + agent ("drawio-figure-replication" workflow; Student: "用 skill 画一下") | Native, editable draw.io replica of the image, 130 cells, Times New Roman, horizontal font compression (`scaleX(0.76–0.92)`) | Student: "这个图就按你这样一模一样的做出来吗？" B: "对 … 试着用pptx画图skill或者drawio画图skill … 我怕这种直接用会被reviewer嫌弃" (`chat:1on1@2026-09-27T22:43–22:44`) |
| 6 | 09-28 00:10 | `msr:393f596` "add" (`figures/study-workflow.drawio` +447, PDF; `03-design.tex` gains the figure and "two authors … κ = 0.74 … κ = 0.81") | Senior B | Replica becomes the paper figure | B 23:21: "先替换掉然后等初稿改完给[Senior A]一起看" |
| 7 | 09-28 00:15–00:48 | Screenshots `Weixin Image_202609280019_2.jpg` (circled detail lines), `…0047_3.jpg` (red redline) | Senior A | Redline: strike phase badges and 9 of 12 detail lines (incl. "two first authors", "κ = 0.74", "291 held out · κ = 0.81"); handwritten note: name the ecosystems or write "x proof assistants" to state scope | "这个图的风格太AI了，现在reviewer看到AI生成的东西就反感"; "这些小字可以去掉（AI的风格）"; "关键信息只需要保留和数据相关的，比如dataset有几个repo，几个issue" (`chat:group-raw@2026-09-28T00:15–00:42`) |
| 8 | 09-28 01:15–01:17 | `academic_revision.py`, `qa/redline-validation.json` (badges removed 3, detail labels removed [1,3,4,6,7,8,9,11,12], kept [2,5,10], `horizontal_font_scaling: false`) | Student + agent | Redline applied in place; scope line added | Senior A's redline (README "Redline revision — 2026-09-28") |
| 9 | 09-28 18:27–18:28 | `overview-variants/` (6 generated candidates from `variants.yaml`, Arial, "Cohen's kappa = 0.74" in step 7 detail) | Student + agent | Columns, rows, single-line pipeline, validation-focused, RQ-output, monochrome | None recorded. **No variant was adopted** (no commit or chat references them) |
| 10 | 09-28 20:44 → 21:17 | Chat image `…282044_4.jpg`; `msr:748f1df` (PDF + SVG) | Student | Ecosystem names under step 1, numbers only in steps 2, 5, 10, no phase badges | B 20:56: "有的有字，有的呢，它就没有字 … 要不就是都是黑字" |
| 11 | 09-29 11:35 | `msr:9809b8c` `\todo{the overview figure and the content in methodology is not synced … update the whole section and overview figure}`; `\todo{put this information in the overview figure and plot the link btw the data to each RQ, remove this table}` on the funnel table | Senior A | — | Chat 11:40–11:47: SAIL examples (subsections 5.1 / 5.1.1 match figure boxes); "新生常见问题，通常是没梳理清楚paper的methodology … 建议先整理好文字部分，再手工画出来"; "这个表可以拿掉，把信息放到methodology图里" |
| 12 | 09-29 18:19 | `09-paper-snapshot/figures/study-workflow-UPDATE-PLAN.md` (in `msr:815305e`) + `05-figures-tables/METHODOLOGY-FIGURES-REVIEW.md`, `…ACTION-ITEMS.md` | Agent (Cursor) | Plan: phase colours, funnel with dropout branches, **11 key numbers incl. κ = 0.74**, long caption with κ values | Agent reading of checklist MF-01..MF-04. **Never executed**; it contradicts Senior A's "remove small AI text" of 09-28 |
| 13 | 10-02 04:45 → 06:46 | `msr:9c4567c` (labels renamed to match prose: "Freeze export", "Enforce gate order", "Answer RQ1–RQ3"), `msr:5776349` (partly reverted), `msr:fd283fd` "Replace … with the latest reference-replica source" | Student | Three label flip-flops in two hours | Student's own text revision `msr:9c69675` (10-02 02:16) |
| 14 | 10-02 07:45 | `msr:0f96193` `\hao{figure and text are not synced, e.g., you mention 'Build issue payloads' in the figure, where is the text? … redraw the figure from scratch to reflect the text}` | Senior A | — | A also asks B to fix it (`chat:group@2026-10-02T07:29`) |
| 15 | 10-02 11:31 | `msr:9ef4a07` "refine methods and their figure based on [A]'s comments"; chat PDF 11:15 | Senior B | 12 → 10 steps (boxes "Build issue payloads" and "Freeze LLM setup" disappear; B's message names "phase 1 step 3 and phase 2 step 1"), icon spacing fixed, layout rebalanced, page 1454 × 664 | B 11:09: icons touching frames inconsistently; two steps not matching the design text |
| 16 | 10-02 22:26–23:22 | Chat | Senior A, Senior B | A: "1-删除没有信息量的部分 2-图片依然和文字对不上 A. 图片三个大框，文字3.1 3.2却对应两个小块 B. 5 6 7 找不到对应文字 … C. 3.4 如果对应phase 3的话 8 和 9 在哪？"; "图片的底色和配色都简洁化，现在太AI了". B: "配色我试了半天，没发现更好的". A: "那就黑白灰蓝，或者draw.io的经典色". B (screenshot of draw.io's default palette): "那其实已经是了" | — |
| 17 | 10-03 01:24 | `msr:fdc9ca6` "m" | Senior B | 9 steps; phase headings "1. Dataset construction / 2. Gold sample & classifier validation / 3. Issue labeling"; no analysis step | Item 16 |
| 18 | 10-03 03:48 → 10:04 | `msr:b5c0045` "Sync methodology section with study-workflow figure" (step 10 "Analyze patterns" back; `03-design.tex` rewritten as Phase 1–3 subsections with bold "Step k:" run-ins); `msr:4c70db0` deletes phase-mapping sentences; `msr:86199d6` re-adds a 3-sentence overview (page gap) | Senior B | Figure ↔ text become 1:1 (10 steps ↔ 10 run-ins) | Items 11, 14, 16 |
| 19 | 10-04 13:16 | `ol:ba3f1ee` (Overleaf, after the deadline reopening) | Senior A | Counts put in parentheses; a few draw.io classic fills (`#dae8fc`, `#d5e8d4`, `#f5f5f5`) added; gradients remain; caption cut to "Overview of the study." (old caption with 23,671 / 582 / 3,205 / 1,010 commented out) | Senior A's own pass |

### Final design (09-paper-snapshot = `msr:b5c0045` state; then `ol:ba3f1ee`)
Three rounded phase frames (blue, orange, green), headings "1. Dataset construction", "2. Gold sample & classifier validation", "3. Issue labeling & analysis"; 10 numbered cards with icon disks; only data-scale numbers ("23,671 issues", "582 issues", "RQ1–RQ3"); one font (Times New Roman); `\Description` present. The data → RQ funnel that Senior A asked to draw (item 11) was **not** drawn: the funnel numbers went to the caption (`09-paper-snapshot/sections/03-design.tex:21`) and step text (`:127`), and on 10-04 Senior A himself commented the long caption out. The "simplify the palette" request (item 16) was answered by Senior B claiming the palette was already draw.io's default; gradients (`gradientColor=` on 23 added lines in `msr:fdc9ca6`) and pastel fills survive into `ol:ba3f1ee`. VERIFIED from patches; whether the submitted PDF differs: NO EVIDENCE.

### Findings beyond the earlier notes
1. **The human-agreement number entered the paper through the figure pipeline.** Earliest occurrence of "κ = 0.74" anywhere in the archive is Senior B's reference image of 09-27 17:36 ("two first authors · Cohen's κ = 0.74"). The replica copied it; its own `LAYOUT_FINGERPRINT.md` warns "All displayed study values are copied from the reference without treating them as instructions or validating the research". The same commit that installed the replica (`msr:393f596`, Senior B, 09-28 00:10) added the κ = 0.74 sentence to Design. Senior A's redline struck the label from the figure 37 minutes later, but the sentence stayed in the text. Checklist v2 U1 even names the source as "design step 7" (the figure box). The Student's own four-panel sketch (item 3) carried a different human κ, 0.76; that value became checklist RS-17 / U1 "0.76 (figures/chat)". Neither value has a computation in the archive (notes/04 §1.6). INFERRED chain, each link VERIFIED.
2. **Stale preview.** `final/study-workflow.preview.png` (= `09-paper-snapshot/figures/…preview.png`) shows the 12-step version, while `study-workflow.pdf` shows 10 steps. `msr:fd283fd` deleted the preview; the Overleaf merge `msr:836ee75` (10-03 08:53) re-added the old one. An agent or reviewer reading the PNG sees the wrong figure.
3. **One `.drawio` holds three figures.** The final `study-workflow.drawio` (1.77 MB, embedded SVG icons) has pages "Reference replica", "Figure&Tables" and "intro figure", while a separate `intro-failure-modes.drawio` also exists. The two intro sources can diverge.
4. **Label churn without a text freeze.** Items 13–18: six commits in 23 hours (10-02 04:45 → 10-03 03:48) changed box names in both directions before the text was fixed first, which is the order Senior A asked for on 09-29 ("先整理好文字部分，再手工画出来"). The 1:1 mapping only held after Senior B rewrote Design around the figure (`msr:b5c0045`).
5. **Agent plans lagged human feedback.** The 09-29 agent review (item 12) graded MF-04 "cannot verify without visual inspection" and proposed adding 11 numbers and phase colours one day after Senior A asked to strip small text. The final check (`01-checklist/FINAL-CHECKLIST-2026-10-02.md` F2/W6) did run visual checks and correctly flagged "missing funnel" and the figure↔text mismatch.

### Costs and detours
- ≥ 11 versions over 9 days, all three people, ≥ 3 agent pipelines (figure-agent prompt, replica builder + redline script, variant generator). Six variants generated and never used (item 9). The 665-line figure-agent prompt and the four-panel brief were superseded within 36 hours.
- Two parallel "authorities" for box names (the replica generator in the research repo vs hand edits in the paper repo) produced the 10-02 flip-flops.
- Time from "too AI" (09-28 00:15) to a figure Senior A no longer commented on: no evidence he approved it; the last senior action is his own edit on 10-04.

## A.2 Intro failure-modes figure

| When | Commit / source | Who | Change | Driver |
|---|---|---|---|---|
| 09-28 23:15–23:16 | chat | Senior B | "加一个intro的背景图 … 也是惯例 … 用chatgpt create image for reference，然后用drawio画出来" | `chat:1on1@2026-09-28T23:15` (`%TODO` left in TeX by B) |
| 09-29 14:33 / 16:17 | `msr:22721bc`, `msr:d1a40d5` | Student | Raster PNG; source kept as `intro-failure-modes.source.jpeg` (1024 × 576, image-model style: valid/invalid proof → "Proof assistant" with bug icon → Rejected/Accepted) | B's instruction |
| 09-29 16:22 | `msr:e4ebb61` `figures/enhance_intro_failure_modes.py` | Student + agent | 3× upscale, chroma denoise, background whitening of the JPEG | Agent review MF-07 "legible at print size?" **Detour**: polishing a raster that was later discarded |
| 09-30 00:36 | `msr:ab66ce5` | Student | PDF + SVG exports | — |
| 09-30 21:43 | `msr:b73f7df` (+461-line draw.io) | Student | New native diagram: proof scripts → interactive proof assistant (elaborator & tactics → proof terms → trusted kernel); orange "Regression: valid proofs stop checking" and red "Soundness bug: invalid proofs are accepted" panels with downstream proofs | Student 09-30 01:02: "画了两个图，现在感觉还差去 ai 味" |
| 10-02 | FINAL-CHECKLIST F1 | Agent | PASS; notes the figure ties soundness bugs to the kernel only, while the codebook defines soundness by outcome; labels capitalized | — |
| 10-04 | `ol:ba3f1ee` | Senior A | Width 0.75 → 0.78 column; caption "Two failure modes illustrated in a kernel-based proof assistant" | Consistent with the F1 note; no evidence A read it |

Tooling lesson: the image model gave the idea (two rows, valid/invalid × rejected/accepted); the final figure is a different, richer architecture diagram drawn by hand.

## A.3 RQ1: composite vs heatmap

| When | Commit / source | Who | Change | Driver |
|---|---|---|---|---|
| 09-28 23:20–23:50 | chat | Student, Senior B | Student shows a three-panel RQ1 figure. B: (a)/(b)/(c) overlap; "图a你看看要不要变成每一个bar都是issue type，其中repo放到里面呢？… 不如直接对比不同类型的issue里，不同repo的占比"; "不妨将图b+c做成一个heat map" | `chat:1on1@2026-09-28T23:22–23:50` |
| 09-29 00:54 | `msr:643836a` | Student + agent | `render_rq1_overview.R` (top-3 table + issue-type bars + bug-category donut) as primary; heatmap script marked "SIDE EXPERIMENT only. Do not \includegraphics" | — |
| 09-29 00:57 | `msr:7abe3ce` (Co-authored-by Cursor) | Student + agent | Heatmap wired into the body as "An alternative version of Figure …" next to the primary; D3/D6/D7 plots to appendix | — |
| 09-29 11:35 | `msr:9809b8c` | Senior A | `\todo{anything we wanna say about this figure? any new findings? … if not, remove the figure}`; `\todo{if we wanna keep this figure, increase the font size in figure b, make it at least the same (or similar) size as normal text}` | — |
| 09-29 16:14 | `msr:7c705c9` | Student | Alternative removed; RQ1 tables parked | A's todo |
| 09-29 21:14 | `msr:b3dafcd` | Student | Alternative restored "for style comparison" (two RQ1 figures again) | none recorded |
| 09-30 20:15 | `msr:47221f7` | Student | `fig:rq1-overview` parked; heatmap figure becomes the only RQ1 figure | v2 checklist RS-11 "does not replace primary without reason" overruled |
| 10-02 02:16 | `msr:9c69675` | Student | Heatmap renderer reads the research repo's freeze; Balanced column (unweighted mean of five ecosystems) beside the pooled All column | Rocq dominance (FINAL §4) |
| 10-02 | FINAL F3, H15 | Agent | Heatmap cell labels ≈ 3–4 pt, "unreadable in print"; no colour-scale sentence; "Unknown" capitalized | — |
| 10-03 10:36–11:32 | chat | Senior B, Senior A | B: "这个图要拆不？总感觉很小看不太清". A: "感觉不用拆，b的字体弄大一些 … 要拆的话，把a转90度" | — |
| 10-03 12:04 | `msr:94e651f` | Student | Heatmap label `size = 1.95 → 3.8` | A 11:32 (and his 09-29 todo, 4 days earlier) |
| 10-03 19:24 | `msr:f1bc590` | Student | Panel (a) x-labels gain each type's share; caption: "share of the 23,666 issues that receive an issue type" | — |
| 10-04 13:16 | `ol:ba3f1ee` | Senior A | Renderer drops the shares, but the PDF is not regenerated in that commit and the caption still says "Under each bar, the percentage is …", now "of the 23,671 issues that receive an issue type" (23,671 is the full dataset; 23,666 have a type) | — |

Final (`09-paper-snapshot/sections/04-rq1.tex:124–142`): one `figure*`, (a) inverted D1 bars, (b) heatmap with All + Balanced columns explained in the caption. Post-deadline drift (last row) is a script/PDF/caption mismatch; whether it reached the submitted PDF: NO EVIDENCE.

D6/D7: `msr:3e7bab0` (10-02 00:25) commits 7 drafts (`d6d7_drafts/`: compact bars, named share by repo, mechanism × bug category, mechanism × repo, three pies); `msr:9c69675` ships `rq1_d6_d7_donut.pdf`. Its renderer hard-codes the counts ("Counts are freeze values … (do not recompute)", `final/rq1/render_rq1_d6_d7_donut.R:4–5`); FINAL H9 lists D6/D7 shares among numbers the replication outputs do not reproduce.

## A.4 RQ2: TTC matrix, KM, IQR

| When | Commit / source | Who | Change | Driver |
|---|---|---|---|---|
| 09-26 | `msr:5e73a46` import | — | Four single-column figures: median TTC by category, TTC IQR, median TTC by ecosystem, local-patch share by category | — |
| 09-27 22:42 | `msr:00406cd` (Overleaf update) | author unresolvable | `rq2/compare/`: the same boxplot in base R, ggplot2 and matplotlib, plus Q–Q plots | **Tool-comparison detour**; none of these reached the paper |
| 09-28 15:15–16:43 | chat + `jimmy-main-pdf-comments/` (P-01..P-13) | Senior B | "很多图和表，可能得删减或者重置"; median-by-category tables deleted (P-06/P-07), low-information large figures folded (P-08/P-10) | B's annotated PDF |
| 09-29 16:14 | `msr:7c705c9` | Student | Composite `fig:rq2-rq3-overview`: (a) a LaTeX `tabular` of median TTC (n) by category × ecosystem **inside a `figure*`**, with `\footnotesize` and `\tabcolsep 2pt`; (b) RQ3 stacked strategy bars | B's "fewer standalone tables" (`chat:1on1@2026-09-29T11:51`) |
| 10-01 09:20–09:23 | chat | Senior B, Senior A | B: "文章字体恢复到fse默认的样子"; A: "这个算违反policy，会desk reject" | Local font shrinking (G3) |
| 10-02 02:16 | `msr:9c69675` | Student | Kaplan–Meier curves rendered (`rq2_km.R`), parked as `%% PARKED`; import-time closures excluded | Censoring of open bugs |
| 10-02 07:45 | `msr:0f96193` | Senior A | `\todo{… separate it out as a standalone Table. Wait, It is a table! why label it as a figure?! Please format it as a normal table}` | — |
| 10-02 21:38 → 23:34 | chat "我把表和图拆开了"; `msr:405bba7` | Student | `tab:rq2-medians` standalone, bold Total row; RQ3 gets its own figure | A's todo |

Final: RQ2 has no figure, only `tab:rq2-medians` (`05-rq2.tex:47–53`). KM appears as one sentence in Threats; the IQR, Q–Q, boxplot and per-ecosystem figures are all retired. Number check: all 42 cells match `compute_rq2_median_matrix.py` (`01-checklist/CHECKLIST-UPDATE-SUMMARY.md:85–99`).

## A.5 RQ3: strategy and fix-size panels

| When | Commit / source | Who | Change | Driver |
|---|---|---|---|---|
| 09-29 | `msr:7c705c9` panel (b) | Student | All 11 strategies shown, "none were folded" | v2 RS-07 "show all strategies" (origin: Cursor thread 257c0222) |
| 10-03 01:30 | `msr:e0ea09b` | Student + agent | Five drafts (`rq3/drafts/D1…D5`: box, median-IQR, ECDF local vs other, TTC by strategy, size vs TTC) + a triptych preview; chosen: (a) five most common strategies + "other strategies", (b) median/IQR of lines changed by category with a dashed 10-line reference, (c) TTC by strategy, local-patch in blue. Helvetica, base 6.5 pt, legend 5.8 pt (`final/rq3/render_rq3_resolution_panels.R:9–13`) | A's `\todo` "merge this paragraph …"; Student: "又对 RQ3 做了两个图" (`chat:group@2026-10-02T21:39`) |
| 10-02 21:49 | chat | Senior A | "这个需要去一下ai味" after the RQ3 screenshot; B asks "具体在哪里？"; no answer in the archive. Which figure it targets is ambiguous | — |
| 10-02 | FINAL F6 | Agent | Fig. 4 legend ≈ 5 pt | — |
| 10-04 | `ol:ba3f1ee` | Senior A | Caption retitled "Resolution strategies, fix size, and time-to-close"; the sentence explaining the dashed 10-line mark deleted while the renderer (unchanged) still draws it | — |

The drafts folder was committed with a `.skim-build/` preview and a second copy of the 7,085-row CSV. RS-07 ("avoid lumping 'other'") is CONTRADICTED by the final caption.

## A.6 Appendix plots
`msr:643836a` / `msr:7abe3ce` (09-29) add `d3_trigger` and `d6_d7_domain_mechanism` to an appendix. Senior A: "怎么appendix还在？reviewer不会看的", "放上去充页数=直接reject" (`chat:group@2026-10-01T08:47–08:56`), "不要appendix，软工的人不喜欢" (`…10-02T01:51`). `msr:59f15be` (10-02 06:02) deletes `A-appendix.tex`; the Overleaf merge `msr:836ee75` resurrects the file (+145) although `main.tex` does not input it. D6/D7 moved into RQ1 as donuts; D3 described in prose, its figure parked "because it looks poor" (`01-checklist/checklist.md` F5).

## A.7 Cross-figure costs and detours
- Raster polishing before a vector redraw (intro).
- Rendering-tool comparison (three boxplot engines) for a figure that was later deleted.
- Draft fan-out without a decision record: 6 overview variants, 7 D6/D7 drafts, 5 RQ3 drafts; only the RQ3 choice is visible in a commit.
- Figure renderers depend on a sibling private repo (`render_rq1_alt_heatmap.R` searches for `mining-github-issue/analysis/llm_annotation/freeze_23671_labels.jsonl` above the paper root); D6/D7 counts are hard-coded.
- Post-deadline caption edits without regenerating figures (RQ1, RQ3, workflow).

## A.8 Derived figure rules

Scope: **G** general, **SE** SE/MSR-specific, **V** venue/ACM-specific. "Upstream" = `skills/figure-designer` (+ `references/design-rules.md`, `tools.md`, `solution-overview.md`), `skills/drawio-reconstruction`, `skills/pre-submission-reviewer` (Dimension 5), `skills/paper-writer/references/verification-checklist.md`, `handbook-en/04_Scientific_Plotting/4.2`, `4.4`.

| # | Rule | Evidence | Scope | New vs upstream |
|---|---|---|---|---|
| FR1 | Number the overview's boxes and give Methods one same-named run-in ("Step k: …") per box, in the same order. Check both directions after every redraw: count boxes = count steps, every step has a box. | `chat:group@2026-09-29T11:40–11:42`, `…10-02T22:26`; `msr:9809b8c`, `msr:0f96193`, `msr:b5c0045` | G | Extends upstream ("module names consistent with section headings", handbook 4.2; pre-submission-reviewer D5) with numbering, ordering and a two-way count check |
| FR2 | Write the Methods text first, then draw the overview from it; if they disagree, redraw the figure "from scratch to reflect the text". | `chat:group@2026-09-29T11:46`; `msr:0f96193` | G | New |
| FR3 | Every number printed inside a figure must come from the same script or ledger as the text. A number copied from a sketch, an AI image or a reference figure is a placeholder until re-sourced. | κ = 0.74 chain (A.1 finding 1); `overview-reference-replica/LAYOUT_FINGERPRINT.md` last line | G | New. `drawio-reconstruction`'s fidelity contract ("visual fidelity is the primary goal") would preserve such numbers; add an explicit "re-source all data values" step when the reference is a sketch |
| FR4 | Use AI images only to explore layout. Rebuild natively (draw.io), then do a human redline pass on a screenshot, then hand edits. Do not ship AI raster art and do not upscale it. | `chat:group-raw@2026-09-22T23:42`, `@2026-09-27T17:36`; `chat:1on1@2026-09-27T22:44`, `@2026-09-28T23:16`; `msr:e4ebb61` → `msr:b73f7df` | G | New as a process. Upstream tools matrix recommends draw.io/PPT but says nothing on AI sketches |
| FR5 | Remove AI-look markers: a detail line under every box, numbered phase badges, gradient pastel frames, uneven icon placement, mixed text presence. Keep only data-scale numbers (repositories, issues, sample size). Plain palette (black/white/grey/blue or the tool's default). | `chat:group-raw@2026-09-28T00:15–00:42`, `…20:56`; `chat:group@2026-10-02T11:09`, `22:28`, `23:19` | G (2026 reviewer culture) | New. Upstream has "no chartjunk" and colour-blind rules, not "AI style" |
| FR6 | A figure is for information you cannot say in a sentence; agreement statistics and sample splits go in prose. | `chat:group-raw@2026-09-22T21:29` (Senior B) | G | New wording; consistent with handbook "text first" |
| FR7 | Presentation order: prose → figure → table; in kept tables bold the headline numbers. | `chat:1on1@2026-09-29T11:51`; checklist W8/TB5 (C-035 verbatim is an unverified relay) | G | Partly new |
| FR8 | A `tabular` must be a table, never a panel of a `figure`; split mixed composites. | `msr:0f96193` → `msr:405bba7` | V/G | New |
| FR9 | Do not shrink fonts locally (`\footnotesize`, small `\tabcolsep`) in tables or captions to fit; at SE venues this is a policy violation and a desk-reject risk. In plots, label text at least close to body size. | `chat:group@2026-10-01T09:20–09:23`; `msr:9809b8c` heatmap todo; `msr:94e651f`; FINAL G3, F6 | V | Strengthens upstream 8 pt rule ("similar to body text"; table shrinking named) |
| FR10 | One figure per RQ. An "alternative" figure stays only if it adds a finding; decide, do not keep both. | `msr:9809b8c` todo → `msr:7c705c9` → `msr:b3dafcd` → `msr:47221f7` | G | New |
| FR11 | Arrange bars so the comparison the RQ asks about is adjacent (one bar per issue type with repository shares inside, not one bar per repository). | `chat:1on1@2026-09-28T23:29–23:31` | G | Refines upstream "chart type matches data" |
| FR12 | For category × ecosystem shares use one heatmap with a pooled column and an equal-weight (balanced) column, and explain the colour scale and both columns in the caption. | `chat:1on1@2026-09-28T23:50`; `04-rq1.tex:139–140`; FINAL F3 | SE (multi-repository mining) | New |
| FR13 | When a panel is too small, enlarge the critical panel's text or rotate a panel before splitting the figure. | `chat:group@2026-10-03T11:32` | G | New (tip) |
| FR14 | Whenever a renderer changes, regenerate the PDF in the same commit; whenever a caption changes, re-read the figure; delete or regenerate previews with the PDF. | `ol:ba3f1ee` (RQ1, RQ3), stale preview via `msr:836ee75` | G | New. Upstream says "generated by code" only |
| FR15 | One source file per figure (no multi-figure `.drawio`); keep drafts outside the manuscript repo or in an ignored folder; record which draft won and why. | A.1 finding 3; `msr:e0ea09b` drafts; unused variants | G | New |
| FR16 | Figure renderers must run from the replication package: read the released data, no hard-coded counts, no path to a private sibling repo. | `render_rq1_alt_heatmap.R`, `render_rq1_d6_d7_donut.R:4–5`; FINAL H9 | SE (artifact evaluation) | New |
| FR17 | Labels inside figures follow the paper's label conventions by hand, because LaTeX macros do not reach figures. | checklist W10, F6; FINAL F6 ("Unknown", "Regression" capitalized) | G | Partly upstream ("names consistent") |
| FR18 | `\Description{}` for every ACM figure, and it must match the actual layout (side by side vs top/bottom). | FINAL H15; agent review MF-22 | V (ACM) | Partly new (layout match) |
| FR19 | Validation data is drawn as validation only: the gold sample never feeds the RQ boxes. | `sources/briefs/drawio-overview-brief.md` ("never connects to RQ outputs"); checklist MF-06, F2 | SE | New |
| FR20 | Agent-written figure plans and reviews are checked against the latest human feedback before execution. | `study-workflow-UPDATE-PLAN.md` vs `chat:group-raw@2026-09-28T00:19` | G | New |
| FR21 | An intro figure contrasts the failure modes the paper studies (here: valid proof rejected vs invalid proof accepted) and its caption scopes the architecture it assumes. | `chat:1on1@2026-09-28T23:15`; FINAL F1; `ol:ba3f1ee` caption | G (pattern), SE wording | Upstream "motivated example" covers the idea; scoping caption is new |

Observation, not a rule: Senior A's last pass replaced the long, number-carrying workflow caption with "Overview of the study." (`ol:ba3f1ee`). Upstream asks captions to be self-contained and to state the finding; for an overview figure the team chose brevity. One data point, low confidence.

## A.9 What the archive adds beyond upstream (figures)
Upstream gives design rules for a single figure (vector, ≥ 8 pt, colour-blind safe, self-contained caption, no chartjunk, tool matrix) and a high-fidelity reconstruction workflow. The archive adds: (1) the **process** of getting an overview figure accepted by seniors (AI sketch → native replica → redline → text-first sync), with its failure modes; (2) **data integrity of figures** (numbers in figures re-sourced, renderer/PDF/caption sync, runnable renderers in the artifact); (3) **AI-look** as a 2026 review risk; (4) **venue red lines** that touch figures (no local font shrinking, no tables disguised as figures, no appendix); (5) SE/MSR patterns (stratified heatmap with balanced column, validation-only gold in the workflow).

---

# PART B — Checklist evolution

## B.1 Version chain

| # | Date | File (archive path) | Author | Form | Items |
|---|---|---|---|---|---|
| 0 | 2026-09-29 | `10-requirements/paper-refs/CHECKLIST-DRAFT.md` (+ `SUMMARY.md` "Generated … 2026-09-29", `REFS.md`) | Student + agent | One-line checkboxes, IDs C/M/F/D/A/T/R + final, each tagged with a REFS id (H-Cx = Senior A comment lines, MG-10 = partner devil's-advocate review, CRITIQUE, B-x = BUILD) | 101 |
| 1 | 2026-09-29 | `01-checklist/versions/FULL-PAPER-CHECKLIST.v1.md` | Student + agent (merge of paper-refs, group chat, 1:1 chat, Cursor summaries; "later source wins") | One-line checkboxes in 9 sections + U1–U5 + Superseded table; all unticked | 140 |
| 2 | 2026-09-29 | `01-checklist/FULL-PAPER-CHECKLIST.md` "master v2" | Generated by `scripts/generate_checklist_v2.py` ("merges v1 + keyword provenance", `enriched/README.md`) from `enriched/{paper-refs,group-chat,jimmy-chat,cursor-history}.md` | Each item a block: What to check / Misreadings / Provenance (Who, Where, Quote) / Refs; IDs CF/MF/RS/RW/AH/TH/RP/CO/FP | 140 (texts identical to v1; 43 ticked: CF 6, MF 17, RS 11, RW 9) |
| 2a | 2026-09-29 | `05-figures-tables/METHODOLOGY-FIGURES-REVIEW.md`, `…ACTION-ITEMS.md`; `01-checklist/CHECKLIST-UPDATE-SUMMARY.md` | Agents | Verification passes over MF (17 ticked) and TH/RP ("can mark [x]", not applied in the archived v2) | — |
| 3 | 2026-10-01 00:41 | paper-repo `checklist.md`, `msr:0c0dae0` (+415) | Student + agent | New format: G/W/C/A/R/AT/F/TB/T in 9 categories; each item: what, how to check, why, source, Blocker/High/Medium; snapshot pinned to `msr:f198041` | ≈ 77 |
| 3a | 2026-10-01 00:58 | `04-comms/20260929-1007-wechat-group/media/checklist.md` | Student shares in group: "我根据历史聊天和我们的文件和我们敲定的东西，大概做了个 checklist" | State of `msr:f1c7df8` (10-01 00:51) | same |
| 4 | 10-01 → 10-03 01:30 | `checklist.md` edits: `msr:f1c7df8`, `55ed3d0`, `ed9f21e`, `464168f`, `ff0108e`, `c8adb43`, `3e7bab0`, `9c69675`, `9c4567c`, `59f15be`, `e0ea09b` | Student (+ agent) | Venue facts filled from the official call; author rules added; decisions logged (T2, T3, T5, T8) | `01-checklist/checklist.md` = state at `msr:e0ea09b` |
| 5 | 2026-10-02 | `01-checklist/FINAL-CHECKLIST-2026-10-02.md` | Agent, read-only, against `msr:59f15be` + uncommitted edits | Status table for all 77 checklist.md items + blockers + writing/rhetoric/consistency/devil's-advocate audits | 77: PASS 27, FAIL 11, PARTIAL 34, OPEN-DECISION 3, N/A 2 |

v1/v2 files later travelled with `local-refs/` (tracked `msr:f1c7df8`, untracked `msr:c8adb43`, re-imported as `.bak4–.bak9` by the Overleaf merge `msr:836ee75`). No evidence that anyone worked from v2 after `checklist.md` appeared; `checklist.md` cites v2 only indirectly (enriched J-/GC- ids).

## B.2 Added, removed, superseded, and why

**v1 → v2.** No item text changed (140/140 identical after whitespace normalization). v2 added machine-generated blocks and ticked 43 items; ticks came from agent verification passes (A.7 / 2a). U1–U5 grew from one table to sections with options; U1 now lists four κ values (0.65 gate, 0.74 "two-author … design step 7", 0.81, 0.76 "figures/chat").

**v2 Superseded appendix (10 rows):** four-panel overview → single three-phase figure; gold/prompt agreement as figure → prose; RQs only in Design → full RQs in intro; Overleaf-newer → "git main newest"; strip all numbers from the figure → keep dataset-scale numbers; Student waits for B → parallel editing; "a table for every result" → heatmaps/merged/narrative; senior comments target old Overleaf → current PDF; edits on backup branch → main only; composite `rq2_rq3_overview.pdf` → table + stacked bars. Two of these were themselves superseded later: "git main newest" (reversed 10-03, notes/04 §1.5) and the table + stacked-bars composite (dismantled by `msr:405bba7`).

**v2 → checklist.md (10-01).** Dropped as a category: Advisor (AH) and the per-item provenance blocks; dropped items that were project-mechanics only (sibling paths RP-01..03, specific bib keys RW-08/09, PR #2 CO-09, project id CO-03). Added (not in v2): official venue facts (G2 page limit from the call, G3 template class and package list, G8 Data Availability, G9 AI-use description, G10 submission-system accounts), the whole Attachment category AT1–AT7 (replication repo, anonymous mirror, identity traces, artifact citation, promises vs repo, page = paper, nothing private), "every citation supports its sentence" (R3, Blocker), parked-float decisions (TB2), marker tracker (T1), Adams/SAIL rhetoric (W5), an explicit tie of figure to Design (W6, "highest priority").

**Changes inside checklist.md (10-01 → 10-03):**
| Commit | Change | Why |
|---|---|---|
| `msr:464168f` 10-01 18:58 | Page limit, template, deadline filled from the call; G7 "appendix holds only what a reviewer needs" ticked; TB3 label table moved to package; AT2/AT3 become Blockers | Venue call fetched 10-01; Senior A 10-01 08:47–08:56 (no appendix) |
| `msr:ff0108e` 10-01 21:20 | G3 package list, sample `\acmConference`; G10 HotCRP; R5 ACM BibTeX format | Official template downloaded |
| `msr:c8adb43` 10-01 22:07 | C3 decided: print pooled 0.81 and three dimensions; `local-refs` gitignored again | Author decision; private material leak (notes/08 §1.3) |
| `msr:3e7bab0` 10-02 00:25 | C5: drop "about six times" | Agent review C7 |
| `msr:9c69675` 10-02 02:16 | **Rule: print κ only when ≥ 0.65**; denominators and import-time closures | Author rule |
| `msr:9c4567c` 10-02 04:45 | KM only in Threats; R5 all uncited entries commented out | — |
| `msr:e0ea09b` 10-03 01:30 | W10 rule "dataset, never snapshot or corpus; import-time closures, never migration artifacts" | Senior A `\todo`s in `msr:0f96193` |

**FINAL-CHECKLIST (10-02)** adds what no earlier list had: two Blockers (B1, B2), 19 high-priority items (H1–H19: first-run-only κ rule broken, Simpson-type pooling, cohort reversal, contribution over-claim, scope of "cores vs libraries", evidence parked in comments, conclusion longer than abstract, stale mirror, overclaimed Data Availability, duplicated caveats, gold-not-oracle threat missing, wrong `\Description`, overfull boxes, effect-size adjective, synonym drift), a 14-point cross-section mismatch list, and a devil's-advocate review.

## B.3 Status at submission

- **B1 — κ = 0.74 and "two authors independently annotate all 582 issues" untraceable.** First flagged by an agent on 09-28 (`02-comments-hao/adams-skill-revision-comments.md` C12 [P0]: dual coding "not found … [AUTHOR: where are <Senior B>'s labels and the 0.74 script?]"; C4: "Human–human per-dimension κ (the 0.74 breakdown) was not found"). Same evening the Student asked Senior B; reply "我这边儿对了，没事儿，你不用担心这个" (`chat:1on1@2026-09-28T20:16–20:17`). v2 RS-17 ("one consistent κ story", 0.76 vs 0.81) was ticked [x] anyway; `checklist.md` C2 then fixed 0.74 as "two authors labelling the gold sample", source "<Senior B> (κ verified by the authors)". FINAL B1 (10-02) re-raised it with `design_validity.json` "not computable: no pre-adjudication labels from two human annotators". The claim is still in `09-paper-snapshot/sections/03-design.tex:97` and intro `:53`; `ol:ba3f1ee` does not touch it. **No evidence of resolution**; no evidence of what the submitted PDF says (notes/04 §1.6, notes/08 §2.2). New here: the number's earliest appearance is Senior B's reference figure image of 09-27 17:36 (A.1 finding 1).
- **B2 — replication `index.html` names all authors.** FINAL B2 (10-02, latent: mirror served an older clean page). Acted on only after Senior A's warning: "不用index html，readme完整就好 … 这个容易暴露双盲导致desk rejeck" (`chat:group@2026-10-06T05:09`); Senior B: put it in `.gitignore` (`09:44`); Student "搞定了" (`11:57`). **Fixed 10-06, three days after the deadline**, in the window before reviewers would open the artifact (notes/08 §2.7).
- **Other FINAL items:** no record of item-by-item closure. Spot checks against `09-paper-snapshot` (`msr:87bf139`): H15 heatmap legibility addressed (`msr:94e651f`); F4/H15 composite split (`msr:405bba7`); H1 (two runs printed) still open (`03-design.tex:112`, `main.tex:171`, notes/08 §2.3); T1 markers: `%% PARKED` blocks remain (notes/06b). Final page count: NO EVIDENCE.
- **checklist.md at its last commit (`msr:e0ea09b`):** ticked only G7, C5, TB3, T2, T3, T5, T8; every other item, including the Blockers G2, G3, G8, G10, R3, AT2, AT3, is unticked. Ticks were not used as the completion record in the final 48 h; FINAL's status table was.
- **v2 TH/RP:** `CHECKLIST-UPDATE-SUMMARY.md` says TH-01..11 and RP-01..09, 11 "can mark [x]"; the archived v2 shows them unticked. RP-12 (record the data-repo SHA) stayed a placeholder "[INSERT SHA HERE …]".

## B.4 Provenance audit (v2 "Who" lines and checklist.md "Source" lines)

How v2 provenance was made: by keyword matching (`generate_checklist_v2.py`, `enriched/README.md`). 90 of 140 v2 items carry a Who label that pairs **Senior A's given name with the Student's Chinese name** in parentheses (counted from the `**Who:**` lines). The same conflation appears in the 1:1 chat summary header, which calls the Student's name the "导师" whose comments Senior B relays (`04-comms/past-chat-jimmy/SUMMARY.md:4`), and in v1 ("C-020 (<Senior A> via <Senior B>)"). The likely root: an agent-written summary mis-identified the relayed advisor and the Student. INFERRED.

Sample (44 rows covering 55 item IDs). Verdicts: **OK** (person and source verified), **WRONG-PERSON**, **AGENT→HUMAN** (agent output labelled as a senior's comment), **UNVERIFIED**, **TICKED-CONTRADICTED**.

| ID | v2 Who / checklist.md Source | Verified source | Verdict |
|---|---|---|---|
| CF-01 | Senior-A-name (Student-name); group | Quote "Why should I care about issue trackers in proof assistant?" = `02-comments-hao/comments_hao.md:18` (Senior A). "RQs in intro" = Senior B, `chat:group-raw@2026-09-22T23:40` | WRONG-PERSON (label), content OK |
| CF-03 | group | Senior B, `chat:group-raw@2026-09-22T23:40` ("最好在开头引出来") | OK (B, not A) |
| CF-05/06 | Senior A label | `comments_hao.md` §2.3 (lines 54–75) | OK person, label string wrong |
| CF-08 | Senior A label | `comments_hao.md` §2.4 (lines 79–100) | OK |
| CF-12 | Senior A label + partner DA | Partner devil's-advocate review MG-10 (`11-*/tree/docs/partner/…/da-review-2026-09-22.md`); severity wording first raised by the Student (`chat:1on1@2026-09-28T23:12`) | WRONG-PERSON |
| CF-13 | Senior A label + partner DA | MG-10 C2 (DA review) | WRONG-PERSON (task-cited case) |
| CF-14 | Senior A label + partner DA | MG-10 C1; κ gate rule is the research-repo protocol | WRONG-PERSON (task-cited case) |
| CF-15 | Senior A label + partner DA | MG-10 M2 | WRONG-PERSON |
| CF-16 | Senior A label | `CHECKLIST-DRAFT.md` C18 cites "CRITIQUE MAJOR 3" (`11-*/…/CRITIQUE-2026-09-22.md`) | WRONG-PERSON |
| CF-17 | Senior A label | DA review m2; but "Contrary to the common intuition" is Senior A's suggested phrasing (`comments_hao.md:67`) | PARTIAL |
| CF-23 | Senior B | `chat:1on1@2026-09-29T00:24` (Student raised it, B: "需要去掉所有的分号和破折号") | OK |
| CF-24 | Senior B | `chat:1on1@2026-09-22T05:02` (pasted rule); labelled "MSR", venue was FSE (checklist.md G2 corrected it) | OK, venue name stale |
| CF-26..28 | Senior B; text "C-020 (<Senior A> via <Senior B>)" | Relayed advisor, `04-comms/20260926-jimmy-advisor-paper-glimpse/README.md` §2 | WRONG-PERSON |
| CF-29 | Student + agent; text "(<Senior A> C2 theme)" | `adams-skill-revision-comments.md` C2 (agent, 09-28) | AGENT→HUMAN |
| CF-30 | Student + agent; text "(<Senior A> C3)" | Agent C3; denominator idea also in `comments_hao.md:40–43` | AGENT→HUMAN (partly A) |
| MF-01 | group | Senior A, `chat:group@2026-09-29T11:40–11:42`; `msr:9809b8c` | OK |
| MF-02 | group | Senior A, `chat:group@2026-09-29T11:47`; todo in `msr:9809b8c` | OK; outcome: not drawn (A.1) |
| MF-03 | B; group | Senior B, `chat:group-raw@2026-09-27T15:55` | OK |
| MF-04 | group | Senior A `…09-28T00:19–00:42`; Senior B `…20:56` | OK |
| MF-05 | group | Senior B, `chat:group-raw@2026-09-22T21:29` | OK (B) |
| MF-06 | Senior B | Agent brief `drawio-overview-brief.md`; 1:1 SUMMARY; not in raw chat | UNVERIFIED |
| MF-07 | Senior B; agent | `chat:1on1@2026-09-28T23:15` | OK |
| MF-09 | Senior A label | Not in `comments_hao.md` (no κ there); bar 0.65 from research repo (`overlay-high14-review.md`), print rule = author 10-02 (`msr:9c69675`) | WRONG-PERSON |
| MF-14 | Senior B | `04-comms/past-chat-jimmy/raw/jimmy-main-pdf-comments/` (P-01..P-13) | OK |
| MF-16 | Senior B, "C-035" | Verbatim relay not in export (USR-001, notes/04 §4); closest `chat:1on1@2026-09-29T11:51` | PARTIAL |
| MF-18 | Senior B | `chat:1on1@2026-09-28T16:43` (Table 5/6 appendix); superseded by Senior A 10-01 | OK, superseded |
| RS-07 | Student + agent | Cursor thread `257c0222` (`cursor-history-chat/MERGED-SUMMARY.md` row "show all strategies"); item says "(dim 3)" but strategy is D5 | TICKED-CONTRADICTED (final caption merges "other strategies") |
| RS-08 | Student + agent | same thread | TICKED-CONTRADICTED (layout dismantled by `msr:405bba7`) |
| RS-11 | Student + agent | same | Superseded (`msr:47221f7`) |
| RS-12 | Senior B | `chat:1on1@2026-09-28T23:29–23:50` | OK |
| RS-17 | Senior B; agent | B's assurance `chat:1on1@2026-09-28T20:17`; 0.76 from Student's sketch (A.1 item 3); 0.74 from B's image | TICKED-CONTRADICTED (no computation exists) |
| RS-19 | Student + agent; text "<Senior A> C12" | Agent C12 [P0] | AGENT→HUMAN |
| RW-01 | group | Senior A, `chat:group@2026-09-29T11:30` + shared PC scan | OK |
| RW-04 | Senior A label; group | Senior A, `chat:group@2026-09-29T11:44` (DBLP, desk reject) | OK person |
| AH-02 | Senior A label; agent | Senior A, `chat:group@2026-09-29T12:26` ("标签这种最好让agent用宏") | OK person, wrong source file |
| AH-04 | Senior A label | `comments_hao.md:3` | OK |
| RP-11 | Senior A label | `BUILD.md`; executed by agent (`CHECKLIST-UPDATE-SUMMARY.md` 42/42 cells) | WRONG-PERSON |
| CO-01 | agent; group; Senior A label | Student's own practice `chat:group@2026-09-29T12:40`, never a group decision; reversed 10-03 | CONTRADICTED (end state) |
| CO-02 | Senior B; Senior A label | Senior B, `chat:1on1@2026-09-29T11:10` | OK (B) |
| CO-08 | Senior B | `chat:1on1@2026-09-27T23:21` | OK |
| checklist.md C9 | "<Senior A>, C-020" | Relayed advisor | WRONG-PERSON |
| checklist.md C2 | "<Senior B> (κ verified by the authors)" | Only a chat assurance | UNVERIFIED (load-bearing) |
| checklist.md G10, AT1, AT4 | "<Senior B>, WeChat 2026-10-01 17:28", "2026-09-29 20:29 and 21:48" | Not in the group export and after the 1:1 export ends (09-29 12:53) | UNVERIFIED |
| checklist.md W1–W4, W11 | "<Senior A> 2.2 … 2.8" | `comments_hao.md` §2.2–2.8 | OK |

Tally by row (44): OK 21 (several with a wrong label string), WRONG-PERSON 10, AGENT→HUMAN 3, TICKED-CONTRADICTED 3, UNVERIFIED 3, PARTIAL 2, superseded/contradicted 2. Pattern: items that came from agent reviews (Adams-skill C1–C12, devil's-advocate MG-10, CRITIQUE) were relabelled as Senior A's, which inflates the senior's authority behind agent suggestions. The hand-written `checklist.md` is much better (W-items, G-items cite real lines), but two load-bearing sources are wrong or unverifiable (C2, C9).

## B.5 Classification of reusable items into target checklists

Each row: generalized wording · original IDs (`v2` = FULL-PAPER-CHECKLIST v2, `cl` = paper-repo `checklist.md`, `FIN` = FINAL-CHECKLIST, `draft` = CHECKLIST-DRAFT) · verified provenance. "Agent" = agent-generated source, verified to exist.

### master (gate items every paper needs)
| Generalized item | IDs | Provenance |
|---|---|---|
| Run a read-only full pre-submission check at least one day before the deadline; treat its Blockers as stop-ship and assign each an owner | FIN B1/B2; cl T14 | FIN itself; notes/08 rule 37 |
| No reviewer-visible marker remains (`\todo`, `%TODO`, placeholders, parked blocks decided) | v2 FP-07; cl T1, TB2, G5 | Senior B `%TODO`s `chat:1on1@2026-09-28T23:15`; FIN T1 |
| Abstract, intro preview, RQ answers, takeaways and conclusion state the same findings, scope words, denominators and numbers | cl A5; FIN §5 | `se-paper-refinement` 9 (agent skill); Senior A 2.4 |
| A devil's-advocate pass lists the strongest objections from the paper's own numbers | FIN §6; cl T14 | Agent; skill `se-paper-reviewer` |

### writing
| Generalized item | IDs | Provenance |
|---|---|---|
| Lock a term table; one name per concept; never switch | v2 AH-01, AH-04, FP-01; cl W10, TB4 | `comments_hao.md:1–3` |
| Introduction answers the outsider question (why this artifact matters to the venue's audience) before methods | v2 CF-01; cl A2 | `comments_hao.md:8–29` |
| State all RQs in full in the introduction | v2 CF-03; cl A2 | Senior B `chat:group-raw@2026-09-22T23:40` |
| Why before how for every method choice | v2 MF-10, AH-07; cl W1 | `comments_hao.md:33–50` |
| No "study plan"/execution framing; outward scientific framing | v2 CF-05, CF-06, AH-08; cl W11 | `comments_hao.md:54–75` |
| Number diet: per results paragraph ≤ 1 proportion, 1 contrast, 1 effect, 1 implication; exact counts in tables | v2 CF-07, CF-08, AH-09; cl W3; FIN W3 | `comments_hao.md:79–100` |
| Each RQ section: question → why → minimal method → 1–2 findings → implication; open with the substance | v2 CF-09, CF-10, AH-10, AH-11; cl W2 | `comments_hao.md:104–120, 141–157` |
| State each caveat once, in methods or threats | v2 CF-11, AH-12; cl W4; FIN H11 | `comments_hao.md:158–171` |
| Paragraphs build on each other (no listicle structure) | v2 CF-22; cl W7 | Senior B `chat:1on1@2026-09-28T23:14` |
| De-AI pass on prose (no semicolons/em dashes per team rule, no tier-1 vocabulary, no templated paragraphs) | v2 CF-23, FP-06; cl G1, W11; FIN §3 | Senior B `chat:1on1@2026-09-29T00:24`; Senior A on AI style `chat:group-raw@2026-09-28T00:15` |
| No claims about unmeasured constructs (e.g. severity when no severity was coded) | v2 CF-12; cl W9 | Student `chat:1on1@2026-09-28T23:12`; DA review (agent) |
| Results do not carry implications; implications add no new numbers or unmeasured mechanisms | cl C6; FIN H4, C6 | Agent C8; `se-paper-refinement` 4c/4d |
| Effect-size adjectives match a stated scale | v2 RS-02; FIN H18 | Agent |
| Conclusion: one paragraph, shorter than the abstract, one sentence per RQ, ends on a research direction | cl A4; FIN H7 | `se-paper-writing`/`se-paper-refinement` (skills); provenance of the rule to a human: unverified |
| Gap claim scoped ("to our knowledge"), stated once, after what prior work does | v2 CF-21; cl A3, R4, W9 | Agent C11; group "soften absolutes" (Senior A, `chat:group@2026-09-29T11:30` with PC scan) |
| Every citation supports its sentence (open the paper) | cl R3 (Blocker) | Venue call (fabricated citations = desk reject); Student/Senior B per cl (unverified) |
| References verified against DBLP/publisher; keep the audit output | v2 RW-04..07, RW-13; cl G4, R5 | Senior A `chat:group@2026-09-29T11:44`; audit `chat:group@2026-10-03T19:18` |
| Uncited bib entries removed or commented; keys resolve | v2 RW-11; cl R5 | Senior B compile errors (per cl; unverified) |
| Single term for each measure across abstract/intro/RQs (e.g. one name for fix size) | FIN H19 | Agent |
| Label names via macros in prose; check spacing in the PDF | v2 AH-02, AH-03; cl W10 | Senior A `chat:group@2026-09-29T12:26`; Cursor thread 085dba30 (agent) |
| Learn how venue papers introduce your niche domain from a named exemplar | v2 CF-04 | `comments_hao.md:4` |

### figures
FR1–FR21 above, plus:
| Generalized item | IDs | Provenance |
|---|---|---|
| Each overview box ↔ same-named, numbered Methods step, both directions | v2 MF-01; cl W6, F2 | Senior A (A.1 items 11, 14, 16) |
| Overview is one integrated figure, not panels | v2 MF-03; cl F2 | Senior B `chat:group-raw@2026-09-27T15:55` |
| No AI micro-labels; consistent text style; keep dataset-scale numbers only | v2 MF-04; cl F6 | Senior A/B 09-28 |
| Agreement and splits in prose, not a figure | v2 MF-05 | Senior B 09-22 21:29 |
| Fewer standalone tables; text → figure → table; bold headline cells | v2 MF-15, MF-16; cl W8, TB1, TB5 | Senior B `chat:1on1@2026-09-29T11:51` |
| Intro failure-mode figure exists and is legible | v2 MF-07; cl F1 | Senior B `chat:1on1@2026-09-28T23:15` |
| Inverted bars; merged panels as a heatmap; colour scale in caption | v2 RS-12; cl F3 | Senior B 09-28 23:29–23:50 |
| Captions state what is shown, the denominator and how to read colour, and do not repeat a table | v2 MF-21; cl F6, TB6 | `comments_hao.md:79` ("DO NOT repeat the numbers in the table"); Senior A |
| No retired or superseded figure referenced; no figure needed for compile is git-ignored | v2 MF-20, MF-23, MF-24; cl F6 | `BUILD.md` (agent-checked) |
| Regenerate figure PDFs whenever a renderer or its data changes | v2 RS-09, RP-11, RP-13; cl F6 | `BUILD.md`; Senior B `chat:1on1@2026-09-28T15:15` (data owner reruns) |
| Senior review of the finished overview together with Methods | v2 CO-08; cl W6, F2 | Senior B `chat:1on1@2026-09-27T23:21` |
| Every coded dimension is shown or explicitly scoped out, with its denominator | cl F5, C11 | Senior B (per cl; unverified in raw chat) |

### threats-to-validity
| Generalized item | IDs | Provenance |
|---|---|---|
| Scope every general claim (ecosystems covered, dominant contributor, missing major ecosystem) in claims and in Threats | v2 CF-16, TH-02, TH-03, TH-10; cl C7 | Advisor (relayed) on the missing ecosystem; CRITIQUE (agent) |
| Small held-out counts for rare classes disclosed next to claims that use them | v2 CF-15, TH-04 | DA review (agent) |
| Low-agreement dimensions are described as classifier readings, not as ground truth | v2 CF-14, TH-05; cl C3 | DA review; author rule 10-02 |
| Gold labels are a consensus of study authors, not an oracle; corrections that assume a perfect reference say so | v2 TH-09; FIN H13; cl W5 | CRITIQUE-2026-09-22 line 59; Adams skill |
| Alternative explanations named (triage priority, closure culture) | v2 TH-07, TH-08 | Unverified (draft/critique) |
| Selection effects of filtered subsets stated where their rates are cited | v2 RS-16 | Unverified |
| Do not drop results that contradict the framing | v2 CF-18 | CRITIQUE minor 5 (agent) |
| A threat statement and the results agree (e.g. "we report per repository before pooling" is actually done) | FIN H12 | Agent |
| A cited comparison notes when the measures differ | v2 CF-19 | CRITIQUE minor 4 (agent) |

### double-blind / anonymity
| Generalized item | IDs | Provenance |
|---|---|---|
| The PDF links only the anonymous mirror; never a personal page, account or lab URL | cl AT2; FIN AT2 | Senior B `chat:group@2026-10-02T00:45` |
| Grep everything a reviewer can open (paper, repo, README, LICENSE, project page, repo description, account name, PDF metadata, image EXIF) for names, affiliations, domains, labs | cl AT3; FIN B2, AT1, AT3 | Venue call; FIN B2 → `chat:group@2026-10-06T05:09` |
| Prefer a complete README over a rendered project page in the anonymous artifact | — (new from chat) | Senior A `chat:group@2026-10-06T05:09` |
| Refresh the mirror after every artifact change and re-grep the mirrored copy | cl AT2; FIN H8 | Agent; Senior B (per cl, unverified) |
| Artifact name and citation do not name the venue and survive a later arXiv version | cl AT4 | Senior B per cl (unverified) |
| Self-citations in third person; no acknowledgements; arXiv version does not mention the venue | cl AT3 | Venue call |
| Private material (chats, other papers, notes) never tracked in the manuscript or artifact repo | v2 CO-10 (inverse); cl AT7 | notes/08 §1.3 (`msr:f1c7df8` → `msr:c8adb43`) |

### artifact / replication
| Generalized item | IDs | Provenance |
|---|---|---|
| What the paper promises (dataset, codebook, gold, prompts, labels, scripts) is in the package; no "recomputes every number" unless true | cl AT5; FIN H9, AT5 | Agent number audit; Student/Senior B chat 10-03 20:20–20:24 |
| All analysis code used for printed numbers moves to the package the same day it is written | — | `chat:group@2026-10-03T20:20–20:22` |
| Package is not empty on day one after the deadline | — | Senior A `chat:group@2026-10-03T23:16` |
| Large data on a data host, listed in a manifest | — | Senior B `chat:group@2026-10-03T20:24` |
| Clean build from a fresh clone; build doc matches the figure set | v2 RP-05, RP-06; cl G5 | `BUILD.md`; agent verification |
| No frozen data copied into the manuscript repo; no secrets, DBs or tokens committed | v2 RP-04, FP-04, FP-05; cl AT7 | `BUILD.md`; agent |
| Data Availability section present and accurate | cl G8; FIN G8 | Venue call |
| Project page (if any) equals the final paper | cl AT6; FIN H8 | Agent |

### venue-formatting
| Generalized item | IDs | Provenance |
|---|---|---|
| Page limit checked on the compiled PDF, incl. what counts (appendix inside the limit) | v2 CF-24, FP-02; cl G2 | Senior B `chat:1on1@2026-09-22T05:02`; venue call |
| Official template, class options and fonts untouched; no local font or spacing shrinking | cl G3; FIN G3 | Senior B/A `chat:group@2026-10-01T09:20–09:23` |
| No appendix used as padding at venues whose limit includes it; definitions to the package with a pointer and a compact table | v2 MF-17/18 (superseded); cl G7, TB3 | Senior A `chat:group@2026-10-01T08:47–10:09`, `…10-02T01:51` |
| `\Description` on every figure, matching the layout | v2 MF-22; FIN H15 | ACM; agent |
| Clean log: no undefined refs, no overfull boxes | cl G5, TB7; FIN H16 | Agent |
| Submission-system metadata (authors, conflicts, topics, corresponding author) done a day early; abstract field plain text | v2 FP-03; cl G10 | `chat:group@2026-10-03T17:28–18:43` (notes/08 §3) |
| Venue facts re-fetched from the official call into a dated file | cl header, T5 | `10-requirements/venue/fse-2027-requirements.md` |
| AI use in the research method is described in Methods | cl G9 | Venue call |

### collaboration / records
| Generalized item | IDs | Provenance |
|---|---|---|
| Declare one writable source of truth per phase; record every switch in the repo | v2 CO-01; cl G6 | CONTRADICTED as written (git main); lesson from notes/04 §1.5 |
| Pushing to git does not update the co-edited copy; sync explicitly and check it | v2 CO-02 | Senior B `chat:1on1@2026-09-29T11:10` |
| Sync filters keep non-manuscript files out of the shared editor | v2 CO-04 | `msr:c93ef1f` |
| A senior's bulk edit is checked against earlier agreed requirements before merging | v2 CO-07 | Student `chat:group@2026-09-29T12:10` |
| Agents commit only when the human asks; agents stay out of sections the human fenced off | v2 CO-05, CO-06 | Cursor threads (agent rules) |
| Co-author annotations (PDF comments) are tracked item by item to closure | v2 MF-14; cl T10 | `jimmy-main-pdf-comments/` |
| Senior comment drops are committed and their resolution is visible (separate macro for items only the student may resolve) | v2 AH-13; cl T1 note | `msr:9809b8c` protocol |
| Requirement packs keep an explicit superseded table; latest wins | v2 CO-10, Superseded appendix | group/1:1 SUMMARY files |
| Checklist provenance is written by hand from primary sources; machine-matched provenance is marked unverified | — (lesson from B.4) | This audit |
| Ticks record evidence (commit, check output), not intent | — (lesson: RS-07/08/17 ticked, TH/RP unticked though verified) | This audit |
| Open decisions live in a register with options and owner | v2 U1–U5; cl T2–T8 | `10-requirements/DECISION-HINTS.md` |

### experiment-integrity (gold freezing, agreement numbers, number-to-script traceability)
| Generalized item | IDs | Provenance |
|---|---|---|
| Every printed count traces to the frozen data through a named script; the same number is printed identically everywhere | v2 MF-11, RS-04, RS-05, RP-11; cl C1 | Agent verification (42/42 cells) |
| Record the data/code commit SHA used for every number | v2 RP-12 | `CHECKLIST-UPDATE-SUMMARY.md` (left as placeholder) |
| Every agreement statistic has raw independent label sets and a rerunnable script in the package; otherwise rewrite the method | v2 RS-17 (ticked wrongly); cl C2; FIN B1 | Agent C12 [P0] 09-28; FIN B1 |
| One κ story: name which comparison each κ is (human–human, model–gold, reporting bar); never merge | v2 RS-17, U1; cl C2 | Agent; Senior B assurance only |
| A reporting rule for agreement (e.g. print only ≥ bar; first run only) is written down and applied everywhere incl. Data Availability | cl C3; FIN H1 | Author rule `msr:9c69675` |
| Freeze codebook, gate order and gold before evaluating the model; disclose any later gold edit made after seeing model output | v2 MF-08, RS-19; cl C3 | Agent C12; `overlay-high14-review.md` (notes/08 §2.2) |
| Frozen-input identifiers (snapshot date, gold id, codebook version) printed consistently | v2 RS-14, RP-07..09 | Agent |
| Analysis follows the planned tests; no unplanned post-hoc | v2 RS-01, RS-03 | Agent (paper-refs) |
| Numbers inside figures come from the same scripts as the text | FR3, FR16 | A.1 finding 1 |
| Pooled claims stratified first (no Simpson-type pooling) | FIN H2; cl W5 | Agent; Adams skill |

### field-SE-specific (MSR / issue mining)
| Generalized item | IDs | Provenance |
|---|---|---|
| Motivate the study through SE maintenance/evolution uses (bug datasets, triage, repair benchmarks, mining validity) | v2 CF-02; cl A2 | `comments_hao.md:122–140` |
| Closed ≠ fixed: report all-closed and fixed-only denominators, motivate both first, name the denominator wherever cited | v2 CF-30, TH-01, TH-11; cl C5 | `comments_hao.md:40–43`; author decision 10-01 |
| Time-to-close is calendar time, never effort/labour/cost | v2 CF-29; cl C4 | Agent C2 (Adams rule) |
| Censoring of open issues acknowledged (KM or statement) | v2 TH-06 | Agent; `msr:9c69675` |
| Tracker imports/migrations create artificial closing times; detect and set aside for duration analyses | cl W10 rule, C1; v2 TH-02 | `msr:9c69675`; Senior A term todo `msr:0f96193` |
| Residual "other" class is a result (size, where it concentrates) | cl C8 | Agent C9 (Adams) |
| Repository labels are not study labels (keep tracker `bug` label distinct from coded type) | v2 AH-06 | `tab:terms` (unverified human) |
| Codebook provenance per dimension (built, borrowed, model-proposed) | v2 CF-26; cl C9 | Advisor (relayed) |
| Cross-domain baseline and expected/surprising contrasts discussed | v2 CF-28; cl C9 | Advisor (relayed) |
| Related work covers what the likely PC members published; position the closest paper exactly | v2 RW-01, RW-02; cl R1, R2 | Senior A `chat:group@2026-09-29T11:30` |
| Benchmark RQ methods against the closest empirical papers before adding tests | v2 RS-18 | group SUMMARY req 8 (raw unverified) |
| Text-only coded strategy says nothing about code size; check against diffstats | v2 CF-13; FIN H4 | DA review MG-10 (agent) |
| Every test in Design has its value in Results and a one-clause gloss for SE readers | cl C10 | Student (per cl) |

### project-specific, not reusable
v2: CF-04 (specific arXiv exemplar), CF-20, CF-27 (§3.1 "~400"), MF-12, MF-13, MF-17, MF-19, RS-06, RS-07, RS-08, RS-10, RS-11, RS-13, RS-15, RW-03, RW-08, RW-09, RW-10, RW-12 (method-borrow corpus), RP-01, RP-02, RP-03, RP-10, RP-13, CO-03, CO-09; cl R1 (named MEDIUM papers), T2–T13 (decisions of this paper), TB2 P-mapping, C11 dimension list; FIN H2–H6, H14, H19 contents (the generic lessons are lifted above). U2 (artifact names), U4, U5.

## B.6 What the archive adds beyond upstream (checklists)
Upstream `verification-checklist.md` checks one delivery for invented facts, citations, AI trace and format; `pre-submission-reviewer` scores macro logic, writing, grammar, LaTeX and figures. Neither has: (1) **venue hard-fail items** fetched from the call (page rule incl. appendix, untouched template fonts, Data Availability, AI-use in methods, submission-system metadata); (2) a **double-blind/artifact** sub-checklist (mirror-only links, identity grep across every reviewer-visible file, README over project page, artifact non-empty after the deadline); (3) **experiment integrity** (agreement numbers backed by raw label sets and scripts, one κ story, frozen gold, number → script → SHA, figures' numbers from scripts); (4) MSR rhetoric (closed ≠ fixed, calendar time ≠ effort, residual class, migration artifacts, stratify before pooling); (5) **checklist hygiene** itself: provenance written from primary sources, agent-origin marked, ticks backed by evidence, a dated read-only final check whose Blockers get owners. The archive also shows the cost of skipping (5): a ticked item (RS-17) hid the one claim that FINAL later called a desk-reject risk.

## B.7 No evidence / open
- Whether B1 changed in the submitted PDF; the final page count; whether Senior A approved the final workflow figure.
- Who generated Senior B's 09-27 reference image and with which tool ("我给你生成一个样子" is the only statement).
- Which figure Senior A's 10-02 21:49 "去一下ai味" targeted.
- Source of checklist.md G10/AT1/AT4 chat quotes (10-01 17:28; 09-29 20:29/21:48): outside both chat exports.
- Who ticked the 43 v2 items (agent reports claim 17 MF ticks; the rest unattributed).
