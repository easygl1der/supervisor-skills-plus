# RQ1 section evolution (subagent report, saved verbatim-in-substance on pause)

Status: produced by a helper agent of the stopped Phase 2 "section evolution" run. Not yet reviewed by the main session. Claims cite commits; re-verify before use. Contains paper-identifying details (dataset size, a concrete issue URL); private notes only.

## Key findings
- Findings format: Senior co-author A introduced "Table/Figure X shows that..." as sentence 2 in `msr:9809b8c` (09-29); then posted the slide rule as `\todo`s in `msr:0f96193` (10-02 07:45): bold finding first, sentence 2 cites a figure/table, rest digs deeper. A's other todo in the same commit ("show it in the first sentence") conflicts with it. Student complied in stages (`405bba7`, `ee351a3`, `ac172bd`), appended "[Partly addressed ...]" and finally commented the todos out in `ac172bd` (10-03 18:37), never resolved. At HEAD the maintainers and D3 findings still cite no figure/table.
- Parking with `\iffalse`: `tab:rq1-types`, `tab:rq1-cats` in `msr:7c705c9` (Student, 09-29 16:14; commit message hides that the whole D1 result was removed); `fig:rq1-overview` in `msr:47221f7` (09-30 20:15); `fig:rq1-d3-trigger` in `464168f`, deleted in `3e7bab0`.
- D1 result missing for about a day: removed in `msr:7c705c9`, restored by Senior co-author B in `msr:5262231` (commit subject "add todo" understates it).
- Heatmap: A's todo "if not, remove the figure" (`9809b8c`) → removed (`7c705c9`) → re-added 5 h later (`b3dafcd`) → replaced the primary composite (`47221f7`). B requested heatmap in `04-comms/past-chat-jimmy/SUMMARY.md:17,30`.
- Body tables oscillated 0 → 1 (`ol:de73385`) → 0 (`ol:de0ed88`) → 3 (`msr:393f596`) → 0 (`msr:7c705c9`).
- Why-first opening adopted from A's suggested text (`02-comments-hao/comments_hao.md:147-162`) in `ol:01fcd0f`, later deleted by A in `msr:9809b8c` (rationale folded into the first finding).
- Number trimming (`ol:01fcd0f`, `6af100c`, `de0ed88`, `msr:9809b8c`, `9c4567c`, `59f15be`) alternated with numbers restored (`ol:1bda8f0`, `msr:5262231`, `3e7bab0`), while robustness checks grew (`msr:9c69675`: balanced share, Rogan-Gladen correction, stricter rule).
- Literature-first → results-first after A's todo "readers are here to read our results, talk our results first" (`msr:0f96193` → `405bba7`).
- A in chat 10-02 01:51: "不要appendix，软工的人不喜欢".
- A in chat 09-29 12:26: "标签这种最好让agent用宏" → label macros in `msr:c93ef1f`.
- Defect at HEAD: duplicated kernel/soundness share sentence (introduced by `ac172bd`), final lines ~161 and ~164 of `04-rq1.tex`.
- Shared checklist F3 stale relative to `47221f7`.

## Rewrite-type tags (with commits)
Procedural opening → why-first: `ol:01fcd0f`, `ol:1bda8f0`, `msr:f141169`, `msr:393f596`. Finding-first: `msr:9809b8c`. Study-plan language removal: `ol:01fcd0f`, `ol:6247934`. Claim softening: `msr:24d8c65`, `msr:2e7702a`. Placeholder → concrete example: `msr:f141169` → `msr:b7a448b` (page gap, B chat 10-03 09:25). Annotation protocol: A's todos `9809b8c`, `0f96193`; "(Done)" replies `405bba7`; deletion by B `4f8b488`, `1f68c99`.
