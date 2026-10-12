# Study design / methodology section evolution (subagent report, saved on pause)

Status: produced by a helper agent of the stopped Phase 2 "section evolution" run. Not yet reviewed by the main session; re-verify before use. Contains identifying details (dataset size, repo and issue numbers, anonymous URL); private notes only.

## Key findings
- Figure-mirroring methodology. Senior co-author A `\todo` in `msr:9809b8c`: "the overview figure and the content in methodology is not synced, check previous papers from SAIL ... update the whole section and overview figure". A in chat 09-29 11:42: "图上这些在methodology的文字都能找到对应"; 10-02 22:26 lists unmatched boxes/steps. Resolved by Senior co-author B: figure redrawn 12 → 10 steps (`msr:9ef4a07`), then Phase 1/2/3 subsections with bold "Step 1..10" run-ins mirroring the figure (`msr:b5c0045`), phase-mapping sentences deleted (`4c70db0`) and a 3-sentence overview re-added (`86199d6`, page gap).
- A's `\hao{}` in `msr:0f96193` ("figure and text are not synced ... redraw the figure from scratch") and `\todo`s ("do not call it snapshot, call it dataset"; "fix AI smells, e.g., `Corpus'") resolved by B in `9ef4a07`, marked Done by Student in `405bba7`, deleted by B in `b5c0045`.
- κ reporting rule. Student `643836a` printed all per-dimension κ incl. below-bar; A `9809b8c` cut to "κ from 0.71 to 0.83"; final rule in `msr:9c69675` header comment: print κ only when ≥ 0.65 (paper-repo `checklist.md` C3, "Rule (author, 2026-10-02)"). Below-bar dimensions described as "the classifier's reading of the tracker text (values in the replication package)".
- Human κ = 0.74 first appears in B's `msr:393f596` (09-28). Pre-import `ol:1bda8f0` (Student, 09-26) deleted the sentence "The artifact has no two-rater human table, so this paper reports no human--human agreement." Source of 0.74 not visible in any patch. Consistent with notes/04 and notes/08 (FINAL-CHECKLIST B1).
- **REVISION-SUMMARY.md describes an agent revision that never landed.** Its "after" strings (e.g. "Issue trackers conflate multiple maintenance activities", the SE-context opening citing Harrison 2014) appear in no `03-design.tex` diff in either repo; the tex committed in `msr:815305e` is the summary's "Before" text. Its "Hao's Comments Addressed ✅" claims are unsupported. Lesson: verify agent change reports against the diff.
- Why-before-how sentence in `ol:5ecaf3f` is near-verbatim from A's model sentence (`02-comments-hao/comments_hao.md:43`); same commit deletes defensive phrases listed at `comments_hao.md:170-171`.
- Many commit subjects misdescribe their patches (`ol:5ecaf3f` "Lock a term table", `msr:5262231` "add todo", `msr:3e7bab0` "Baseline: snapshot...", `msr:815305e` "cursor-safety: checkpoint...", `msr:d0d4c03`).
- "Snapshot" vs "dataset" flip-flopped across A, Student, B (`9809b8c`, `815305e`, `59f15be`, `0f96193`, `9ef4a07`).
- Codebook table `tab:codebook-labels` added in `464168f` after A chat 10-01 10:09 ("把表格浓缩成只有D1-D7+label…指向replication package").
- Page-budget expansion: chat 10-02 22:36 B "还差一页多才能18页满"; A 22:44 "methodology 可以写详细来".
- `%% PARKED (author 2026-10-02, discuss first)` block from `9c69675` still in final text; no evidence of discussion.
- Checklist errors: CF-14@v2 provenance "Who: Hao (乐绎华)" misattributed (乐绎华 is the Student); RS-17/RS-19 cite κ 0.76 that never appears in 03-design.
