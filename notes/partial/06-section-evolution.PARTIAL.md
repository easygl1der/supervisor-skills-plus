# 06 — Section evolution (SE/MSR empirical paper case)

Private Phase-2 note. Evidence: `~/Projects/supervisor-skills-msr-tpa` (see `03-archive-map.md` for citation formats §4 and gaps §5). Paths below are relative to the archive root. All times Asia/Shanghai (UTC+8).

Roles only in §§2–5 of each section and in the pattern/skeleton parts: **Student** (first author), **Senior co-author A** (written comments, two in-repo comment passes, final pass), **Senior co-author B** (repo hub, restructuring, methods figure, page budget). "Unknown" = Overleaf anonymous or a sync commit whose real author cannot be resolved. Name mapping stays in `private/CASE.md`.

Privacy flag: `[ID]` marks an excerpt that would identify the paper if reused publicly (title, the dataset size, repository/library names, issue/PR numbers, the anonymous URL). Paper text is quoted here only because this is a private note.

---

## 0. Read this first: what "final" means, and four traps in the evidence

1. **The snapshot is not the submitted version.** `09-paper-snapshot/` = paper repo HEAD `msr:87bf139` (10-03 19:38). The submission system went down near the deadline and the window was extended ("还有18小时", chat:group@2026-10-04T02:06, Senior co-author A). Senior co-author A then edited in Overleaf and "提交了一个新版本" (chat:group@2026-10-04T08:46); Senior co-author B submitted again (chat:group@2026-10-04T18:04). Those edits exist only in the Overleaf git: `ol:ba3f1ee` (10-04 13:16, A, +127/−153 across abstract and sections 01–09), plus `ol:1499336`, `ol:3410f5e` (B, refs.bib only). The last pre-deadline Overleaf commit by A, `ol:a610d1d` (10-03 19:38:54), was overwritten 10 s later by the GitHub→Overleaf sync `ol:214cc0c` (an exact reverse diff), which is what A complained about: "别用git了吧，感觉很多改动都没了 … 我改了半天的东西都没了" (chat:group@2026-10-03T19:41–19:42). `ol:ba3f1ee` re-applies all of `ol:a610d1d` and goes further. **Each section below therefore ends with a "Post-snapshot delta (`ol:ba3f1ee`)" line.**
2. **`09-paper-snapshot/main.tex` does not match `msr:87bf139` either.** Its abstract (14 short sentences, "To fill this gap… For researchers… For tool builders…") is the Student's Overleaf edit made between 19:44 and the 19:56 upload ("我直接 overleaf 改了", chat:group@2026-10-03T19:44; "交了", 19:56). It never reached the paper repo; its sentences survive only as `%` comment lines that A left in `ol:ba3f1ee`. Section files in the snapshot do match `msr:87bf139`.
3. **Sync commits look like edits.** In the paper repo, "Updates from Overleaf" and merges are made under Senior co-author B's account but usually duplicate an adjacent real commit (e.g. `msr:578d640` ≈ `msr:9809b8c`; `msr:8fc36d3` ≈ the Student's 09-29 commits). In the Overleaf repo, "Sync GitHub main @ <sha>" is a bot copy. Only the unique Overleaf-side edits are attributed below. The Chinese one-line summaries in `07-overleaf-history/*SUMMARY-TABLE.md` are generated from subject + touched files; several are misleading (e.g. `msr:815305e` "cursor-safety: checkpoint before destructive delete" actually carries the agent-assisted 03-design rewrite documented in `06-revision/REVISION-SUMMARY.md`).
4. **Two drafting lines before 09-26.** From 09-22 to 09-27 the Student revised an independent "census draft" in the Overleaf repo, already answering Senior co-author A's written comments (`02-comments-hao/comments_hao.md`, dated 09-22 per `TIMELINE_DRAFT.md` §5.1, secondary; the file itself first appears in the paper repo in `msr:00406cd`, 09-27 22:42). Senior co-author B imported that state as `msr:5e73a46` (09-26 19:37) and restructured it on 09-27/28. The appendices were dropped from the build on 10-01 (`msr:464168f`).

### 0.1 Whole-paper phase map

| Phase | Dates | Who drove it | Evidence |
|---|---|---|---|
| Census draft answers A's comments (term lock, why-before-how, counts to tables, finding-first results) | 09-22 → 09-27 | Student | `ol:5ecaf3f`, `ol:0b63ad2`, `ol:01fcd0f`, `ol:de73385`, `ol:b28f788`, `ol:6af100c`, `ol:1857886`, `ol:59236e2` |
| Import + restructure (SE framing, title, abstract, intro rewrite, appendix creation) | 09-26 → 09-28 | B | `msr:5e73a46`, `msr:f141169`, `msr:393f596`, `msr:bd086a7`, `msr:d0bc904` … |
| B's PDF annotations: tables → text, lowercase labels, cut low-interest tables | 09-28 (date-level) | B | `04-comms/past-chat-jimmy/raw/jimmy-main-pdf-comments/page_*.md`; executed in `msr:dfc2128`, `msr:7c705c9` |
| A's in-repo rewrite + `\hao{}`/`\todo{}` protocol | 09-29 11:35 | A | `msr:9809b8c`; "主要改了写作还有格式" (chat:group@2026-09-29T11:51) |
| Merge of A's version, label macros, new figures, borrowed analyses | 09-29 → 10-02 | Student (+B todo pass `msr:5262231`) | `msr:c93ef1f`, `msr:815305e`, `msr:9c69675`, `msr:9c4567c`, `msr:24d8c65` |
| Appendix removed; page budget fixed at exactly 18 | 10-01 → 10-02 | A + B decisions, Student executes | chat:group@2026-10-01T08:47–10:09, 2026-10-02T01:35, 01:51; `msr:464168f` |
| A's second comment pass; B aligns methods text ↔ figure | 10-02 | A, B | `msr:0f96193`, `msr:9ef4a07`, `msr:b5c0045` |
| Deadline day: page-filling expansion (implications, threats, details), abstract rounds | 10-03 | B (expansion), Student (abstract/RQ1) | chat:group@2026-10-02T22:30–22:44, 2026-10-03T09:25; `msr:d0d4c03`, `msr:86199d6`, `msr:1ec1a0f`, `msr:13179f3`, `msr:b7a448b` |
| Post-deadline-extension pass: title, abstract, scoping, numbers, implications | 10-04 | A | `ol:ba3f1ee` |

---

## 1. Title and abstract (`main.tex`)

### 1.1 Timeline (verified against patches)

Title:

| When | Commit | Role | Title |
|---|---|---|---|
| 08-14 13:29 | `ol:20a6d25` | Student | "Mining GitHub Issues in Interactive Theorem Prover Ecosystems" |
| 09-22 03:01 | `ol:af26086` | Student | census draft: "What Breaks in Interactive Theorem Provers, and What Maintainers Change" |
| 09-22 13:09 | `ol:04c5e27` | B (Overleaf) | proposes "What Slows Down Proof Development? An Empirical Study of Developer Challenges in Interactive Proof Assistants" (not kept) |
| 09-22 13:32 / 17:06 | `ol:30f5bf0`, `ol:efe7cb4` | Student | "Theorem Provers" → "Proof Assistants" (comments_hao.md:3), then drops "Interactive" |
| 09-28 14:36 | `msr:bd086a7` | B | adds `% NOTE: better and more interesting title needed here!` |
| 09-28 14:42 | `msr:d0bc904` | B | "Proof Engineering in the Wild: An Empirical Study of Issue Reports in Proof Assistants" |
| 10-03 17:57 | `msr:9355e35` | Student | "What Breaks in Proof Assistants, and How Maintainers Fix It: An Empirical Study of 23,671 Issue Reports" `[ID]` |
| 10-03 19:38 → 10-04 | `ol:a610d1d` (reverted by sync `ol:214cc0c`), re-applied in `ol:ba3f1ee` | A | "Maintaining Proof Assistants: An Empirical Study of Reported Bugs and Resolution Patterns" `[ID]`; keywords drop "closed coding" |

Abstract (substantive rounds only):

| When | Commit | Role | What changed |
|---|---|---|---|
| 09-26 | `msr:5e73a46` | Student text (imported by B) | 6 sentences; codebook labels in caps (`\textit{BUG}`…); "In this frozen snapshot"; exact medians (34.6 days) and 79.7% in prose |
| 09-27 23:15 | `msr:f141169` | B | rewritten as context → mixing problem → study → 2 findings → "only when" implication; labels replaced by plain words |
| 09-28 00:10 → 15:28 | `msr:393f596`, `bd086a7`, `d0bc904`, `1fd0584`, `3a4c1dc`, `0b8bd5a` | B | one-paragraph versions; "To fill this gap" appears in `3a4c1dc`; `0b8bd5a` makes strong claims ("The most severe bugs close fastest", "small edit", "bug severity is a poor guide to repair effort") |
| 09-29 00:54 | `msr:643836a` | Student | adds prior-work sentence; hedges strategy as "In the classifier's reading of tracker text"; medians with n in prose |
| 09-29 11:35 | `msr:9809b8c` | A | 7 cautious sentences: "Approximately 29% … receive non-bug labels", "assigned categories", "These observations show why studies … need to distinguish issue types and state their repository composition and closure criteria" |
| 09-30 02:32 | `msr:0952732` | B | "Yet no prior work…" + "First/Second/Third" findings + "These results caution against treating…" |
| 09-30 13:30 | `msr:5262231` | B | splits a semicolon sentence (team rule: no semicolons/dashes, B in 1:1 chat 2026-9-29 00:24, `CF-23@v2`) |
| 10-02 00:25 / 02:16 / 04:45 / 06:58 | `msr:3e7bab0`, `msr:9c69675`, `msr:9c4567c`, `msr:24d8c65` | Student | ecosystem effect "six times more" → "nine percent" → "about five percent" as import-time closures were excluded; new findings (label recall 16–68%, maintainers file project work, fix size); `24d8c65` adds the scope "pooled over ecosystems" |
| 10-03 17:57 → 19:38 | `msr:9355e35`, `ac172bd`, `4af1aff`, `10e2e5f`, `f1bc590`, `87bf139` | Student | failure-mode opening; "what users file / how long / how resolved" triad; macros removed then `\textsf`; repo count dropped; compressed to background → gap → "To fill this gap" → findings → recommendation; recommendation split by audience |
| 10-03 ~19:44–19:56 | Overleaf only (= snapshot `main.tex`) | Student | shorter sentences, 14 lines (~270 words), uploaded 19:56 |
| 10-04 | `ol:ba3f1ee` | A | new 5-sentence-paragraph abstract (~210 words), exact numbers (29.4%, 1.2%), final sentence "Hence, reliable mining … requires explicit issue classification, comparisons that account for ecosystem and filing period, and direct measurement of recorded fixes." |

### 1.2 Instructive rewrites

**(a) Overclaim → hedge → measured claim ("small edit").** `[ID: none]`

Before, `msr:0b8bd5a` (B, 09-28):
> The most severe bugs close fastest: soundness bugs close in a median of four days, whereas performance bugs, which only slow down proof checking, take about a month, and the kind of bug explains only about 1\% of the variation in time-to-close. Even soundness bugs are usually fixed by a small edit at the failing site, and fixes that break downstream code are rare. These findings […] show that bug severity is a poor guide to repair effort

Middle, `msr:643836a` (Student, 09-29): "In the classifier's reading of tracker text, four out of five bugs with a confirmed strategy, soundness bugs among them, are described as a local patch at the failing site".

After, `msr:9c69675` (Student, 10-02) → `msr:87bf139`:
> Soundness bugs close among the fastest and are fixed mainly by a local patch at the defect site, whereas performance bugs stay open longest and are fixed mainly by optimization, and a local patch does not imply a small recorded change.

Reason: checklist items `CF-12@v2` (category, not "severity"), `CF-13@v2` (no "how much code changes" without diff evidence), `CF-29@v2` (time-to-close ≠ effort); A asked for borrowed analysis methods from the closest papers (chat:group@2026-09-29T12:30), and the fix-size measurement following Lou et al. arrived in `msr:9c69675`. The provenance lines of those CF items are machine-generated; the chat message is the verified anchor.

**(b) Template imposed in chat, executed within minutes.**

Senior co-author B, chat:group@2026-10-03T19:18: "应该先交代一句背景，然后说明research gap，然后说to fill this gap, 我们做了一个关于的study，其中通过什么方法去做了什么，1-2条最重要的findings，我们最后推荐什么，每一个1句话上下" (background → gap → "to fill this gap" study + method → 1–2 key findings → recommendation, about one sentence each). Then 19:40: "你这个abstract每个句子太长了".

Before, `msr:ac172bd` (18:37, 12 sentences, one per finding, plus "Nor does the repository bug label recover those bugs…"). After, `msr:f1bc590` (19:24):
> Users bring these failures to maintainers through issue reports, yet what users file, how long bugs stay open, and how maintainers resolve them have not been fully examined for proof assistants.
> To fill this gap, we study $23{,}671$ GitHub issues from five ecosystems (\textsf{Lean}, …) with a proof-assistant-specific codebook and an LLM classifier validated against a held-out, adjudicated gold sample. `[ID]`
> […]
> We recommend labeling issue type before constructing a bug dataset, evaluating closure time within each ecosystem, and measuring repair size from the recorded change rather than from the reported strategy.

Related chat decisions on the same evening: name the five ecosystems, not the repositories (A, 18:27); no codebook labels or macros in the abstract (B 18:36 "abstract里不应该出现label的", A 18:37 "文本叙述吧，安全一些", B 18:43 "latex文本【无宏】"). Side effect: `msr:4af1aff` stripped the macros and turned F* into "F" by accident; `msr:10e2e5f` restored it as `\textsf{F*}` 9 minutes later.

**(c) Senior co-author A's last pass: vague quantifiers → exact numbers, explicit scope.**

Before (snapshot / Student, 10-03):
> We find that nearly one in three issues is not a bug, and that the bug share differs sharply between ecosystems.
> […] This order does not hold in every ecosystem, and ecosystem explains more of the variation in time-to-close than bug category does.

After (`ol:ba3f1ee`, A, 10-04):
> We find that 29.4\% of issue reports are not bugs, and that reported bugs concentrate in elaboration and tactics rather than in the kernel. Among closed bugs, category explains only 1.2\% of the rank variation in time to close, despite large differences between the pooled medians for performance and soundness bugs. […] Hence, reliable mining of proof-assistant maintenance requires explicit issue classification, comparisons that account for ecosystem and filing period, and direct measurement of recorded fixes.

Reason: no message states it. Note the tension with A's own rule "prose should highlight patterns, tables/figures should carry exact counts" (comments_hao.md:79–100): in the abstract and RQ headlines the final pass prefers one exact number per claim over verbal quantifiers. The "filing period" qualifier comes from a robustness result that sat in threats (see §8 and the RQ2 section). Reason for the period emphasis: no evidence beyond the edit itself.

### 1.3 Final structure (snapshot abstract, 14 sentences, ~270 words)

S1–S2 what a proof assistant guarantees and the two failure modes; S3 issue reports as the channel; S4 gap (three-part question); S5 "To fill this gap" + dataset scope; S6 method in one sentence (codebook + validated LLM classifier); S7–S12 findings, RQ order, one or two per sentence, pooled claim followed by its exception; S13–S14 recommendations split by audience (researchers, tool builders).

Post-snapshot delta (`ol:ba3f1ee`): 5 sentences + one 4-sentence findings block; method sentence keeps "(validated against human annotations)"; findings use exact percentages; recommendations collapse into one "Hence, reliable mining … requires …" sentence; keyword "closed coding" removed.

<!-- SECTIONS 2-12 BELOW -->
