# 06 — Section evolution (SE/MSR empirical paper case)

Private Phase-2 note. Evidence archive: `~/Projects/supervisor-skills-msr-tpa` (HEAD `669b29a`). Paths are relative to the archive root. Times are Asia/Shanghai (UTC+8) unless a patch offset is quoted. Citation formats follow `03-archive-map.md` §4: `msr:<sha>` = `07-overleaf-history/patches-msr-tpa/*_<sha>.patch`, `ol:<sha>` = `07-overleaf-history/patches-overleaf/*_<sha>.patch`, `chat:group@…` = `04-comms/20260929-1007-wechat-group/messages.jsonl`, `chat:1on1@…` = `04-comms/past-chat-<B>/raw/chat-history-merged.txt`.

Roles only: **Student** (first author, implementation, most drafting), **A** = Senior co-author A (written comments `02-comments-<A>/comments_<A>.md`, two in-repo comment drops, final Overleaf pass), **B** = Senior co-author B (repo/Overleaf owner, restructuring, methods figure, page budget), **Advisor (relayed)**. "Unknown" = Overleaf `Anonymous` or a sync/merge commit made under B's account whose real author cannot be resolved. The name mapping is in `private/CASE.md`.

Sources merged here: the stopped run's `notes/partial/06-section-evolution.PARTIAL.md` (phase map, title/abstract) and three helper reports (`06a` RQ1, `06b` design, `06c` RQ2/RQ3). Helper claims were spot-checked against patches (§0.3). Sections intro, related work, implications, threats, conclusion, appendix/terms and Data Availability were mined directly for this note.

Privacy: paper text is quoted only because this note is private. `[ID]` marks an excerpt that would identify the paper if reused publicly; §4 lists all of them.

---

## 0. What "final" means, and the evidence traps

### 0.1 Three different "final" states

| State | Where | What it is |
|---|---|---|
| Git snapshot | `09-paper-snapshot/` = `msr:87bf139` (10-03 19:38) | Last paper-repo commit. Section files match `msr:87bf139`. **Exception:** the snapshot `main.tex` abstract (14 sentences, ~274 words) is not the `msr:87bf139` abstract (6 sentences). It is the Student's Overleaf edit made after the 19:39 overwrite ("我直接 overleaf 改了", `chat:group@2026-10-03T19:44`). Its sentences reappear only as `%` comment lines inside `ol:ba3f1ee` |
| PDF uploaded at the deadline | Submission site, 10-03 19:56 | Title already "Maintaining Proof Assistants…" (submission-site screenshot, notes/04 §1.2). Text = Overleaf state around 19:47–19:56, after A's own rollback. Not in the archive |
| Last Overleaf state (best proxy for the re-submitted version) | `ol:ba3f1ee` (10-04 13:16, A) + `ol:1499336`, `ol:3410f5e` (B, `refs.bib` only) + `ol:5661971` (Student, empty) | A's post-extension pass. 14 files, +468/−453, of which `main.tex` +15/−8, section files +131/−92, `refs.bib` +127/−153 (DBLP-style normalization), `study-workflow.drawio` +185/−186. (Correction: the partial note's "+127/−153 across abstract and sections" is the `refs.bib` count.) A said 「我修改了一下稿子，提交了一个新版本」 (`chat:group@2026-10-04T08:46`); B 「我提交了」 (`…T18:04`). Whether either upload equals `ol:ba3f1ee`: no evidence |

Rule used below: each section gives the snapshot structure, then a **Post-snapshot delta (`ol:ba3f1ee`)** line. No submitted PDF or hash exists (GAPS item 10).

### 0.2 Evidence traps

1. **Commit subjects lie about content.** `msr:5262231` "add todo" (B) rewrites the intro gap paragraph, un-comments the intro method sentence, restores the missing RQ1 issue-type result, deletes the RQ3 κ caveat, and deletes the threats sentence disclosing a 14-cell gold overlay. `msr:86199d6` "expand details" (B) *shrinks* the conclusion. `msr:815305e` "cursor-safety: checkpoint before destructive delete" carries an agent design rewrite. `msr:3e7bab0` "Baseline: snapshot of uncommitted main working tree" carries content edits (RQ3 hedge restored, label macros in related work). `ol:5ecaf3f` "Lock a term table" also inserts A's model why-sentence and deletes study-plan sentences. B's seven `add` commits on 09-27/28 (`msr:f141169` … `msr:0b8bd5a`) are whole-section rewrites. Always read the patch.
2. **Stale-base reverts.** A's `msr:9809b8c` (written in A's evening on a base older than the Student's 09-28/29 commits) silently reverted the Student's lowercase issue-type labels (`msr:dfc2128`) and some hedges (`msr:643836a`). The Student re-applied lowercase in `msr:cfabd75` 51 min later. A's `ol:a610d1d` (10-03 19:38:54) was erased 10 s later by the one-way sync `ol:214cc0c` (exact inverse hunks), and A re-applied it in `ol:ba3f1ee`.
3. **Sync toggles look like edits.** "Updates from Overleaf" / "Merge overleaf-…" commits under B's account usually duplicate an adjacent real commit (`msr:578d640` ≈ `msr:9809b8c`; `msr:8fc36d3` ≈ the Student's 09-29 commits; `msr:bfaf29c` toggles text the other way). `msr:836ee75` (10-03 08:53) silently resurrected `sections/A-appendix.tex`, which the Student had deleted in `msr:59f15be`. On Overleaf, `Sync GitHub main @ <sha>` is a bot copy and `Update on Overleaf.` bundles every web edit since the last bridge pull. The Chinese one-line summaries in `*SUMMARY-TABLE.md` are generated from subjects and inherit the same errors.
4. **Agent reports that never landed, or landed partly.** `06-revision/REVISION-SUMMARY.md` lists "after" strings (e.g. "Issue trackers conflate multiple maintenance activities") that appear only inside the summary file in `msr:815305e` (patch line 114, in the `REVISION-SUMMARY.md` hunk), never in `03-design.tex`; its "Senior A's Comments Addressed ✅" is unsupported. The related-work `\todo` carried an agent "Progress:" note claiming 156 papers analyzed and three "directly applicable" papers (`msr:84b9197`); none of those three is cited in the final related work. `(Done: …)` replies appended to A's `\todo`s (`msr:405bba7`, `msr:e0ea09b`) are self-reports, and some are only partly true (06a: RQ1 findings still lacking figure/table sentences). `01-checklist/FINAL-CHECKLIST-2026-10-02.md` (agent, read-only) flagged B1 (κ 0.74 untraceable), H1 (two-run reporting), H9 ("recompute every number" overclaim), H13 (no gold-label threat): H9 was acted on within an hour (`msr:24d8c65`), H13 arguably by `msr:d0d4c03`, B1 and H1 never.
5. **Dead files keep getting edited.** `A-terms.tex` left the build in `msr:393f596` (09-28), yet A (`msr:9809b8c`) and the Student (`msr:6a30984`, `msr:fd0b7cd`, `msr:e0ea09b`) kept editing it. `A-appendix.tex` left the build in `msr:464168f` (10-01). Both files are in `09-paper-snapshot/` but not in the PDF.
6. **Machine-generated checklist provenance.** v2 items say "Who: Senior A (乐绎华)" (the second name is the Student). Re-verify any `CF/TH/RW` provenance before citing it as a senior's rule.

### 0.3 Spot-checks of the helper reports (all confirmed)

| Helper claim | Check |
|---|---|
| 06a: slide-rule `\todo`s in `msr:0f96193`; commented out (not resolved) in `msr:ac172bd` | `0f96193` adds both todos; `ac172bd` lines 46–52 turn them into `% \todo{…}` |
| 06a: D1 tables parked with `\iffalse` in `msr:7c705c9`, D1 result back via B's `msr:5262231` | `7c705c9` adds `% Parked: tab:rq1-types … Restore by removing iffalse`; `5262231` re-adds "Nearly one in three issues is not a bug…" |
| 06b: REVISION-SUMMARY never landed | see trap 4 |
| 06b: κ rule header in `msr:9c69675` | `%% … Kappa printing rule: only values >= 0.65 (checklist.md C3).` |
| 06b/06c: `%% PARKED (author 2026-10-02, discuss first)` still in HEAD | `03-design.tex:149`, `05-rq2.tex:13,23,35`, `04-rq1.tex:145` |
| 06c: `msr:5262231` deleted RQ3 κ caveat; Student restored a hedge in `msr:3e7bab0` | confirmed ("Resolution strategy is read from tracker text, so the shares below describe how the classifier reads that text.") |
| 06a: duplicated kernel/soundness sentence at HEAD | `04-rq1.tex:161` and `:164`; A commented out `:164` in `ol:ba3f1ee` |

### 0.4 Whole-paper phase map

| Phase | Dates | Driver | Evidence |
|---|---|---|---|
| Census draft answers A's written comments (term lock, why-before-how, no study-plan voice, counts to tables, finding-first) | 09-22 → 09-27 | Student (+agents) | `ol:5ecaf3f`, `ol:0b63ad2`, `ol:01fcd0f`, `ol:de73385`, `ol:6af100c`, `ol:6247934`, `ol:1df2367`, `ol:ac81b3a`, `ol:59236e2`, `ol:1bda8f0` |
| Outside skim | 09-26 | Advisor (relayed) | `04-comms/20260926-<B>-advisor-paper-glimpse/README.md` §2 |
| Import + SE-framing rewrite (intro, related, implications by audience, threats by Wohlin category, appendix consolidation) | 09-26 → 09-28 | B | `msr:5e73a46`, `msr:f141169`, `msr:393f596`, `msr:bd086a7`, `msr:3a4c1dc`, `msr:0b8bd5a`, `msr:15bc523` |
| A's in-repo rewrite + `\noteA{}`/`\todo{}` protocol | 09-29 11:35 | A | `msr:9809b8c`; 「主要改了写作还有格式」 (`chat:group@2026-09-29T11:51`) |
| Merge, macros, new figures, borrowed analyses, hedging | 09-29 → 10-02 | Student (+B `msr:5262231`) | `msr:c93ef1f`, `msr:815305e`, `msr:7c705c9`, `msr:9c69675`, `msr:9c4567c`, `msr:5776349`, `msr:24d8c65` |
| Appendix veto; 18-page target | 10-01 → 10-02 | A, B decide; Student executes | `chat:group@2026-10-01T08:47`–`10:09`, `@2026-10-02T01:35`, `01:51`; `msr:464168f` |
| A's second comment drop; B aligns methods text ↔ figure | 10-02 | A, B | `msr:0f96193`, `msr:9ef4a07`, `msr:b5c0045` |
| Page filling; abstract rounds | 10-03 | B (fill), Student (abstract, RQ1) | `chat:group@2026-10-02T22:44`, `@2026-10-03T09:25`; `msr:d0d4c03`, `msr:86199d6`, `msr:1ec1a0f`, `msr:13179f3`, `msr:b7a448b` |
| Post-extension pass: title, abstract, scoping, numbers, implications | 10-04 | A | `ol:ba3f1ee` |

---

## 1. Per-section evolution

### 1.1 Title and abstract (`main.tex`)

**Title timeline**

| When | Commit | Role | Title |
|---|---|---|---|
| 08-14 | `ol:20a6d25` | Student | "Mining GitHub Issues in Interactive Theorem Prover Ecosystems" `[ID]` |
| 09-22 03:01 | `ol:af26086` | Student | "What Breaks in Interactive Theorem Provers, and What Maintainers Change" `[ID]` |
| 09-22 13:09 | `ol:04c5e27` | B | proposes a "What Slows Down Proof Development?…" title (not kept) |
| 09-22 13:32 / 17:06 | `ol:30f5bf0`, `ol:efe7cb4` | Student | "Theorem Provers" → "Proof Assistants" (`comments_<A>.md:3`), drops "Interactive" |
| 09-28 14:36 / 14:42 | `msr:bd086a7`, `msr:d0bc904` | B | `% NOTE: better and more interesting title needed here!`, then "Proof Engineering in the Wild: …" `[ID]` |
| 10-03 17:57 | `msr:9355e35` | Student | "What Breaks in Proof Assistants, and How Maintainers Fix It: An Empirical Study of 23,671 Issue Reports" `[ID]` |
| 10-03 19:38 → 10-04 | `ol:a610d1d` (erased by `ol:214cc0c`), re-applied `ol:ba3f1ee` | A | "Maintaining Proof Assistants: An Empirical Study of Reported Bugs and Resolution Patterns" `[ID]`; keyword "closed coding" dropped |

**Abstract timeline (substantive rounds)**

| When | Commit | Role | Change |
|---|---|---|---|
| 09-26 | `msr:5e73a46` | Student (imported by B) | 6 sentences; codebook labels in caps; "In this frozen snapshot"; exact medians in prose |
| 09-27 → 09-28 | `msr:f141169` … `msr:0b8bd5a` | B | context → mixing problem → study → 2 findings → "only when" implication; plain words for labels; `0b8bd5a` adds strong claims ("The most severe bugs close fastest", "small edit", "bug severity is a poor guide to repair effort") |
| 09-29 00:54 | `msr:643836a` | Student | "In the classifier's reading of tracker text…" hedge |
| 09-29 11:35 | `msr:9809b8c` | A | 7 cautious sentences ending "…need to distinguish issue types and state their repository composition and closure criteria" |
| 09-30 | `msr:0952732`, `msr:5262231` | B | "Yet no prior work…" + First/Second/Third; semicolon split (no-semicolon rule, `CF-23@v2`) |
| 10-02 | `msr:3e7bab0` → `msr:24d8c65` | Student | ecosystem effect "six times more" → "nine percent" → "about five percent" as import-time closures were excluded; "pooled over ecosystems" scope added |
| 10-03 17:57 → 19:38 | `msr:9355e35`, `ac172bd`, `4af1aff`, `10e2e5f`, `f1bc590`, `87bf139` | Student | B's template applied (below); macros removed (`4af1aff` broke F* → "F", fixed 9 min later in `10e2e5f`) |
| 10-03 ~19:44–19:56 | Overleaf only (= snapshot `main.tex`) | Student | 14 short sentences (~274 words) |
| 10-04 | `ol:ba3f1ee` | A | 5 sentences + one 4-sentence findings block (~192 words); exact numbers; one "Hence, … requires …" closing sentence |

**Instructive rewrites**

(a) Overclaim → hedge → measured claim. Before, `msr:0b8bd5a` (B):
> The most severe bugs close fastest: soundness bugs close in a median of four days, whereas performance bugs […] take about a month […] Even soundness bugs are usually fixed by a small edit at the failing site […] bug severity is a poor guide to repair effort

After, `msr:9c69675` (Student) → `msr:87bf139`:
> Soundness bugs close among the fastest and are fixed mainly by a local patch at the defect site, whereas performance bugs stay open longest and are fixed mainly by optimization, and a local patch does not imply a small recorded change.

Reason: `CF-12/13/29@v2` (category ≠ severity; no "small" without diff evidence; time-to-close ≠ effort); the fix-size measurement arrived in `msr:9c69675` after A asked for analyses borrowed from the closest papers (`chat:group@2026-09-29T12:30`). CF provenance is machine-generated; the chat message is the verified anchor.

(b) Template in chat, executed in minutes. B, `chat:group@2026-10-03T19:18`: 「应该先交代一句背景，然后说明research gap，然后说to fill this gap, 我们做了一个关于的study，其中通过什么方法去做了什么，1-2条最重要的findings，我们最后推荐什么，每一个1句话上下」; 19:40 「你这个abstract每个句子太长了」. After (`msr:f1bc590`, 19:24):
> To fill this gap, we study $23{,}671$ GitHub issues from five ecosystems (\textsf{Lean}, …) with a proof-assistant-specific codebook and an LLM classifier validated against a held-out, adjudicated gold sample. `[ID]`

Same evening: name the five ecosystems, not the repositories (A 18:27); no labels or macros in the submission-form abstract (B 18:36 「abstract里不应该出现label的」, A 18:37 「文本叙述吧，安全一些」, B 18:43 「latex文本【无宏】」).

(c) A's last pass: verbal quantifiers → one exact number per claim, plus a scope qualifier from threats. Before (snapshot): "We find that nearly one in three issues is not a bug, and that the bug share differs sharply between ecosystems." After (`ol:ba3f1ee`):
> We find that 29.4\% of issue reports are not bugs […] Among closed bugs, category explains only 1.2\% of the rank variation in time to close […] Hence, reliable mining of proof-assistant maintenance requires explicit issue classification, comparisons that account for ecosystem and filing period, and direct measurement of recorded fixes. `[ID]`

Reason: no message states it. The "filing period" qualifier comes from the 2021+ robustness check that sat in threats (§1.9) and that A moved into RQ2 on 10-03/04.

**Final structure.** Snapshot abstract: S1–S2 what the assistant guarantees and the two failure modes; S3 issue reports as the channel; S4 gap as a three-part question; S5 "To fill this gap" + scope; S6 method in one sentence; S7–S12 findings in RQ order, pooled claim then its exception; S13–S14 recommendations split by audience.

Post-snapshot delta (`ol:ba3f1ee`): problem-first opening ("Bugs in proof assistants can interrupt verified developments or undermine their logical guarantees, yet…"), "little is known about" gap, method sentence with "(validated against human annotations)", four findings with exact percentages, a single "Hence … requires …" recommendation; old sentences kept as `%` comments.

---

### 1.2 Introduction (`01-introduction.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 16:47–19:04 | `ol:5ecaf3f`, `ol:0b63ad2`, `ol:2193c6b` | Student | Term table put into the intro, then moved out to an appendix; "Motivate the census before the study mechanics" (SE-cost paragraph first, per `comments_<A>.md` §2.1/§2.6) |
| 09-22 23:18 → 09-23 00:23 | `ol:d62850d` … `ol:a2c534e` | Student | RQs stated in intro; contributions one finding per RQ; `a2c534e` *removes* the measurement caveat ("labels from tracker text rather than measured diffs") |
| 09-26 | `msr:5e73a46` | Student (import) | 5 paragraphs; codebook labels in caps in prose; contributions 2–4 commented out ("Contributions are written last…") |
| 09-27 23:15 | `msr:f141169` | B | Canonical SE intro: context → tracker as record → gap → RQ bullets with one motivation clause → four-stage method → three **bold** findings → four contributions → roadmap |
| 09-28 | `msr:393f596`, `bd086a7`, `3a4c1dc`, `0b8bd5a`, `15bc523` | B | Findings reworded toward severity framing ("severity runs opposite to time-to-close", "the most severe bugs close fastest") |
| 09-29 11:35 | `msr:9809b8c` | A | Removes the method paragraph, findings list and roadmap (commented out); each RQ becomes a block: bold question → "so we…" why sentence → "We find…"; contributions as itemized list; adds "TODO: add an intro figure (as in TOSEM Fig. 1)" |
| 09-29 13:33 | `msr:6f652b4` | Student | Adds intro figure (two failure modes: regression vs soundness) |
| 09-30 13:30 | `msr:5262231` | B | Gap paragraph rebuilt as "depart … in three ways. First/Second/Third"; un-comments the one-sentence method paragraph |
| 10-02 | `msr:9c69675`, `9c4567c`, `5776349`, `24d8c65` | Student | "The first empirical study" → "An empirical study"; "Yet no prior work" → "To our knowledge, no prior work"; three assumptions → "two assumptions from other domains and one expectation specific to proof assistants", each with a citation; "pooled over ecosystems … although this order does not hold in every ecosystem" |
| 10-03 10:10 | `msr:1ec1a0f` | B | Restores the roadmap paragraph A had commented out (page filling) |
| 10-03 19:38 / 10-04 | `ol:a610d1d` / `ol:ba3f1ee` | A | Caption scoped to "a kernel-based proof assistant"; "depart … so such results cannot simply be carried over" → "Three features of the selected repositories motivate a domain-specific study"; RQ "We find" sentences get exact numbers; "three-phase methodology" → "methodology" |

**Instructive excerpts**

(a) Study-plan voice and procedure first → SE framing first. Before, `msr:5e73a46` (Student):
> This paper quantifies that tracker mix and what maintainers change afterward.
> We freeze seven repositories, label every issue under one codebook, and check the labeler against a held-out human gold sample before reading the frozen snapshot as evidence.

After, `msr:f141169` (B, kept in substance to the end):
> Proof assistants are therefore long-lived software infrastructure whose maintenance and evolution carry a high cost of regression.
> GitHub issue trackers are the main public record of how that infrastructure is maintained.

Reason: `comments_<A>.md` §2.1 (context before methodology), §2.6 ("Motivate from Maintenance and Evolution"; its five-step outline is nearly the paragraph order B wrote). The Advisor (relayed) had asked "what are the overall findings/implications?" one day earlier; no message links that relay to this rewrite.

(b) Findings list → RQ blocks with why + answer. Before, B's base as removed by `msr:9809b8c`:
> Our analysis yields the following findings.
> First, \textbf{bug reports concentrate in the elaborator and tactics rather than the kernel.}

After, `msr:9809b8c` (A):
> \textbf{RQ2: How does time-to-close vary across bug categories and ecosystems?}
> Triage models and effort estimates often treat bug category as a prior on repair difficulty~\cite{Islam_2019}, so we test whether category separates how long bugs stay open and whether ecosystem separates it more.
> We find that soundness bugs close fastest and performance bugs slowest, yet bug category explains only about one percent…

Reason: `comments_<A>.md` §2.5 (question → why → method → result → implication) applied to the intro; A's commit message is only "<A>'s comments".

(c) Absolute novelty → hedged novelty. `msr:9809b8c` "The first empirical study of proof-assistant issue reports" and `msr:5262231` "Yet no prior work has studied…" → `msr:9c69675` "An empirical study…", "To our knowledge, no prior work…". Reason: `RW-01@v2` ("soften 'nobody studied PA issue reports' absolutes"; misreading note: "Absolute 'no prior work' claims trigger PC rebuttals"). The CF/RW provenance is machine-generated; no human message in the archive asks for this specific edit.

**Final structure (snapshot, ~1,110 words, 10 prose blocks + 1 figure)**
1. Context: what a proof assistant is (definition with examples), why regressions are expensive (downstream dependency), pointer to Fig. 1.
2. Figure 1: two failure modes (regression, soundness bug).
3. Issue reports as SE data (bug datasets, triage, repair benchmarks; domain codebooks) + "departs in three ways": core/library split, unnamed components, soundness.
4. Gap: existing SE work on proof assistants (replay; contributors) and what it misses; two inherited assumptions (each cited) + one domain expectation; "To our knowledge, no prior work…".
5. "To address this gap": dataset scope (+ ecosystem homepage footnotes) and "test all three in turn"; "We investigate three RQs".
6–8. One block per RQ: bold question; one why sentence ("…, so we…"); 2–3 "We find" sentences.
9. One-sentence method (two-author gold sample, codebook, tune/validate classifier, apply to all).
10. Contributions (4 bullets: study, codebook + pipeline, evidence on the assumptions, dataset/replication package).
11. Roadmap.

Post-snapshot delta (`ol:ba3f1ee`): figure width and caption scoped to "kernel-based"; motivation sentence reattributed to "the selected repositories"; "Maintainers who prioritize reports … fall back on two assumptions" → "Two assumptions drawn from issue-mining work in other domains therefore warrant examination"; RQ1/RQ2 answers get 29.4%, 30.5%, 15.7–77.3%, 15.5–67.6%, 1.2% vs 4.9% and the filing-period caveat `[ID]`.

---

### 1.3 Background and related work (`02-related-work.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 21:18 | `ol:1df2367` | Student | "Related Work" → "Background and Related Work"; three subsections each opening "X matters because…" |
| 09-23/24 | `ol:ac81b3a`, `ol:59236e2` | Student | Rewritten around "the unit is the filed ticket"; κ removed from Section 2 by author decision (09-23, recorded in `notes/da-review-related-work.md`); "Polish … for SE motivation and Lihao prose constraints"; drops numbers (12,079 failures, 123 repositories) |
| 09-27/28 | `msr:f141169`, `msr:393f596`, `msr:bd086a7` | B | Background on components; "Breakage events" vs "Issue reports" bold pseudo-terms; added "Time-to-Close and Resolution Status" and "The Missing Tracker Perspective" subsections |
| 09-29 11:35 | `msr:9809b8c` | A | Deletes the time-to-close subsection and the gap subsection; removes bold pseudo-terms; "Author et al.~\cite" → `\citet`; section renamed "Components of a Proof Assistant"; `\todo{include more papers, see the file I shared}` |
| 09-29 15:56 / 22:17 | `msr:84b9197`, `msr:3d34425` | Student | Appends an agent "Progress:" note to the todo; adds one sentence listing three verification-tool bug studies |
| 09-30 13:30 | `msr:5262231` | B | Background rebuilt as "That dependency is fragile in practice" → tracker → "three respects" |
| 10-02 02:16 / 04:45 | `msr:9c69675`, `msr:9c4567c` | Student | Each cited study gets method + scale + result (Luan 12,079 / 36.4%; Islam 2,716 + 500; Zhang 62 bugs / 7 categories; Bringolf 31/19; Zhang 149 commits); string-solver cite corrected (`Lin_2023` → `Zhang_2023`); Ahmed 2025 added; citations added to background claims |
| 10-02 06:02 | `msr:59f15be` | Student | Comments out A's todo + progress note (never resolved) |
| 10-03 10:04 / 11:30 | `msr:86199d6`, `msr:b7a448b` | B | Section-opening roadmap sentence; two background sentences (metaprogramming; type-class search can be exponential) — page filling; deletes the commented todo |
| 10-03 19:38 / 10-04 | `ol:a610d1d` / `ol:ba3f1ee` | A | Scope: "kernel-based assistants"; F* + SMT footnote; new paragraph on repository roles (assistant vs library vs verified-software project) "These roles give context to the ecosystem comparisons"; synthesis sentence narrowed to "the cited automatic-classification studies" |

**Instructive excerpts**

(a) Pseudo-terms and a separate gap subsection → one complementarity sentence. Before (B, removed by `msr:9809b8c`):
> \textbf{Breakage events} capture \emph{what breaks}: failures reconstructed by replaying a proof archive against a new tool version […]
> \textbf{Issue reports} capture \emph{what maintainers are asked to fix and how they respond}: […]

After (`msr:9c69675`, final):
> The two views are complementary, because replay shows which proofs a version change breaks, whereas a tracker shows which failures users report and how maintainers resolve them.

Reason: A's pass; no stated reason. Consistent with `comments_<A>.md` §2.8 (defensive/fragmented prose) and the de-AI pass (bold coined terms read as AI style, cf. 「这个需要去一下ai味」, `chat:group@2026-10-02T21:49`, said of another item).

(b) Vague list → one sentence per study with method, scale, result. Before (`msr:3d34425`, Student):
> Studies of verification tools adjacent to proof assistants provide related empirical evidence: \citet{Zhang_2019} characterize bugs in software model checkers, \citet{Bringolf_2022} analyze incompleteness bugs in SMT solvers, and \citet{Lin_2023} investigate performance regressions in string solvers.

After (`msr:9c69675`):
> Studies of verification tools adjacent to proof assistants find their bugs by testing rather than by mining user reports.
> \citet{Zhang_2019} fuzz three C software model checkers and group the 62 unique bugs they find into seven categories by the module in which each resides.
> \citet{Bringolf_2022} fuzz SMT solvers and report 31 incompleteness bugs, of which 19 were fixed.

Reason: the topic sentence states the *difference* (testing vs mining), and each citation carries what was done; this answers A's "include more papers" only partly. The commit also fixes a wrong citation key. DBLP rule: 「引用的paper都用dblp查一下 … 现在查处一个错的引用直接desk reject」 (`chat:group@2026-09-29T11:44`).

(c) Scope narrowing in A's final pass (`ol:a610d1d`, re-applied `ol:ba3f1ee`):
> -A proof assistant checks machine-readable proofs […] so that a result is accepted only when a small trusted kernel has verified every inference.
> +A proof assistant checks machine-readable proofs of theorems and program properties against a formal logic.
> +In systems such as \Lean and \Rocq, a small trusted kernel checks the inferences on which an accepted result depends.

Reason: no message. The edit removes a universal claim that is false for SMT-backed systems (F*) and for the verified-compiler repository, which A then explains in a new paragraph.

**Final structure (snapshot, ~1,150 words, 9 paragraphs)**
- Opening roadmap sentence (added for page fill).
- 2.1 "Proof Assistants as the Foundation of Verified Software": P1 guarantee → large libraries → dependency; P2 "That dependency is fragile" → tracker → "depends on what it actually contains".
- 2.2 "Components of a Proof Assistant": P3 parser → elaborator → tactics → metaprogramming → search cost → kernel/soundness → toolchain/IDE → ecosystems; P4 "shares concerns … but differs in three respects" (First/Second/Third) + bridge to review.
- 2.3 "Related Work" with three `\subsubsection`s: PA maintenance studies (per-paper method/scale/result; what replay misses; complementarity); bug studies in other domains (domain codebooks; testing-based verification-tool studies; Herzig misclassification); automatic issue classification (noise sensitivity; LLM–human κ; agreement-based suitability; "not on domain-specific dimensions").
- Synthesis paragraph: "Taken together, …" (one clause per strand) + "Our study takes …".

Post-snapshot delta (`ol:ba3f1ee`): kernel-based scoping; F* SMT footnote; repository-roles paragraph (CakeML as verified-software project, its reports "concern that project rather than the HOL4 assistant") `[ID]`; "three respects" → "three features of the selected repositories motivate a domain-specific study".

---

### 1.4 Methodology (`03-design.tex`) — from helper 06b, spot-checked

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 16:47 | `ol:5ecaf3f` | Student | Denominator why-sentence near-verbatim from `comments_<A>.md:43`; defensive phrases from `comments_<A>.md:170–171` deleted |
| 09-26 12:05 | `ol:1bda8f0` | Student | Deletes "The artifact has no two-rater human table, so this paper reports no human--human agreement." |
| 09-28 00:10 | `msr:393f596` | B | First "two authors independently annotate all 582 issues … κ = 0.74" (no computation record in the archive; notes/04 §1.6) `[ID]` |
| 09-29 00:54 / 11:35 | `msr:643836a` / `msr:9809b8c` | Student / A | All per-dimension κ printed / cut to "κ from 0.71 to 0.83"; A's `\todo` "the overview figure and the content in methodology is not synced, check previous papers from SAIL…"; "put this information in the overview figure … remove this table" |
| 09-29 18:19 | `msr:815305e` | Student (agent) | Design rewrite under a misleading subject; the accompanying REVISION-SUMMARY claims never landed |
| 10-01 18:58 | `msr:464168f` | Student | Codebook condensed to a D1–D7 + labels table in the body, definitions to the package (A, `chat:group@2026-10-01T10:09`) |
| 10-02 02:16 | `msr:9c69675` | Student | κ printing rule (≥ 0.65 only); `%% PARKED (author 2026-10-02, discuss first)` analyses |
| 10-02 07:45 | `msr:0f96193` | A | `\noteA{figure and text are not synced, e.g., you mention 'Build issue payloads' in the figure, where is the text? … redraw the figure from scratch}`; `\todo{do not call it snapshot, call it dataset}`; `\todo{fix AI smells, e.g., 'Corpus'}` |
| 10-02 11:31 → 10-03 10:04 | `msr:9ef4a07`, `msr:b5c0045`, `msr:4c70db0`, `msr:86199d6` | B | Figure redrawn 12 → 10 steps; three "Phase n:" subsections with ten bold "Step n" run-ins mirroring the figure; phase-mapping sentences cut, then a 3-sentence overview re-added for pages |
| 10-04 | `ol:ba3f1ee` | A | "Phase n:" dropped from subsection titles ("ten steps grouped into three stages"); caption → "Overview of the study."; repository definition widened to "a selected verified-software project"; "at most one label … on each applicable dimension"; filing-period robustness sentence |

**Instructive excerpt** (figure-mirroring, `msr:b5c0045`, B):
> \subsection{Phase 2: Gold Sample and Classifier Validation}
> \textbf{Step~3: Define codebook.} … \textbf{Step~4: Draw gold sample.} … \textbf{Step~7: Calibrate and validate classifier.}

Reason: A, `chat:group@2026-09-29T11:42` 「图上这些在methodology的文字都能找到对应」 with an example paper's numbered subsections; `chat:group@2026-10-02T07:29` 「图和文字需要对应」; B 11:07 「我修改了，目前是对应上的了」.

**Final structure (snapshot, ~1,870 words, 18 paragraphs, 1 figure, 1 table)**: overview paragraph + workflow figure; Phase 1 (Step 1 select repositories: definition + inclusion criteria; Step 2 collect issues: cutoff, fields, cleaning, import-time closures); Phase 2 (Step 3 codebook: closed coding, seven dimensions, gate order, Table of D1–D7 labels with a pointer to definitions in the package; Step 4 stratified gold sample; Step 5 independent annotation with κ; Step 6 adjudication; Step 7 classifier: model, temperature, prompt, demonstrations, tuning/held-out split, κ only where ≥ 0.65); Phase 3 (Step 8 label all; Step 9 gates and exclusions with the denominators per RQ and their "why"; Step 10 statistics: Cramér's V, Kruskal–Wallis ε², error correction). Parked analyses remain as `%%` blocks.

Post-snapshot delta: see last row of the timeline; the study-workflow drawio was also edited (+185/−186).

---

### 1.5 RQ1 (`04-rq1.tex`) — from helper 06a, spot-checked

**Timeline (condensed)**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 16:49 | `ol:01fcd0f`, `ol:de73385` | Student | "Lead results with the question and the finding"; opening "Before reasoning about defects, we need to know whether these trackers mostly contain defects at all" (= `comments_<A>.md:162`); plan language removed |
| 09-27/28 | `msr:f141169`, `msr:393f596` | B | Takeaway retitled "Summary (RQ1): <headline>"; three body tables |
| 09-29 11:35 | `msr:9809b8c` | A | Why-opening deleted (folded into first finding); "Table/Figure X shows that…" as sentence 2; takeaway → "RQ1 Summary"; heatmap todo "if not, remove the figure" |
| 09-29 16:14 → 21:14 | `msr:7c705c9`, `msr:b3dafcd` | Student | Tables parked with `\iffalse` (D1 result lost for a day); heatmap removed then re-added |
| 09-30 13:30 | `msr:5262231` | B | D1 result restored under "add todo" |
| 10-02 02:16 | `msr:9c69675` | Student | Robustness grows: balanced shares, Rogan–Gladen correction, label recall 16–68%, maintainer vs outsider filing |
| 10-02 07:45 | `msr:0f96193` | A | Slide rule todos (bold finding / figure-or-table sentence / dig deeper); "readers are here to read our results, talk our results first"; "avoid subsubsection" |
| 10-02 23:34 → 10-03 18:37 | `msr:405bba7`, `msr:ee351a3`, `msr:ac172bd` | Student | Results-first reorder; "(Done…)"/"[Partly addressed…]"; todos commented out, not resolved |
| 10-04 | `ol:ba3f1ee` | A | Headlines turned into exact-number headlines; duplicate kernel sentence commented out; **new defect**: two bold headlines merged into one paragraph ("\textbf{Nearly one in three…} The issue-type counts in \textbf{Non-bug issues make up 29.4\%…} The issue-type counts in Figure…") |

**Instructive excerpt** (A's rule, `msr:0f96193`):
> \todo{I copied and paste the info here: – First sentence: highlight the finding in bold
> – Second sentence refers to a figure or table
> – Rest of the paragraph further discusses and digs deeper into the finding}

Final paragraph shape (snapshot `04-rq1.tex`): "\textbf{Nearly one in three issues is not a bug, and the bug share differs sharply between ecosystems.} The issue-type counts in Figure~\ref{…}a show that \bug reports account for 70.6\% of the 23,671 issues." `[ID]`

**Final structure (snapshot, ~870 words, 7 paragraphs, 2 figures)**: `\section{Results}` + RQ1 subsection; six bold-headline finding paragraphs (issue mix; who files what; bug categories; core vs library and across ecosystems; trigger; mathematical domain/proof mechanism); takeaway "RQ1 Summary" (4 sentences). Two findings (maintainers; trigger) still cite no figure/table (06a).

Post-snapshot delta: exact-number headlines ("Ordinary input exposes 69.7\% of the bugs, and an environment change exposes 24.2\%."), counts replace "about one in five", and the merged-headline defect above. Whether it survived into the uploaded PDF: no evidence.

---

### 1.6 RQ2 (`05-rq2.tex`) — from helper 06c, spot-checked

**Timeline (condensed)**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 | `ol:01fcd0f` | Student | Why-before-how on the denominator, near-verbatim `comments_<A>.md:38–43` |
| 09-29 11:35 | `msr:9809b8c` | A | +22/−83: rewrite; stale base reverts Student's lowercase/hedges |
| 10-02 02:16 / 04:45 | `msr:9c69675`, `msr:9c4567c` | Student | Kaplan–Meier, creation-year ladder, last-comment endpoint, closure-record check → parked as `%% PARKED … discuss first`; why-paragraph shrinks |
| 10-02 07:45 | `msr:0f96193` | A | `\todo{space filling, remove this:}` on the method reminder; "Wait, It is a table! why label it as a figure?! Please format it as a normal table" |
| 10-02 23:34 | `msr:405bba7` | Student | Figure split into a real table (「我把表和图拆开了」, `chat:group@2026-10-02T21:38`) |
| 10-03 10:15 / 11:30 | `msr:13179f3`, `msr:b7a448b` | B | Five extra `\midrule`s (page fill); method reminder deleted |
| 10-03 19:38 / 10-04 | `ol:a610d1d` / `ol:ba3f1ee` | A | Headline scoped ("In the studied ecosystems…" → "Among closed bug reports pooled across ecosystems…"); 2021+ cohort moved from threats into RQ2 body; third finding rewritten as "Measured against each ecosystem's own baseline, only the slow closure of \performance bugs holds in every ecosystem" with per-ecosystem ratios |

**Final structure (snapshot, ~340 words prose + 1 table)**: three bold-headline paragraphs (category order with Table pointer; effect sizes: category ~1% vs ecosystem ~5%; pooled order not universal, Agda counterexample); table of medians by category × ecosystem; takeaway "RQ2 Summary" (2 sentences). Robustness lives in threats (§1.9) and in `%% PARKED` comments.

Post-snapshot delta: RQ2 grows by the filing-period paragraph and the per-ecosystem-baseline finding (+16/−10).

---

### 1.7 RQ3 (`06-rq3.tex`) — from helper 06c, spot-checked

**Timeline (condensed)**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-27/29 | `msr:f141169`, `msr:9809b8c` | B, A | "Four out of five fixed bugs are resolved by a local patch … a small edit" |
| 09-29 16:54 | `msr:c544e4a` | Student | Strategy table removed (subject: "Remove commented-out table") |
| 09-30 13:30 | `msr:5262231` | B | Deletes "Because agreement on resolution strategy stays below our κ bar …, the shares … describe how the classifier reads tracker text" |
| 10-01 / 10-02 | `msr:464168f`, `msr:9c69675` | Student | Diffstat analysis contradicts "small"; codebook definition "fix at the defect site with no structural change"; "Recorded diffstats do not show local patches to be small" |
| 10-02 00:25 | `msr:3e7bab0` | Student | Hedge restored as a one-line scope sentence |
| 10-02 07:45 | `msr:0f96193` | A | "merge this paragraph with the next paragraph, if we have nothing to talk, talk nothing" |
| 10-03 01:30 | `msr:e0ea09b` | Student | RQ3 analysis and figure panels (a)(b)(c) |
| 10-03 19:38 / 10-04 | `ol:a610d1d` / `ol:ba3f1ee` | A | Worked examples with real issue/PR numbers (test-only and documentation-only strategy labels; an 8-line fix with 47 test lines) `[ID]`; summary opens "Even a bug that lets the assistant accept a false proof is usually repaired at the defect site." |

**Instructive excerpt** (hedge erosion in the last pass). Snapshot summary: "As the tracker text describes them, a \localpatch is the most common strategy…". `ol:ba3f1ee`:
> Even a bug that lets the assistant accept a false proof is usually repaired at the defect site.
> Maintainers describe 79.7\% of the fixes, including 83.5\% of \soundness fixes, as local patches […] `[ID]`

The second sentence keeps the "describe" hedge; the first states it as fact. No message discusses it.

**Final structure (snapshot, ~700 words, 6 paragraphs, 1 three-panel figure)**: one scope sentence (strategy is read from tracker text); four bold-headline findings (local patch dominant except performance; other strategies stay open longer; diffstats show local patches are not small; soundness/performance fixes largest); takeaway "RQ3 Summary" (3 sentences).

---

### 1.8 Implications (`07-implications.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 → 09-24 | `ol:6af100c`, `ol:e03c20a` | Student | Counts moved out; internal codename "Hamilton 2000" dropped from implications |
| 09-26 | `msr:5e73a46` | Student (import) | "Implications for Software Engineering Research": one 9-sentence paragraph of statistics, ε², "In this frozen snapshot" |
| 09-27 23:15 | `msr:f141169` | B | "Implications": three audiences (researchers, maintainers, tool builders), `\paragraph` imperative headlines, each item = evidence (RQ) → consequence → recommendation |
| 09-28 00:10 | `msr:393f596` | B | Reordered maintainers → tool builders → researchers; "RQx shows that…" as sentence 1; causal claim "This happens since…"; placeholder `%% EXAMPLE: cite one long-lived performance issue with its URL.` |
| 09-29 11:35 | `msr:9809b8c` | A | `\emph` headlines → `\textbf`; opening sentence commented out; `\citet` |
| 10-02 02:16 | `msr:9c69675` | Student | Speculation hedged ("One possible reason, which our data do not test,"); "Expect local patches that are not necessarily small"; label-recall finding (16–68%) and Herzig contrast; import-time-closure item |
| 10-02 06:02 / 06:58 | `msr:59f15be`, `msr:24d8c65` | Student | "misses at least a third … in every tracker" → "misses between 32\% and 84\%"; "depending on tracker history" dropped |
| 10-03 09:58 | `msr:d0d4c03` | B | Page fill (+31/−21): opening sentence restored; 5 → 7 items; new "Build benchmarks around elaborator and tactic bugs", "Measure fix size directly", "Analyze cores, libraries, and ecosystems separately"; author-role filter |
| 10-03 11:30 | `msr:b7a448b` | B | `%% EXAMPLE` placeholder filled with a real issue + PR (two URLs) `[ID]` |
| 10-04 | `ol:ba3f1ee` | A | Largest section change of the last pass (+34/−19): "Predict time-to-close within each ecosystem" → "Evaluate closure predictions by ecosystem and filing period"; benchmark item rewritten with explicit acceptance criteria per category; exact numbers everywhere; "can use the author's repository role as a cheap first filter" deleted; old items kept as `%` comments |

**Instructive excerpts**

(a) Results restated → stakeholder actions. Before (`msr:5e73a46`):
> In this frozen snapshot, \textit{performance} and \textit{tactic} remain the two longest bug categories when the denominator changes […]
> The grouping that keeps those categories separate has $\varepsilon^{2} = 0.0139$ on all closed \textit{BUG} issues, which is not under the one-percent line […]

After (`msr:f141169` → final shape):
> \textbf{Record why an issue was closed.}
> Nearly one in five closed issues (3,427 of 18,085) carries no recoverable resolution status (\S\ref{…}), so the tracker cannot distinguish a repair from an abandoned report.
> […] Maintainers should adopt close-reason labels or closing templates, especially in library trackers, so that the tracker becomes a usable record of maintenance for both the community and researchers.

Reason: `comments_<A>.md` §2.5 step 5 ("what should researchers/maintainers do differently?") and §2.4 (no number laundry); Advisor relay "what are the overall findings/implications?" (09-26).

(b) Causal speculation → flagged speculation. `msr:393f596` (B): "This happens since a \performance bug has no single failing proof that marks it as fixed". `msr:9c69675` (Student): "One possible reason, which our data do not test, is that a \performance bug has no single failing proof that marks it as fixed". Reason: no message; matches the 10-02 "fix claims that could be misread" pass (`msr:24d8c65` subject).

(c) A's final reframing (`ol:ba3f1ee`):
> +\textbf{Evaluate closure predictions by ecosystem and filing period.}
> +[…] The relative association reverses on all closed bugs filed from 2021 onward, so ecosystem differences in the full dataset should not be assumed to persist in later periods.
> +[…] Tool builders should evaluate such models within each ecosystem and on later filing periods, using only information available at the prediction time.

Reason: the 2021+ cohort result from threats contradicted the unqualified "ecosystem explains more" headline; A propagated it into abstract, RQ2, implications and conclusion in one pass. No message states the reason.

**Final structure (snapshot, ~900 words, 8 paragraphs)**: one-sentence audience roadmap; 7.1 Maintainers (2 items); 7.2 Triage and repair tool builders (3 items); 7.3 Researchers (2 items). Each item: **bold imperative headline** → "RQx shows that …" (1–2 evidence sentences, sometimes two RQs combined) → mechanism or consequence ("therefore", "One possible reason, which our data do not test") → optional worked example → "<Audience> should …".

Post-snapshot delta: headlines 7 → 7 but two replaced; per-category acceptance criteria for repair benchmarks; exact numbers (18.9%, 60.6%/66.2%, 79.7%/83.5%, 16.5%, 90.5 lines, 83.3%, 62.8%) `[ID]`.

---

### 1.9 Threats to validity (`08-threats.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 21:41 → 23:29 | `ol:ee75959`, `ol:6af100c`, `ol:4f1cc00` | Student | Held-out κ table replaced by "the verified agreement pattern"; counts moved to appendix; change-size note |
| 09-26 | `msr:5e73a46` | Student (import) | Three ad-hoc paragraphs: "Design choices", "Generalizability", "Manual effort"; states "the artifact contains no second human labeler, so a human--human agreement threshold is not something this paper measured"; discloses the 14-cell overlay |
| 09-27 23:15 | `msr:f141169` | B | Re-sorted into Construct / Internal / External / Conclusion validity (`\paragraph`); keeps "we do not report human--human agreement" |
| 09-28 00:10 | `msr:393f596` | B | Reordered Conclusion → Construct → External → Internal; adds "the two authors reach κ = 0.74 … we resolve each disagreement through joint review"; removes the no-human-agreement sentence; adds selection-bias sentence (≥1,000 stars) and "To partially mitigate this concern, we report each repository and each ecosystem separately" |
| 09-29 11:35 | `msr:9809b8c` | A | `\paragraph{}` → `\textbf{… Validity.}`; "snapshot" → "dataset" |
| 09-30 13:30 | `msr:5262231` | B | Semicolon sentences split; deletes "mathematical domain and proof mechanism clear it only after a 14-cell overlay" |
| 10-02 02:16 / 04:45 | `msr:9c69675`, `msr:9c4567c` | Student | Robustness checks become threat mitigations (last-comment endpoint, administrative closures, Kaplan–Meier, 2021+ cohort, reverse causality RQ3, training-data contamination); then one citation per threat (Tomczak, Wessel, Herbold, Kaplan–Meier, Baltes) |
| 10-02 07:45 | `msr:0f96193` | A | `\textbf{}` run-ins → `\subsection{}`; `\todo{too long, please break it down}` on Internal Validity |
| 10-03 01:30 | `msr:e0ea09b` | Student | Splits into a new "Reliability" subsection; todo marked "(Done: …)" |
| 10-03 09:58 | `msr:d0d4c03` | B | Page fill: Wohlin intro sentence; Reliability folded back into Conclusion/Construct; adds "The gold labels reflect the reading of two authors whose independent agreement was κ = 0.74, so the classifier's agreement with them shows that it follows that reading" |
| 10-03 10:10 / 11:30 | `msr:1ec1a0f`, `msr:b7a448b` | B | Author-association sentence removed; adds "The issue examples that we cite all come from \Lean~4 and were chosen to illustrate the findings, not to represent them." |
| 10-04 | `ol:ba3f1ee` | A | "against" → "vs." only (+1/−1); the 2021+ result now also appears in RQ2 |

**Instructive excerpts**

(a) Ad-hoc limitation headings → standard validity taxonomy. Before (`msr:5e73a46`): `\paragraph{Design choices.}`, `\paragraph{Generalizability.}`, `\paragraph{Manual effort.}`. After (final `msr:d0d4c03` + `msr:0f96193`):
> We discuss threats to conclusion, construct, internal, and external validity~\cite{Wohlin_2012}.
> \subsection{Conclusion Validity}

Reason: B's restructure (no stated reason); A's todo asked for subsections and shorter Internal Validity. The intro sentence was added on the page-filling day.

(b) Robustness check written as a threat + mitigation + residual (`msr:e0ea09b`/final):
> Two checks leave the RQ2 order unchanged: ending the interval at the last comment before closing~\cite{Zhang_2021} lowers the pooled median from 28.7 to 11.3 days on the 10,202 closed bugs with such a comment, and […] dropping them moves no fixed-only median by more than 0.3 days. `[ID]`

Reason: A's requests for analyses borrowed from close papers (`chat:group@2026-09-29T12:30`) produced checks that were "PARKED … discuss first" in RQ2 and surfaced here instead.

(c) Disclosure reversed (integrity-relevant). `msr:f141169` (B, 09-27):
> Agreement is measured between the model and one gold sample on 291 held-out issues; the gold sample was not labeled by a second independent human, so we do not report human--human agreement.

`msr:393f596` (B, 09-28) replaced it with: "the two authors reach $\kappa = 0.74$ on the stratified sample". The archive has no computation record for 0.74 (notes/04 §1.6); B's only support is a 1:1 chat assurance (`chat:1on1@2026-09-28T20:17`). `FINAL-CHECKLIST-2026-10-02.md` B1 flagged it as a desk-reject risk; the final threats section repeats 0.74 (`08-threats.tex:20`). The 14-cell gold overlay disclosure was deleted in `msr:5262231` and never returned (notes/08 §2.2). Treat both as cautionary, not as practice to copy.

**Final structure (snapshot, ~720 words, 8 paragraphs)**: Wohlin intro sentence; Conclusion validity (2 paras: effect sizes over p-values; independence; collapsed categories; error-correction assumption; one model/prompt/temperature, two runs κ 0.81/0.82 → release everything); Construct validity (2 paras: time-to-close ≠ difficulty + two checks; strategy read from text + diffstat upper bound; classifier inputs; gold = two authors' reading; training-data contamination; one category per dimension); Internal validity (2 paras: import-time closures; open bugs and Kaplan–Meier; ecosystem × filing period; RQ3 direction of causation; missing status bias); External validity (1 para: selection criteria and exclusions; popularity bias; uneven volume → per-repository reporting and balanced shares; July 2026 snapshot; examples from one ecosystem, illustrative only). Each sentence pattern: threat → what we did/checked → residual.

---

### 1.10 Conclusion (`09-conclusion.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 16:49 | `ol:01fcd0f` | Student | Removes "tested a study plan's predictions against the counts" |
| 09-26 | `msr:5e73a46` | Student (import) | 3 sentences, label-literal ("issue type \textit{BUG} is the majority…", "\textit{local-patch} is the recorded mode"), ends on a limitation |
| 09-27 / 09-28 | `msr:f141169`, `msr:393f596` | B | "In this work, we present…"; three findings; "only when issue type is labeled first"; future work (survival analysis, diff-level labeling); "stable baseline" for longitudinal research |
| 09-30 13:30 | `msr:5262231` | B | Long semicolon sentence split into one sentence per finding |
| 10-02 02:16 / 04:45 | `msr:9c69675`, `msr:9c4567c` | Student | "only when" → "when"; one future-work direction (survival analysis now done); numbers added (16–68%, one vs five percent) |
| 10-02 06:58 | `msr:24d8c65` | Student | "Pooled over ecosystems," added |
| 10-03 10:04 | `msr:86199d6` | B | Subject "expand details" but compresses: numbers, κ and "pooled over ecosystems" removed; "LLM-based classifier validated against a manually labeled sample" |
| 10-04 | `ol:ba3f1ee` | A | Numbers restored (29.4%, 32–84%, 22.5%, 17.8%, 1.8%, 79.7%, 83.5%, 55.4%); "pooled across ecosystems … though not in every ecosystem"; filing-period sentence |

**Instructive excerpts**

(a) Overclaim → conditional. `msr:393f596` (B): "Our results indicate that such trackers can support bug datasets, triage models, and repair benchmarks only when issue type is labeled first…" → `msr:9c69675` (Student) and final: "These results suggest that proof-assistant issue reports can support bug datasets, triage models, and repair benchmarks when issue type is labeled first and analyses are stratified by ecosystem."

(b) Trim then restore within 30 hours. `msr:86199d6` (B, 10-03): "\performance bugs stay open longest and \soundness bugs close among the fastest, but ecosystem explains more of the variation in time-to-close than bug category does." `ol:ba3f1ee` (A, 10-04):
> Among closed bugs pooled across ecosystems, \performance and \tactic bugs stay open longest and \soundness bugs close among the fastest, though not in every ecosystem.
> Across the full filing period, ecosystem explains more of the rank variation in time-to-close than bug category does, but their relative association depends on the filing period.

Reason: none stated for either edit. The pattern is "scope qualifiers removed for brevity, then restored by the senior who owns red lines".

**Final structure (snapshot, ~145 words, 1 paragraph, 6 sentences)**: what we did (1) → three findings in RQ order (3) → "These results suggest … when …" (1) → one future-work direction tied to the main construct limitation (1). No contribution recap, no new claims.

Post-snapshot delta: 7 sentences, one exact number per claim, scope qualifiers restored.

---

### 1.11 Appendix and term table (`A-terms.tex`, `A-appendix.tex`)

**Timeline**

| When | Commit | Role | One line |
|---|---|---|---|
| 09-22 16:47 → 19:04 | `ol:5ecaf3f`, `ol:2193c6b` | Student | Term table ("Locked terms", rejected aliases "theorem prover, interactive theorem prover, ITP") created inside the intro, then moved to an appendix the same evening (`comments_<A>.md:1–3`) |
| 09-26 | `msr:5e73a46` | Student (import) | Five appendices in the build: terms, gold allocation, RQ1/RQ2/RQ3 detail |
| 09-28 00:10 | `msr:393f596` | B | Consolidated into one `A-appendix.tex` (gold allocation, within-ecosystem time-to-close, change size); **A-terms leaves the build** |
| 09-28 | — | B | Asked for an appendix of label definitions (`chat:1on1@2026-09-28T16:43`, notes/04 D8) |
| 09-29 → 09-30 | `msr:7abe3ce`, `msr:c017e0f`, `msr:b45f60d` | Student | Adds κ table, D3/D6/D7 plots, prompt-template figure, bug-category counts, then a 190-line codebook `longtable` |
| 09-29 11:35 | `msr:9809b8c` | A | Removes the prompt-template appendix; in A-terms renames "Frozen snapshot" → "Dataset" (and, from a stale base, uppercase issue types) |
| 09-29 / 10-03 | `msr:fd0b7cd`, `msr:e0ea09b` | Student | A-terms gains an "Excluded reading" column ("A funnel result after filtering", "The words snapshot and export", "Migration artifact") — edits to a file outside the build |
| 10-01 08:47 → 10:09 | chat | A, B | A: 「怎么appendix还在？reviewer不会看的」, 「有用的可以挪进正文，没用的挪去replication package」, 「没人看的，放上去充页数=直接reject」; B: 「把appendix table放到replication package里面，并在readme里提一下」; A: 「把表格浓缩成只有D1-D7+label（最多半页纸），然后指向replication package」 |
| 10-01 18:58 | `msr:464168f` | Student | `\appendix \input{sections/A-appendix.tex}` removed; codebook table condensed; `\todo{add the anonymous link to codebook-labels.md}` |
| 10-02 00:19 → 01:51 | chat | Student, B, A | Student asks whether to keep a small appendix; B: small category-label mapping table, definitions in the package; A: 「不要appendix，软工的人不喜欢」 |
| 10-02 06:02 / 10-03 08:53 | `msr:59f15be` / `msr:836ee75` | Student / sync | File deleted; resurrected by an Overleaf merge (still not in the build) |

**Instructive excerpt** (veto in two lines, `chat:group@2026-10-01T08:47–08:48`, A):
> 我打开看了一下，怎么appendix还在？reviewer不会看的
> 有用的可以挪进正文，没用的挪去replication package

**Final state**: no appendix in the PDF. What the appendix held went to three places: (1) the body (D1–D7 label table in Methodology Step 3; κ ≥ 0.65 rule in text), (2) threats (robustness checks), (3) the replication package (definitions with examples, per-ecosystem tables, prompt). `A-terms.tex` survives as an internal glossary: Term | Object | Excluded reading; italic codebook values via macros; lowercase values; typewriter for GitHub labels; roman for dimension names. Consequence: removing the appendix took the paper from 20 to 17 pages (notes/08 §3) and caused the 10-03 page-filling sprint (§2.11).

---

### 1.12 Data Availability (`main.tex`, unnumbered)

| When | Commit | Role | One line |
|---|---|---|---|
| 10-01 | `msr:0c0dae0`, `msr:464168f` | Student | Checklist plan (anonymous mirror, cite only the anonymous link); item G8 "Data Availability section … does not count toward the page limit. The paper has none yet." |
| 10-02 00:45 | chat | B | Do not cite the project page, 「那个会暴露名字」; anonymous mirror requested |
| 10-02 06:39 | `msr:5776349` | Student | `\section*{Data Availability}` added with the anonymous URL and an inventory sentence ending "the scripts that recompute every number and figure in §…" `[ID]` |
| 10-02 06:58 | `msr:24d8c65` | Student | "every number and figure" → "the shares, medians, effect sizes, and figures" (FINAL-CHECKLIST H9: 28 printed numbers not in the replication outputs) |
| 10-02 23:34 | `msr:405bba7` | Student | "snapshot of the issues" → "dataset of issues" (A's todo) |
| 10-03 10:04 | `msr:86199d6` | B | Trailing slash removed from the URL |
| 10-04 | `ol:ba3f1ee` | A | unchanged |

**Final structure (~80 words, 2 sentences)**: (1) "The replication package is available at <anonymous URL>." (2) One inventory sentence: data, codebook with definition + example per label, gold sample + split, prompt + demonstrations, outputs of both held-out runs, all labels, scripts with the scope of what they recompute. Open issue at submission: "outputs of both held-out runs" conflicts with the author rule "report only the first validation run" (FINAL-CHECKLIST H1).

---

## 2. Cross-section rewrite patterns

Each pattern: what changed, citations (≥ 2), and the reusable rule.

**2.1 Why before how.** `comments_<A>.md:33–50` (model pair at `:40–43`) and `:158–162`. Executed near-verbatim: `ol:5ecaf3f` (denominator sentence, Design), `ol:01fcd0f` (RQ1 opening), `ol:0b63ad2` (intro "Motivate the census before the study mechanics"); A's own `msr:9809b8c` intro RQ blocks ("…, so we test whether…"). Final intro RQ blocks keep it ("A bug dataset built by sampling whole repositories inherits each repository's issue mix, so we first ask…"). Counter-move: once the RQ sections went finding-first, A marked the RQ2 method reminder `\todo{space filling, remove this:}` (`msr:0f96193`) and B deleted it (`msr:b7a448b`); the "why" for denominators now lives only in Design Step 9 and Threats. Rule: put the why in the intro RQ block and the methodology step; results start with the finding.

**2.2 Study-plan voice removal.** `comments_<A>.md` §2.3, §2.7. `ol:5ecaf3f` deletes "The plan fixed three questions, which we keep in their original wording." and "A good outcome for the plan would be…"; `ol:01fcd0f` deletes "because the plan made specific predictions about each proof assistant" and, in the conclusion, "tested a study plan's predictions against the counts". The same voice survived as "frozen snapshot" process talk (`msr:5e73a46` "before reading the frozen snapshot as evidence"), removed by B (`msr:f141169`) and A ("dataset", `msr:9809b8c`, `msr:0f96193`). Rule: the reader evaluates findings, not plan adherence; plan details go to methods in one sentence at most.

**2.3 Number trimming vs restoring (oscillation).** Rule source `comments_<A>.md` §2.4 ("prose should highlight patterns, tables/figures should carry exact counts"). Trims: `ol:6af100c`, `ol:59236e2` (related work loses 12,079 and 123), `msr:9809b8c`, `msr:86199d6` (conclusion). Restores: `msr:9c69675` (related work gets method/scale/result per study), `msr:59f15be` ("at least a third" → "between 32% and 84%"), `ol:ba3f1ee` (abstract, intro, RQ1 headlines, implications, conclusion all get exact percentages). RQ1 body tables went 0 → 1 → 0 → 3 → 0 (06a). Reading: the rule that held was "no laundry lists", not "no numbers"; the last senior pass wants **one exact number per claim** in headline positions (abstract, RQ headline, summary box, conclusion) instead of verbal quantifiers. Rule for the skill: one number per claim sentence, the rest in the table, and decide the convention once for abstract/summary/conclusion.

**2.4 Finding-first slide rule.** A, `msr:0f96193`: "First sentence: highlight the finding in bold / Second sentence refers to a figure or table / Rest … digs deeper", plus "readers are here to read our results, talk our results first" and "avoid subsubsection". Earlier: `ol:01fcd0f`/`ol:de73385` "Lead results with the question and the finding"; `msr:9809b8c` introduced the "Table/Figure X shows that…" second sentence. Final RQ paragraphs follow it ("The Total column of Table~\ref{tab:rq2-medians} shows that…"), and B carried the same shape into implications (bold imperative → "RQx shows that…"). Compliance gaps: two RQ1 findings cite no figure (06a); A's own 10-04 edit produced a doubled bold headline in RQ1 (§1.5). Rule: bold claim sentence, figure/table sentence, deeper sentences; check every finding paragraph for the figure/table sentence.

**2.5 Figure-mirroring methodology.** `chat:group@2026-09-29T11:42` (A: every figure box has matching methodology text, with an example paper's numbered subsections); `msr:9809b8c` todo; `msr:0f96193` `\noteA{figure and text are not synced …}`; `chat:group@2026-10-02T07:29`; execution `msr:9ef4a07` (12 → 10 steps), `msr:b5c0045` (Phase subsections + ten bold Step run-ins), `msr:4c70db0`, `msr:86199d6`; A's 10-04 pass keeps the ten steps but drops "Phase n:" from titles and shortens the caption to "Overview of the study." (`ol:ba3f1ee`). Also: A, 「这个表可以拿掉，把信息放到methodology图里」 (`chat:group@2026-09-29T11:47`). Rule: number the figure's boxes; one bold run-in per box, in order; the figure is the outline.

**2.6 Claim softening and tracker-text hedges.** Novelty: "The first empirical study" → "An empirical study"; "Yet no prior work" → "To our knowledge, no prior work" (`msr:9c69675`; `RW-01@v2`). Severity framing: "severity runs opposite to time-to-close" / "the most severe bugs close fastest" (`msr:3a4c1dc`, `msr:0b8bd5a`) → "soundness bugs close among the fastest" + "pooled over ecosystems … although this order does not hold in every ecosystem" (`msr:24d8c65`; `CF-12@v2`). Causality: "This happens since" → "One possible reason, which our data do not test" (`msr:9c69675`). Necessity: "only when" → "when" (conclusion). Measurement hedges for text-derived labels: "In the classifier's reading of tracker text" (`msr:643836a`), "judged from tracker text" (`msr:9c69675`), "As the tracker text describes them" (snapshot RQ3 summary). Oscillations: `ol:a2c534e` removed a measurement caveat; `msr:5262231` deleted the RQ3 κ caveat; `msr:3e7bab0` restored a hedge; `ol:ba3f1ee` re-scopes universal claims to "the selected repositories" / "kernel-based" assistants but also writes "is usually repaired at the defect site" (hedge erosion). Rule: every claim built on model-read text carries "as described in tracker text" once per paragraph; novelty claims carry "to our knowledge"; speculation is labelled as untested.

**2.7 κ printing rule.** `msr:643836a` printed every per-dimension κ including those below the bar; `msr:9809b8c` (A) cut to a range; `msr:9c69675` header comment "Kappa printing rule: only values >= 0.65 (checklist.md C3)"; appendix caption "Dimensions with κ below 0.65 are omitted" (`A-appendix.tex`); below-bar dimensions described as the classifier's reading with values in the package. Related: κ removed from related work by author decision (`ol:ac81b3a`), only external κ (Colavito 0.68–0.70) kept there. Unresolved at submission: the "first run only" rule vs printing 0.81 and 0.82 (`FINAL-CHECKLIST` H1; `08-threats.tex:12`), and the untraceable human κ 0.74 (§1.9c). Rule: decide which agreement numbers print, where, and with which run, in one written rule; every printed κ needs a script and input in the package.

**2.8 Terminology locks and macros.** `comments_<A>.md:1–3` ("Create a Table of Terms … DO NOT switch terms"; "proof assistant" not "theorem prover"). `ol:30f5bf0`, `ol:efe7cb4`; term table `ol:5ecaf3f` → `ol:2193c6b` → `A-terms.tex` with an "Excluded reading" column (`msr:fd0b7cd`). Lock changes still happened: snapshot → dataset (`msr:9809b8c`, `msr:0f96193`, `msr:405bba7`, `msr:e0ea09b`), family → ecosystem, migration artifact → import-time closure (`msr:9ef4a07`, `msr:e0ea09b`), uppercase → lowercase issue types (`msr:dfc2128`, reverted by A's stale base, re-applied `msr:cfabd75`). Macros: A, 「标签这种最好让agent用宏，后续修改就改宏」 (`chat:group@2026-09-29T12:26`) → `msr:c93ef1f` `codebook-labels.tex`; `msr:3e7bab0` (`\parser`, `\elaborator`, `\kernel`, `\soundness`). Exception: no macros in the submission-form abstract (`chat:group@2026-10-03T18:43`; `msr:4af1aff` → `msr:10e2e5f` repair). Citation form: "Author et al.~\cite" → `\citet` (A, `msr:9809b8c`). Rule: a term table with a rejected-readings column, macros for labels, and a grep after every senior pass for the rejected readings.

**2.9 Parking with `\iffalse` / `%% PARKED` / `%` comments.** `msr:7c705c9` (`% Parked: tab:rq1-types … Restore by removing iffalse.`), `msr:47221f7`, `msr:464168f`; `msr:9c69675` `%% PARKED (author 2026-10-02, discuss first)` ×5, still in HEAD with no recorded discussion; A comments out rather than deletes (`msr:9809b8c` intro roadmap and method sentence; `ol:ba3f1ee` old title, abstract, two implication items); B un-parks for pages (`msr:1ec1a0f` roadmap; `msr:5262231` method sentence). Parked analyses later surfaced in threats (Kaplan–Meier, last-comment endpoint, closure-record check) and the 2021+ cohort in RQ2 (`ol:a610d1d`). Risk: a parked result can vanish (D1 result missing ~1 day, 06a). Rule: park with a one-line restore note and an owner; list parked blocks in the status file; resolve before the final pass.

**2.10 Appendix veto.** `chat:group@2026-10-01T08:47`, `08:48`, `08:56` 「没人看的，放上去充页数=直接reject」, `10:09`; `@2026-10-02T01:51` 「不要appendix，软工的人不喜欢」. Commits `msr:393f596` (5 → 1 appendix), `msr:464168f` (out of build), `msr:59f15be`/`msr:836ee75` (deleted, resurrected by sync). Rule for SE venues with an all-in page limit: no appendix; condensed table in body + pointer to the package.

**2.11 End-game page filling.** Trigger: `chat:group@2026-10-02T22:30–22:36` (B: 「还差一页多才能18页满」); A's priority list `22:44`: 「1. results里那些很短的段落，可以删掉/合并/扩充（加解释和例子） 2. methodology 可以写详细来 3. background看看有没有东西加」; B `@2026-10-03T09:25` 「页数还是差一页，我打算扩写一下implication和threats」. Commits: `msr:d0d4c03` (implications 5 → 7 items; threats intro sentence), `msr:86199d6` (related-work and design overview sentences), `msr:1ec1a0f` (intro roadmap back), `msr:13179f3` (five `\midrule`s, RQ1 figure to full width), `msr:b7a448b` (worked example with real issue/PR; two background sentences). After the overwrite A noted 「页数越写越少」 (`@2026-10-03T19:41`). Rule: when cutting (appendix), recount pages and plan the fill (examples in results, method detail, background gaps, implications, threats); never fill with appendix.

**2.12 Identifying details introduced late.** Title with the dataset size (`msr:9355e35`, 10-03 17:57); real issue/PR numbers and URLs in implications (`msr:b7a448b`, 10-03) and RQ3 (`ol:a610d1d`, `ol:ba3f1ee`, 10-03/04); anonymous URL whose slug names the topic (`msr:5776349`, 10-02); "examples … all come from \Lean~4" (`msr:b7a448b`). These do not break double-blind authorship, but they make the paper recognizable. Separately, TeX sources carried author-revealing material: the `\noteA` macro name, a lab name in A's todo ("check previous papers from SAIL", `msr:9809b8c`) and a private slide-deck URL (`msr:0f96193`); notes are hidden only by `\shownotesfalse`, which `msr:0f96193` switched to `\shownotestrue` and the snapshot still has (no live notes remain in body sections). Rule: grep sources for macros/URLs/lab names before any source upload; keep worked examples but expect them to fingerprint the paper.

---

## 3. SE/MSR empirical paper skeleton (from the final paper)

Word counts are measured on `09-paper-snapshot/` prose: `%` comments and `\iffalse` blocks removed, figure/table environments excluded, LaTeX commands stripped (regex count, ±5%). Page budget: 18 pages incl. figures, + 4 for references; Data Availability does not count.

| # | Section | Words (snapshot) | Floats | Post-snapshot (`ol:ba3f1ee`) |
|---|---|---:|---|---|
| — | Title | 2-part: claim/topic + "An Empirical Study of …" | — | topic-first title |
| — | Abstract | ~274 (14 sentences) | — | ~192 (5 sentences + findings block) |
| 1 | Introduction | ~1,110 (10 blocks + contributions) | 1 figure | ~same, numbers added |
| 2 | Background and Related Work | ~1,150 (9 paragraphs) | — | + repository-roles paragraph |
| 3 | Methodology | ~1,870 (18 paragraphs) | 1 workflow figure, 1 codebook table | ~same |
| 4 | Results: RQ1 | ~870 (7) | 2 figures | ~same |
| 4 | Results: RQ2 | ~340 (5) | 1 table | + filing-period paragraph |
| 4 | Results: RQ3 | ~700 (6) | 1 three-panel figure | + worked examples |
| 5 | Implications | ~900 (8) | — | + ~15 lines |
| 6 | Threats to Validity | ~720 (8) | — | unchanged |
| 7 | Conclusion | ~145 (1) | — | ~190 |
| — | Data Availability | ~80 (2 sentences) | — | unchanged |
| | **Total** | **≈ 7,900 body + Data Availability (≈ 8,150 with abstract)** | 5 figures, 2 tables | |

**Paragraph functions**

- *Abstract*: background (1) → gap (1) → "To fill this gap, we study …" with scope (1) → method in one sentence (1) → 1–2 key findings, or one per RQ (2–6) → recommendation (1, or one per audience). Plain text, no macros or labels (submission form).
- *Introduction*: context for a general SE reader (what the system is; why failures are costly) → figure that shows the phenomenon → why the data source matters to SE (datasets, triage, benchmarks) and why the domain differs ("three ways") → gap: what prior SE work covers and misses; assumptions inherited from other domains, each cited → "To address this gap" + scope → RQ blocks (bold question; one "…, so we…" why sentence; 2–3 "We find" sentences) → one-sentence method → itemized contributions (study, instrument, evidence, dataset) → roadmap.
- *Background and related work*: one roadmap sentence → domain background for SE readers (components named as they appear later) → "shares concerns with general X, but differs in N respects" → one subsubsection per research strand; one sentence per cited study with method, scale, result; a sentence on what the strand does not cover → "Taken together, …" synthesis + "Our study takes …".
- *Methodology*: overview paragraph pointing to the workflow figure → one subsection per figure phase, one bold "Step n" run-in per figure box → each step: purpose clause, then procedure, then the number it produced. Agreement statistics only where they pass the stated bar.
- *Results*: one subsection per RQ; finding paragraphs; summary box.
- *Implications*: one sentence naming audiences → one subsection per audience → items in the bold-imperative format.
- *Threats*: one sentence naming the four categories with a citation → one subsection per category → threat → check or mitigation → residual.
- *Conclusion*: one paragraph: what we did, findings in RQ order, conditional implication ("suggest … when …"), one future-work direction tied to the main limitation.
- *Data Availability*: URL + one inventory sentence whose scope matches what the package really recomputes.

**RQ answer format (per finding paragraph)**
1. `\textbf{<finding as a full sentence, scoped: "pooled over …", "in the studied …">}`
2. "<Figure/Table/column X> shows that …" with one or two exact numbers.
3. 1–3 sentences that dig deeper: breakdown, exception, robustness, or a definition the reader needs.
Paragraphs with nothing new are merged (A: "if we have nothing to talk, talk nothing", `msr:0f96193`). No `\subsubsection` inside an RQ.

**Summary (takeaway) box format.** `tcolorbox` (`colback=black!3`, `colframe=black!55`, bold title), placed at the end of each RQ subsection, titled only "RQn Summary". Title history: "Takeaway for RQn" (Student census draft, `ol:af26086`) → "Summary (RQn): <headline claim>" (B, `msr:f141169`) → "RQn Summary" (A, `msr:9809b8c`). Content: 2–4 sentences, pooled claim first then its exception, one or two exact numbers at most, same hedges as the body ("As the tracker text describes them").

**Threat categories used.** Conclusion validity (effect sizes vs p-values, independence, collapsed categories, model non-determinism and run-to-run variation), Construct validity (proxy ≠ construct, text-derived labels, classifier inputs vs validation, gold as one reading, training-data contamination, one label per dimension), Internal validity (data artifacts such as tracker imports, censoring of open items, confounding of group with period, direction of causation, missing-status bias), External validity (selection criteria and exclusions, popularity bias, uneven group sizes, time of snapshot, illustrative examples from one group). A "Reliability" category existed for one day (`msr:e0ea09b`) and was folded back.

---

## 4. Excerpts that would identify the paper if reused publicly

Everything below must be paraphrased or replaced with placeholders before it enters a public skill, checklist or handbook case.

| Where in this note | Identifying element |
|---|---|
| §1.1 title table, §1.1(b)(c), §1.2 delta | All titles; "23,671"; "five ecosystems" with names (Lean, Rocq, Agda, F*, CakeML); the 10-04 abstract numbers (29.4%, 1.2%) |
| §1.2 (a)(b), final structure, delta | "proof assistant", "soundness bug", "elaborator/tactics/kernel" together with dataset size; seven repositories; ecosystem homepage footnotes; 29.4/30.5/15.7–77.3/15.5–67.6/1.2 vs 4.9 |
| §1.3 (b)(c), delta | Cited works with their numbers (12,079 failures, 36.4%, 62 bugs, 31/19, 149 commits); F*/SMT footnote; CakeML/HOL4 role sentence |
| §1.4 | "582", "291", κ 0.74/0.71–0.83, "Build issue payloads", 12 → 10 steps, the lab name in A's todo, the star date and snapshot date |
| §1.5 | "70.6% of the 23,671 issues", 69.7%/24.2%, 16–68% label recall, "Mathlib4/UniMath" |
| §1.6 | Medians 48.3/31.4/7.2/8.2 days, per-ecosystem ratios, Agda counterexample, 2021+ ε² values (0.0052/0.0102/0.0249/0.0108) |
| §1.7 | All issue/PR numbers (#6140, #6173, #6125, #3096, #3098, #4650, #4651), 79.7%/83.5%, 48 lines |
| §1.8 | Issue #3941 and PR #7177 with URLs, 11.6 → 7.5 s, 343 days; 3,427 of 18,085; 74.7%/60.8%; 60.6%/66.2%; 90.5 lines; 83.3% |
| §1.9 | 291 held-out issues, κ 0.81/0.82/0.74, 28.7 → 11.3 days on 10,202, 40 (2.7%), 145 Agda / 46 Rocq bugs, 3,205 open bugs, "July 2026", "≥ 1,000 stars", "issue examples … from Lean 4" |
| §1.10 | 22.5%/17.8%/1.8%/55.4% and the full conclusion sentences |
| §1.11 | A-terms rows naming repositories (`leanprover/lean4`, `mathlib4`, `rocq-prover/rocq`, `UniMath`), import dates (8 Aug 2015, Bugzilla ≤ 2006) |
| §1.12, §2.12 | Anonymous mirror URL (slug names the topic); "codebook-labels.md" path |
| §2.12 | TeX-source items: senior's macro name, lab name, private slide-deck URL |
| Chat quotes throughout | Safe in substance (no names), but the Chinese wording plus dates fingerprints the team; paraphrase in public files |
| Not quoted here on purpose | Author block in `09-paper-snapshot/main.tex` (names, affiliations, emails), commit author strings, the replication repo's personal Pages URL in `chat:group@2026-10-05T22:46` |

Public-safe generalizations already used in §2–§3: "niche software ecosystem", "text-derived labels", "a two-author gold sample", "an LLM classifier validated on a held-out half", "five ecosystems / seven repositories" (keep counts out), "issue tracker as a record of maintenance".

---

## 5. No-evidence items for this note

- Why A changed the abstract, RQ headlines and conclusion to exact numbers on 10-04; why A softened scope to "selected repositories"/"kernel-based": no message.
- Whether the uploaded PDFs (10-03 19:56, 10-04 08:46, 10-04 18:04) equal any archived state, and whether the RQ1 doubled-headline defect was fixed before upload.
- Whether any `%% PARKED … discuss first` item was discussed.
- Who asked for "first empirical study" → "An empirical study": only the machine-provenance item `RW-01@v2`.
- The computation behind human κ = 0.74 (notes/04 §1.6), and why the 14-cell overlay disclosure was deleted.
- Whether the Advisor relay (09-26) caused B's 09-27 implications and contributions rewrite: timing only.
