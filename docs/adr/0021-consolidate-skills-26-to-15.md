# ADR 0021: 把 26 个 skill 收紧为 15 个，统一 `sv-` 前缀命名

Status: proposed
Date: 2026-10-18
Deciders: owner（待审），Claude Code（方案起草）

## Context

### 用户反馈的问题（owner，2026-10-18）
1. skill 太多（26 个）。
2. 单个 skill 内容太多。
3. 名字难以辨认。
4. 内容太多，导致交互时给的提示词没有被准确匹配到用户想要的那部分。
5. 单个 skill 范围太宽，例如 `study` 同时管学习和画图。
6. 很多 skill 内容重合。

### 这些 skill 是怎么长出来的（git 历史）
| 阶段 | 日期 | 数量 | 来源 |
|---|---|---|---|
| 上游 v1/v2 | 2026-04-19 → 04-22 | 7 | HKUSTDial/Supervisor-Skills，每个 skill 对应 handbook 一章（2.2 想 idea、3.x 论文模板、4 作图、5 vibe research） |
| 上游 v2.1 | 2026-07-03 → 07-16 | 12 | 增加 drawio-reconstruction、paper-polish、paper-writer、deep-research |
| Plus Phase 0–5 | 2026-10-12 → 10-13 | 21 | 挖掘私有档案 `supervisor-skills-msr-tpa`（一篇 FSE 2027 实证 SE 论文的群聊、Hao 的批注、140 条 checklist v2，以及 Cursor 里的 se-paper-writing、avoid-ai-writing、journal-adapt 等 skill），经 notes/01–08 和 DESIGN.md 新增 research-core、research-supervisor、research-records、experiment-workflow、feedback-to-revision、deai-writing、check-loop、journal-adapt、lessons-harvest |
| 阅读与汇报扩展 | 2026-10-16 → 10-17 | 26 | `docs/handoff/supervisor-skills-audit-2026-10-16.md` 按流程列缺口，逐个补成新 skill：paper-quickread、study、research-bridge、proposal-writer、group-beamer；journal-adapt 并入 style-mine（ADR 0001、0019） |

一周内从 12 涨到 26（上游起点是 7 个），每个“缺口”都变成一个新 skill。审计文档自己写了“反堆叠：每个缺口只引入一个 skill”，但新 skill 与已有 skill 的边界没有回头收紧。上游那 12 个本来按 handbook 章节切分，切的是读者的章节，不是 agent 的任务。

### 重合点（读 SKILL.md 小节标题得出）
- **写作骨架四份**：tech-paper-template、benchmark-paper-template（自带“Introduction six-part flowchart”）、intro-drafter（六段式 Intro）、paper-writer。前三个的 hand-off 互相指来指去。
- **去 AI 味三处**：paper-polish 有“Removing AI tone”小节，deai-writing 专做这件事，check-loop 第 3 轮再跑一次 de-AI。
- **审稿两套**：pre-submission-reviewer（五维一次性）与 check-loop（多轮），后者的 hand-off 又指回前者。
- **意见处理两套**：feedback-to-revision（导师/合作者意见编号、一条一改）与 rebuttal-guidance（审稿意见策略），流程相同，只是来源不同。
- **项目记录三套**：research-supervisor（入口、阶段判断）、research-records（STATUS/ADR/日志）、lessons-harvest（把记录沉淀成规则），读写同一批文件。
- **行为守则不是任务**：vibe-research-workflow 是人机协作守则，没有可以单独触发的任务，更像 research-core 的一章。
- **study 混了两件事**：37k 行里绝大部分是 `kit/`（vendored 字体、elkjs、模板、渲染检查），与学习协议无关。drawio-reconstruction 又是另一套画图工具（48k 行）。
- **research-bridge** 是 study / quickread 之后的“这对我的项目意味着什么”，单独存在时用户需要知道第三个名字。

### 其他事实
- 本机 `~/.claude/skills`、`~/.codex/skills`、`~/.cursor/skills` 里**没有**指向本仓库的链接；`~/.claude/skills` 里反而有旧的独立副本 `journal-adapt`、`avoid-ai-writing`、`paper-writer`。Claude Code 会话里列出的 skill 超过 300 个，本库的名字在里面无法辨认，还与 `anthropic-skills:deep-research`、`agent-skills:review`、`paper` 等撞名。
- 上游 `skills/` 最近一次改动是 2026-09-05（rebuttal-guidance），之前是 2026-07-16。fork 已经给这 12 个上游 skill 加了约 3,700 行（`git diff --shortstat upstream/main -- skills/<name>`），上游同步早已需要手工合并。
- 许多规则的 `[src: arc:msr:...]` 来自同一篇实证 SE 论文，而 owner 的主方向是统计/因果。这是内容问题，不在本 ADR 范围内（见 Do not）。

## Options considered
1. **保持 26 个，只改 description 和路由**：改动最小，上游同步不变。但问题 1、2、5、6 都不解决，用户仍需记 26 个名字。
2. **保留所有目录，加一层薄 router skill**：用户只记几个入口。但总数变成 26 加 router，agent 的 skill 列表更长，重合内容仍在两处维护。
3. **按任务合并为 15 个，旧 skill 变为新 skill 的 mode 或 references 文件，统一前缀**：直接解决 1、3、5、6；配合 SKILL.md 上限解决 2、4。代价是与上游目录结构分叉，需要一张映射表来手工移植上游改动。
4. **更激进地合并到 8–10 个**（例如 polish、review、feedback 合成一个 revise）：名字更少，但单个 skill 又会变宽，正是问题 5。

## Decision
选 **Option 3**。

### 26 → 15 映射
| 新名字 | 合并来源 | 旧 skill 变成什么 |
|---|---|---|
| `sv-supervisor` | research-supervisor + research-records + lessons-harvest | modes：`brief`（阶段判断、阻塞项、路由）、`records`（STATUS/TODO/ADR/日志）、`harvest`（沉淀规则） |
| `research-core` | research-core + vibe-research-workflow | 不对用户直接触发的共享库；vibe 守则变为 `references/core/ai-collaboration.md` |
| `sv-idea` | idea-evaluator | 改名 |
| `sv-litreview` | deep-research | 改名（避免与 anthropic-skills:deep-research 撞名）；literature-map 仍是一个 mode |
| `sv-quickread` | paper-quickread | 改名；结尾可选 `bridge` 步骤，引用 sv-study 的 bridge 文件 |
| `sv-study` | study + research-bridge | 学习协议不变；bridge 变为 `references/bridge.md` 和 `bridge` mode；**`kit/` 移出到 sv-figure** |
| `sv-proposal` | proposal-writer | 改名 |
| `sv-experiment` | experiment-workflow | 改名 |
| `sv-write` | paper-writer + intro-drafter + tech-paper-template + benchmark-paper-template | modes：`skeleton`（technique / new-problem / benchmark 三张骨架表）、`intro`、`draft`；三个模板变为 `references/skeleton-*.md` |
| `sv-figure` | figure-designer + drawio-reconstruction + study 的 `kit/` | modes：`design`（三张核心图的设计建议）、`drawio`（参考图重建）、`explain`（学习用讲解图，原 study kit） |
| `sv-polish` | paper-polish + deai-writing | 一次润色依次做语言 pass 和 de-AI pass；deai 的只报告模式保留为 `audit` mode；去掉 paper-polish 里重复的 AI 味小节 |
| `sv-style` | style-mine | 改名；dissect / accumulate / apply 三个 mode 不变 |
| `sv-review` | pre-submission-reviewer + check-loop | modes：`once`（五维一次性终审）、`loop`（有轮数上限的多轮检查，调用 sv-style apply 和 sv-polish audit） |
| `sv-feedback` | feedback-to-revision + rebuttal-guidance | 共用“编号 → 分诊 → 一条一改 → diff 核实”；modes：`revise`（导师/合作者意见）、`guidance`（专家建议记录）、`rebuttal`（审稿意见策略） |
| `sv-slides` | group-beamer | 改名；周报 / paper talk 两个 mode 不变 |

数量核对：3+2+1+1+1+2+1+1+4+2+2+1+2+2+1 = 26（study 的 `kit/` 是目录，不计为 skill）。

### 命名规则
- 用户可触发的 skill 一律 `sv-` 前缀加一个任务名词。300 多个 skill 的列表里输入 `sv-` 就能列出全家；也避开现有撞名。
- `research-core` 不加前缀，description 写明“由其他 sv- skill 加载，不直接调用”。
- 每个 description 先用一句话写唯一的任务，然后列出中英文触发词（例如 sv-slides 写“组会、周报、汇报、beamer、group meeting”）。现在只有 paper-quickread、research-bridge、study 三个 description 含中文。

### 体量规则（针对问题 2、4）
- SKILL.md 不超过 150 行：触发条件、mode 表、主循环、hand-off。细节一律放进 `references/`，按 mode 加载。
- 每个 skill 开头必须有一张 **mode 表**（mode、用户可能怎么说、加载哪些 references）。skill 开始工作时先说一句“按 X mode 处理”，让用户一眼看出意图有没有被抓对，抓错可以当场纠正。
- description 不超过 60 词（现有 lint 规则是 40–80 词，改为 30–60）。

### 上游同步的取舍
- 上游 12 个 skill 不再保持原目录名。新增 `docs/upstream-map.md`，逐文件列出 `upstream skills/<old>/<file>` → `skills/<new>/<file>`。上游以后改动时，用 `git diff <last-synced> upstream/main -- skills/` 加这张表手工移植。
- 理由：上游近三个月只改过 rebuttal-guidance，fork 已经在这 12 个 skill 上多出约 3,700 行，原样同步本来就做不到。
- `handbook/` 与上游 PhD.Skills 的同步规则不变（CONTRIBUTING.md 第 46 行）。
- 合并后的 SKILL.md 保留上游 frontmatter 里的 `license` 和署名，THIRD_PARTY.md 补上“合并于本 ADR”的说明。

## Consequences
- 用户要记的名字从 26 个降到 14 个（research-core 不需要记），且都以 `sv-` 开头。
- 需要同步修改的地方：`sv-supervisor` 的路由表、`skills/README*.md`、根 README 和 llms.txt、`scripts/lint_skills.py` 与 `check_checklists.py` 里的 skill 名与 PLANNED 集合、research-core 里所有 `skill:<name>` 来源前缀、各 skill 的 hand-off、evals 路径、CHANGELOG（附新旧名对照表）。
- ADR 0004（study 单 skill）部分被取代：study 仍是单 skill，但 `kit/` 移到 sv-figure。ADR 0007–0011 里的 `skills/study/kit/` 路径改为 `skills/sv-figure/kit/`，决策本身不变。
- ADR 0001–0020 作为历史保留旧名，不改写。
- 旧安装链接会失效：`scripts/install.sh` 需要清理指向本仓库、但目标已不存在的链接。`~/.claude/skills` 里旧的独立副本（journal-adapt、avoid-ai-writing、paper-writer）不由本仓库管理，由 owner 决定是否删除。
- 合并后单个 skill 的 references 会变多。要盯住 mode 表是否真的能让 agent 只加载需要的文件。

### 实施顺序（每步一个 commit，lint 通过后再做下一步）
1. sv-polish（paper-polish + deai-writing）：重合最明显，风险最小。
2. sv-write（四合一）。
3. sv-review（reviewer + check-loop）。
4. sv-feedback（feedback + rebuttal）。
5. sv-supervisor 和 research-core（含 vibe 守则）。
6. sv-study 和 sv-figure（移 kit，改 ADR 0007–0011 路径）：文件最多，放最后。
7. 其余纯改名（idea、litreview、quickread、proposal、experiment、style、slides），更新 install.sh、README、llms.txt、CHANGELOG。

## Do not
- 不保留旧名的 pointer stub（沿用 ADR 0019 的理由：stub 只会让 skill 列表更长）。
- 不在合并时改写规则内容。合并只移动和去重；规则的取舍另开 ADR。
- 不处理 research-core 里实证 SE 偏重、stats/causal profile 偏薄的问题；那是内容工作，另开 ADR。
- 不把 sv-polish、sv-review、sv-feedback 再合成一个 skill（Option 4，会重新造成问题 5）。

## Sources
`git log`（本仓库与 `upstream/main`）；`notes/02-local-skills-verdicts.md`、`notes/03-archive-map.md`；`docs/handoff/supervisor-skills-audit-2026-10-16.md`；各 `skills/*/SKILL.md` 的小节标题；ADR 0001、0004、0007–0011、0019；owner 反馈 2026-10-18。
