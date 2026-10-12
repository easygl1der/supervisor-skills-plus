# RQ2 / RQ3 section evolution (subagent report, saved on pause)

Status: produced by a helper agent of the stopped Phase 2 "section evolution" run. Not yet reviewed by the main session; re-verify before use. Contains identifying details (issue/PR numbers, URL); private notes only.

## Key findings
- Why-before-how on the denominator (`ol:01fcd0f`, Student) near-verbatim from `02-comments-hao/comments_hao.md:38-43`; later shrank (`msr:9c4567c`), marked `\todo{space filling, remove this:}` by Senior co-author A (`msr:0f96193`), deleted by Senior co-author B (`msr:b7a448b`). Final "why" survives only in design (`03-design.tex:147`), threats (`08-threats.tex:15`) and one RQ2 clause.
- "Local patch" claim softened: "Four out of five fixed bugs are resolved by a local patch ... a small edit" (`msr:f141169`/`9809b8c`) → codebook definition "fix at the defect site with no structural change" + "Recorded diffstats do not show local patches to be small" (`msr:9c69675`). The Student's own diffstat analysis (`464168f`) contradicted the "small edit" definition. No direct evidence of who asked.
- Figure → table: A's todo in `msr:0f96193` ("Wait, It is a table! why label it as a figure?! Please format it as a normal table") → Student split it in `msr:405bba7` (chat 10-02 21:38 "我把表和图拆开了").
- A's `msr:9809b8c` silently reverted the Student's `643836a` hedges and lowercase terms (stale base); two sync commits from B's account then toggled the text back and forth (`bfaf29c`, `578d640`).
- B's "add todo" commit `msr:5262231` deleted the RQ3 κ caveat; Student restored it in `3e7bab0`. Commit subjects misdescribe patches (`5262231`, `c544e4a`, `13179f3`).
- Parked analyses (`%% PARKED (author 2026-10-02, discuss first)`: Kaplan-Meier, creation-year ladder, last-comment endpoint, closure-record check) added in `msr:9c69675`, still in HEAD; some reappear in threats. No chat about "discuss first".
- Page-budget moves on 10-03: extra `\midrule`s (`13179f3`, B, chat 09:25 "页数还是差一页"), worked example with real issue/PR URL (`b7a448b`, after A chat 10-02 22:44 "加解释和例子"), which identifies the repository.
- Checklist: RS-08 ticked but describes a layout later dismantled; RS-07 contradicted by final caption; CF-13/CF-14 "Hao (乐绎华)" provenance internally contradictory; CF-29/CF-30 "Hao C2/C3" not verifiable in `comments_hao.md`.
- Appendix vetoed by A in chat (10-01 08:47; 10-02 01:51), after tables had been pushed to appendix pre-import and pulled back by B.

## Rewrite types (with commits)
Why-before-how: `ol:01fcd0f`, `ol:de73385`, `msr:f141169`. Numbers to tables/appendix: `ol:0842e26`, `6af100c`, `f54f954`, `de0ed88`, `msr:9c4567c`; reversed by `ol:1bda8f0`, `msr:9c69675`, `59f15be`, `ac172bd`. Finding-first: `ol:01fcd0f`, `msr:f141169`, `9809b8c`, `ac172bd`. Hedging: `643836a`, `7c705c9`, `3e7bab0`, `24d8c65`, `9c69675`. Speculation removed: urgency explanation dropped in `9c69675`. Floats parked: `7c705c9`, `c544e4a`, `464168f`. Terminology: `ol:1bda8f0`, `dfc2128`, `cfabd75`, `9ef4a07`, `10e2e5f`.
