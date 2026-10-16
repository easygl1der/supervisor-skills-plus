# Awesome-Journal-Skills 调研（2026-10-16）

来源：franklee16/academic-research-skills 中的 [Awesome-Journal-Skills-main/](https://github.com/franklee16/academic-research-skills/tree/master/Awesome-Journal-Skills-main)。这是 [brycewang-stanford/Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) 的一份 vendored 快照（Stanford REAP × CoPaper.AI 维护）。

## 1. 真实规模与结构
- 顶层目录共 321 个，其中真正含 SKILL.md 的只有 **119 个**。另外 **202 个是只有一份 README（约 100–170 词）的占位/跳转目录**（例如 `Econometrica/`、`Ruan-Kexue/`）。
- SKILL.md 共 **1833 个**，与 README 宣称的约 1600 大体相符。分布：
  - 4 个"广度包"占了 461 个：Computer-Science-Conference（156 个会议）、Chinese-SocialScience（103）、English-SocialScience（101）、English-NaturalScience（101）。这些包是"每个期刊/会议 1 个 skill"。
  - 其余约 115 个"深度包"，每包 11–14 个 skill。
- **深度包结构**（Econometrica-Skills / Journal-of-Econometrics-Skills / JBES-Skills 三包已通读）：
  - 每包约 12 个 skill：workflow（路由）、topic-selection、literature-positioning、identification(-strategy)/theory-model、data-analysis 或 robustness、writing-style、tables-figures、replication(-and-data-policy)、submission（含 templates/checklist.md 和 manuscript_template.md）、review-process/referee-strategy、rebuttal。
  - 另有 resources/official-source-map.md（官网链接锚点）、external_tools.md、.claude-plugin/plugin.json（可直接作为 Claude Code 插件安装）、LICENSE（MIT）、中英 README。
  - 单个 skill 的写法：When to trigger → 规范清单 → Anti-patterns → 固定输出格式（【Estimand】【Assumptions】……）。
  - 内容是三样东西的混合：风格规则、结构模板、审稿人视角检查清单。
- **质量判断**：
  - 深度包较好。以 joe-identification-strategy 为例，它要求区分 primitive 与 high-level 条件，给出 ULLN→rate→CLT→方差估计 的证明路径，处理 Neyman-orthogonality 和弱识别，内容专业、可操作。
  - Econometrica 包约 1.2 万词，PROGRESS 记录称已核对投稿费、页数限制、编辑、Data Editor 等事实（v0.2.0）。
  - 广度包是按 `_build-spec.md` 模板批量生成的 10 段式"选刊/改投/desk-reject"卡片。ICSE 那张卡约 1100 词，偏通用，适合选刊，不适合写作细节。
  - 期刊事实（费用、编辑、页数）随年份变化，各 skill 也都声明"以官网为准"。

## 2. 期刊清单（与你相关的部分）
完整目录见仓库（大量中文经管期刊，如经济研究、管理世界、中国工业经济、数量经济技术经济研究等，以及会计、金融、管理、社会学、医学、Nature/Cell 系）。

| 方向 | 有 | 没有 |
|---|---|---|
| 统计 | JBES（深度包）、Review of Economics & Statistics（广度卡）、AISTATS（深度包）、JMLR（广度卡） | **JASA、JRSSB、Annals of Statistics、Biometrika、Biometrics、Stat Med 全部没有** |
| 因果/计量 | Econometrica、Journal of Econometrics、REStud、Econometric Theory、Journal of Applied Econometrics、The Econometrics Journal、Quantitative Economics、JBES（以上均为深度包）；另有 AER/QJE/JPE 等 | — |
| SE | ICSE、FSE、ISSTA、ASE、ESEM、MSR、ICSME、SANER（广度卡，在 CS-Conference 包内） | TOSEM、TSE（没有期刊卡） |
| AI/ML | NeurIPS、ICML、ICLR、AAAI、IJCAI、AISTATS（深度包）；TPAMI、Nature MI（广度卡） | — |
| 数学 | Annals of Mathematics（深度包）；Inventiones、JAMS（广度卡）；Mathematical Finance（深度包） | 概率/统计数学类期刊 |

## 3. 能否填 supervisor-skills-plus 的 stats / causal profile
现状：`skills/research-core/references/fields/causal.md` 和 `stats.md` 都是 stub（v0.1，2026-10-13），全部为 Unknown。

journal-adapt 规定：
- 规则必须来自 5–10 篇范文，满足 k/n 共识阈值，并带 `[src: lit:…]` 标注；
- 写入 research-core 必须经过 lessons-harvest 审核；
- 禁止凭空发明规则。

因此，AJS 的内容**不能直接作为 evidenced 规则灌进 profile**。它属于"published guide"类来源，按 journal-adapt 的 lifecycle 只能以 `candidate` 状态进入；或者等范文语料印证后再升为 `confirmed`。

**判断**：
- **causal**：可以较好地填充。计量深度包恰好覆盖 profile 模板的各个标题。
- **stats**：只能部分填充（JBES、AISTATS）。JASA/JRSSB/AoS/Biometrika 缺失，仍需走 `lessons-harvest --new-field stats` 加范文的路径。

**映射方案**（只作建议，尚未改动任何仓库）：

| AJS 来源 | → supervisor-skills-plus 目标 |
|---|---|
| joe-/ecta-identification-strategy、jbes-identification-strategy | fields/causal.md「Rigor and threats」「What reviewers care about」 |
| joe-/jbes-data-analysis（Monte Carlo 的 size/power 设计）、ecta-robustness | fields/stats.md「Rigor and threats」、checklists 新增条目（Status: candidate） |
| *-writing-style、*-contribution-framing | 两个 profile 的「Tone and phrasing」「Typical structure」，以及 journal-adapt 的 references/base_rules/economics.md（作为 P4 静态基规则） |
| *-tables-figures | 两个 profile 的「Figures and tables」 |
| *-replication-and-data-policy、submission/templates/checklist.md | checklists/venue-submission，新建 venues/econometrica.md、venues/joe.md、venues/jbes.md（套 venues/_template.md） |
| *-review-process、*-rebuttal | feedback-to-revision / check-loop 的参考资料 |
| NeurIPS/ICML/ICLR/AISTATS 深度包 | fields/ai-ml.md 的补充来源，以及 venues/ |
| CS-Conference 包中的 ICSE/FSE 卡 | 与已有的 venues/fse.md 对比，补充选刊信息 |

另外，franklee16 仓库的 `data-analysis/econometric-research-writing/references/`（iv-causal-methods.md、rdd-matching-methods.md、panel-methods.md、method-selection.md）在方法层面更贴近 causal profile，可作为第二来源。它的许可证未单独核实。

**操作流程建议**：
1. 对每条规则写 `[src: guide:AJS/<skill>@<commit>]`，状态设为 candidate；
2. 经 lessons-harvest 在 `learn/ajs` 分支提交 diff；
3. 再用 journal-adapt 的 Profile 模式拿 5–10 篇 JoE/Econometrica 范文去印证并升级状态。

**许可证兼容性**：
- AJS 是 MIT（Copyright 2026 Bryce Wang），各深度包也各带 MIT LICENSE。
- supervisor-skills-plus 根目录是 CC BY-NC-SA 4.0（journal-adapt 自身标 MIT）。
- 把 MIT 内容并入 CC BY-NC-SA 项目是允许的，只需保留 MIT 版权声明（例如放 NOTICE 或 THIRD_PARTY.md）。
- 反方向（把本仓库内容回馈给上游 MIT 项目）则不行。
- franklee16 仓库根目录**没有 LICENSE**，它是多个来源的合集，应以上游 brycewang-stanford 仓库和子目录自带的许可证为准。建议直接从上游引用。

## 4. 许可证、活跃度、Star（2026-10-16 查询）
- [franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)：223★，34 fork。创建于 2026-04-19，最后推送 2026-09-18 20:12 SGT。无根 LICENSE。共 8 个 commit（浅克隆计数）。
- 上游 [brycewang-stanford/Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills)：1262★，161 fork，MIT。最后推送 2026-09-27 16:08 SGT，比 franklee16 的快照更新。
