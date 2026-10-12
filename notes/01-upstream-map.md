# 01 Upstream map: HKUSTDial/Supervisor-Skills

Read-only survey of the upstream skill library, written for the merge-design phase.
Repo root: `/Users/wriseai/Projects/supervisor-skills-plus` (branch `design`, whose only
commit beyond upstream `main` is `bfbfea1`, adding `PROGRESS.md`). All paths below are
relative to that root. Upstream `main` HEAD = `5f9432d` (2026-10-12).

Everything here was read in full except binaries (PNG/JPG/WebP/PDF) and the three
`.drawio` example XML files (see section 3.3). Where something is absent it is stated.

---

## 1. Repo overview

### 1.1 Purpose

- Distils a PhD advisor's (Yuyu Luo, HKUST-GZ) research and reviewing experience at
  SIGMOD/VLDB/ICML/NeurIPS into LLM-executable "AI Skills" plus a human curriculum
  ("Guide + Skills dual track"). `README.md:28-41`, `README.en.md:30-45`.
- Target audience stated as researchers writing for "NeurIPS, ICML, ICLR, VLDB, SIGMOD,
  KDD, ACL, EMNLP, CVPR, and similar top venues". `llms.txt:5`.
- News: v2.1 (2026-07-10) added `paper-writer`, `paper-polish`, `deep-research`;
  deployed in Doubao Office Mode (2026-07-15). `README.md:17-24`.

### 1.2 License (exact)

- `LICENSE`: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
  (CC BY-NC-SA 4.0)", "Copyright (c) 2026 Yuyu Luo (methodology) and contributors."
  Summarises Share/Adapt + Attribution/NonCommercial/ShareAlike; links legalcode.
- CHANGELOG: license changed CC BY 4.0 -> CC BY-NC-SA 4.0 in v2.0.0. `CHANGELOG.md:136-137`.
- CONTRIBUTING: all contributions licensed CC BY-NC-SA 4.0. `CONTRIBUTING.md:48-50`.
- Per-skill frontmatter `license:` is inconsistent with the repo license:
  `CC-BY-4.0` in benchmark-paper-template, figure-designer, idea-evaluator,
  pre-submission-reviewer, tech-paper-template, vibe-research-workflow;
  `CC-BY-NC-SA-4.0` in deep-research, intro-drafter, paper-polish, paper-writer;
  no `license:` field in drawio-reconstruction and rebuttal-guidance (frontmatter of each
  `skills/*/SKILL.md`).
- `skills/drawio-reconstruction/LICENSE` is MIT ("Copyright (c) 2026 VCG-Bench Authors");
  adapted from `sxy1499894281/drawio-reconstruction-skill`. `CHANGELOG.md:11-14`,
  `skills/drawio-reconstruction/README.md` "License".

### 1.3 Layout

```
README.md            zh root README (canonical), 225 lines
README.en.md         en root README, 214 lines
CONTRIBUTING.md      63 lines
CHANGELOG.md         185 lines (Keep a Changelog)
llms.txt             54 lines
LICENSE              CC BY-NC-SA 4.0
PROGRESS.md          (design branch only; Phase 0 log)
requirements-lint.txt  PyYAML>=6.0
.github/workflows/lint.yml   runs lint_skills.py + check_shared_sync.py on push to main and PRs
scripts/lint_skills.py       233 lines
scripts/check_shared_sync.py 87 lines
assets/              top-level images used by handbook + README (PNG/WebP/JPG)
handbook/            zh curriculum, 6 chapters (+ 17 MB companion PDF in 01_Preliminary)
handbook-en/         en mirror, same chapter/file structure (no PDF, no images except flowchart)
skills/<name>/       12 skill dirs (+ skills/README.md, skills/README.en.md, skills/.gitkeep)
```

`skills/README*.md` are not inside a skill dir, so the linter ignores them
(`scripts/lint_skills.py:213` iterates only directories).

### 1.4 Install documentation

- Root READMEs Quick Start: paste `Help me install Supervisor-Skills from
  https://github.com/HKUSTDial/Supervisor-Skills with Skills.` into Claude Code / Cursor /
  Codex. `README.md:178-184`, `README.en.md:185-191`.
- `llms.txt:7-21`: longer prompt, "Treat each directory containing SKILL.md as a separate
  skill; do not install the repository root as one skill. If you are Codex, use
  $skill-installer"; single-skill install for drawio-reconstruction via
  `$skill-installer .../tree/main/skills/drawio-reconstruction`.
- `skills/README.en.md` "How to actually use these skills": installed (natural-language
  triggers listed per skill) or uninstalled (paste SKILL.md as system prompt, or use as a
  static checklist).
- drawio-reconstruction has its own Codex install section (symlink into
  `~/.agents/skills`), Python 3.10+, Pillow, Draw.io Desktop CLI, `DRAWIO_PATH`.
  `skills/drawio-reconstruction/README.md` "Installation As A Codex Skill", "Requirements".
- No plugin manifest exists (`.claude-plugin/` was removed when the layout was flattened;
  "no plugin manifest ever existed" for the nested path). `CHANGELOG.md:43-46`.

### 1.5 Documentation drift (count of skills)

- 12 skill dirs exist. `rebuttal-guidance` was added 2026-09-05 by a different author
  ("Mu Xing", commits `dd39456`, `198c46c` "Add files via upload") and is listed only in
  the zh root README skill table (`README.md:176`) and zh tree (`README.md:138`).
- Still saying "eleven"/11 and omitting rebuttal-guidance: `CONTRIBUTING.md:7`,
  `llms.txt:3,25`, `skills/README.md`, `skills/README.en.md` (title, cards, trigger list,
  cross-ref table), `README.en.md` tree and table, `CHANGELOG.md` (no entry for it).
- Root README "TODO" still lists "How to write a strong rebuttal" as a missing guide.
  `README.md:218-221`, `README.en.md:207-210`.

### 1.6 Handbook organisation

zh is canonical ("preserved verbatim from the methodology author"); en is "a faithful
English mirror"; PRs must keep both trees symmetric. `CONTRIBUTING.md:44`. Re-sync from
upstream `HKUSTDial/PhD.Skills` permits only the image-path rewrite to `../../assets/`.
`CONTRIBUTING.md:46`.

| # | zh file (`handbook/`) | en file (`handbook-en/`) | lines zh/en | One-line content |
|---|---|---|---|---|
| 1.1 | `01_Preliminary/1.1_如何评价一篇论文的质量.md` | `01_Preliminary/1.1_how-to-evaluate-paper-quality.md` | 27/27 | Reviewer view: Novel Problem / Novel Method / Nice Story / Nice Presentation; 4 dislikes (old problems, reused DB methods, worse presentation, weak baselines) |
| PDF | `01_Preliminary/博士生科研入门辅导.pdf` | (none) | 17 MB | Companion slides |
| 2.1 | `02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md` | `.../2.1_idea-lifecycle-and-capability-matching.md` | 30/30 | Idea lifecycle (LLM-agent apps 3-6 months); 6-row idea-type x lifecycle x student-profile table; <5 h/day warning |
| 2.2 | `.../2.2_想Idea的思路_更高更快更强.md` | `.../2.2_higher-faster-stronger.md` | 67/67 | 5 dimensions Higher/Faster/Stronger/Cheaper/Broader with entry strategies; all examples Text-to-SQL / LLM agents / DB |
| 2.3 | `.../2.3_进阶_如何做颠覆式创新.md` | `.../2.3_disruptive-innovation.md` | 41/41 | First principles, elephant in the room, technology cycle, Hamming's list |
| 3.1 | `03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md` | `.../3.1_the-essentials-of-a-research-paper.md` | 61/61 | Background/Why/Problem, What (challenges, core idea), How, So What (main results, ablation, case study); running-example principles; "draw main figures before text" |
| 3.2 | `.../3.2_Introduction写作的思考模型.md` | `.../3.2_introduction-writing-flowchart.md` | 37/37 | 6-part Intro organisation + flowchart image `intro_flowchart_board.png`; links to 6.1-6.3 and 3.3/3.4 |
| 3.3 | `.../3.3_技术类Full_Paper思考模板.md` | `.../3.3_technical-paper-template.md` | 114/52 | Technique vs New Problem/Setting; fill-in thinking table (zh uses an HTML 3-col table, en a 2-col markdown table; same content) |
| 3.4 | `.../3.4_Benchmark与Evaluation类论文思考模板.md` | `.../3.4_benchmark-paper-template.md` | 290/253 | Benchmark vs technique; five core elements; benchmark Intro flowchart; Section 2-7 plan; instantiation table; 4-part checklist; StatQA / nvBench 2.0 / VisJudge-Bench. H1 lacks the "3.4" number in both languages |
| 3.5 | `.../3.5_写作细节与Checklist.md` | `.../3.5_writing-details-and-checklist.md` | 627/446 | DB-centric writing checklist: topic > novelty > results; LaTeX macros/layout; grammar; "LLM writing issues" (em-dash ban, quote punctuation, banned vocabulary); per-section verb tables; Abstract 5-sentence and Intro 6-paragraph tables; Problem Formulation; Framework; Experiments; Related Work; Conclusion; good/bad paper traits; revision LaTeX template. zh adds 3 images |
| 4.1 | `04_Scientific_Plotting/4.1_Motivated_Example_Figure.md` | `.../4.1_motivated-example-figure.md` | 62/56 | 5 "ironclad" plotting rules; Fig.1 paradigms (running example + failure, existing vs ours, performance teaser) |
| 4.2 | `.../4.2_Solution_Overview_Figure.md` | `.../4.2_solution-overview-figure.md` | 49/45 | Pipeline / system architecture / multi-level (offline-online) overview figures |
| 4.3 | `.../4.3_Experimental_Results_Figure.md` | `.../4.3_experimental-results-figure.md` | 56/52 | Chart-type table; self-contained captions; dual encoding; highlight Ours; honest Y axis; small canvas; `plot_utils.py` |
| 4.4 | `.../4.4_绘图Checklist与工具速查表.md` | `.../4.4_plotting-checklist-and-tools.md` | 29/29 | 10-item figure checklist; tool table |
| 5.1 | `05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md` | `.../5.1_vibe-research-and-vibe-coding.md` | 510/295 | Boyan Li talk: 6-item code of conduct; Vibe Coding mindset + 6 techniques; Vibe Figure 3 steps; Vibe Writing rules. zh additionally contains "Figure Prompt 与生成结果" with two full image-generation prompts and images (zh lines 299-495), absent in en |
| 5.2 | `.../5.2_李伯岩实战经验分享与会议纪要.md` | `.../5.2_liboyan-practical-notes.md` | 156/156 | AI-generated meeting minutes of the same talk, Q&A, timestamp table |
| 6.1 | `06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md` | `.../6.1_icml2025-alpha-sql-analysis.md` | 83/67 | Technique paper Intro analysis |
| 6.2 | `.../6.2_ICLR_2025_AFlow写作剖析.md` | `.../6.2_iclr2025-aflow-analysis.md` | 84/68 | Technique paper (automated agentic workflow) |
| 6.3 | `.../6.3_VLDB_2026_LEAD写作剖析.md` | `.../6.3_vldb2026-lead-analysis.md` | 81/71 | New Problem/Setting paper (LLM instruction-tuning data selection) |

Structural asymmetry: the en mirror drops all images except the Intro flowchart (grep of
`![` in both trees), drops the "关键插图" sections of 6.1-6.3, and drops the 5.1 prompt
showcase. The handbook is not linted; it contains em-dashes in both languages
(e.g. 12 in `handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md`, and in
every case-study H1).

### 1.7 Case studies 6.1-6.3: exact style (template for a future 6.4)

File naming: zh `6.N_<VENUE>_<YEAR>_<PaperName>写作剖析.md`; en
`6.N_<venue><year>-<paper-slug>-analysis.md` (lower-case, hyphenated).

Section order (zh, every file; en identical except where noted):

1. H1 `# 6.N <VENUE YEAR> — <Paper> 写作思路剖析` / en `# 6.N <VENUE YEAR> — <Paper> Writing Analysis`.
2. Blockquote metadata, 3 lines: `**论文**` full title, `**会议**` venue, `**原文链接**` URL
   (OpenReview / proceedings / arXiv PDF). en: Paper / Venue / Paper link.
3. `---`, then H2 "论文 Introduction 写作的思考模型（Introduction 是整个论文的精简版）" with
   the same boilerplate paragraph verbatim in all three files (copied from 3.3).
4. `---`, H2 "Introduction 写作/构思的 Flowchart": 6.1 embeds
   `../../assets/intro_flowchart_alpha_sql.png` (with an HTML comment); all give a
   one-line blockquote chain "研究背景 → 研究前沿（现有方法）→ Limitations（不超过 3 点）→
   Key Idea / Our Goal → Challenges（不超过 3 点）→ 方法总览 → 贡献点" (6.3 writes
   "Our Goal / Key Idea", matching its type).
5. `---`, H2 "基于 Flowchart，对原文 Introduction 的写法进行剖析":
   - H3 "快速定位：这篇论文是什么类型？" listing the Technique bullet pair
     (主轴 Key Idea / Goal 一句话) and, in 6.1 and 6.3, the New Problem/Setting pair, then a
     one-sentence classification (6.3 adds a `> **批注**` blockquote).
   - `---`, H3 "基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段", a
     "请下载原文，对照着看。原文链接：..." blockquote, then one 2-column table
     `逻辑阶段 | 原文内容与写作思路剖析` with rows: 研究背景 (section row + question row),
     研究问题分析与属性解读, Limitation 1, Limitation 2, Limitation 3, 论文的 Novelty 和创新思路讨论,
     [Our Goal row in 6.3], Key Idea, Challenges, 方法总览, 贡献点. Cells quote the paper's
     English Introduction verbatim (long passages, bolding key transition phrases such as
     "Based on this idea", "First", "Second") followed by `**写作思路**：` commentary in
     Chinese. Missing stages are explained, not skipped (e.g. "Limitation 3: 这篇论文没有讨论
     第三类局限。因为...", "Challenges: NA ... 投稿 AI 会议的论文经常采用这种写法").
6. `---`, H2 "关键插图" (zh only): H3 per figure "Figure N：<name>", one sentence on what
   the figure does for the Intro, image from `../../assets/` (`performance_teaser_example.png`,
   `alpha_sql_solution_overview.png`, `aflow_existing_vs_ours.png`, `aflow_solution_overview.png`,
   `lead_solution_overview.png`).
7. `---`, H2 "评论区批注（写作思路详细解读）" (6.2 and 6.3 only): 2-col table
   `段落位置 | 批注内容`, 3-4 short rows.
8. `---`, H2 "其他资源": paper link; "建议配合 3.2 ... 和 3.3 ... 一起阅读" (6.3 links only 3.2
   and adds a comparison bullet pointing at 6.1).

Length and tone: 81-84 lines zh, 67-71 lines en; one big table carries the content;
conversational advisor voice in first person ("我转成 Table"), informal phrasing
("LLMs 很牛", "ok，那我们能不能..."), commentary focuses on rhetorical moves (A-type vs
B-type method framing, root-cause vs surface fix, killing two birds with one stone).
6.3 openly notes gaps in its source ("Word 原稿中...为截图，无法还原"). Coverage is
Introduction-only in all three; none analyse later sections. All three are ML/DB-for-LLM
papers from the author's lab.

What each covers: 6.1 Alpha-SQL (zero-shot Text-to-SQL via MCTS; A/B method-family
framing; no Challenges paragraph; contributions merged into method paragraph);
6.2 AFlow (automating agentic workflows; two limitations; challenges = search space
expressiveness + efficiency; formal 3-item contributions); 6.3 LEAD (new setting:
iterative data selection without full-dataset inference; research-question framing
"Can we retain ... while eliminating ...?"; 5 contributions incl. theory).

Touchpoints if a 6.4 is added (all currently enumerate 6.1-6.3): `README.md:122-125,157`,
`README.en.md:127-130,163`, `llms.txt:48`, `handbook/03_Paper_Writing/3.2*.md` and
`3.3*.md` reference lists (and en mirrors), plus image assets under `assets/`.
`CONTRIBUTING.md:44` requires the zh/en pair.

---

## 2. Conventions

### 2.1 SKILL.md frontmatter and naming

Observed fields: `name`, `description`, optional `license` (see 1.2). Descriptions are
either plain scalars, quoted strings (drawio), or folded `>-` blocks (most).

Enforced by `scripts/lint_skills.py` (rules listed in its docstring, lines 4-12):

| Rule | Implementation | Notes |
|---|---|---|
| Frontmatter present and valid YAML mapping | `parse_frontmatter` lines 45-66: file must start with `---\n`, closer `\n---\n`, `yaml.safe_load`, keys strings | PyYAML required (`requirements-lint.txt`) |
| `name` present, string, regex `[a-z0-9][a-z0-9\-]{0,62}[a-z0-9]` (kebab, 2-64 chars) | lines 173-185 | must equal directory name |
| `description` present, string, 40-80 words | `check_description` lines 69-82 | words counted after stripping `>-`/`>` and newlines |
| Third person | regex `\b(I|my|we|our|us)\b`, case-insensitive | also catches words like "US"; applies to description only |
| Contains "Use when" or "use when" | substring test | |
| Body (after frontmatter) <= 500 lines | `check_body` line 88 | frontmatter not counted |
| No em-dash U+2014 in body | line 90 | frontmatter not scanned for em-dash |
| No CJK (U+3400-4DBF, 4E00-9FFF, kana, Hangul) in body | lines 34, 94 | only SKILL.md body; references may contain CJK (they do) |
| No banned attribution strings in body | `BANNED_ATTRIB` lines 37-42: "Co-Authored-By: Claude", "Generated with [Claude Code]", "🤖 Generated with", "Anthropic SDK" | |
| Pointers resolve | `check_pointers` 106-117: only `See: references/X.md` and markdown links `[..](references/X.md)` or `(./references/...)` | bare mentions like "references/x.md" or backticked paths are NOT checked (deep-research uses bare mentions throughout) |
| Reference files (`references/**/*.md`, recursive): no em-dash, no banned attribution | `check_reference_file` 120-151 | |
| No nested refs | a `See: references/...` string inside a reference file is an error | markdown links between reference files are not detected |
| ToC for reference files > 100 lines | first 20 lines must contain "table of contents", "## contents", or "toc" (case-insensitive substring) | "toc" substring is weak (would match e.g. "protocol") |
| Exit code | 0 clean, 1 on any violation | |

Not checked by the linter: scripts/, assets/, README files inside skills, `license` field,
orphan reference files, commit messages, handbook. Current state: `lint: 12 skill(s)
clean` (run 2026-10-12 with `~/.venvs/ssp-lint`, also logged in `PROGRESS.md`).

Measured description word counts (linter's method): benchmark 65, deep-research 67,
drawio 72, figure-designer 74, idea-evaluator 76, intro-drafter 67, paper-polish 67,
paper-writer 71, pre-submission-reviewer 66, rebuttal-guidance 61, tech-paper-template 67,
vibe 73. Max SKILL.md body: drawio 347 lines.

### 2.2 references/ usage patterns

- Progressive disclosure: SKILL.md gives procedure; depth lives in `references/*.md`
  loaded on demand ("See: references/X.md"). `CONTRIBUTING.md:13-19`.
- Every reference >100 lines starts with "## Table of contents" (or "## Contents").
- Integrity-gate pattern (six older skills): bullets tagged `[inspection]`,
  `[attestation]`, `[user-attest]`, `[user-verify]`; v2.1 rule: "Run the gate silently ...
  a failure surfaces as a concrete finding". `CHANGELOG.md:63-64`;
  e.g. `skills/idea-evaluator/SKILL.md` "Integrity gate".
- Orphan reference files (present but never linked from their SKILL.md):
  `idea-evaluator/references/paradigm-{elephant,examples,first-principles,hamming,technology-cycle}.md`
  and `worked-examples.md`; `intro-drafter/references/worked-examples.md`;
  `tech-paper-template/references/worked-examples.md`; in paper-writer the three shared
  copies (`academic-phrasebank.md`, `ai-tone-guardrails.md`, `section-conventions.md`)
  are not linked from `paper-writer/SKILL.md` (verification-checklist mentions "the
  AI-tone guardrails list" without a path).

### 2.3 Shared-reference sync (`scripts/check_shared_sync.py`)

- Rationale: "every skill directory must stay self-contained (a user may copy a single
  skill folder), shared files are duplicated per consuming skill: one copy is canonical,
  the others carry a header comment pointing at it." lines 4-12.
- Hard-coded map `SHARED` (canonical -> copies), lines 26-42:

| Canonical | Copy |
|---|---|
| `paper-polish/references/academic-phrasebank.md` | `paper-writer/references/academic-phrasebank.md` |
| `paper-polish/references/ai-tone-guardrails.md` | `paper-writer/references/ai-tone-guardrails.md` |
| `paper-polish/references/section-conventions.md` | `paper-writer/references/section-conventions.md` |
| `paper-writer/references/evidence-discipline.md` | `intro-drafter/references/evidence-discipline.md` |
| `paper-writer/references/prose-delivery.md` | `intro-drafter/references/prose-delivery.md` |

- Check: `strip_header` removes ONE leading HTML comment (`<!-- ... -->`) after
  `lstrip()`, then leading newlines; canonical body must equal copy body byte-for-byte.
  Errors: canonical missing, copy missing, out of sync. Exit 1 on any. lines 45-83.
- Header text convention: canonical `<!-- Canonical copy. If this file is duplicated into
  another skill, edit THIS copy (<skill>/references/) and re-sync;
  scripts/check_shared_sync.py enforces parity. -->`; copy `<!-- Copy. Canonical lives at
  <skill>/references/<file>; edit the canonical, then re-sync.
  scripts/check_shared_sync.py enforces parity. -->` (first lines of each file).
- "Sync" is manual: there is no sync/copy tool; you edit the canonical and copy the body.
  Adding a new shared file requires editing the `SHARED` dict. Current state:
  "shared-sync: 5 copy(ies) in sync".
- Shared content NOT under sync: intro-drafter tells the model the tone files "live with
  their canonical copies in `paper-polish`" and to consult them there
  (`skills/intro-drafter/SKILL.md` "Tone references"), i.e. a cross-skill dependency
  that breaks self-containment. Several near-duplicates are independent files:
  `intro-drafter/references/paper-types.md` vs `tech-paper-template/references/paper-types.md`;
  three `worked-examples.md` (idea-evaluator, intro-drafter, tech-paper-template) all
  derived from 6.1-6.3; `pre-submission-reviewer/references/section-guides.md` vs
  `paper-polish/references/section-conventions.md` vs `paper-writer/references/section-guidance.md`;
  banned-word lists in `pre-submission-reviewer/references/forbidden-patterns.md` vs
  `paper-polish/references/ai-tone-guardrails.md`; `deep-research/references/hedge-calibration.md`
  vs the verb ladder in `academic-phrasebank.md`.

### 2.4 CONTRIBUTING rules (`CONTRIBUTING.md`)

- New skill: issue first; must fill a real gap; attribute non-handbook content; follow
  conventions. lines 5-11.
- Skill layout: `SKILL.md` English, <500 lines, YAML with name+description;
  `references/*.md` (ToC if >100 lines); optional `scripts/*.py`, `assets/*`. lines 13-19.
- Hard rules (CI): list at lines 21-30, mirrors the linter plus shared-copy parity and
  "Commits must not contain 'Claude', 'Co-Authored-By: Claude', or Anthropic attribution."
  (repeated line 63). Note: no script checks commit messages; this conflicts with the
  session-level Claude co-author attribution, so the merge plan must decide.
- Bilingual: keep `handbook/` and `handbook-en/` symmetric. lines 42-46.
- Commits: Conventional Commits `feat(skill): <name>`, `feat(<area>)`, `fix(<area>)`,
  `docs(<area>)`, `build:`, `chore:`, `refactor(<area>)`. lines 52-61. (Recent upstream
  commits mostly follow this; the rebuttal-guidance commits do not.)

### 2.5 CHANGELOG format

Keep a Changelog 1.1.0 + SemVer (`CHANGELOG.md:3-5`); sections `## [x.y.z] - YYYY-MM-DD`
with `### Added / Changed / Fixed / Removed / Unchanged / Included`; wrapped prose
bullets naming paths. Versions: 1.0.0 (2026-04-19), 2.0.0 and 2.0.1 (2026-04-20),
2.1.0 (2026-07-10). No Unreleased section; nothing after 2.1.0.

---

## 3. Per-skill reference

Line counts are total file lines (`wc -l`). Field assumption key: "ML/DB" = examples,
defaults and checks assume AI/ML or data-systems papers.

### 3.1 benchmark-paper-template (SKILL.md 142 lines)

- Trigger: writing/structuring a benchmark or evaluation paper, checking whether a
  benchmark idea is substantive, drafting its Intro, planning construction or experiments.
- Inputs (prompt template): research area, benchmark name, gap, construction approach,
  evaluation framework, data scale, 1-3 findings.
- Procedure: five-pillar audit (Research Gap, Construction Pipeline, Evaluation
  Framework, Empirical Findings, optional Companion Method) -> six-part Intro chain
  (Background+Running Example, <=3 benchmark limitations, 2-3 RQs, Design
  Considerations, Proposal, Contributions) -> section sketch Sec.2-7 -> load checklist.
  Delivered as a copy-paste "Prompt template" (Role/Task/Input/Output Steps 1-4).
- Outputs: completeness table, Intro chain table, per-section sketch, Critical/Major
  issues.
- Checklists: `references/checklist.md` (113): Introduction (8 items: Fig.1 running
  example, <=3 gaps, Table 1 vs >=5 benchmarks, 2-3 RQs, design rationale, 2-4
  contributions mapped to RQs/sections, narrative flow, concrete numbers); Benchmark
  section (9: G1-G4 goals, scope in/out, pipeline Fig.2 with counts and gates, per-step
  I/O, QC with IAA, stats Table 2, distribution figures, examples, taxonomy coverage);
  Experiments (8: >=10 models open/closed/scales, overall table, RQ-organised
  fine-grained analysis, error taxonomy, human vs model, 2-4 cases, Finding X,
  research opportunities); Structure & completeness (15: logical thread, open source,
  hosting, license, limitations, ethics, datasheet, related-work table, appendix,
  reproducibility, mean+-std and significance, contamination, maintenance plan, page
  budget, verified references); venue-specific (NeurIPS E&D 2026 incl. Croissant,
  ICLR/ICML, ACL/EMNLP/NAACL); severity Critical/Major/Minor + READY/NOT READY verdict.
- References: `gap-analysis.md` (86: landscape table = Table 1, three gap patterns
  Dimension Blindness / Assumption Violation / Granularity Mismatch, 4-check gap
  validation, gap-statement template, RQ derivation); `benchmark-design.md` (180: G1-G4,
  scope, three taxonomy patterns, metric table, LLM-as-judge validation, companion method,
  contamination table, difficulty calibration "~0.1-9%" on hardest subset); 
  `construction-pipeline.md` (127: reverse synthesis / controlled injection / adaptive
  generation + expert annotation, 5-stage table with quality gates, 6 QC strategies incl.
  Cohen's/Fleiss' kappa, ICC, stats to report, Fig.2 guidelines); `experiments.md`
  (159: 10-15 models on 4 axes, protocol table, human baseline, baseline fairness,
  RQ analysis template, analysis-type priority table, overall table format, "Finding X"
  micro-structure, case-study types, companion-method experiments, research
  opportunities); `paper-structure.md` (209: Intro parts, Fig.1/Table 1 must-haves,
  section skeletons with page budgets, figure placement table, appendix A-F);
  `instantiation-template.md` (194: fill-in tables; its ToC lists 7 items but body has 12;
  contains CJK "预期洞察", "信达雅"); `orchestrator-notes.md` (96: "historical notes",
  stage-detection DOT graph routing to non-existent sub-skills `bench-gap-analysis`,
  `bench-design`, etc.).
- Scripts: none.
- Cross-links: tech-paper-template, intro-drafter; README says figure-designer and
  pre-submission-reviewer downstream (`skills/README.en.md` benchmark card).
- Field assumptions: strongly LLM-evaluation specific: baselines are LLM families and
  sizes (GPT-4o, Claude, LLaMA, 7B-100B+), prompting strategies (CoT, few-shot), companion
  methods (DPO, GRPO), contamination of training data, "Human vs LLM". Venues are
  ML D&B tracks. The gap/RQ/pipeline/QC/IAA parts generalise to empirical datasets.

### 3.2 deep-research (SKILL.md 209 lines)

- Trigger: literature review, field survey, landscape mapping, deep dive.
- Capability check: scholarly search tool, else web search, else shell to Crossref /
  Semantic Scholar / arXiv / DBLP; no retrieval means the skill refuses; sub-agents per
  perspective if available.
- Procedure: Step 0 freeze brief (topic + 2-3 RQs + angle + reader) -> Phase 1 scout
  (3-5 perspectives: mainstream, critics, adjacent fields, methodology, application/
  policy; two rounds wide->narrow; blind-spot merge; verify every citation) -> Phase 2
  synthesize (extract, MECE clustering, serial section writing citing only assigned
  works, in-sentence cross-comparison) -> self-adversarial review -> six gates loop ->
  present as survey paper.
- Outputs: Markdown survey report written to a workspace file (Abstract, Intro with RQs,
  Methodology, Taxonomy, branches with comparison tables, synthesis, open problems,
  conclusion answering each RQ, references). Report language follows the user's language
  (deliberately unlike drafting skills). Allows "[unconfirmed: ...]" markers (explicitly
  contrasted with paper-writer's zero-placeholder rule).
- Checklists/gates: six gates table (Angle CRITICAL, Coverage MAJOR, Citation CRITICAL,
  Taxonomy MAJOR, Calibration MAJOR, Weaving MAJOR) with CLEAR/SUSPECTED/INSUFFICIENT
  verdicts and failure routes (`references/quality-gates.md`).
- Iteration rule: Coverage/Citation failure -> targeted re-scout (incremental, not
  restart); iterate until all gates CLEAR and self-adversarial pass finds nothing.
  `SKILL.md` "The six gates and the iteration loop".
- References: `citation-protocol.md` (52: two-step existence + quote check, five grades
  VERIFIED/MINOR/MAJOR/UNVERIFIABLE/PAYWALL, grey zone = unused, invented-citation
  signals); `hedge-calibration.md` (62: strong/medium/weak/no-evidence ladder, en+zh;
  over/underclaiming; correlation vs causation); `output-structure.md` (177: skeleton,
  title = topic + angle, per-section guidance, IEEE-like reference format without URLs/
  DOIs, formatting discipline); `quality-gates.md` (96); `search-strategy.md` (57: five
  keyword patterns, blind-spot checks, discipline adjustments CS/biomed/social/cross);
  `self-adversarial.md` (68: three retrospective questions, perspective-omission check,
  concession rules); `synthesis-framework.md` (123: extraction, MECE taxonomy, serial
  synthesis, weaving pattern, comparison-table rules, contradictions, per-section
  skeleton).
- Scripts: none. Cross-links: idea-evaluator, paper-writer, intro-drafter, paper-polish.
- Field assumptions: explicitly cross-disciplinary (evidence standards for CS/AI,
  biomedicine, social science, economics; RCT/IV/DID/RDD named). SKILL.md uses bare
  "references/x.md" mentions (not linter-checked).

### 3.3 drawio-reconstruction (SKILL.md 351 lines)

- Trigger: turn a diagram image, research figure, architecture diagram, slide, UI
  screenshot, or image folder into `.drawio` XML.
- Inputs: reference image(s), output dir, naming/overwrite policy, optional
  user-approved reference `.drawio` or redline screenshot.
- Procedure: resolve `$SKILL_DIR`; fidelity contract (visual fidelity > editability;
  script pass is not completion; never silently rewrite text); batch workflow (manifest,
  bounded worker pool or serial fallback, exclusive write sets, parent opens every
  preview); mandatory visible-element inventory (id, bbox, content, medium
  native/SVG/crop/generated-cleanup, style, status); medium decision rules (8 rules +
  blocking medium defects); icon role-to-symbol map; screenshot crop rules
  (`crop_assist.py`); curves/arrows inventory; typography box-model; default 11-step
  workflow; mandatory visual audit (11 blocking defects); user-approved reference
  reuse; redline feedback; verification commands; short final response.
- Outputs: `<name>.drawio`, `<name>.png`, `<name>.audit.md` (batch/complex),
  `drawio_batch_manifest.json`.
- Iteration rule: "Iterate ... until both technical checks and visual audit pass";
  "If any item fails, continue editing."
- Scripts (`scripts/`): `batch_manifest.py` (132: scans image folder, writes manifest
  JSON with `-vN` revision names if outputs exist); `batch_verify.py` (102: runs check +
  export per manifest/dir/file, summary pass/fail); `check_drawio.py` (335: XML parse,
  counts, page containment, hard-coded semantic containment rules for ids like `ev_*`,
  `out_*`, `why_*`, text-clipping estimate, duplicate icon payloads, `#` in SVG data URL,
  "complex visual uses SVG" heuristic); `export_drawio.py` (109: finds Draw.io CLI via
  `--drawio-path`, `DRAWIO_PATH`, common paths, PATH; `-x -f png -s 1`);
  `crop_assist.py` (397: Pillow, ROI/anchor/exclude, foreground mask, connected
  components, candidate crops + preview).
- Other files: `README.md`/`README.zh-CN.md` (Codex + GPT-5.5 xhigh reproduction
  config, VCG-Bench citation), `agents/openai.yaml` (Codex display metadata),
  `requirements.txt` (Pillow>=10.0), `.gitignore`, MIT `LICENSE`.
  `examples/`: three reference PNGs and three reconstructed `.drawio` files
  (`data_lake.drawio` 316 lines, `data_man.drawio` 369, `data_sci2.drawio` 407; very long
  lines with embedded images; purpose: reproducible showcase inputs/outputs, not read
  in full). `assets/cases/`: README before/after images.
- Cross-links: none in SKILL.md; README positions figure-designer upstream.
- Field assumptions: domain-neutral (any diagram); Codex-oriented packaging.

### 3.4 figure-designer (SKILL.md 207 lines)

- Trigger: design Figure 1, plot results, choose chart type/tool, "figure looks
  unprofessional"; audit of an existing figure image.
- Procedure: Step 1 classify into motivated-example / solution-overview /
  experimental-results (load image with Read tool in `figure-audit` mode; that mode is
  not otherwise defined); Step 2 paradigm; Step 3 layout sketch; Step 4 labels (real
  names, ColorBrewer/Viridis); Step 5 tool; Step 6 universal rule audit; Step 7
  integrity gate (7 items, `[inspection]`/`[user-verify]`); Step 8 output.
- Outputs: 8-part template (type, paradigm + rejected alternatives, layout, labels, tool,
  rule-audit checkboxes, gate result, severity summary).
- Checklists: universal audit (vector, >=8pt, colour-blind safe, self-contained caption,
  honest axes, no chartjunk); gate items 1-7.
- References: `design-rules.md` (99: format, typography, colour, caption "first sentence
  states the finding", axis, decoration); `motivated-example.md` (138: paradigms A
  running example + failure, B existing vs ours, C performance teaser; 30-second test);
  `solution-overview.md` (145: pipeline / system architecture / multi-layer; names match
  section titles); `experimental-results.md` (127: chart decision matrix, encoding,
  highlight-Ours, honest axes, 150x100 pt canvas, `plot_utils.py`); `tools.md` (124:
  PPT, Figma, draw.io, Matplotlib/Seaborn, TikZ/PGFPlots, Plotly, OmniGraffle; avoid
  Excel images, Illustrator edits, AI image generators).
- Cross-links: intro-drafter, tech-paper-template, pre-submission-reviewer.
- Field assumptions: "technical paper" with a method and a "beat the baselines" story
  (Highlight Ours rule; Text-to-SQL canonical example; AFlow/Alpha-SQL/LEAD). No
  guidance for statistical plots (CIs, distributions of effects), math diagrams beyond a
  TikZ tool row, or empirical-study figures (e.g. RQ result plots, taxonomies).

### 3.5 idea-evaluator (SKILL.md 327 lines)

- Trigger: "evaluate/score this idea", feasibility, novelty check, before committing.
- Inputs: idea description, user capability (hours/week, skills), resources, venue.
- Procedure: Step 1 first impression + paradigm classification by method (STEM,
  humanities, empirical social science, finance/economics, law); Step 2 fatal-flaws
  audit first, with retrieval-grounded novelty (3-5 closest works, differing axes; "not
  found" != novel) and "data-refuted mechanism = automatic CRITICAL"; short-circuit to
  Reject and Pivot on any CRITICAL; Step 3 lifecycle/capability; Step 4 five-dimension
  scoring (start at 5; data- or mechanism-based grounds; attribution cap); Step 5
  paradigm-shift probe (4 questions); Step 6 feasibility (compute/data/engineering/
  timeline); Step 7 silent integrity gate (7 items); Step 8 verdict.
- Outputs: 7-section evaluation (first impression, fatal flaws table, lifecycle table,
  5-dim radar table, probe table, feasibility table, verdict Strong Accept / Accept with
  Revisions / Reject and Pivot + top 3 actions).
- References: `fatal-flaws.md` (217: F1-F10 with detection rules and defenses, severity
  escalation, data-refuted section; F3 hard-codes "2026 result"); `five-dimensions.md`
  (297: per-dimension strategies + 1-10 rubrics + grounded examples from Alpha-SQL, LEAD,
  StatQA, AFlow; aggregation rules; grounds; attribution discipline);
  `lifecycle-capability-matching.md` (177: six categories, hours/skills/preference/
  infrastructure rubric, mismatch flags + recovery, 3 examples); `paradigm-shift-probe.md`
  (160: four principles, 0-8 scoring; note SKILL.md uses "two or more yes" instead);
  `domain-evaluation-frameworks.md` (162: humanities/social-science and
  finance/economics substitute 5 dimensions and fatal flaws, framework chooser table);
  orphans: `paradigm-first-principles.md` (115), `paradigm-elephant.md` (112),
  `paradigm-technology-cycle.md` (116), `paradigm-hamming.md` (137, includes a dated
  top-10 problem list template), `paradigm-examples.md` (107: Transformer, adaptive
  query processing, agent data cleaning, multi-agent workflows), `worked-examples.md`
  (206: retrospective evaluations of Alpha-SQL, AFlow, LEAD).
- Cross-links: intro-drafter, tech-paper-template, benchmark-paper-template ("separate
  plugin", a stale phrase), pre-submission-reviewer; handbook 2.3.
- Field assumptions: STEM path is ML-systems flavoured (GPUs, baselines, Text-to-SQL,
  agents); has explicit non-STEM routing, but no SE/MSR, pure math, or statistics paradigm.

### 3.6 intro-drafter (SKILL.md 211 lines)

- Trigger: draft, outline, or restructure an Introduction (STEM/technical).
- Inputs: research area, limitations, key idea, challenges, solution overview,
  optional references; running example only if user supplies a real one.
- Procedure: pre-check STEM (else route to paper-writer CER); Step 1 type positioning
  (Technique vs New Problem/Setting); Step 2 plan six paragraphs (purpose, points, gaps);
  Step 3 running example (never fabricate); Step 4 silent alignment checks; Step 5 write
  prose (100-250 words/paragraph, numeric citations, 15-25 verified refs, 3-5 retrieval
  rounds, citation ladder at >=3 citations, tense rules, tone pass); Step 6 optional
  <=3-line note. Outline mode on explicit request (type, per-paragraph plan, five
  consistency checks).
- Outputs: six paragraphs + References + optional note; nothing else.
- Checklists: five consistency checks (running-example loop, limitations-to-challenges,
  goal-to-contribution-1, challenge-to-module, contribution-to-section); contribution
  audit (8 items) in `contribution-patterns.md`.
- References: `flowchart.md` (204: per-paragraph purpose/points/failures, word budgets);
  `paper-types.md` (155: Technique vs New Problem profiles, word weights, Alpha-SQL/AFlow/
  LEAD, mixed cases); `running-example.md` (133: real/specific/simple/recurring/
  failure-revealing; two patterns); `contribution-patterns.md` (116); orphan
  `worked-examples.md` (168, internal outlines of the three case studies);
  `evidence-discipline.md` and `prose-delivery.md` (shared copies, see 2.3).
- Cross-links: paper-writer (citation ladder), benchmark-paper-template, paper-polish,
  pre-submission-reviewer, idea-evaluator; tone files in paper-polish.
- Field assumptions: STEM technique/system papers with "challenges -> modules" (Intro
  skeleton from DB/AI conference practice). Non-STEM delegated. Empirical SE / math
  Intros (RQ-driven or theorem-driven) have no scaffold.

### 3.7 paper-polish (SKILL.md 267 lines)

- Trigger: polish, fix wording, remove AI flavour, translate Chinese draft, tone down
  overclaims.
- Procedure: overriding faithfulness rule (pure language edits free; meaning-touching
  edits flagged before/after); never add data/equations/citations/mechanisms; light
  touch by default; one pass = understand -> diagnose (language vs logic) -> edit ->
  account; section conventions; calibration (verb strength); fair to prior work; AI-tone
  removal; Chinese-to-English rules; edit files in place (diff = change record) vs pasted
  text; chunking; unreadable content; route deeper problems to paper-writer /
  pre-submission-reviewer / idea-evaluator.
- Outputs: clean polished text + 3-5 change notes; before/after list for meaning-risk
  edits; allows short parenthetical notes to the author.
- References (all canonical shared copies): `academic-phrasebank.md` (98: verb ladder,
  gap/comparison/limitation/implication phrases, transitions, en+zh);
  `ai-tone-guardrails.md` (85: 13 AI-tone signal families, inflated-claim wordlist
  en+zh, replacements); `section-conventions.md` (124: Intro/Methods/Results/Discussion/
  Conclusion/Abstract/Title must-answer questions, order, faults).
- Field assumptions: largely general (biomed-style examples: gene names, cohorts);
  Chinese-author orientation.

### 3.8 paper-writer (SKILL.md 284 lines)

- Trigger: write a section, turn idea/results into paper text, full draft; STEM and
  non-STEM.
- Hard rules (6): three legitimate sources only (user, verified retrieval, L0 common
  knowledge), zero placeholder tags, no invented specifics, claim <= evidence, real vs
  planned results separated, no leaked scaffolding.
- Procedure: capability check; Phase 1 Scope (granularity, paradigm by method incl.
  review, Draft vs Final mode); Phase 2 Evidence (inventory files, 2-3 retrieval rounds,
  gap list, Evidence Map for full papers); Phase 3 Blueprint (STEM Intro -> intro-drafter;
  STEM other -> section-guidance; non-STEM -> CER per paragraph: Claim, Evidence,
  Reasoning, Role; benchmark -> benchmark-paper-template); Phase 4 Draft (7 rules);
  Phase 4.5 red-flag table (13 stop signals); Phase 5 Review (checklist, independent
  citation verification, limits of self-review); Phase 6 Deliver.
- Outputs: prose (+References, <=3-line note) or manuscript file; Evidence Map and
  chapter blueprint as separate working files.
- Checklists: `verification-checklist.md` (121: source recall; literature 7; facts 8;
  evidence matching 5; cross-section 4; AI-trace 6; formulas/tables 6; delivery 3).
- Iteration/convergence: citation pass loops until "no unresolved problem entries
  remain"; fixes are targeted sentence rewrites then re-verify
  (`verification-ladder.md` section 7).
- References: `evidence-discipline.md` (152, canonical: L0-L4 evidence hierarchy,
  Evidence Map template with "cannot support" column and file paths, provenance
  thinking, five fabrication red-flag families, D0-D5 experimental evidence gates,
  contribution-to-evidence tracing, Draft vs Final); `prose-delivery.md` (62, canonical:
  allowed output, forbidden scaffolding list, formula/table rules, chunking);
  `verification-ladder.md` (132: rungs fresh-context sub-agent / same-context grounding /
  closed book; trigger table; statuses VERIFIED, METADATA_MISMATCH, NOT_FOUND, OVERCLAIM,
  INCONCLUSIVE); `verification-checklist.md`; `section-guidance.md` (115: Abstract
  200-250 words, Related Work by themes, Methods, Results describe-then-interpret,
  Discussion 3 layers, Conclusion, Future Work); `citation-style.md` (146: numeric
  default, entry formats, APA 7, Chicago AD/NB, Harvard, Vancouver, universal rules);
  shared copies of the three polish files.
- Field assumptions: most field-general skill in the repo; still assumes
  method/modules/challenges logic chain for STEM and LLM-retrieval tooling.

### 3.9 pre-submission-reviewer (SKILL.md 326 lines)

- Trigger: review/audit/proofread a draft; within a week of a deadline.
- Procedure: Step 0 paradigm (STEM, humanities, empirical social science,
  finance/economics, law with different weights) + venue fit; Step 1 macro logic (Intro
  flowchart, contribution mapping, ablation-based attribution, claim strength;
  retrieval-grounded novelty and citation completeness); Step 2 writing details;
  Step 3 grammar; Step 4 LaTeX; Step 5 figures; Step 6 banned-vocabulary + em-dash
  scan; Step 7 section-by-section; Step 8 silent integrity gate (7 items); Step 9 output.
- Outputs: summary counts, five dimension tables (finding/severity/fix), banned-word list,
  score 1-10, recommendation (Ready / 1-2 days / major revision).
- Checklists: severity taxonomy with examples and "severity honesty" rule;
  `logic-and-structure.md` failure-pattern table; banned-word list (28 terms).
- References: `logic-and-structure.md` (125: Logic First, Self-contained, Leading Text,
  Running Example, paragraph discipline 3-8 sentences, section consistency);
  `grammar-rules.md` (135: articles, agreement, tense, complexity, which/that, passive,
  Chinglish, quote punctuation); `latex-rules.md` (158: file layout, macros, `~\cite`,
  `fig:` labels with underscores, figures/tables, equations, L12 quotes, L13 dashes,
  revision conventions); `forbidden-patterns.md` (163: em-dash, banned vocabulary,
  chartjunk, overclaims, plagiarism, detection heuristics); `section-guides.md`
  (169: abstract 5-sentence formula; Intro; Problem Formulation; Framework; Experiments
  ">= 3 datasets", All/-A/-B/-C ablation; Related Work with DBLP and SIGMOD/VLDB/ICDE/TKDE
  abbreviations; Conclusion present perfect).
- Cross-links: tech-paper-template, intro-drafter, benchmark-paper-template ("separate
  plugin").
- Field assumptions: DB/ML conference (Intro flowchart, ablations, >=3 datasets, DBLP,
  LaTeX two-column); non-STEM paradigms supported only via Step 0 weights. Gate item 6
  mentions "Dimension 6" although there are five dimensions plus the Step 6 scan.

### 3.10 rebuttal-guidance (SKILL.md 138 lines)

- Trigger: user pastes reviewer comments; rebuttal help; "reply to R1.W2"; OpenReview;
  reviewer ignored the rebuttal.
- Model: conditional persuasion P(Z=1|X,Y): X reviewer mindset cluster, Y strategy
  vector, Z success. Produces guidance, never ready-to-paste prose.
- Procedure: Step 1 inventory W/Q table; Step 2 classify (misunderstanding,
  evidence_gap, novelty, baseline_fairness, scope_claim, writing_clarity, theory,
  efficiency, other); Step 3 score 7 behaviour signals and match a cluster with
  confidence; Step 4 read cluster stats (up-rate, rule diffs, Cohen's d,
  success/failure patterns); Step 5 per-concern guidance block (type, strategy, structure
  Acknowledge -> Response -> Evidence -> Revision note, clarify-from-paper, new experiment,
  tone, template A/B/C, avoid); Step 6 checklist; Step 7 output.
- Outputs: "## Rebuttal Guidance" with mindset summary, 3-5 global priorities,
  per-concern blocks, checklist highlights. Unverified numbers marked `[TO VERIFY]`
  (contrasts with paper-writer's zero-placeholder rule; acceptable because output is
  guidance).
- References (all in Chinese; allowed by linter): `checklist.md` (40: 8-item
  completeness check, tone red lines, low-openness advice, common mistakes);
  `concern-classification.md` (41: type table with signals/dimensions/templates, W vs Q,
  keywords, compound concerns); `mindset-matching-heuristics.md` (43: 7 signals, a
  6-cluster quick table whose names do not match the library's clusters);
  `mindset-library.md` (335: six clusters "Auto-generated from
  data/behavior/mindset_library.json" (file not in repo), each with sample share,
  historical up-rate, acceptance rate, signals, rule-stat diffs, Cohen's d, success/
  failure patterns, key strategy); `strategy-dimensions.md` (45: 10 dimensions incl. risk
  dims overpromise_risk, vague_future_work; synergies); `response-templates.md` (92:
  templates A clarify, B add evidence, C concede and narrow scope).
- Missing vs description: no step or data for retrieving "similar successful historical
  (review, rebuttal) pairs" although the description promises it optionally.
- Cross-links: idea-evaluator, pre-submission-reviewer.
- Field assumptions: ML conference review (ICLR/NeurIPS/ICML/EMNLP, OpenReview, W/Q
  format, score increases); statistics derived from an unshipped dataset. Overlaps
  handbook 3.5 revision template (`responses/r1.tex`, `R1.W1` margin notes) which it
  does not reference.

### 3.11 tech-paper-template (SKILL.md 192 lines)

- Trigger: brainstorming, advisor meeting, pre-drafting skeleton, "paper logic chain".
- Procedure: Step 1 Technique vs New Problem/Setting (benchmarks redirected); Step 2 fill
  template cells (background, <=3 limitations, key idea/goal, <=3 challenges, modules one
  per challenge, 3-4 contributions with sections); Step 3 four consistency checks
  (Limitations->Key Idea, Key Idea->Challenges, Challenges->Methodology,
  Methodology->Contributions; every failure CRITICAL); Step 4 methodology outline; Step 5
  gate (7 `[inspection]` items; not marked "silent"); Step 6 output.
- Outputs: type, filled template table, check results, severity summary, next skill.
- References: `thinking-template.md` (194: per-cell content contract, strong/weak,
  detection rules, methodology-outline derivation); `consistency-checks.md` (166);
  `paper-types.md` (127: three categories incl. Cross-domain Technique; positioning
  questions); orphan `worked-examples.md` (124).
- Cross-links: intro-drafter, benchmark-paper-template, pre-submission-reviewer,
  idea-evaluator.
- Field assumptions: systems/ML technique papers ("modules", "search-space explosion").

### 3.12 vibe-research-workflow (SKILL.md 198 lines)

- Trigger: how to use AI for research, Vibe Coding tips, tool choice, session start.
- Procedure: Step 1 phase (coding/figure/writing/mixed); Step 2 recap six behavioural
  rules (permitted uses; substance owned by user, drafting legitimate within boundary;
  verify every AI output; no fabricated citations; no misconduct; honour disclosure
  rules); Step 3 phase procedure; Step 4 tool selection; Step 5 gate (mostly
  `[user-attest]`); Step 6 output.
- Outputs: phase, rules acknowledged, time-block workflow table, tool table, red lines,
  verification and disclosure plan.
- References: `behavior-guidelines.md` (149: six rules with compliance/non-compliance
  examples); `vibe-coding.md` (154: Coder->Commander, six mindset principles, Plan
  first, clear requirements, small steps, context, error reports, git discipline);
  `vibe-figure.md` (131: discuss -> select & prompt -> Gemini sketch -> vectorise by
  hand; what AI cannot do; figure-designer integration); `vibe-writing.md` (181: v1
  contradiction 3.5 vs 5.1 "resolved"; red lines incl. "Copy AI-generated paragraphs
  verbatim" forbidden; flow A-E; delegates banned-word list to
  pre-submission-reviewer); `tool-selection.md` (144: Cursor, Claude Code, Codex,
  sketch/layout/chart tools, Grammarly/Overleaf, cost, mainland China access).
- Field assumptions: ML-lab tooling (GPU, Python, Cursor); general in principle.
- Tension: `vibe-writing.md` says rewrite AI paragraphs in your own words, while v2.1
  `paper-writer` drafts submittable prose; SKILL.md resolves this by routing drafting
  requests to paper-writer ("What stays forbidden is fabrication, not drafting").

---

## 4. Cross-cutting inventory

### 4.1 Existing checklists (where, what)

| Location | Items (brief) |
|---|---|
| `handbook*/03_Paper_Writing/3.1*` | Pre-writing reflection checklist: Background/Why/Problem, What (<=3 challenges, core idea), How, So What (main results, ablation, in-depth analysis, case study) |
| `handbook*/03_Paper_Writing/3.4*` section 6 | Benchmark checklist: Intro 6, Benchmark chapter 6, Experiments 8, Overall 4 |
| `handbook*/03_Paper_Writing/3.5*` | Writing checklist: logic, outline-first, paragraph/sentence connection, figures, running example, self-contained, focused; LaTeX rules; grammar; LLM-writing rules; Abstract 5 sentences; Intro 6 paragraphs; Experiments (>=3 datasets, baselines, ablation); Related Work; good/bad paper traits; "Detailed Notes" |
| `handbook*/04_Scientific_Plotting/4.4*` | 10-item figure checklist (vector, >=8pt, caption, axis units, legend, dual encoding, Y-axis, names match text, Ours highlighted, code-generated) |
| `skills/benchmark-paper-template/references/checklist.md` | 4 categories + venue checks + severity (see 3.1) |
| `skills/benchmark-paper-template/references/gap-analysis.md` Step 3 | 4 gap validation checks |
| `skills/intro-drafter/references/contribution-patterns.md` section 6 | 8-item contribution audit |
| `skills/paper-writer/references/verification-checklist.md` | ~39 delivery checks in 7 groups |
| `skills/paper-writer/references/evidence-discipline.md` section 6 | D0-D5 experimental evidence gates |
| `skills/deep-research/references/quality-gates.md` | Six gates with detection questions |
| `skills/figure-designer/SKILL.md` | Universal rule audit + 7 gate items |
| `skills/idea-evaluator/SKILL.md` + `fatal-flaws.md` | 7 gate items; F1-F10 detection rules |
| `skills/pre-submission-reviewer/SKILL.md` + refs | 5 dimensions, 28 banned terms, failure-pattern table |
| `skills/tech-paper-template/SKILL.md` | 4 consistency checks + 7 gate items |
| `skills/rebuttal-guidance/references/checklist.md` | 8 completeness items, tone red lines |
| `skills/vibe-research-workflow/SKILL.md` | 7 gate items (mostly user-attest) |
| `skills/drawio-reconstruction/SKILL.md` | Inventory fields; 11 blocking visual-audit defects; blocking medium defects |

### 4.2 Field / venue profiles

- Paradigm routing by research method (STEM / humanities / empirical social science /
  finance-economics / law): `idea-evaluator/SKILL.md` Step 1 +
  `references/domain-evaluation-frameworks.md`; `pre-submission-reviewer/SKILL.md`
  Step 0; `paper-writer/SKILL.md` Phase 1 (adds "review"); `intro-drafter/SKILL.md`
  pre-check.
- Evidence standards by discipline (CS/AI, biomedicine, social science, economics,
  cross-disciplinary) and search adjustments: `deep-research/SKILL.md`,
  `references/search-strategy.md`.
- Citation styles by field (IEEE numeric default; APA, Chicago, Harvard, Vancouver):
  `paper-writer/references/citation-style.md`.
- Venue-specific checklist rows: NeurIPS E&D, ICLR/ICML, ACL/EMNLP/NAACL in
  `benchmark-paper-template/references/checklist.md` section 5. Venue fit as fatal flaw
  F2 (`idea-evaluator/references/fatal-flaws.md`) and as a review finding
  (`pre-submission-reviewer/SKILL.md` Step 0).
- DB-community norms hard-coded in the handbook: ">=50% performance, >=10% accuracy",
  ">100 citations is decent in DB", DBLP bibtex, SIGMOD/VLDB/ICDE/TKDE abbreviations
  (`handbook-en/03_Paper_Writing/3.5*`, mirrored in `pre-submission-reviewer/references/section-guides.md`).
- There is no venue-profile data structure (no YAML/JSON profiles); all profiles are
  prose embedded in skills. No SE (ICSE/FSE/ASE/MSR/TSE/TOSEM/EMSE), math, statistics, or
  causal-inference venue profile exists (grep: zero hits outside drawio example blobs).

### 4.3 Check loops and iteration rules

- deep-research: six gates with failure routes; targeted re-scout; iterate until CLEAR
  and self-adversarial pass is clean (`deep-research/SKILL.md`).
- paper-writer: citation verification convergence ("no unresolved problem entries"),
  targeted rewrite + re-verify (`verification-ladder.md` s7); Phase 4.5 stop signals.
- drawio-reconstruction: inventory statuses pending/done/needs-fix/accepted; iterate until
  checks + visual audit pass (`SKILL.md` "Default Workflow", "Mandatory Visual Audit").
  The unmerged sync branch upgrades this to producer/reviewer loops (section 6).
- idea-evaluator: early short-circuit on CRITICAL; downgrade verdict if gate fails.
- tech-paper-template / intro-drafter: fix chain breaks in the plan before writing ("Never
  write around a broken chain"); intro outline mode re-exposes checks.
- pre-submission-reviewer: single pass; recommendation must match counts.
- vibe-writing Step D: repeated violations mean update the polish prompt.
- No skill defines a multi-round revise-and-recheck loop for a whole manuscript, and no
  loop has an explicit stop/round budget besides drawio's "until pass".

### 4.4 Records and process tracking

- paper-writer: Evidence Map (with file paths and line refs), chapter blueprint, contribution
  tracing table, kept as separate working files (`evidence-discipline.md` s2, s7;
  `prose-delivery.md`).
- deep-research: frozen brief (topic + RQs + angle + reader); report file; disclosed
  degradations.
- drawio-reconstruction: `<stem>.audit.md` inventory, batch manifest JSON.
- paper-polish: when editing files, "the version diff serves as the precise change record".
- benchmark: `instantiation-template.md` and design-document template; idea-evaluator
  `paradigm-hamming.md` dated top-10 list with add/remove log.
- handbook 3.5: revision workflow with `responses/r1.tex..r3.tex`, `\revision{}` blue
  marks, margin tags `R1.W1`, and a per-reviewer summary table.
- vibe-coding: commit after each minimal unit with detailed messages.
- Absent: research logs, experiment registries, decision records, data/version
  provenance for analyses, replication-package tracking.

### 4.5 De-AI and writing-style rules

- Handbook origin: `handbook*/03_Paper_Writing/3.5*` "LLM Writing Issues": em-dash ban,
  logical quote punctuation, banned vocabulary list, "do not write a Chinese draft and
  translate with GPT", and "It is strictly forbidden to use LLMs or AI to generate
  content".
- `paper-polish/references/ai-tone-guardrails.md`: 13 signal families + inflated-claim
  list (en/zh) + replacements + "clean but lifeless" warning.
- `pre-submission-reviewer/references/forbidden-patterns.md`: 28 banned terms by group,
  em-dash MAJOR, thresholds (3+ uses MAJOR), overclaim and plagiarism rules.
- `paper-writer/references/prose-delivery.md`: no headings/labels/gate reports/preambles/
  placeholder tags/emoji/markdown emphasis in paper prose.
- Calibration ladders: `paper-polish/references/academic-phrasebank.md`,
  `deep-research/references/hedge-calibration.md`.
- Grammar for Chinese authors: `pre-submission-reviewer/references/grammar-rules.md`;
  Chinese-to-English section in `paper-polish/SKILL.md`.
- Output-language rule (drafting/polish: explicit request > Chinese venue > English; never
  infer from user's language) in paper-writer, intro-drafter, paper-polish; deep-research
  deliberately follows user language.

### 4.6 Figure rules

- Handbook ch.4 (5 ironclad rules, three figure types, 10-item checklist, tool table).
- `figure-designer/references/*` (rules + paradigms + tools); `vibe-research-workflow/
  references/vibe-figure.md` (AI sketch then hand vectorisation);
  `pre-submission-reviewer` Dimension 5 + chartjunk list; `benchmark-paper-template`
  figure placement and pipeline figure guidance; `drawio-reconstruction` for executable
  diagram rebuilding.
- Tension: `figure-designer/references/tools.md` "avoid AI image generators" vs
  handbook 5.1 / vibe-figure recommending Gemini/Nano Banana drafts (resolved only
  implicitly: drafts yes, final figures no).

---

## 5. Gaps and AI/ML bias

### 5.1 Most AI/ML-specific skills (descending)

1. benchmark-paper-template: LLM model families, CoT/few-shot, DPO/GRPO companion
   methods, contamination, Human vs LLM, ML D&B venues.
2. rebuttal-guidance: OpenReview W/Q format, ML-venue statistics.
3. figure-designer, tech-paper-template, intro-drafter, pre-submission-reviewer: the
   challenges->modules->ablation chain and "beat baselines" story; all examples are
   Alpha-SQL / AFlow / LEAD / Text-to-SQL; DB conventions.
4. idea-evaluator: STEM path tuned to ML systems (GPUs, SOTA baselines "2026"), but has
   non-STEM substitutes.
5. Least biased: paper-writer, paper-polish, deep-research (explicit multi-discipline
   handling), drawio-reconstruction (domain-neutral), vibe-research-workflow (tooling).

### 5.2 What would need to change per target field (absent today)

- SE / MSR (empirical): RQ-driven paper type (RQ1..RQn as the spine, not
  challenges->modules); mining pipeline and dataset provenance (repos, sampling frames,
  bots/forks filtering, time windows); qualitative coding with IAA; Threats to Validity
  section (construct/internal/external/conclusion; zero repo hits for "threats to
  validity"); replication/artifact package (zero hits for "replication package");
  SE venue profiles (ICSE, FSE, ASE, MSR, EMSE, TSE, TOSEM; ACM SIGSOFT Empirical
  Standards, artifact badges); figure types for empirical findings (distributions,
  taxonomies, Sankey/upset, effect plots) rather than "Highlight Ours"; idea-evaluator
  dimensions for empirical studies (the humanities/social-science substitute is the
  closest existing hook); benchmark checklist rows that do not assume LLM baselines.
- Mathematics: theorem/lemma/proof paper type (contribution = result + proof technique);
  notation and definition discipline beyond "notation table if >6 symbols"
  (`handbook-en/03_Paper_Writing/3.5*`); proof-checking review dimension
  (pre-submission-reviewer only says "experiments reads as proofs" for theory papers);
  amsthm/LaTeX conventions; math-journal venue profiles; no Lean/formal verification hook.
- Statistics: estimand/assumption/inference reporting, CIs and effect sizes as first-class
  (only scattered mentions: figure CIs, "mean +- std", APA style), multiple-testing and
  power (zero hits for "power analysis"), simulation-study design, reproducible analysis
  code; journal norms (JASA, Annals) absent.
- Causal inference: identification strategy exists only in the finance/economics
  substitute framework (IV/DID/RDD) and deep-research evidence standards; missing DAGs,
  confounding/positivity/consistency assumptions (zero hits for "confound"), sensitivity
  analysis, pre-registration (only F10 "preregister two failure modes"), target-trial
  framing; hedge rules do cover "correlation written as causation".
- Cross-cutting: handbook case studies are all ML/DB Intro analyses; worked examples in
  four skills reuse the same three papers; venue profiles are prose, not data.

### 5.3 Overlaps between upstream skills

- tech-paper-template vs intro-drafter: same six-stage chain, same Technique/New
  Problem positioning, near-duplicate `paper-types.md`, same consistency checks (4 vs 5),
  three parallel `worked-examples.md` (also idea-evaluator).
- paper-writer vs intro-drafter: shared evidence/prose discipline (synced); intro-drafter
  is effectively paper-writer's STEM Introduction route.
- pre-submission-reviewer vs paper-polish vs paper-writer: per-section guidance in three
  files with different content; two AI-tone/banned-word lists (synced only between
  polish and writer); em-dash rule in reviewer, polish guardrails ("excessive dashes"),
  linter, and handbook 3.5.
- figure-designer vs vibe-research-workflow (vibe-figure) vs drawio-reconstruction vs
  handbook ch.4: figure rules repeated.
- benchmark-paper-template internal duplication: SKILL.md, `orchestrator-notes.md`,
  `paper-structure.md`, `instantiation-template.md` each restate pillars and structure.
- deep-research vs idea-evaluator/pre-submission-reviewer retrieval-grounded novelty
  checks (three implementations of "find 3-5 closest works").
- rebuttal-guidance vs handbook 3.5 revision template vs pre-submission-reviewer trigger
  "Rebuttal is drafted" (`skills/README.en.md`).

---

## 6. Upstream git branches

`git branch -a` (2026-10-12): local `design`, `main`; `origin/design`, `origin/main`
(private fork easygl1der/supervisor-skills-plus); `upstream/HEAD -> upstream/main`,
`upstream/main`, `upstream/agent/preserve-original-drawio-skill`,
`upstream/chore/sync-drawio-reconstruction`, `upstream/feat/doubao-backport`,
`upstream/feat/drawio-reconstruction-skill`.

`git log --oneline -15 main`: `5f9432d` docs DataMagic/DeepEye; `207bc6f`, `668a474`
Update README.md (rebuttal row); `198c46c`, `dd39456` Add files via upload
(rebuttal-guidance); `aff5de9` restore one-click install prompt; `1bb65a3` PyYAML
frontmatter parsing; `e66fa8d`, `f546647` Doubao news; `93dccd1` wire CI lint;
`c387c28` drawio description 40-80 words; `557f670` merge PR #10; `3972636` restore
complete drawio package; `a01b0b4` remove Star History; `eeedd71` merge
feat/doubao-backport v2.1.0.

| Remote branch | Tip | Commits not in main | Status |
|---|---|---|---|
| `upstream/feat/drawio-reconstruction-skill` | `a57f3b4` 2026-07-03 | 0 | merged (29 behind) |
| `upstream/feat/doubao-backport` | `3c5a06f` 2026-07-10 "release: cut v2.1.0" | 0 | merged via `eeedd71` |
| `upstream/agent/preserve-original-drawio-skill` | `3972636` 2026-07-13 | 0 | merged via PR #10 `557f670` |
| `upstream/chore/sync-drawio-reconstruction` | `090587e` 2026-08-07 (author xysu) | 1 | UNMERGED; 5 commits behind main |

Content of the only unmerged commit `090587e` "chore: sync drawio-reconstruction skill
from upstream" (28 files, +2446/-425, all under `skills/drawio-reconstruction/`):

- SKILL.md rewrite: new description ("Each image requires independent icon and
  reconstruction review passes. Batch requests begin with a manifest and one worker per
  image"); "Mandatory Role Separation" with Producer/Reviewer agents, literal agent ids,
  per-round audit rows `phase | artifact_version | producer_id | reviewer_id | verdict |
  fix_ids | artifact_sha256`, gates 0-4 (reference immutability, icon production, icon
  review, reconstruction production, reconstruction review), no fixed round limit;
  "Icon Preparation Repair Loop" (`<stem>_icons/icons.json`, sharded review sheets <=8
  rows, PASS/FIX ledger format); preview renamed `<stem>_preview.png`; mandatory one
  sub-agent per image (no silent serial fallback); data-URI `%3B` encoding rule.
- Regressions relative to main: removes the `$SKILL_DIR` resolution section and
  hard-codes `~/.codex/skills/drawio-reconstruction/scripts/...` paths (main had removed
  such paths); removes the Pillow install note.
- New scripts: `scripts/validate_review_result.py` (187: validates reviewer PASS/FIX
  ledger against `icons.json` ids, version and SHA-256 hashes); tests
  `tests/test_skill_contract.py` (254) and `tests/run_forward_case.ps1` (46); reworked
  `check_drawio.py` (generic checks, byte-zero header, parent containment) and other
  scripts.
- New examples/assets: `data_cn`, `m1`, `m2`, `m3` (`.drawio` + PNG/JPG; one original
  image ~14 MB).
- Not verified here whether it passes `lint_skills.py` (branch not checked out; read-only
  survey).

`origin/design` = `main` + `bfbfea1` (PROGRESS.md). No other remotes.
