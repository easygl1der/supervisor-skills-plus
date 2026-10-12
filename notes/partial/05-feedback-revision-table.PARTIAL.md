# 05 — Feedback-to-revision table (comment → change → commit → status)

Archive: `~/Projects/supervisor-skills-msr-tpa` (all paths below are relative to its root). Times are Asia/Shanghai (UTC+8); git `AuthorDate` values in `-0400` were converted. Citation formats follow `notes/03-archive-map.md` §4: `msr:<sha7>` = `07-overleaf-history/patches-msr-tpa/<YYYYMMDD-HHMM>_<sha7>.patch`; `ol:<sha7>` = `07-overleaf-history/patches-overleaf/<YYYYMMDD-HHMM>_<sha7>.patch`; `chat:group@...` = `04-comms/20260929-1007-wechat-group/messages.jsonl`.

Method. Every "addressed-verified" status below was checked by reading the `.tex` hunks of the cited patch (not the auto-generated Chinese summaries, not `REVISION-SUMMARY.md`). Inline `\hao{}` / `\todo{}` markers were traced with a script that lists every added/removed `.tex` line containing the marker across all 105 `patches-msr-tpa` and all 252 `patches-overleaf`; phrase-level checks used the same script on `.tex` hunks only, plus the final paper (`09-paper-snapshot`, HEAD `87bf139`). Commit authorship comes from `msr-tpa-commits.tsv` / `overleaf-commits.tsv`; "Updates from Overleaf" commits under Senior B's account have author `?` (content editor not resolvable, `msr-tpa-SUMMARY-TABLE.md`).

Roles: **A** = Senior co-author A; **B** = Senior co-author B; **S** = Student (first author); **ADV** = Advisor (relayed through B); **AG** = agent-generated. Sections 1–2 quote sources verbatim (quotes may contain names); sections 3–5 use roles only.

Status vocabulary: **verified** = addressed-verified; **partial** = addressed-partially; **not** = not addressed; **superseded** = overtaken by a later decision or rewrite; **no evidence** = nothing in the archive shows the change either way.

---

## 1. Comment inventory

Columns: ID · origin (role, channel) · date · quote/paraphrase (original language, <25 words) · source · type · size · needs-author-decision.

### 1.1 Senior co-author A — written comments file (`02-comments-hao/comments_hao.md`)

Delivery date: the file's first commit is `ol:2698705` (2026-09-26 12:43, committed by S's account). A burst of S commits on 2026-09-22 16:47–23:59 whose messages paraphrase the file's headings (§2) and one of which inserts the file's suggested sentence verbatim (`ol:01fcd0f`) means the comments were in hand by 2026-09-22 16:47. Exact delivery time: no evidence. `comments.md` (2026-09-28) is a consolidated checklist of the same 11 items (lines 10–19); it adds no new comment.

| ID | Quote / paraphrase | Source | Type | Size | Decision? |
|---|---|---|---|---|---|
| FB-A-01 | "Create a Table of Terms we are using in the draft, and follow the terms, DO NOT switch terms" | `comments_hao.md:1` | terminology | M | no |
| FB-A-02 | "Proof assistant is a better name vs. Theorem Prover, fix the draft throughout" | `:3` | terminology | S | no |
| FB-A-03 | check arXiv 2511.17330 "to learn how SE people introduce rocq/proof assistant" | `:4` | citation / framing | M | yes: whether to cite it |
| FB-A-04 | §2.1 "The draft needs more context before methodology details"; say why SE readers should care about PA trackers | `:8–29` | structure / framing | L | no |
| FB-A-05 | §2.2 "Motivate 'why' before 'how' … This is the biggest writing problem." | `:33–50` | framing | L | no |
| FB-A-06 | §2.3 "REMOVE/REWRITE all the places mention study plan" | `:54–75` | framing / scope | M | yes: how much preregistration to keep |
| FB-A-07 | §2.4 "Too many numbers in prose, AVOID laundry list style writing, DO NOT repeat the numbers in the table" | `:79–100` | claim-evidence / structure | M | no |
| FB-A-08 | §2.5 results need "question → answer → implication" structure (5-step template) | `:104–120` | structure | L | no |
| FB-A-09 | §2.6 "motivate the paper in SE terms … Motivate from Maintenance and Evolution" | `:124–143` | framing | L | no |
| FB-A-10 | §2.7 "Some section openings are too procedural … Open with the substantive point" | `:147–164` | structure | M | no |
| FB-A-11 | §2.8 "The draft is too defensive … Be precise once, then move on." | `:168–184` | framing | M | no |

### 1.2 Senior co-author A — inline `\hao{}` / `\todo{}` macros in the paper repo

Protocol defined by A in `msr:9809b8c` (`main.tex`, patch lines 65–74): `\hao{...}` = "Hao's notes; resolved by Hao or the agent"; `\todo{...}` = "action items left for the student to fix; the agent must not resolve them"; notes render in colour while `\shownotestrue`.

Drop 1 = `msr:9809b8c` "hao's comments", 2026-09-29 11:35 (author A). Drop 2 = `msr:0f96193` "hao's comments", 2026-10-02 07:45 (author A).

| ID | Macro | Quote (verbatim, trimmed) | Location / patch line | Type | Size | Decision? |
|---|---|---|---|---|---|---|
| FB-A-INL-01 | `\todo` | "include more papers, see the file I shared" | `02-related-work.tex`; `msr:9809b8c` l.226 | citation | M | yes: which papers (file not in archive) |
| FB-A-INL-02 | `\todo` | "the overview figure and the content in methodology is not synced, check previous papers from SAIL …" | `03-design.tex` subsection title; l.311 | figure / structure | L | no |
| FB-A-INL-03 | `\todo` | "put this information in the overview figure and plot the link btw the data to each RQ, remove this table" | funnel-table caption; l.470 | figure / structure | M | no |
| FB-A-INL-04 | `\todo` | "anything we wanna say about this figure? any new findings? … if not, remove the figure" | RQ1 alt figure; l.659 | figure / claim-evidence | M | yes: keep or drop |
| FB-A-INL-05 | `\todo` | "if we wanna keep this figure, increase the font size in figure b" | alt-figure caption; l.670 | figure / formatting | S | no |
| FB-A-INL-06 | `\hao` | "figure and text are not synced, e.g., you mention `Build issue payloads' in the figure, where is the text?" | study-workflow caption; `msr:0f96193` l.40 | figure / structure | L | no (re-raise of INL-02) |
| FB-A-INL-07 | `\todo` | "do not call it snapshot, call it dataset" | `03-design.tex` subsection title; l.49 | terminology | S | no |
| FB-A-INL-08 | `\todo` | "fix AI smells, e.g., `Corpus'" | subsection title; l.58 | terminology | S | no |
| FB-A-INL-09 | `\todo` | "which figure/table support the claim? show it in the first sentence. Follow the slides … P42" | `04-rq1.tex` first finding; l.70 | structure / claim-evidence | M | no |
| FB-A-INL-10 | `\todo` | "First sentence: highlight the finding in bold – Second sentence refers to a figure or table – Rest … digs deeper" | `04-rq1.tex`; l.72–74 | structure | M | no |
| FB-A-INL-11 | `\todo` | "readers are here to read our results, talk our results first" | `04-rq1.tex` reporter paragraph; l.84 | structure | S | no |
| FB-A-INL-12 | `\todo` | "avoid subsubsection, remove it, just follow the slides" | `04-rq1.tex`; l.92 | structure | S | no |
| FB-A-INL-13 | `\todo` | "space filling, remove this:" | `05-rq2.tex` opener; l.106 | structure | S | no |
| FB-A-INL-14 | `\todo` | "It is a table! why label it as a figure?! Please format it as a normal table" | `05-rq2.tex`; l.108 | figure / formatting-venue | M | no |
| FB-A-INL-15 | `\todo` | "merge this paragraph with the next paragraph, if we have nothing to talk, talk nothing" | `06-rq3.tex`; l.121 | structure | S | no |
| FB-A-INL-16 | `\todo` | "too long, please break it down" | `08-threats.tex` Internal Validity; l.151 | structure | M | no |

Also in drop 2 (not a comment, an action): A switched `\shownotesfalse` back to `\shownotestrue` (`msr:0f96193` l.25–27) 66 min after S had turned notes off in `msr:5776349` (2026-10-02 06:39, l.305–306).

Pre-protocol `%%` notes (author: no evidence; committed by S's account in `msr:643836a`, 2026-09-29 00:54, l.3045 and l.3064):

| ID | Quote | Type | Size |
|---|---|---|---|
| FB-UNK-INL-01 | "%% Note in above description that Yihua indead checked the prompt consistency by randomly pick half of the gold sample …" | claim-evidence | S |
| FB-UNK-INL-02 | "%% The following paragraph should be compressed. (Yihua)" | structure | S |

### 1.3 Senior co-author A — group chat (paper-revision requests seen while verifying inline comments)

<!--CHAT-A-->

### 1.4 Senior co-author B — 1:1 chat, PDF annotations, group chat

<!--B-->

### 1.5 Advisor (relayed)

<!--ADV-->

### 1.6 Agent-generated comments (`02-comments-hao/adams-skill-revision-comments.md`)

Header: "Produced: 2026-09-28. Twelve independent Opus 5.5 subagents, one issue each" and "Status: comments only. No TeX edits." (lines 3–5). **Agent output, not a human comment.** Priorities as tagged in the file.

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
| FB-AG-11 | C11 [P2] | "no prior work" repeated; keep the "What Breaks…" title retired | `:201` | framing | M | yes: title |
| FB-AG-12 | C10 [P2] | Related Work lacks a time-to-close / closed≠fixed cluster; "Do not invent keys" | `:213` | citation | M | yes: bibliography |

---

## 2. Resolution table

Latency = comment time → first commit that makes the requested change (→ marker removal, where different).

### 2.1 Senior A written comments (`comments_hao.md`)

The responses landed in the Overleaf "census draft" line (`patches-overleaf`, S's account), mostly as one commit per comment heading on 2026-09-22. The paper repo (`msr-tpa-paper`) was later re-imported from Overleaf (`msr:5e73a46`, 09-26), and A re-applied several of these rules himself in `msr:9809b8c`. Final-state checks are against `09-paper-snapshot`.

| ID | Change made (what moved) | Commit(s) | Status |
|---|---|---|---|
| FB-A-01 | Locked-terms table added with "Rejected aliases (do not use in our prose): theorem prover, interactive theorem prover, ITP"; then moved out of the intro and dropped to prose; survives as internal table `sections/A-terms.tex` ("Locked names"; lists "The words snapshot and export" as rejected for *Dataset*), not compiled into final `main.tex` | `ol:5ecaf3f` (09-22 16:47) "Lock a term table and stop switching names for the same concept."; `ol:2193c6b` (19:04); `ol:b8bc34d` (19:09) | verified (as an authoring artifact, not a paper table) |
| FB-A-02 | Titles and prose "Theorem Prover(s)" → "Proof Assistant(s)"; keywords "interactive theorem proving" → "proof assistants"; "Interactive" dropped from title. Final paper: 0 occurrences of "theorem prover" | `ol:30f5bf0` (09-22 13:32); `ol:5ecaf3f`; `ol:efe7cb4` (17:06); `ol:f1addde` (17:10) | verified |
| FB-A-03 | arXiv 2511.17330 not in `09-paper-snapshot/refs.bib`; no commit references it | — | no evidence |
| FB-A-04 | Abstract/intro now open with what PAs are, cost of regressions, trackers as maintenance record, naive mining risk; "Each issue must be labeled into a category before defects can be counted" | `ol:55ea198`, `ol:0b63ad2` (09-22 16:47–48) "Motivate the census before the study mechanics."; `ol:805bf08` (23:36) | verified |
| FB-A-05 | Design passages rewritten motivation-first, e.g. "Defect statistics are meaningless if the tracker mix is unknown, so every issue receives an *issue type* before any defect field." | `ol:6247934` (09-22 21:28) "Revise passages that still miss the writing comments." | verified (sampled passages) |
| FB-A-06 | Removed "Our idea is to treat a written study plan as a set of predictions"; "because the plan made specific predictions"; "A good outcome for the plan would be". 01fcd0f still added "pre-registered family signatures" in a finding head. Final paper: 0 hits for "study plan", "preregist", "the plan predicted" | `ol:55ea198`; `ol:01fcd0f` (16:49); `ol:4d393bd`/`ol:5ecaf3f` | verified (final); partial on 09-22 |
| FB-A-07 | Exact counts moved out of prose ("Table~… and Figure~… carry the exact medians"; detail counts to appendix) | `ol:0842e26`, `ol:b28f788` (16:50–52) "Leave exact counts in tables and state the pattern in prose."; `ol:6af100c` (21:56) | partial (final RQ2 prose still lists several medians, e.g. 48.3 / 31.4 / 7.2 days) |
| FB-A-08 | Results lead with question and finding (01fcd0f); A himself rewrote intro RQs as question → why it matters → finding (`msr:9809b8c` patch l.128–138) | `ol:01fcd0f`, `ol:de73385` "Lead results with the question and the finding."; `msr:9809b8c` | superseded by A's later finding template (FB-A-INL-09/10) |
| FB-A-09 | Abstract opener rewritten almost line-for-line from the §2.6 bullet list ("increasingly important software infrastructure … main public record of their maintenance … naive mining can distort bug datasets, triage models, repair benchmarks, and effort estimates") | `ol:55ea198` (09-22 16:47) | verified (then superseded by later abstract rewrites; final abstract keeps the bug-dataset recommendation) |
| FB-A-10 | A's suggested opener inserted verbatim ("Before reasoning about defects, we need to know whether these trackers mostly contain defects at all."); "The approach is a count …" removed | `ol:01fcd0f` (16:49) | verified (sentence later rewritten; not in final) |
| FB-A-11 | "and nothing more" removed; "we do not read that decision as evidence" never found in any `.tex` hunk | `ol:5ecaf3f` | partial / no evidence for the second phrase |

`06-revision/REVISION-SUMMARY.md` (agent-written; added to the repo in `msr:815305e`, 2026-09-29 18:19, commit message "cursor-safety: checkpoint before destructive delete") marks all 11 items "✅ Addressed" for the design section and gives before/after LaTeX. **None of its "After" sentences appears in any `.tex` hunk of either repo or in the final paper** (checked: `Harrison_2014`, "Issue trackers conflate", "This design trades oracle-level", "How an issue is closed differs", "Mining these trackers supports"); the `.tex` committed in the same commit contains its "Before" sentence ("Since manually labeling 23,671 issues is infeasible, we combine …"). Treat REVISION-SUMMARY as a plan, not evidence of change.

### 2.2 Senior A inline macros

| ID | Change made | Commit(s) | Marker removed | Latency | Status |
|---|---|---|---|---|---|
| FB-A-INL-01 | S appended a progress note *inside* the `\todo` (156 papers screened; "Manuscript text not yet updated—awaiting author decision on which papers to cite"); one sentence with three new cites added (Zhang_2019, Bringolf_2022, Lin_2023); S then commented the marker out; B deleted it. Final RW cites 16 keys incl. Zhang_2019, Bringolf_2022, Ahmed_2025, Zhang_2023, Selsam_2020 | `msr:84b9197` (09-29 15:56); `msr:3d34425` (22:17); `msr:59f15be` (10-02 06:02, `% \todo`); `msr:b7a448b` (10-03 11:30, B) | `b7a448b` (B) | 4h21m note; 10h42m first cites | partial (the shared file is not in the archive, so coverage cannot be checked) |
| FB-A-INL-02 | Methods restructured into subsections that mirror the figure phases; caption gained phase text. Marker removed in an S-account agent checkpoint commit. Re-raised by A as FB-A-INL-06 | `msr:815305e` (09-29 18:19) | `815305e` (S account) | 6h44m | superseded → re-raised (see INL-06) |
| FB-A-INL-03 | `tab:analysis-funnel` deleted; dropout counts moved into the workflow caption ("Open bugs (3,205) drop out before RQ2 …"); figure itself redrawn later by B. Same request also made in chat (`chat:group@2026-09-29T11:47`) | `msr:815305e`; figure: `msr:9ef4a07`, `msr:fdc9ca6`, `msr:b5c0045` | `815305e` | 6h44m | verified (table removed; dropouts in caption and figure) |
| FB-A-INL-04 | S removed the alt figure (16:14), then reinstated it 5 h later as `fig:rq1-alternative` with a caption saying "Both panels show identical data"; in the final paper the alternative *replaced* the original overview figure ("Superseded by fig:rq1-alternative", `09-paper-snapshot/sections/04-rq1.tex:66`) and every RQ1 finding cites it | `msr:7c705c9` (09-29 16:14); `msr:b3dafcd` (21:14) | `7c705c9` | 4h39m | superseded (resolved by swapping primary and alternative) |
| FB-A-INL-05 | Marker deleted together with the figure in 7c705c9 while the font was unchanged; re-raised by A in chat (`chat:group@2026-10-03T11:32`, "b的字体弄大一些"); heatmap label size 1.95 → 3.8 | `msr:94e651f` (10-03 12:04) | `7c705c9` (before fix) | 4d0h29m (32 min after chat re-raise) | verified (late) |
| FB-A-INL-06 | B rewrote the methods opener and caption, deleted the "Build issue payloads" step from the drawio (`msr:9ef4a07` l.122), redrew the figure (`fdc9ca6`), then rewrote §3 as "Phase 1: Dataset Construction … Step 1: Select repositories. … Step 2: Collect issues." so each subsection describes one figure step; S added "(Done: … redrew the figure from scratch with ten steps …)" inside the `\hao` | `msr:9ef4a07` (10-02 11:31); `msr:405bba7` (23:34, Done note); `msr:fdc9ca6` (10-03 01:24); `msr:b5c0045` (03:48) | `b5c0045` (B) | 3h46m first fix; 20h03m closed | verified |
| FB-A-INL-07 | Subsection "Issue Snapshot and Data Cleaning" → "Issue Collection"; body "frozen snapshot" → "collect … this copy"; S re-inserted the marker with a Done note listing remaining replacements in Threats/Data Availability (`main.tex` "snapshot of the issues" → "dataset of issues") | `msr:9ef4a07` (B); `msr:405bba7` (S) | `b5c0045` | 3h46m | verified (final compiled sections: 0 "snapshot") |
| FB-A-INL-08 | "Full-Corpus Labeling and Analysis" → "Issue Labeling and Analysis"; "full corpus" removed from caption. The phrase had been introduced by the S-account agent commit `815305e` | `msr:9ef4a07` (B) | `b5c0045` | 3h46m | verified (final: 0 "corpus") |
| FB-A-INL-09 | First findings rewritten to "The issue-type counts in Figure~\ref{fig:rq1-alternative}a show that …", "Figure~…b shows that …"; S then commented the marker out with "[Partly addressed: … The remaining findings still need review.]" | `msr:ee351a3` (10-03 14:31); `msr:ac172bd` (18:37) | commented out by S (`ac172bd`); never deleted | 30h46m | partial |
| FB-A-INL-10 | Same pass as INL-09; findings keep a bold first sentence; marker commented out | `msr:ee351a3`, `msr:ac172bd` | commented out by S | 30h46m | partial |
| FB-A-INL-11 | Paragraph now opens with own numbers; the Bissyandé comparison moved to the last clause | `msr:405bba7` (S) | `msr:1f68c99` (10-03 09:23, Overleaf, author `?`) | 15h49m | verified |
| FB-A-INL-12 | `\subsubsection{Trigger, Mathematical Domain, and Proof Mechanism}` removed; content became two RQ1 findings; takeaway moved after them | `msr:405bba7` | `msr:4f8b488` (09:21, author `?`) | 15h49m | verified |
| FB-A-INL-13 | Whole sentence deleted (by B, not S) | `msr:b7a448b` (10-03 11:30) | same | 27h45m | verified |
| FB-A-INL-14 | `figure*` with a booktabs table in panel (a) → standalone `\begin{table}` `tab:rq2-medians` with caption above; strategy chart panel moved to RQ3 | `msr:405bba7`; `msr:e0ea09b` (Done note updated) | `4f8b488` | 15h49m | verified |
| FB-A-INL-15 | RQ3 lead paragraph merged into the next one; three-panel figure added | `msr:e0ea09b` (10-03 01:30) | `4f8b488` | 17h45m | verified |
| FB-A-INL-16 | Internal Validity shortened; model-related threats moved to a new `\subsection{Reliability}` (patch l.14841), GitHub-only scope to External Validity. B later folded Reliability back during "expand threats+implications" (`msr:d0d4c03`, 10-03 09:58); final Threats has 4 subsections | `msr:e0ea09b`; `msr:d0d4c03` | `4f8b488` | 17h45m | verified, then partly undone by B for page budget (chat 10-03 09:25: one page short, expand implications and threats) |
| FB-UNK-INL-01 | Phase-2 description now states the tuning half / held-out half split checked "by computing Cohen's κ against the gold labels" | `msr:9809b8c` (A, 09-29 11:35) | same | ≤11h | verified (resolved by A himself) |
| FB-UNK-INL-02 | Classification methodology rewritten as three short "Step" paragraphs | `msr:9809b8c` (A) | same | ≤11h | verified (resolved by A himself) |

### 2.3 Senior A chat requests

<!--RES-CHAT-A-->

### 2.4 Senior B (chat, PDF, group chat)

<!--RES-B-->

### 2.5 Advisor (relayed)

<!--RES-ADV-->

### 2.6 Agent-generated comments

| ID | Change made | Commit(s) | Status |
|---|---|---|---|
| FB-AG-01 (C12) | The "14-cell overlay … we do not use that overlay" sentence was deleted by A in his rewrite; no paper text discusses the overlay afterwards; data-side action: no evidence | `msr:9809b8c` (A) | partial (text); `[AUTHOR]` facts: no evidence |
| FB-AG-02 (C1) | A changed "The classifier labels four out of five fixed bugs as resolved by a local patch" → "Four out of five fixed bugs are resolved by a local patch" and kept one hedge sentence in the body — the opposite of C1 for the headline, consistent with A's §2.8 "be precise once". Final RQ3 keeps one hedge ("the shares below describe how the classifier reads that text", `06-rq3.tex:29`); final abstract states the local-patch finding unhedged | `msr:9809b8c` | partial (conflict A vs agent; A's style won) |
| FB-AG-03 (C2) | "repair effort" removed from `.tex`; final: 0 hits | removals in `msr:3e7bab0`, `msr:9c69675` (10-02) | verified |
| FB-AG-04 (C3) | A rewrote the abstract without numbers; final abstract: "close among the fastest" (C3's suggested wording), both-denominator numbers gone from the abstract | `msr:9809b8c`; final abstract | verified |
| FB-AG-05 (C7) | A *added* "about six times more" to the intro (`msr:9809b8c` l.134) a day after C7 said to drop it; S removed all five occurrences in the baseline commit before the methodology/RQ revision; final abstract adds "This order does not hold in every ecosystem" | `msr:9809b8c` (+); `msr:3e7bab0` (−5, 10-02 00:25) | verified (after conflict) |
| FB-AG-06 (C5) | Conflicts with FB-A-INL-03. S's agent commit removed the funnel table and put dropouts in the figure caption, i.e. A's request won; the 1,010 residue now appears in Design (`03-design.tex`) | `msr:815305e` | superseded by A |
| FB-AG-07 (C4) | S added per-dimension κ ("0.826 on issue type, 0.713 and 0.736 on bug category …") the night after C4 was produced; A compressed it to "κ from 0.71 to 0.83" for the three finding dimensions | `msr:643836a` (09-29 00:54); `msr:9809b8c` | verified |
| FB-AG-08 (C8) | "This happens since …" removed | `msr:9c69675` (10-02 02:16) | verified |
| FB-AG-09 (C6) | "how severe they look" and "most severe bugs" removed (final: 0); "layers above the kernel" never found in `.tex` | `msr:7c705c9`, `msr:9c69675` | verified |
| FB-AG-10 (C9) | "a limit of the codebook" removed; `other` reported as an RQ1 finding (already present in `msr:9809b8c` RQ1) | `msr:643836a` | verified |
| FB-AG-11 (C11) | C11: keep "What Breaks…" retired. Title went "What Breaks…" → "Proof Engineering in the Wild" (`msr:d0bc904`, 09-28) → back to "What Breaks in Proof Assistants, and How Maintainers Fix It" by S (`msr:9355e35`, 10-03 17:57); final `main.tex:116` | `msr:9355e35` | not (author decision overrode agent) |
| FB-AG-12 (C10) | S added a "Time-to-Close and Resolution Status" RW subsection citing Zaman_2011/2012, Shihab_2013, Tagra_2022 (C10 had warned these keys did not exist in `refs.bib`); 11 h later A deleted that subsection and cut "four respects" to "three" | `msr:643836a` (+); `msr:9809b8c` (−) | superseded by A |
