# supervisor-skills-plus「读与学」升级总规格（SPEC）

- 日期：2026-10-16（SGT）
- 仓库：`easygl1der/supervisor-skills-plus`（私有），分支 `main`
- 建议在仓库里的位置：`docs/specs/2026-10-16-reading-upgrade.md`
- 附带的画图套件：`study-kit.tar.gz`（解压后放到 `<repo>/skills/study/kit/`，或由用户告诉你所在路径）
- 读者：Claude Code（执行者）。本文写清**做什么、为什么这样做、哪些已经定了、哪些要你二次调查后自己定**。

---

## 0. 怎么读这份文档

| 章节 | 内容 | 对你的约束 |
|---|---|---|
| §1 | 背景和精神 | 所有判断都按这里的原则来 |
| §2 | 讨论记录：考虑过哪些方案、为什么否掉 | 不要把已否掉的方案又捡回来 |
| §3 | **已敲定的决策** | 照做，不重新讨论 |
| §4–§9 | 每个 skill 的详细设计 | 结构照做，措辞和细节你可以改得更好 |
| §10 | 合并与改名（journal-adapt → style-mine）的文件级清单 | 照做，并用 `rg` 查漏 |
| §11 | 待定问题、二次调查方法、决策协议 | 你自己调研、自己定，写进 ADR |
| §12 | 验收标准和测试计划 | 交付前逐条核对 |
| 附录 | 来源链接 | 引用时用原始仓库，不用二手镜像 |

---

## 1. 背景与精神

### 1.1 背景
main 上现有 21 个 skill，全部围绕「一个论文项目」排布：想 idea → 设计实验 → 跑实验 → 写作 → 画图 → 内部检查 → 投稿 → rebuttal，由 `research-supervisor` 按项目阶段推荐下一步。**缺的是「读」和「学」这一层**：没有单篇论文速读/精读，没有读教材的学习 skill，也没有把学到的东西挂回项目的环节。

用户（Yihua Yue）的研究横跨因果推断（主方向）、统计、SE（FSE 投稿）、AI/ML；常读的教材有 Murphy PML、UDL、刘汉中、丁鹏的书。读论文和学概念的目的是**做研究时真正理解**，不是应试。

### 1.2 精神（所有设计都要服从）
1. **理解优先，不是考试**。study 的核心是「让我把一个概念真正弄懂、建立直觉」，不是刷题、背卡片、打分。
2. **先让用户自己想**。默认给提示不给答案（Bastani et al. 2025 PNAS：不加限制的 AI 辅导让撤掉 AI 后成绩低 17%，只给提示的版本基本消除了负面效应）。但用户时间有限，不能变成苏格拉底式拷问；一次只问一个问题，复述是唯一必经的「让你想」环节。
3. **有动机、有联系、有图**。每个概念必须讲清它解决了之前什么问题、从哪里演化来；挂到用户已经懂的概念上；配生动的图（双重编码）。不能是空中楼阁。
4. **不编造**。数字、公式、引文照抄原文并标出处（§、Table、Fig、Thm、Eq、页码）。原文没有就写「原文未给出」。图上的数字要么有出处，要么标「示意」。自己补的推导步骤标「补」。
5. **输入只走 MinerU**。PDF 一律用 MCP 工具 `mineru_parse_documents_smart` 转成 markdown 和图片（复用 journal-adapt 现有的 Step 2）。失败就大声报错停止，不回退到 pdf-parse / PyMuPDF / pypdf 等。arXiv TeX 源只能作旁证。
6. **跨工具**。skill 要在 Cursor、Claude Code、Codex、Claude.ai 都能用；不依赖某一家的专有功能，必要时分环境写降级方式。
7. **反堆叠（anti-accretion）**。一个缺口只放一个 skill；能并进现有 skill 的就不新建；风格记忆只有一套。文字写成「从来就是这样」的终稿口吻，变更历史只进 `CHANGELOG.md`。
8. **遵守仓库约定**：frontmatter；SKILL.md 结构为 Overview / When to use / When NOT to use / Step 0 加载 research-core / Workflow / Checklist / Outputs / Handoff；来源标 `[src:...]`；general core + per-field profile；checklist 做骨架；progressive disclosure（主文件短，细节放 `references/` 按需读）。
9. **中文默认输出，术语保留英文**；语言跟随用户。
10. **先做后议**：直接提交到 main，用户之后测试、再讨论还要加什么。所以要把「你拿不准、需要用户定」的点清楚列出来，而不是停下来等。

---

## 2. 讨论记录（考虑过、被否掉的方案）

| # | 方案 | 结论 | 理由 |
|---|---|---|---|
| D1 | 新开分支 `feat/reading-skills` + PR | **否** | 用户要直接在 main 上加，测完再迭代 |
| D2 | 把提示词写死成固定内容 | **否** | 让 Claude Code 结合文献、联网调研、对仓库的理解自己设计细节；本 SPEC 定架构和硬规则 |
| D3 | study 拆成 study-paper 和 study-book 两个 skill | **否** | 用户要「一个 study」，自动判断是论文还是教材，分两种模式 |
| D4 | 单独新建 style-mine 与 journal-adapt 并存 | **否** | 两套风格记忆会打架；改成**把 journal-adapt 改名并合并为 style-mine** |
| D5 | 文风拆解做成独立第三个 skill | **否** | 作为 paper-quickread 的 `--style` 选项，产出交给 style-mine |
| D6 | study 以提取练习、间隔重复、Anki、FSRS 复习队列为核心（Dunlosky 2013 思路） | **否（降为可选）** | 用户说「太泛」「不是考试」；要的是研究式理解对话。自测、费曼复述、苏格拉底只做可选开关 |
| D7 | 一上来做一次大摸底测试 | **否** | 改成渐进式：用到某前置概念而档案里没有时，弹一个简短选择题；越用越少 |
| D8 | 诊断只给一个「对了 2/4」 | **改** | 改为按心智模型三层（机制 / 条件 / 边界）给分层比例，加四类标签 |
| D9 | 动画用 Manim | **否** | TheoremExplainAgent（ACL 2025）：完整生成成功率 o3-mini 93.8%、GPT-4o 55%、Claude 3.5 Sonnet 2.1%，成功的也多有元素重叠；Manim 慢。用户明确不要 |
| D10 | 默认用 Mermaid 画图 | **降级** | 用户嫌单调。实测 HTML（SVG + KaTeX）能复刻 TikZ 教科书图（约 0.9 s），浏览器内 elkjs/dagre 自动排版 10 节点约 1 s。Mermaid 不再默认 |
| D11 | Graphviz / TikZ 作为主力 | **否** | Graphviz 只用于很大的图（几十节点）；TikZ 只给要进论文的图 |
| D12 | Excalidraw 模板、D2 sketch、付费/免费 AI 插画作为默认 | **否** | 实测 Excalidraw 模板结构错、emoji 乱码；D2 中英字体不统一；AI 插画文字数字易错 |
| D13 | 学习档案放在 skill 或 research-core 里 | **否** | 放独立私有仓库 `study-vault`，skill 升级不会覆盖个人记录，多环境共享 |
| D14 | 组会汇报 / slides skill（交给 Marp Bot） | **暂不做** | 用户认为 Marp Bot 不合适；以后需要再做，可复用 study 的 HTML 画图套件 |
| D15 | 实验代码 skill | **不做** | experiment-workflow、vibe-research-workflow 已覆盖 |
| D16 | 新建 lit-map 文献地图 skill | **否** | deep-research 已在做分类、对比、找空白，加一个模式即可 |
| D17 | 同时同步到 Notion「因果/LLM 文献精读」由 skill 负责 | **否** | 默认只写 Markdown 到本地目录；Notion 同步由 Grok Bot 每晚做，不进 skill |
| D18 | 引入 claude-paper 的 pdf-parse、PyMuPDF、Nuxt 阅读器、代码 demo、交互 HTML | **否** | 违反 MinerU 规则、依赖太重、ML 偏向，对数学/统计/因果论文无益 |
| D19 | 直接引用 franklee16/academic-research-skills 里的 Awesome-Journal-Skills 拷贝 | **否** | 该仓库无根 LICENSE；引用上游 `brycewang-stanford/Awesome-Journal-Skills`（MIT） |

---

## 3. 已敲定的决策

1. **直接提交到 main**，不开分支、不开 PR；按逻辑分多个 commit。跑仓库现有检查脚本（见 §12）。更新 `skills/README.md`（现在写 11 个，实际 21 个；本次后为 21 − 1 + 4 = 24 个实体 skill，journal-adapt 留 stub 不计入，具体口径你在 README 里写清）和 `CHANGELOG.md`。仓库**没有 AGENTS.md**：先读 `DESIGN.md`、`skills/README.md`、`notes/09-implementation-conventions.md`。
2. **research-supervisor 新增路由类别「读与学」**：与项目阶段无关，没有 `research.yaml` 也能用。触发：用户给了一篇论文 / 一章教材 / 说「我想搞懂 X」。
3. **新增 `paper-quickread`**：单篇、5 分钟、固定 9 节；`--style` 选项产出标准 Style Card 交给 style-mine。
4. **journal-adapt 改名并合并为 `style-mine`**：拆 / 攒 / 用 三环节；原有内容全保留；留 `skills/journal-adapt` stub；全仓库引用改名。
5. **新增 `study`**：一个大 skill，`references/` 下渐进加载子模块；自动判论文/教材；以理解为中心的对话协议；心智模型三层诊断；学习档案在独立仓库 `study-vault`；HTML 画图套件。
6. **deep-research 加「文献地图」模式**：吃 quickread 卡片和 study 笔记，产出演化图和空白点。
7. **新增 `research-bridge`**：把学到的东西挂到当前项目。
8. **新增 `proposal-writer`**：开题、计划书、PhD 研究计划、基金申请。
9. **不做**：组会 slides skill、实验代码 skill。
10. **全局规则**：见 §1.2 第 4、5、7、8、9 条。

---

## 4. paper-quickread

### 4.1 文件树
```
skills/paper-quickread/
  SKILL.md
  THIRD_PARTY.md            # 或并入仓库根 THIRD_PARTY.md（你定，二选一，不要两处都写）
  references/
    template-9.md           # 9 节模板 + 每节篇幅表
    field-method-blocks.md  # 方法节按领域写什么（指向 research-core/references/fields/*）
    style-mode.md           # --style：产出 Style Card 的步骤
  evals/                    # 若仓库有 eval 约定则照约定，否则放 2 个例子
```

### 4.2 SKILL.md 大纲
- frontmatter：name、description（含触发词：速读、quick read、这篇论文讲什么、5 分钟看懂）
- Overview：一页、≤700 字（不含表）、5 分钟读完
- When to use / When NOT to use（要深入理解 → study；要写综述 → deep-research）
- Step 0：加载 research-core 和对应 field profile
- Workflow：
  1. MinerU 转写（失败即停）；有 arXiv TeX 源时可作旁证
  2. **先评估再写**（借 claude-paper）：论文类型（理论 / 方法 / 实证 / 系统 / 综述）、领域 → 决定方法节写法、哪些节可为「不适用」
  3. 按 9 节写；数字照抄并标出处
  4. 自检 checklist
  5. 写盘 + `index.json` **只追加不覆盖**
- Outputs：`<project>/reading/papers/<YYYY-MM-DD>_<firstauthor>_<short-title>/quickread.md`（无项目时写到当前目录的 `reading/`）
- Handoff：要深入 → study；有启发 → research-bridge；`--style` → style-mine

### 4.3 固定 9 节（template-9.md）
| # | 节 | 篇幅 | 要求 |
|---|---|---|---|
| 1 | 元信息 + 一句话总结 + 恰好 2 个标签 | 1 句 + 2 tag | 标签一个问题域、一个方法，不用泛词 |
| 2 | 问题与动机 | 2–3 句 | |
| 3 | 核心想法 | 2–3 句 | |
| 4 | 方法（按领域） | ≤150 字 | causal：识别假设、estimand、估计量；stats：模型、渐近性质、模拟设计；math：定理链、关键引理；SE：RQ、数据、效度威胁；ai-ml：架构、数据、基线 |
| 5 | 结果表 | 1 张表 | 只抄原文数字，每格带出处（§ / Table / Fig）；不估读图中数值 |
| 6 | 贡献 | 3–5 条 | 每条标【证明 / 实证 / 猜想】；借 ecta 的「proved / assumed / cited」区分 |
| 7 | 主张—证据对照 | 1 张表 | 复用 `research-core/assets/templates/claim-ledger.md` 格式；标可疑点 |
| 8 | 局限 | 2 栏 | 「作者承认的」和「我们的判断」分开 |
| 9 | 与我方向的关联 | 2–3 句 | 对当前项目的启发（借 karpathy read-arxiv-paper） |

方法节附加借鉴：
- michaelrizvi `paper`：列出全部假设；区分证明 / 实证 / 猜想；标可疑主张。
- joe-writing-style：假设清单；证明路径按 consistency → rate → distribution。
- jbes-literature-positioning：与 3–6 个现有方法逐个对比「比谁强、强在哪」（放在第 3 或第 7 节，你定）。
- K-Dense scholar-evaluation：主张 ↔ 证据，指出哪条主张缺哪份证据。

### 4.4 `--style` 选项（style-mode.md）
- 只拆一篇论文，产出**一张标准 Style Card**：沿用 `journal-adapt/references/style-card.md` 的 A–L 字段、`exemplar_NNN` 编号、`lit:` 引用键。不另定格式。
- 拆的维度：引言修辞步骤序列（贴 move 标签，参考 SNL-UCSB 的 rhetorical moves 分类 / CARS）、每段功能和过渡、3–5 个抽象成占位符的句型模板（不长段引用原文）、hedging 用法、句长和语域。字段命名参考 claude-scholar `paper-miner`（writing patterns / structure signals / reusable phrasing / venue signals），分节维度参考 paper-alchemist。
- 卡片交给 style-mine 的「攒」环节，作为候选，不直接成为规则。

---

## 5. style-mine（journal-adapt 改名合并）

### 5.1 三个环节
| 环节 | 输入 | 输出 | 规则 |
|---|---|---|---|
| 拆 | 一篇范文（或 quickread `--style` 调用） | Style Card（A–L） | 沿用 style-card.md |
| 攒 | 多张卡片 | 按 venue/field 归档；5–10 篇 + k/n 共识 + 人工确认 → 正式规则 | 沿用 journal-adapt 原有 lifecycle（candidate → confirmed），写入 research-core 需经 lessons-harvest |
| 用 | 目标期刊 | 写稿/改稿时加载规则，逐条对照（原 check-mode） | 沿用 check-mode.md、revision-phase.md |

### 5.2 内容
- journal-adapt 现有全部文件原样搬入 `skills/style-mine/`（base_rules/、check-mode、method-card、profile-output、revision-phase、style-card、style-profile、README）。
- Awesome-Journal-Skills（brycewang-stanford，MIT）中 Econometrica / JoE / JBES 的内容只以 **candidate** 状态进入 `research-core/references/fields/causal.md` 和 `stats.md`，每条标 `[src: guide:AJS/<skill>@<commit>]`，等范文印证后升级。
- stats 核心期刊（JASA / JRSSB / AoS / Biometrika）AJS 没有 → 写明走「5–10 篇范文」路线，不编规则。
- 许可：仓库根是 CC BY-NC-SA 4.0，并入 MIT 内容需保留 MIT 版权声明（THIRD_PARTY.md）。

---

## 6. study（核心）

### 6.1 文件树
```
skills/study/
  SKILL.md                      # 短：触发、模式判断、主流程、子模块索引
  references/
    protocol.md                 # 一个概念一轮的对话协议（§6.3）
    diagnosis.md                # 心智模型三层诊断、四类标签、Chi 层级、纠正方法
    learner-profile.md          # study-vault 的结构、读写规则、渐进式询问
    session-save.md             # 会话落盘、自动 commit/push、各环境降级
    paper-mode.md               # 论文模式：quickread 9 节 + insights/method/qa/reflection
    book-mode.md                # 教材模式：按章推进、概念地图、定理与证明思路、例子反例、习题、progress
    options.md                  # 可选：苏格拉底、费曼复述、轻量自测、只写笔记
    learning-science.md         # 依据：每条原理一行 + 引用 + 在本 skill 的落地规则
    visuals.md                  # = study-kit/references/visuals.md
  kit/                          # = study-kit（templates/、render.sh、render.mjs、vendor/、package.json）
  evals/
```

### 6.2 模式
- 自动判断：有 abstract + references、≤约 60 页 → paper；有目录 / 用户说「第 N 章」/ 讲义 → book；用户只说「我想搞懂 X」→ concept（无材料，靠知识 + 联网 + 档案）。可用 `--mode` 覆盖。
- 先评估：材料类型、难度、前置知识（查 study-vault），决定写哪些文件。

### 6.3 一个概念一轮的协议（protocol.md）
0. **定位**：为什么学它（哪个研究点），档案里已有哪些相关概念；缺前置时走渐进式询问（§6.5）。
1. **大白话原理**：≤2 句，不用术语。
2. **动机与来历**：之前卡在哪个问题、旧方法为什么不行、怎么演化来的（Pólya / 历史发生法）。
3. **简单例子**：最小例子 → 一般化 → 形式定义（concreteness fading）。**找不到贴切的就明说，不硬凑**；判断标准：例子本身还要再解释就不贴切。
4. **连到已知**：2–3 条「它和你懂的 X 相同在哪、不同在哪、类比在哪里失效」（Clement 桥接类比）。
5. **图**：默认 1 张 motivation 图（场景卡片或四格漫画）+ 1 张结构图（DAG / 心智模型），HTML 出图（§6.7）。
6. **你来复述（必经）**：AI 停下，请用户用自己的话讲一遍，并说出联想到什么。除非用户说「只要笔记」。
7. **诊断**（§6.4）。
8. **纠正**：从用户自己的联想出发（Linn 知识整合：用户原想法当素材，不清空）；误解先给反例让用户自己看到问题，再给新理解并说明它为何能解释反例（Posner 概念转变）；重画心智模型图，三色区分「原来就对 / 被纠正 / 新加」。
9. **循环**：用户继续问 → 重复 6–8，直到没有「误解」。
10. **落盘**（§6.6）。

默认给提示不给答案；一次只问一个问题；回复短。

### 6.4 诊断（diagnosis.md）
- 先画**专家心智模型**三层：
  - 核心机制：靠什么起作用（例：IV = 借外生推动撬动处理变量）
  - 成立条件：必须满足的假设（相关性、排他性、独立性）
  - 边界与推论：能回答什么、不能回答什么（LATE、弱工具变量）
- 把用户复述也画成心智模型，对照：哪部分对上、哪条边连错、哪层缺失。
- 输出：**分层比例**（如「机制层对、条件层 2/3、边界层缺」）+ 逐条四类标签：
  - ✅ 核心正确：指出对应原文/定义哪一部分
  - 🟡 部分正确：补条件，用反例说明为何需要
  - ❌ 误解：标 Chi 层级（孤立错误信念 / 心智模型缺陷 / 本体类别错置）；后两类要重建框架，不能只改一句
  - 🔗 缺少联系：补一条桥接边，画进图里
- 「真懂 vs 只记住名词」判定：借 alchaincyf/feynman-skill。换种说法、去掉术语就讲不下去 → 判「名词」；可请用户在一个新情境用一次。
- 示例（写进 diagnosis.md）：用户复述 IV「找个和 X 相关的变量替换 X 回归就没偏了，像 2SLS 第一阶段」→ 逐条判定并从「第一阶段」联想出发重画 DAG（Z→X→Y，U→X，U→Y，加红色虚线 Z→Y 演示违反排他性）。

### 6.5 学习档案（learner-profile.md）
- 位置：**独立私有仓库 `study-vault`**（建议 `easygl1der/study-vault`），不放进 skill、不放进 research-core。skill 通过环境变量或配置（如 `STUDY_VAULT=~/study-vault`）找到它；找不到时降级为当前目录 `reading/` 并提示。
- 结构：
```
study-vault/
  profile/
    knowledge.yaml       # 每个概念一条
    sources.yaml         # 学过的课程/教材/论文，学到哪一章
    misconceptions.md    # 偏过的理解及纠正方式
  concepts/<prefix>-<kebab-name>.md   # def- thm- lem- method- ex-
  sessions/<YYYY-MM-DD>_<concept>.md
  papers/<YYYY-MM-DD>_<author>_<short-title>/
  books/<book-slug>/progress.md, chNN-<slug>/
  index.json             # 只追加
```
- `knowledge.yaml` 每条字段：`concept`、`field`、`proficiency_self`、`proficiency_ai`（四档：没学过 / 学过生疏 / 能用 / 能讲给别人听；两者分开存，不一致时问一句）、`sources`（如「丁鹏 第 3 章」「Murphy PML §5.2」）、`prereqs`、`last_restatement`（日期 + 诊断结论 + 链接）、`notes`。
- **渐进式询问**：讲到某概念时，若其前置在档案里没有记录，弹一个简短选择题（四档）+「照哪本书/课学的」。在有提问控件的环境用控件，否则用文本选项。随档案丰富询问越来越少，只在拿不准时问。不做一次性大摸底。

### 6.6 会话落盘（session-save.md）
每次使用结束时自动：
1. `sessions/日期_概念.md`：结构化摘要（问了什么、怎么讲的、用户复述、诊断、图），不存逐字原文。
2. 更新/追加 `concepts/<prefix>-<name>.md`（同一概念再次出现时追加，不新建）。
3. 更新 `knowledge.yaml`、`misconceptions.md`。
4. `git commit` + `push`；支持后台 agent/subagent 的环境交给后台做，不打断用户。
- 环境降级：Cursor / Claude Code / Codex 直接读写；Claude.ai 不能写文件 → 结尾输出整理好的 Markdown 让用户贴回（读档案可通过 Project knowledge）。
- Grok Bot 可每晚把新会话同步到 Notion —— 不在 skill 里实现，只在文档里注明。

概念笔记模板：frontmatter（concept / aliases / status / related / sources / updated）+ 一句话直觉 / 动机与来历 / 原理 / 图（嵌 PNG）/ 和已知概念的关系表（含类比失效处）/ 复述与诊断记录（按轮）/ 待解决问题。

### 6.7 画图（visuals.md + kit/）
- 默认 **HTML（SVG + KaTeX）**：场景卡片、四格漫画、教科书 DAG、心智模型图、时间线。
- 节点多时浏览器内 elkjs/dagre 自动排版；**Graphviz 只用于很大的图**（几十节点，导出 SVG 再嵌入）；**TikZ 只给论文图**；**不用 Manim**；Mermaid 不默认。
- 每张图都存 `fig-<概念>-<类型>.html` + `.png`，Markdown 里 `![图N：结论句](fig-....png)`。
- 图里数字必须有出处或标「示意」；年份作者凭记忆不写。
- 渲染 → 截图 → 自检循环（render.sh 检查重叠、溢出、KaTeX 错误、JS 错误、未填占位符，退出码 2）→ 能看图的环境必须打开 PNG 看一遍 → 最多 3 轮。
- 统计直觉图：matplotlib（可 xkcd 风）或 Vega-Lite，仅用真实或标明「模拟」的数据。
- 演示过程：默认 **HTML stepper**（6.7.5）；GIF 只是 stepper 的导出物（`render.sh --steps --gif`），仅在需要“会动”的预览时生成。
- vendored：KaTeX、rough.js、elkjs、dagre、visual-explainer 片段 `vendor/ve/`（均 MIT，写进 THIRD_PARTY.md）；**dagitty 是 GPL-2.0，绝不打包**，最多可选在线引用。
- 借 nicobailon/visual-explainer（@69cd739，MIT）：详见 6.7.1–6.7.7。
- 套件来源：`study-kit.tar.gz`（85 个文件，约 1.5 MB，不含 node_modules；首次运行 `npm i` 只装 playwright-core，用系统 Chrome，`CHROME=/path` 可指定）。（2026-10-16 更新：新增 5 个模板、vendor/ve/、render 参数 --full/--figures/--steps/--gif）

### 6.7.1 两种出图粒度
- **单图（默认）**：现有 6 个模板，每次 1–3 张，html+png 嵌笔记。
- **概念讲解页（新，`explainer-page.html`）**：用户说「讲透 X / 出一页讲解」或 study 讲一个核心概念收尾时可选生成。页型固定为：问题（标题写结论句）→ 直觉图（scene-cards 或混杂/机制 SVG）→ 机制（stepper 分步，可选）→ 边界与反例（small multiples 卡片）→ 要记住的 3 条。产物：`concept-<名>.html` + 整页 `concept-<名>.png` + 每个 `<figure>` 单独截图 `concept-<名>-fig<N>.png`（笔记只嵌单图，整页链接 HTML）。

### 6.7.2 图的原则（改编自 visual-explainer "Show, don't tell"，保留其 MIT 声明）
1. 一张图一个论断；`<figcaption>` 以「图 N」开头，写一句结论。
2. 画机制不画名字：每条边写动词（「买得起更多」「医疗更好」），不写空箭头。
3. 首屏即答案：讲概念时首屏可以是「问题 + 框架图」。
4. 状态靠形状/线型+颜色表达，绝不只靠颜色：实线=因果、虚线=被禁止或未观测、红色加粗=本图要你看的路径（如后门路径）、红 ✕=该路径必须不存在（排他性）。
5. 多种情形用 small multiples（同一小图画多遍），不用句子表格。
6. 每个事实先在图里找位置（节点、边动词、尺寸线、编号 callout、图注），找不到才写成句子。
7. 每个数字配图；数字必须有出处或标「示意」。
8. 安静底色、一个信号：约 90% 中性色，强调色 ≤10%，每屏一个焦点。

### 6.7.3 视觉 token（结构图/讲解页用；scene-cards/漫画保留 emoji 与彩色）
- 采用 VE「Paper·light」色板：`--bg #f7f7f4 --surface #fff --border #e3e3dc --border-bright #8e8e8a --text #17191c --text-dim #575c63 --accent #2c4cd0 --ok #1d7443 --warn #836000 --risk #b3301d --info #1b6a94`；只做浅色（截图稳定）。
- 字体离线：正文 `Noto Sans CJK SC`，标题 `Noto Serif CJK SC`，等宽标签 `Noto Sans Mono CJK SC`；不走 Google Fonts CDN。
- 字号 scale：.75/1/1.25/1.625rem + 标题；`html{font-size:17px}`；正文 ≥16px，SVG 标签 ≥12px；间距只用 .25/.5/.75/1/1.5/2/3/4.5rem。
- 舞台：dot-grid 背景 + 1px 边框 + 10px 圆角；节点 rx 6、1.5 描边；关键节点强调色浅底 + 2px 描边；边 1.75，主角边 2.75。
- 禁止：紫/品红 Tailwind 色、霓虹、玻璃拟态、渐变文字或背景、全部居中、圆角卡片加彩色侧条、无顺序含义的 01/02/03。结构图与讲解页不用 emoji（scene-cards/四格漫画例外）。
- 手画 SVG 流程：先 ASCII 草图再定坐标；节点间距 ≥40；SVG 文字不换行，每行 ≤12 个汉字，第二行用 `<tspan dy="1.2em">`；先画边后画节点；>12 节点拆成总览+细节或改 elk 自动布局。
- 无障碍：`<svg role="img" aria-label="…">`；文字对比 ≥4.5:1。

### 6.7.4 交付前检查（追加到 render.sh 自检之后，人/模型逐项看 PNG）
□ 首屏是图+一句结论 □ 每张图有「图 N」结论图注 □ 每条边有动词 □ 颜色之外还有线型/形状区分 □ 数字有出处或「示意」 □ 1100px 宽无横向溢出 □ 中文无豆腐块 □ 讲解页的单图截图齐全。

### 6.7.5 演示过程
默认用 **HTML stepper**（借 VE `diagrams.md` 的 `data-s` 分步 + 每步一句说明，打开时显示全图，不自动播放）；需要嵌进 Markdown 时逐步截图成 `-step1..N.png`，只有用户要动图才合成 GIF。

### 6.7.6 第三方
- 从上游 vendor：Paper token、stepper/callout CSS+JS 片段、Known traps 清单 → `kit/vendor/ve/`，附上游 `LICENSE`（MIT，© 2025 Nico Bailon）与 commit 号，登记到 `THIRD_PARTY.md`。
- **不把 visual-explainer 作为 study 的必装依赖**；README 可推荐另装它做 diff/plan review。

**kit 改动（已在 study-kit 中实现，Claude Code 只需核对）**：
1. 新增 `templates/explainer-page.html`：以 `/workspace/study-visual-demos/ve/coffee-iv.html` 为蓝本，顶部改成数据块 `PAGE = {title, lead, sections:[{h2, figure:{type:'svg'|'cards'|'dag', ...}, caption}], remember:[]}`，设 `window.__READY=true`。
2. `render.mjs` 增加 `--full`（整页截图）与 `--figures`（逐个 `figure` 截 `-figN.png`）。
3. 新增 `templates/stepper.html`（≤6 步，`data-s`，`--steps` 时逐步截图）。
4. `references/visuals.md` §1 表格加两行：「讲透一个概念 → explainer-page」「分步推导 → stepper」；§3 视觉规则替换为 6.7.3。
5. `vendor/ve/LICENSE` + THIRD_PARTY.md 记录。

### 6.7.7 动画/交互场景目录（精简版；全文见 visual-scenarios-catalog-2026-10-16.md，可放 `skills/study/references/visual-scenarios.md`）
图式：P1 结构 stepper · P2 状态机回放（全图常驻、逐步点亮）· P3 推导 stepper · P4 执行追踪（高亮行+数据结构+变量）· P5 数值轨迹（页面 JS 真算）· P6 small multiples · P7 时间线 · P8 概念讲解页 · P9 流动点。

| 场景 | 图式 | 归属 |
|---|---|---|
| 因果概念（混杂、IV、DID、选择偏差） | P8 + P1 / P6 | study |
| git 工作流、算法、数据结构、并发顺序 | P1 / P4 | study |
| 证明与推导（OLS 无偏、CLT、Delta、MLE） | P3 | study（method.md / book-mode） |
| 优化与训练（学习率、训练循环、收敛） | P5 + P6 | study |
| 注意力、前向/反向传播 | P4 变体 + P9 | study |
| 实验管线 | P2 | experiment-workflow / research-bridge |
| 论文修改/投稿/rebuttal、ACA 流程、supervisor 路由 | P2 + P7 | 对应写作 skill / research-supervisor |
| study 协议与 study-vault 落盘循环 | P2 | study（文档自带一张） |
| 论文结构、方法 pipeline、与前人差异 | P1 / P2 / P6 | paper-quickread、deep-research |
| 新方法挂进项目管线 | P6 前后对比 + P2 | research-bridge |
| 方法演变时间线 | P7（年份须核对） | deep-research 文献地图、proposal-writer |

规则：只有“有先后”的内容用 stepper，4–8 步；打开即全图、不自动播放；数值由 JS 真算或标「示意」；笔记嵌最后一帧或 strip。参考 demo：`study-visual-demos/ve2/`（git rebase、梯度下降、OLS 证明、study 循环、二分查找追踪），每个渲染全部产物约 2.5–3.3 s。

### 6.8 论文模式与教材模式
- **paper-mode**：在 quickread 9 节基础上，加 `insights.md`（最重要的 3–5 个洞见：为什么有效、观念转变、取舍）、`method.md`（推导细节，公式照抄，补的步骤标「补」）、`qa.md`（基础/中级/高级各 5 题，`<details>` 折叠；仅作自查，可选）、`reflection.md`（claude-paper 的四个问题：可扩展方向、脆弱假设、可能失败场景、与前人比较）。追问另存 `deep-dive-<topic>.md`，不覆盖。
- **book-mode**：按章推进；每章：概念地图（定义 → 定理 → 例子依赖）、核心定理陈述和证明思路（标节号/页码）、典型例子与反例、习题 3–5 道（提示分级、解答标「自解，待核」）、前后章关联；整本书一份 `progress.md`（进度、遗留疑问）。
- 两种模式里，每个关键概念都走 §6.3 协议。

### 6.9 可选项（options.md，默认关）
苏格拉底全程对话（问题阶梯：澄清 → 假设 → 证据 → 反例）、费曼 explain-back、轻量自测（含信心 1–5 分）、证明重构（关键步留 `TODO(you)`，借 Claude Code Learning 输出风格）、只写笔记（注明低效用）、Anki 导出。间隔复习队列不做默认。

---

## 7. deep-research：文献地图模式
- 在 `skills/deep-research/` 加一个模式（新增 `references/literature-map.md`，SKILL.md 里加入口）。
- 输入：一批 quickread 卡片 + study 笔记（从 `index.json` 读）。
- 输出：按问题 / 方法 / 假设串成的演化图（HTML，复用 study kit 的 auto-dag 模板）、对比表、空白点清单；引用照 deep-research 原有 citation-protocol 核验。

## 8. research-bridge（新）
- 输入：study / quickread 产物 + 当前项目 `research.yaml`。
- 输出：能不能用？怎么用？最小验证实验（数据、指标、预期、失败判据）。
- Handoff：idea 成形 → idea-evaluator；要做实验 → experiment-workflow；决定记录 → research-records（ADR）。
- 没有 research.yaml 时：问一句当前项目是什么，或只给通用启发。

## 9. proposal-writer（新）
- 场景：开题报告、研究计划书、PhD research plan、基金申请。
- 结构：RQ、动机与文献缺口、方法与可行性、时间线与里程碑、预期贡献、风险与备选。
- 复用：deep-research 查相关工作；idea-evaluator 判可行性；paper-writer 的证据门控和引用核查；style-mine 管文体。
- 文体与论文不同，模板放 `references/`；领域差异走 research-core fields。

---

## 10. 合并与改名：文件级改动清单

| 操作 | 文件 |
|---|---|
| git mv | `skills/journal-adapt/{SKILL.md,README.md,references/**}` → `skills/style-mine/` |
| 改写 | `skills/style-mine/SKILL.md`：name、description、三环节结构；加「来自 paper-quickread --style 的卡片」入口 |
| 新建 stub | `skills/journal-adapt/SKILL.md`：一段话「已并入 style-mine」+ 链接；frontmatter 保留以免安装脚本/lint 失败（若 lint 不允许 stub，按 lint 规则调整并在 ADR 记录） |
| 全仓替换引用 | `rg -n "journal-adapt"` 覆盖：`skills/research-supervisor/**`、`skills/research-core/**`、`skills/lessons-harvest/**`、`skills/check-loop/**`、`skills/paper-writer/**`、`skills/deai-writing/**`、`README*.md`、`skills/README*.md`、`DESIGN.md`、`llms.txt`、`notes/**`（notes 属历史记录，你判断是否改；CHANGELOG 历史条目不改）、`scripts/*`（如 check_shared_sync.py 有硬编码名单） |
| 新增 | `skills/paper-quickread/**`、`skills/study/**`（含 kit）、`skills/research-bridge/**`、`skills/proposal-writer/**` |
| 修改 | `skills/deep-research/SKILL.md` + `references/literature-map.md` |
| 修改 | `skills/research-supervisor/SKILL.md`（+ `scripts/session_brief.py` 如需要）：新增「读与学」路由，4 个新 skill 的触发条件 |
| 修改 | `skills/research-core/references/fields/causal.md`、`stats.md`：AJS candidate 规则 + 方法节字段 |
| 修改 | `skills/README.md`、`skills/README.en.md`、`README.md`、`README.en.md`、`llms.txt`、`scripts/install.sh`（若列名单） |
| 新增/修改 | `THIRD_PARTY.md`（claude-paper MIT、AJS MIT、KaTeX/rough.js/elkjs/dagre MIT、visual-explainer 若借原文） |
| 修改 | `CHANGELOG.md`、`PROGRESS.md`（如有约定） |
| 新增 | ADR（放 research-records 约定的位置，或 `docs/adr/`） |

---

## 11. 待定问题、二次调查、决策协议

### 11.1 你需要自己定的问题
1. 仓库 THIRD_PARTY 放根目录还是各 skill 内？
2. stub `journal-adapt` 与 lint / install.sh 的兼容方式。
3. quickread 的 700 字上限是否合理（用真实论文试出来）。
4. study 主 SKILL.md 的长度和子模块切分是否合理（progressive disclosure）。
5. `study-vault` 路径发现机制（环境变量 / 配置文件 / 约定路径）和首次初始化脚本。
6. kit 是否全量放进仓库（vendor 3 MB 字体）还是只放模板 + 首次下载脚本。
7. 各环境里「弹窗选择题」怎么实现（AskUserQuestion 类工具 / 纯文本）。
8. 后台自动 commit/push 在 Claude Code、Cursor、Codex 各自怎么做；失败时如何提示。
9. eval 的格式（仓库若无约定，自己定一个最小格式）。
10. research-supervisor 中「读与学」与现有阶段路由冲突时的优先级。

### 11.2 二次调查方法
1. **完整读原文**（不是摘要）：claude-paper 的 `plugin/skills/summary/SKILL.md` 和 `study/SKILL.md`；michaelrizvi `skills/paper/SKILL.md`；karpathy `read-arxiv-paper`；alchaincyf/feynman-skill；nicobailon/visual-explainer；anthropics claude-for-legal `socratic-drill`；mordor-forge/study-skill；lfnovo/open-cognition；AJS 的 ecta-writing-style、joe-writing-style、jbes-literature-positioning；SNL-UCSB 的 rhetorical moves；claude-scholar paper-miner。记下真正借了什么。
2. **核对引用**：learning-science.md 里每条文献核对作者、年份、期刊、DOI（前期调研只用了标准书目信息，没逐篇核对）；Bastani 2025 PNAS 的 17% / 48% 数字核对原文；TheoremExplainAgent 的成功率核对论文。核不到就删或标「未核」。
3. **联网补充**：搜 2026 年新的学习/读论文/概念讲解类 skill，看有无更好的做法；只吸收能讲清理由的部分。
4. **实测**：
   - 1 篇因果论文（MinerU 转写）→ quickread（含 `--style`）→ study paper 模式至少一个概念完整走一轮（模拟一段用户复述，含一个错误）。
   - 1 章教材，例如 Murphy PML 的一章 → study book 模式（概念地图 + 1 个概念协议 + 习题）。
   - 每张图跑 render.sh 无警告，并打开 PNG 自查。
   - 检查：数字是否都有出处、有没有编造、比例和四类标签是否合理、文件命名和交叉链接是否正确、index.json 是否只追加。

### 11.3 决策协议
- 标准（按优先级）：①不违反 §1.2 精神和 §3 决策 ②用户时间成本低 ③跨工具可用 ④不增加重复 ⑤实测效果。
- 每个 §11.1 问题的决定写成 ADR：背景、选项、决定、理由、何时重审。
- 拿不准且影响用户体验的，**先按你认为最好的做法实现**，并列进最终报告的「待用户讨论」清单，不要停下来等。

---

### 11.x 画图二次调查（visual-explainer 相关）
- 再读上游 `references/diagrams.md` 的 stepper 实现，确认在 headless Chrome 下逐步截图可行；不可行则只保留静态多帧。
- 用 IV、DID、选择偏差三个概念各出一页 explainer，看 3 分钟内能否一次过自检；不能则讲解页降级为可选、不进默认流程。
- 检查 stepper 在 Claude 网页版 artifact 中是否可用；不可用时只给 strip PNG。

## 12. 验收标准与测试计划
- [ ] main 上按逻辑分 commit（建议：①style-mine 改名合并 + 引用更新 ②paper-quickread ③study + kit ④deep-research 文献地图 ⑤research-bridge ⑥proposal-writer ⑦supervisor 路由 + README/CHANGELOG/THIRD_PARTY/ADR）。
- [ ] `python scripts/lint_skills.py`、`scripts/check_sources.py`、`scripts/check_checklists.py`、`scripts/check_shared_sync.py` 全部通过（依赖见 `requirements-lint.txt`）。
- [ ] `rg journal-adapt` 只剩 stub、CHANGELOG 历史条目和你明确保留的 notes。
- [ ] skills/README 计数和列表正确。
- [ ] 每个新 SKILL.md 符合仓库结构约定，有 When NOT to use 和 Handoff。
- [ ] 所有 PDF 输入路径只写 MinerU，有失败即停的明确文字。
- [ ] study 协议里「复述」是必经步骤；默认不给答案；可选项默认关。
- [ ] 6 个 kit 模板渲染无警告；dagitty 未打包。
- [ ] §11.2 的两个实测样例产物保存在 `skills/study/evals/`（或约定位置），可供用户检查。
- [ ] THIRD_PARTY 写全许可声明。
- [ ] 最终报告：做了什么（按 commit）、作出的决定（链接 ADR）、借鉴清单（借自哪里 / 新写哪些）、待用户讨论的问题、未完成项。

---

### 12.x 画图验收补充
- 每个新模板 `render.sh --full --steps` 退出码 0，逐步帧 strip 人工/模型看过。
- `vendor/ve/LICENSE` 与 NOTICE 在位，THIRD_PARTY.md 登记。
- study 文档至少一张 P2 状态机图（概念协议循环）。

## 附录：来源
- 读论文：
  - alaliqing/claude-paper（MIT）https://github.com/alaliqing/claude-paper
  - michaelrizvi paper skill https://github.com/michaelrizvi/claude-config/blob/main/skills/paper/SKILL.md
  - karpathy read-arxiv-paper https://github.com/karpathy/nanochat/blob/master/.claude/skills/read-arxiv-paper/SKILL.md
  - Charles-Donne/Research-Paper-Skills https://github.com/Charles-Donne/Research-Paper-Skills
  - K-Dense-AI/scientific-agent-skills（scholar-evaluation）https://github.com/K-Dense-AI/scientific-agent-skills
- 文风：
  - Wang-Ruibin/paper-alchemist https://github.com/Wang-Ruibin/paper-alchemist
  - Galaxy-Dawn/claude-scholar（paper-miner）https://github.com/Galaxy-Dawn/claude-scholar
  - SNL-UCSB/paper-writing-skill https://github.com/SNL-UCSB/paper-writing-skill
  - brycewang-stanford/Awesome-Journal-Skills（MIT）https://github.com/brycewang-stanford/Awesome-Journal-Skills
    - ecta-writing-style https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Econometrica-Skills/skills/ecta-writing-style/SKILL.md
    - joe-writing-style https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Journal-of-Econometrics-Skills/skills/joe-writing-style/SKILL.md
    - jbes-literature-positioning https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Journal-of-Business-and-Economic-Statistics-Skills/skills/jbes-literature-positioning/SKILL.md
- 学习与讲解：
  - alchaincyf/feynman-skill https://github.com/alchaincyf/feynman-skill
  - mordor-forge/study-skill https://github.com/mordor-forge/study-skill
  - lfnovo/open-cognition https://github.com/lfnovo/open-cognition
  - anthropics claude-for-legal socratic-drill https://github.com/anthropics/claude-for-legal/blob/main/law-student/skills/socratic-drill/SKILL.md
  - Claude Code output styles https://code.claude.com/docs/en/output-styles
  - Google LearnLM https://arxiv.org/abs/2412.16429
  - Bastani et al. 2025 PNAS https://www.pnas.org/doi/10.1073/pnas.2422633122
  - 理论（待核）：Dunlosky 2013；Chi 1989/1994 与误解层级；Posner 1982；Linn 知识整合；Clement 1993；Fyfe 2014 concreteness fading；Paivio / Mayer 双重编码；Thurston 1994；Sweller 认知负荷
- 画图：
  - nicobailon/visual-explainer（MIT）https://github.com/nicobailon/visual-explainer
  - TheoremExplainAgent https://github.com/TIGER-AI-Lab/TheoremExplainAgent
  - Code2Video https://github.com/showlab/Code2Video
  - KaTeX https://github.com/KaTeX/KaTeX · rough.js https://github.com/rough-stuff/rough · elkjs https://github.com/kieler/elkjs · dagre https://github.com/dagrejs/dagre · dagitty（GPL，勿打包）https://github.com/jtextor/dagitty
- 前期调研报告（box 上，用户可一并提供）：paper-quickread-skill-scan、claude-paper-deepdive、journal-skills-scan、study-skill-learning-science、study-understanding-design、study-visuals(v2)、study-html-visuals、huashu-study-skills、supervisor-skills-audit（均 2026-10-16）。
