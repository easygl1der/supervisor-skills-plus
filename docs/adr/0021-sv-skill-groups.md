# ADR 0021: 26 个 skill 重组为 12 个 `sv-` 组，组内用斜杠子命令细分

Status: proposed
Date: 2026-10-18
Deciders: owner（2026-10-18 讨论中逐项决定），Claude Code（起草）

## Context

### 用户反馈的问题（owner，2026-10-18）
1. skill 太多（26 个）。
2. 单个 skill 内容太多。
3. 名字难以辨认。
4. 内容太多，交互时给的提示词没有被准确捕获。
5. 单个 skill 范围太宽，例如 `study` 同时管学习和画图。
6. 很多 skill 内容重合。

讨论中 owner 确认，最常遇到的是两类：一是“选对了 skill 但没抓住重点”，二是“记不住该点哪个名字”。四大类 skill（读和学、写和改、审和反馈、项目和汇报）过去两周都用过；Claude Code 和 Cursor 都在用，自然语言和点名两种触发方式都用。

### 这些 skill 是怎么长出来的（git 历史）
| 阶段 | 日期 | 数量 | 来源 |
|---|---|---|---|
| 上游 v1/v2 | 2026-04-19 → 04-22 | 7 | HKUSTDial/Supervisor-Skills，每个 skill 对应 handbook 一章 |
| 上游 v2.1 | 2026-07-03 → 07-16 | 12 | 增加 drawio-reconstruction、paper-polish、paper-writer、deep-research |
| Plus Phase 0–5 | 2026-10-12 → 10-13 | 21 | 挖掘私有档案 `supervisor-skills-msr-tpa`（一篇 FSE 2027 实证 SE 论文的群聊、批注、140 条 checklist，以及 Cursor 里的 se-paper-writing、avoid-ai-writing、journal-adapt），经 notes/01–08 和 DESIGN.md 新增 9 个 |
| 阅读与汇报扩展 | 2026-10-16 → 10-17 | 26 | 审计文档 `docs/handoff/supervisor-skills-audit-2026-10-16.md` 按流程列缺口，每个缺口补成一个新 skill；journal-adapt 并入 style-mine（ADR 0001、0019） |

数量涨得快，是因为每个缺口都变成了一个新 skill，而新旧 skill 之间的边界没有回头收紧。

### 重合点
- 写作骨架有四份：tech-paper-template、benchmark-paper-template、intro-drafter、paper-writer。
- 去 AI 味出现在三处：paper-polish 的“Removing AI tone”、deai-writing、check-loop 第 3 轮。
- pre-submission-reviewer 和 check-loop 互相调用；feedback-to-revision 和 rebuttal-guidance 都走“编号 → 分诊 → 逐条处理”。
- research-supervisor、research-records、lessons-harvest 读写同一批 STATUS 和 ADR 文件。
- vibe-research-workflow 是行为守则，没有可以单独触发的任务。

### 为什么“没抓住重点”
agent 只凭 name 和 description 从全部 skill 里挑一个；agent-sync 里现在有 398 个。选中之后读整份 SKILL.md（150–480 行）。SKILL.md 里没有一张表把“用户这句话”对应到“只做哪一步”，所以一句“改改语气”也会把整套流程走一遍。

### 安装现状
SG 上这 26 个一个都没装。`~/.claude/skills` → `~/.codex/skills` → `~/agent-sync/skills`。agent-sync 的提交 `dbd969c`（2026-10-18）删掉了 12 个指向 `/Users/yitwah/.agents/skills` 的坏链（另一台机器上的上游旧版）；14 个 Plus 新增 skill 从未进过 agent-sync。agent-sync 里另有旧的 journal-adapt、avoid-ai-writing 独立副本。

### 工具限制（2026-10-18 查证）
- Claude Code 的 `/X:Y` 是 plugin 命名空间。Cursor 的 skill 名只允许小写字母、数字、连字符，且必须等于目录名，不支持冒号。
- 每个能被模型自动调用的 skill，name 和 description 每轮都在上下文里。Claude Code 用 frontmatter `disable-model-invocation: true` 让 skill 只能斜杠点名，从而不占这份列表；`user-invocable: false` 则相反（只给模型用，不出现在 `/` 菜单）。Cursor 文档确认支持 `user-invocable: false`，**是否支持 `disable-model-invocation` 未核实**。
- 来源：https://code.claude.com/docs/en/skills.md 、https://www.cursor.com/docs/context/skills 、https://cursor.com/docs/cli/changelog.md

## Options considered
1. **保持 26 个，只改 description**：改动最小，但问题 1、3、5、6 都还在。
2. **Claude Code plugin（`/sv-study:quick-explain`）+ Cursor 连字符名**：Claude Code 里写法最好看。但两个工具里名字不一样，plugin 也不能用 `../` 引用 research-core，需要共享 plugin 或复制文件。owner 否决。
3. **平铺 skill，统一连字符名，每组一个自动触发的总入口，子命令只能斜杠点名**：两个工具里名字完全一致；agent 自动挑选时只看 13 个名字；用户可以精确点名子命令；research-core 照旧共享。
4. **把 26 个合并成 15 个、不设子命令**（本 ADR 初稿）：名字少了，但“没抓住重点”仍要靠 skill 内部的 mode 表兜底，无法精确点名。owner 否决，改为 Option 3。

## Decision
选 **Option 3**。

### 命名
- 一律使用 `sv-` 前缀和连字符：`sv-<组>` 是总入口，`sv-<组>-<子命令>` 是子命令。目录名等于 skill 名，平铺放在 `skills/` 下。
- description 全部用英文，不加中文触发词。现有 paper-quickread、research-bridge、study 三个 skill 的中文 description 改成英文。
- `research-core` 不加前缀，也不对用户暴露。

### 触发
- **总入口**（12 个，加 research-core 共 13 个目录）：允许模型自动调用。正文开头是一张路由表，左列是用户可能怎么说，右列是对应的子命令；动手之前先说一句“按 sv-x-y 处理”，路由错了用户可以当场纠正。
- **子命令**：`disable-model-invocation: true`，只能斜杠点名，不占 agent 的自动挑选列表。
- **research-core**：`disable-model-invocation: true` 加 `user-invocable: false`，只作为其他 skill 按路径读取的文件库。

### 体量
- 总入口的 SKILL.md 不超过 120 行，只放路由表、共享主循环和 hand-off。
- 子命令的 SKILL.md 不超过 100 行，只写这一件事。
- 一组共用的细节放在总入口的 `references/` 里，子命令用 `../sv-<组>/references/<file>.md` 引用，和现在引用 research-core 的方式一样。
- description 不超过 60 词，第一句写唯一的任务。

### 分组与子命令（owner 逐组确认）
| 总入口 | 子命令 | 来源 |
|---|---|---|
| `sv-supervisor` | `-brief` `-init` `-records` `-harvest` | research-supervisor、research-records、lessons-harvest |
| `sv-quickread` | `-card` `-style` | paper-quickread |
| `sv-study` | `-quick-explain` `-paper` `-chapter` `-visual-explain` `-drill` `-bridge` | study、research-bridge |
| `sv-idea` | `-evaluate` `-fatal-flaws` | idea-evaluator |
| `sv-litreview` | `-survey` `-map` | deep-research |
| `sv-proposal` | `-kaiti` `-grant` `-statement` | proposal-writer |
| `sv-experiment` | `-freeze` `-runs` `-numbers` `-replication` | experiment-workflow |
| `sv-write` | 结构：`-skeleton`（technique / benchmark / empirical）`-intro` `-section`<br>修改：`-polish` `-translate` `-critique`<br>humanize：`-humanize-paper` `-humanize-report` `-humanize-slides` `-humanize-letter` `-humanize-audit`<br>风格：`-style-mine` `-style-apply` | paper-writer、intro-drafter、tech-paper-template、benchmark-paper-template、paper-polish、deai-writing、style-mine |
| `sv-figure` | `-design` `-drawio` `-plot` `-tikz` `-html` `-poster` `-explain` | figure-designer、drawio-reconstruction、study 的 `kit/` |
| `sv-review` | `-once` `-loop` | pre-submission-reviewer、check-loop |
| `sv-feedback` | `-revise` `-guidance` `-rebuttal` | feedback-to-revision、rebuttal-guidance |
| `sv-slides` | `-weekly` `-talk` | group-beamer |
| `research-core` | （不直接调用；新增 `references/core/ai-collaboration.md`） | research-core、vibe-research-workflow |

各子命令的含义：
- `sv-write-humanize-*` 按场景去 AI 味：
  - `-paper`：论文。
  - `-report`：周报、进展报告、技术报告。
  - `-slides`：幻灯片文字，沿用 deai-writing 现有的 slides profile。
  - `-letter`：开题和基金申请书、rebuttal 信、给导师的邮件。
  - `-audit`：只报告、不改稿。
- `sv-write-critique` 自己挑毛病，不改稿。`sv-review` 则是投稿前的终审或多轮检查。
- `sv-write-style-mine` 从范文生成 Style Card 和 profile，相当于原 style-mine 的 dissect 和 accumulate；`sv-write-style-apply` 按 profile 改稿。
- `sv-figure` 收纳所有和图有关的工作：
  - `-design`：论文三张核心图的设计建议。
  - `-drawio`：原 drawio-reconstruction，**整套原样保留**，包括 scripts 和 references。
  - `-plot`：用 R 或 Python（matplotlib）画数据图和数学图，图和代码一起保存。
  - `-tikz`：LaTeX TikZ。
  - `-html`：SVG 或 HTML 图，以及 Claude Design 风格的图。
  - `-poster`：海报。
  - `-explain`：学习用的讲解图，原 study 的 `kit/`。
- 讲解图工具包只维护一份，放在 `sv-figure-explain`。`sv-study-visual-explain` 保留名字，作为薄入口转去调用它（owner 选 “both” 的含义：两边都能点到，实现只有一处）。

### 上游
- **不再跟上游 HKUSTDial 的 skill 同步。** 上游 `skills/` 最近一次改动是 2026-09-05；fork 已经在这 12 个 skill 上多加了约 3,700 行（`git diff --shortstat upstream/main -- skills/<name>`）。从本 ADR 起，这些 skill 当作本仓库自己的代码维护。
- `handbook/` 与上游 PhD.Skills 的同步规则不变（CONTRIBUTING.md 第 46 行）。
- 源自上游的文件保留原 frontmatter 里的 `license` 和署名，THIRD_PARTY.md 写明“2026-10-18 起不再同步上游，按 ADR 0021 重组”。CONTRIBUTING.md 里关于上游同步 skill 的说明相应删改。

### 落地
一次全部完成（owner 决定）。仍然每组一个 commit，lint 通过后再做下一组，便于逐组回滚。顺序：
1. sv-write（7 个来源，重合最多）
2. sv-review、sv-feedback
3. sv-supervisor、research-core（含 vibe 守则）
4. sv-figure（含 drawio 原样迁入和 study kit 迁入，更新 ADR 0007–0011 中的路径）
5. sv-study、sv-quickread
6. sv-idea、sv-litreview、sv-proposal、sv-experiment、sv-slides
7. 全局：`scripts/lint_skills.py` 与 `check_checklists.py` 的 skill 名单和新规则（行数上限、子命令必须带 `disable-model-invocation`）、research-core 中 `skill:<name>` 来源前缀、README 和 skills/README、llms.txt、CHANGELOG（附新旧名对照表）、`scripts/install.sh`

## Consequences
- agent 自动挑选时只看 12 个总入口；用户想精确时，可以点名约 50 个子命令中的任意一个。目录总数从 26 增到约 64，但只有 13 个是 agent 每轮都要看到的。
- 每个子命令 SKILL.md 很短，“选对了但没抓住重点”主要靠用户直接点名子命令解决，其次靠总入口的路由表加开头的一句报告。
- 风险：总入口的路由表和子命令之间要保持一致。lint 要检查路由表里出现的每个子命令名都有对应目录，反之亦然。
- 风险：如果 Cursor 不认 `disable-model-invocation`，在 Cursor 里约 50 个子命令都会出现在 agent 的自动挑选列表中。实施第 1 步之前先在 Cursor 里验证；不支持的话再定对策。
- ADR 0004 被部分取代：study 仍是一组，但讲解图工具包移到 sv-figure-explain。ADR 0007–0011 中 `skills/study/kit/` 的路径改为 `skills/sv-figure-explain/kit/`，决策本身不变。
- ADR 0001–0020 作为历史保留旧名，不改写。
- 不留旧名的 pointer stub（同 ADR 0019 的理由）。

## Open questions（实施第 7 步之前要定）
- **安装方式。** 平铺的 `sv-*` 目录要进入 Claude Code 和 Cursor 的 skills 目录，而这个目录就是 `~/agent-sync/skills`。agent-sync 的规则是“live 目录只来自 agent-sync 树”，而 `dbd969c` 的提交说明写的是“由 supervisor-skills-plus 的 installer 按机器建链接”。两条路：
  - (a) 由 `install.sh` 在 `~/agent-sync/skills` 下建链接，并在 agent-sync 的 `.gitignore` 里忽略 `sv-*` 和 `research-core`。
  - (b) agent-sync 提交指向 `~/Projects/supervisor-skills-plus/skills/...` 的相对或固定路径链接。
- **旧副本。** agent-sync 里的 journal-adapt、avoid-ai-writing 独立副本是否删除，由 owner 在 agent-sync 里决定。

## Do not
- 不使用 Claude Code plugin 的冒号命名空间（Option 2，两个工具里名字会不一致）。
- 合并时不改写规则内容，只做移动、拆分和去重；规则取舍另开 ADR。
- 不处理 research-core 偏实证 SE、stats/causal profile 偏薄的问题；那是内容工作，另开 ADR。
- 不在 description 里加中文触发词。

## Sources
`git log`（本仓库、`upstream/main`、`~/agent-sync`）；`notes/02-local-skills-verdicts.md`、`notes/03-archive-map.md`；`docs/handoff/supervisor-skills-audit-2026-10-16.md`；各 `skills/*/SKILL.md` 小节标题；ADR 0001、0004、0007–0011、0019；上面列出的 Claude Code 和 Cursor 文档；owner 在 2026-10-18 讨论中的逐项选择。
