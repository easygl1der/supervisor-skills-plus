# Skills：12 个组，每类任务只记一个名字

[English](README.en.md)

ADR 0021 之后，本库按 12 个**组**组织。每组有一个总入口 `sv-<组>`，agent 可以自动选中它；组内有若干**子命令** `sv-<组>-<名>`，只有点名时才运行。所有组共用的规则放在 `research-core`。

| 你想 | 怎么说 |
|---|---|
| 让 agent 自己挑 | 直接描述任务；对应的 `sv-<组>` 会路由，并告诉你选了哪个子命令 |
| 精确指定 | `/sv-write-polish`、`/sv-study-paper`、`/sv-figure-plot` …… |

Claude Code 和 Cursor 里名字完全一样。agent 的 skill 列表里只有 12 个总入口和 `research-core`；51 个子命令不进列表，所以拆得再细也不会让列表变挤。

## 本文件的位置

| 入口 | 给谁看 |
|---|---|
| [`../README.md`](../README.md) | 本库是谁的、装什么、怎么装 |
| [`../handbook/`](../handbook/) / [`../handbook-en/`](../handbook-en/) | 技能仍在引用的来源课程（不是本库品牌） |
| **本文件** | 某个任务该用哪个组、哪个子命令 |
| 各目录的 `SKILL.md` | 给 agent 执行的规格 |
| [`../docs/adr/0021-sv-skill-groups.md`](../docs/adr/0021-sv-skill-groups.md) | 为什么这样分组，以及新旧名字对照 |

## 12 个组

| 组 | 子命令 | 覆盖什么 |
|---|---|---|
| [`sv-supervisor`](sv-supervisor/SKILL.md) | `-brief` `-init` `-records` `-harvest` | 会话简报与路由、项目初始化、STATUS / TODO / ADR / 日志、经验沉淀进 research-core |
| [`sv-quickread`](sv-quickread/SKILL.md) | `-card` `-style` | 一篇论文的九段式五分钟速读卡；可选风格卡 |
| [`sv-study`](sv-study/SKILL.md) | `-quick-explain` `-paper` `-chapter` `-visual-explain` `-drill` `-bridge` | 理解优先的学习：复述、诊断、纠正；接回项目 |
| [`sv-idea`](sv-idea/SKILL.md) | `-evaluate` `-fatal-flaws` | 完整的 idea 评估，或只做致命缺陷早筛 |
| [`sv-litreview`](sv-litreview/SKILL.md) | `-survey` `-map` | 综述级文献调研；已读文献地图 |
| [`sv-proposal`](sv-proposal/SKILL.md) | `-kaiti` `-grant` `-statement` | 开题报告、基金申请、研究陈述 |
| [`sv-experiment`](sv-experiment/SKILL.md) | `-freeze` `-prereg` `-runs` `-numbers` `-replication` | 冻结输入、预注册确证性分析（git 可审计）、运行日志、可追溯数字、复现包 |
| [`sv-write`](sv-write/SKILL.md) | `-skeleton` `-intro` `-section` `-polish` `-translate` `-critique` `-humanize-paper` `-humanize-report` `-humanize-slides` `-humanize-letter` `-humanize-audit` `-style-mine` `-style-apply` | 一切与文字有关的事：搭骨架、起草、润色、中译英、只挑毛病、按场景去 AI 味、期刊风格 |
| [`sv-figure`](sv-figure/SKILL.md) | `-design` `-drawio` `-plot` `-tikz` `-html` `-poster` `-explain` | 各种图：设计建议、draw.io 重建、代码画图、TikZ、HTML、海报、讲解图 |
| [`sv-review`](sv-review/SKILL.md) | `-once` `-loop` | 只读的投稿前终审；有轮数上限的多轮检查 |
| [`sv-feedback`](sv-feedback/SKILL.md) | `-revise` `-guidance` `-rebuttal` | 意见逐条修改并核实、专家指导记录、rebuttal 规划 |
| [`sv-slides`](sv-slides/SKILL.md) | `-weekly` `-talk` | 组会 Beamer：周报与论文讲解 |
| [`research-core`](research-core/SKILL.md) | （不是命令） | 核心规则、领域与会议 profile、checklist、AI 协作守则、模板 |

## 常见链路

**技术类或 Benchmark 论文**：`sv-idea-evaluate` → `sv-write-skeleton` → `sv-write-intro` → `sv-write-section` → `sv-figure-design` → `sv-write-polish` → `sv-review-loop` → `sv-review-once`。

**任意领域的实证研究**：`sv-supervisor-init` → `sv-experiment-freeze` → `sv-experiment-prereg` → `sv-experiment-runs` → `sv-experiment-numbers` → `sv-write-section`（实证骨架）→ `sv-figure-plot` → `sv-review-loop` → `sv-experiment-replication` → `sv-review-once`。

**从阅读到研究**：`sv-quickread-card` → `sv-study-paper` → `sv-study-bridge` → `sv-idea-evaluate` 或 `sv-experiment-freeze`；多张卡片 → `sv-litreview-map`；形成计划 → `sv-proposal`。

**审稿回合**：`sv-feedback-revise`（回复表）→ `sv-feedback-rebuttal` → `sv-write-humanize-letter` → `sv-review-loop`。

**组会**：`sv-supervisor-brief` → `sv-slides-weekly` → `sv-write-humanize-slides` → `sv-supervisor-records`（会议记录）。

## 与手册的对应

| 手册章节 | 组 |
|---|---|
| 第一章 宏观认识 | `sv-review-once` |
| 第二章 Idea 构思 | `sv-idea`、`sv-litreview` |
| 第三章 论文写作 | `sv-write`（skeleton、intro、section、polish）、`sv-review` |
| 第四章 科研作图 | `sv-figure` |
| 第五章 Vibe Research | `research-core`（`core/ai-collaboration.md`） |
| 第六章 案例 | `sv-write-skeleton`、`sv-experiment`、`sv-review` |

## 安装

见 [`../INSTALL.md`](../INSTALL.md)。用 agent-sync 的机器跑 `scripts/sync_agent_links.py`，其他情况用 `scripts/install.sh`。
