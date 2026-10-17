# 计划：统计四大刊因果风格监测 + 刘汉中作者风格挖掘

> 状态：草案（M0） · 日期：2026-10-17（Asia/Singapore）  
> 仓库：`easygl1der/supervisor-skills-plus`（本仓）  
> 配套会话提示：同目录 `2026-10-17-causal-style-mining-and-monitor-CLAUDE.md`  
> **本任务不改写任何 skill 实现**；本文件只定计划，供后续 Claude Code 单会话执行。

## 0. 给打开本仓的 Claude：一句话意图

我们要建一条**可重复的进货与晋升管线**：定时（或半自动）发现 JASA / JRSSB / AoS / Biometrika 上与因果推断相关的新文；每篇走 MinerU → `paper-quickread --style` → 风格卡入库到私有 `causal-style-vault`；用现有 `style-mine`（拆 / 攒 / 用）攒期刊与领域档案；另从 `easygl1der/hanzhong-liu-research`（汉中流 / 刘组工作区）收齐刘汉中已发表范文，挖**作者档**（与期刊档分开）。规则晋升进 `research-core` **必须经主人确认**；禁止每日自动改 core。

**进货/监测的具体数据源尚未敲定（TBD）**——对话里曾误听成 Apify，**不要把 Apify 写成必选或默认实现**。实现监测前先读主人澄清；在此之前可先用人工 DOI/TOC 列表把「转写 → 卡 → vault」跑通。读完本计划 + 同目录 CLAUDE 提示即可理解意图；细节（过滤器措辞、目录微调、是否新建 vault 仓）留给会话内自主决定，但硬约束不可破。

---

## 1. 目标

1. **学怎么发统计四大刊的因果文**：弄清这些刊接受的因果/识别类文章在结构、语气、贡献编号、证据措辞、图表与附录习惯上的可迁移修辞模式（不是抄发现、不是改写结论）。
2. **学刘汉中老师的写作习惯**：开题/综述/论文里「问题先行、贡献编号、证据语气」等可迁移句式，形成独立的 **author profile**，投稿时可与 venue profile 叠用。
3. **喂给 `style-mine`**：稳定进货 → 卡片 → 达阈值后 accumulate → `candidate` 规则 → `lessons-harvest` → 主人批准后才进 `research-core`。
4. **可审计的记忆**：历史看过哪些文、拆过哪些卡、每周摘要、changelog；方便每天/每周小步更新「对因果写作风格的理解」，而不是一次性挖完。

非目标（明确不做）：

- 把论文发现或数字写进 skill 正文。
- 每日自动 merge 进 `research-core`。
- 用云端 agent 无审批判批量改正式规则。
- 在本仓堆 PDF / 全文 transcript / 每日流水（这些进 vault 或刘组仓，不进 skill 仓）。
- **绑定某一家爬虫/API 厂商**（含曾误提的 Apify）作为唯一进货方式。

---

## 2. 必要性：做什么 vs 不做什么

| 值得做 | 不值得做 |
| --- | --- |
| 四大刊因果相关新文的**监测入库**（源 TBD） | 历史四大刊全库一次挖完（成本高、信噪比差） |
| 每篇：MinerU → quickread → `--style` 卡 | 只靠摘要或标题「猜风格」 |
| 满 5–10 篇同刊因果文且 **k/n 过线** 才 accumulate | 单卡直接写成 venue 规则 |
| 刘老师**作者档**与期刊档分开 | 把个人语体和期刊体裁搅在一起 |
| 私有 `causal-style-vault` 存卡与 changelog | 把 PDF、卡片、监测日志塞进 supervisor-skills-plus |
| 晋升前给人看 diff、人点头 | 定时任务自动改 `research-core` |
| 每周监测摘要（新文、已拆卡、离晋升差几篇） | 每天强制改 skill 或刷屏通知 |
| 进货层可插拔（人工列表 / 学术 API / 日后指定工具） | 把计划写成「必须用某某爬虫」 |

**原则**：卡片是证据，不是规则；规则要支持计数；core 只经 `lessons-harvest` + 主人批准。

---

## 3. 架构（三层）

```
[进货 Intake · 源 TBD]           [记忆 Vault]                         [消费 Skills]
可插拔发现层（待主人澄清）         causal-style-vault (private)         supervisor-skills-plus
  · 四大刊新文 / TOC / DOI           venues/jasa|jrssb|aos|biometrika/     style-mine (dissect/accumulate/apply)
  · 因果过滤                         authors/hanzhong-liu/                paper-quickread --style
MinerU 转写                          field/causal/                        lessons-harvest
paper-quickread --style              cards/ + profiles/ + changelog/      research-core (仅主人批准后)
                                     monitor/logs/
刘组仓 hanzhong-liu-research ──► authors/hanzhong-liu/ exemplars
```

- **Supervisor-skills-plus**：只保留**消费侧** skill（`style-mine`、`paper-quickread`、路由等）。不在本仓建监测数据库。
- **causal-style-vault**（拟新建私有仓，或暂用本机目录 + 后迁仓）：唯一风格记忆与监测日志。
- **hanzhong-liu-research**：作者范文与组内论文索引的**来源**（已存在：`easygl1der/hanzhong-liu-research`），不把版权受限全文推到公开 fork。
- **Intake**：接口形状先定（`monitor/queue.yaml` 字段），**具体抓取工具名留空 / TBD**，避免错误绑定。

---

## 4. style-mine 已支持什么；缺口是什么

### 已有（以 `skills/style-mine/SKILL.md` 为准）

| 循环 | 输入 | 输出 |
| --- | --- | --- |
| **Dissect（拆）** | 一篇范文，或 `paper-quickread --style` 的卡 | Paper Style Card（字段 A–L） |
| **Accumulate（攒）** | 同 venue / field 多张卡 | Style Profile；5–10 篇且 k/n 过线 → `candidate` 规则行 |
| **Apply（用）** | 目标刊 + 手稿 | 动态写作 skill / 分段改稿 / check-loop 报告 |

硬规矩已有：**永不增加事实**、**永不改技术内容**、**永不改写语料论文的发现**（只描述结构与修辞）、无卡不成规则、core 只经 harvest + 主人批准。

当前 accumulate 目标主要是 **venue** 与 **field** profile。

### 缺口（本计划要补的「产品」侧；实现细节会话内自主）

1. **Author profile 类型**：与 venue/field 并列的第三种档案（例：`authors/hanzhong-liu/`），叠用规则：venue 管体裁与刊规，author 管论证习惯与中文/双语语体。
2. **Monitor pipeline**：发现（TBD）→ 队列 → MinerU → quickread+style → vault。
3. **Vault 仓与目录约定**（见下节）。
4. **与刘组仓的衔接**：从 `papers/`、`publications.json`、`catalog.json`、`s2-author.json` 等列出刘老师范文，再 dissect。

---

## 5. 外部风格类 skill 调研：借什么 vs 留给会话决定

> 目的：避免重复造轮子，也避免把外部「整包刊规」未经范文印证就写进 core。下列为 **borrow / leave** 指引；具体改哪些文件、抄哪些检查项，由执行会话对照上游 LICENSE 与本仓 THIRD_PARTY 自行决定。

### 5.1 本仓已有（优先延伸，不另起炉灶）

| 来源 | 已提供 | 对本计划 |
| --- | --- | --- |
| **style-mine**（由 journal-adapt 合并） | 拆/攒/用、A–L 卡、venue/field profile、k/n、不改事实 | **主消费端**；作者档应挂在此，而不是新 skill |
| **paper-quickread `--style`** | 读文时顺带出卡 | 监测管线的默认 dissect 入口 |
| **lessons-harvest** | 进 research-core 的闸门 | 晋升唯一路径 |
| **research-core** `fields/causal.md`、`stats.md` | 已有部分 **candidate**（含 AJS 溯源） | 只追加经印证的规则；不覆盖重写 |
| **deai-writing / paper-polish / check-loop** | 去 AI 味、润色、合稿检查 | Apply 阶段可调用；不负责「挖刊风」 |

### 5.2 上游 / GitHub 可参考（MIT 或需核 LICENSE）

| 来源 | 可借（Borrow） | 勿整包搬 / 留给会话决定（Leave） |
| --- | --- | --- |
| **brycewang-stanford/Awesome-Journal-Skills**（MIT） | Econometrica / JoE / JBES 等包里的**检查维度**（贡献分级、文献定位、识别策略表述习惯）→ 仅作 **candidate** 灵感，须范文 k/n 印证；已有约定见 reading-upgrade SPEC | 不要把 AER/QJE/管理世界等整包当统计四大刊规则；不要把 Stata/实证经济学流程 skill 并进 style-mine；是否拉取某一子 skill 的条文，会话内按需 `rg`/打开上游再决定 |
| **AJS：ecta-writing-style** | 「proved / assumed / cited」式贡献语气区分 → 已映射到 quickread 贡献标签思路 | 是否把更多 ecta 句式表升格进 causal field，等四大刊范文卡够数再议 |
| **AJS：joe-writing-style / jbes-literature-positioning** | 文献定位、与 3–6 个既有方法对照的结构提示 | 统计四大刊（JASA 等）**没有**现成 AJS pack → 必须走 exemplar 路线，不能假装有刊包 |
| **franklee16 等二次拷贝的 AJS** | 无 | **不要引用**无根 LICENSE 的拷贝仓；只用 brycewang 上游（SPEC D19） |
| **通用 academic-writing skills**（如 jamditis 等） | CRediT、预注册、OA/披露 LLM 等**流程检查清单**可启发 proposal-writer / pre-submission，与「刊风挖掘」正交 | 不并入 style-mine；会话若要借用，写到对应 skill 的 candidate 笔记，不写进 venue profile |
| **「用范文训个人文风 digital twin」类教程** | 与我们「5–10 篇 + 人确认」同构；可借鉴「样本要像自己」的选篇标准（刘老师线） | 不要做成营销文风 skill；不要无审批判自动覆盖 profile |
| **SNL-UCSB rhetorical moves / claude-scholar paper-miner 等**（若会话检索到） | 修辞动作标签、主张—证据切分的命名 | 是否引入新标签体系：仅当现有 A–L 卡不够用时再扩展；扩展前写一页 ADR 草案 |

### 5.3 统计四大刊的现实缺口

JASA、JRSSB、AoS、Biometrika **没有**像 AJS 那样可直接安装的成熟 pack。因此：

- **Borrow**：AJS 经济计量刊的「维度列表」当检查提纲；
- **Must build**：本计划的监测 + vault + exemplar accumulate；
- **Leave to session**：具体关键词表、TOC 解析脚本、要不要 Graphviz 文献地图，执行时自定。

### 5.4 自主权边界（给 Claude）

**可以自己定**：queue 字段微调、digest 模板、刘老师清单排序、先做哪一刊、是否先人工 DOI 跑通 M1、调研时打开哪些上游文件、candidate 条文的措辞。

**不可自作主张**：进货绑定某一爬虫品牌；自动写入 research-core；改写语料发现；把作者档与 venue 档合并；从本计划删除「人确认」闸门；把 Apify（或任何未澄清工具）写成必选。

---

## 6. 管线步骤（期刊因果文）

1. **发现（源 TBD）**：待主人澄清监测工具后，写入 `monitor/README.md`。在此之前用**人工维护的 DOI/TOC 列表**或已有学术检索结果填 `monitor/queue.yaml`。过滤：causal、IV、RDD、DID/SDID、matching、potential outcomes、identification 等（细则写在 vault `monitor/filters.md`，可迭代）。
2. **去重入库队**：doi、标题、刊名、日期、来源 URL、状态（new / fetched / transcribed / carded / skipped）。
3. **MinerU**：仅用既有 MinerU 路径转写；失败则停并记日志（与 `research-core` inputs-mineru 一致）。
4. **paper-quickread --style**：产出九段快读 + `style-card.md`；快读可进阅读目录，**风格卡必须进 vault** 对应 `venues/<slug>/cards/`。
5. **周报**：`monitor/digests/YYYY-Www.md`：新文列表、已拆卡数、各刊距 5–10 篇还差几篇、跳过原因。
6. **Accumulate**：同刊因果卡达到 **5–10** 且模式满足 **k/n** → 生成/更新 Style Profile + `candidate` 规则（仍不进 core）。
7. **人确认**：展示 diff；主人批准后走 `lessons-harvest` → `research-core` venues/fields。

**进货层约定**

- 接口稳定、工具可替换；密钥不进 git。
- 若发现路径需机构权限或付费全文：只记录元数据与公开 preprint/作者主页链路；不绕过付费墙。
- **v1**：先手动/半自动跑通「1 篇 → 卡 → vault」；自动化监测等源澄清后再接。

---

## 7. 刘汉中作者线

1. **定位仓库**：`git clone git@github.com:easygl1der/hanzhong-liu-research.git`（私有；汉中流 / 刘组研究工作区）。本机若已有则 `git pull`。
2. **收齐范文清单**（只修辞学习，不外发版权全文）：
   - `papers/publications.json`、`papers/catalog.json`、`papers/s2-author.json`、`papers/papers.md`
   - `papers/by-author/`（若有刘老师本人条目则优先）
   - `group/` 介绍与已有笔记中的发表列表
   - 公开主页 / Google Scholar / S2 交叉核对（记入 vault `authors/hanzhong-liu/SOURCE.md`）
3. **Exemplar 集**：在 vault 建 `authors/hanzhong-liu/exemplars.md`（bib 级元数据 + 本地 transcript 路径指针）；PDF 留在刘组仓或本机学习副本，**不**推到 supervisor-skills-plus。
4. **Dissect**：逐篇 `style-mine` dissect（或 quickread `--style` 后转入 author 卡目录 `authors/hanzhong-liu/cards/`）。
5. **Accumulate（author）**：达阈值后出 **author profile**（候选）；与 JASA 等 venue profile **分开文件**；Apply 时可「venue + author」叠用。
6. **中文开题/综述**：若范文含中文计划书/综述，卡片标注 `register: zh-academic`，与英刊卡片分栏，避免把中文语体规则误写入英文 venue。

---

## 8. 节奏（Cadence）

| 频率 | 做什么 | 不做什么 |
| --- | --- | --- |
| **每日（可选）** | 从队列取 **1** 篇：转写 → quickread+style → 更新 vault changelog | 不改 research-core；不强求每日有新文 |
| **每周** | 跑一轮监测（工具 TBD）或更新人工 DOI 列表；写 digest；更新各刊卡计数 | 未达阈值不 accumulate |
| **达阈值时** | accumulate → 给人看 candidate diff | 无人确认不晋升 |
| **晋升后** | lessons-harvest → 更新 core venue/field；changelog 记一笔 | 不 force-push；不开无关 PR |

时区：**Asia/Singapore（UTC+8）**。

---

## 9. Routines（仅提案，本阶段不创建）

以下形状供日后 Academic Bot 创建；**本文档不创建任何 routine**。监测工具名留空。

| 提案名 | 建议 cron（SGT） | 动作草案 |
| --- | --- | --- |
| `causal-top4-monitor-weekly` | 周日 10:00 | 跑监测（源 TBD）→ 更新 queue → 写周报 |
| `causal-style-queue-daily` | 工作日 21:00 | 若队列非空，处理 1 篇；否则跳过 |
| `causal-style-promote-nudge` | 当某刊 cards ≥ 5 时人工触发或周检 | 提醒主人审 candidate，**不**自动 merge |

标注：**to be created later by Academic Bot**。

---

## 10. Cloud agent

- **可选、非 v1 必需**。
- 适用：批量 dissect 已入库、已转写的 exemplars。
- 不适用：无人值守改 `research-core`；上传版权 PDF 到不可控环境；代替未澄清的进货源乱爬。
- 若启用：只写 vault 的 cards/profiles/candidate，晋升仍走人工。

---

## 11. 成功指标、风险、未决问题

### 成功指标

- `monitor/README.md` 写清进货接口；**源字段标明 TBD 或已澄清工具名**。
- Vault 目录就位；至少 **1** 刊有 ≥3 张真实 style card（来自真实论文，非虚构）。
- 刘老师线：exemplars 清单 ≥5 篇元数据齐全，其中 ≥2 篇已 dissect。
- 第一次达阈值的 accumulate 产出可读的 candidate diff，且主人能拒绝/批准。
- 零次「自动写入 research-core」。
- 外部 AJS 等只以 candidate/灵感出现，并带 `[src: ...]`。

### 风险

| 风险 | 缓解 |
| --- | --- |
| **版权** | 不把 PDF/全文推进公开仓；卡片与规则**只写修辞与结构**；遵守刘组仓 README |
| **许可** | skill 仓 MIT；外部 skill 条文核 LICENSE 后记录 SOURCE/THIRD_PARTY |
| **误伤技术内容** | 沿用 style-mine 硬规矩 |
| **进货工具误绑** | 源 TBD 直至主人澄清；不写死某一厂商 |
| **作者档污染期刊档** | 目录与 profile 类型强制分离 |
| **skill 名膨胀** | 监测不做成新 skill；逻辑在 vault + 现有 style-mine / quickread |

### 未决问题（Open questions）

1. **监测/进货的具体工具与数据源是什么？**（最高优先；曾误听，待主人澄清）
2. `causal-style-vault` 新建独立私有仓，还是先放在 `hanzhong-liu-research` 子树再迁出？
3. 因果过滤：规则关键词 vs 分类器 vs 人工初筛，v1 选哪档？
4. Author profile 的 schema：复用 venue 的 A–L 子集，还是另加「论证节奏 / 中文贡献编号」字段？
5. 周报投递渠道：邮件 / Slack / 仅写 vault？
6. 是否与 Social Monitor / Notion 文献精读打通，还是严格分离？

---

## 12. 分阶段里程碑（M0–M3）

### M0 — 计划落地（本提交）

- [x] 本计划写入 `docs/plans/2026-10-17-causal-style-mining-and-monitor.md`
- [x] Claude 会话提示 `docs/plans/2026-10-17-causal-style-mining-and-monitor-CLAUDE.md`
- [x] CHANGELOG / handoff 指针
- [x] 外部风格 skill 调研节（§5）
- [ ] **不**改 skill 代码（本阶段约束）
- [ ] 进货源：**TBD**（等主人澄清后再开 M1 自动化部分）

### M1 — Vault + 进货骨架

- 创建 `causal-style-vault`（或暂定路径）目录：`venues/`、`authors/hanzhong-liu/`、`field/causal/`、`monitor/`、`changelog/`
- `monitor/README.md`：队列契约；进货源写 TBD 或已澄清名称
- 克隆/定位 `hanzhong-liu-research`，写出刘老师 exemplars 初稿清单
- 端到端手动跑 **1** 篇四大刊因果文：MinerU → quickread `--style` → 卡入 vault（可用人工 DOI）

### M2 — 作者档 + 达阈值前的批量

- 刘老师 ≥2 篇 dissect；author cards 目录就位
- 至少一刊 cards 接近 5；周报格式固定
- 提案 author profile 输出格式（仍 `candidate`）
- Routines：**仍不创建**，只把 cron 提案抄进 vault `monitor/ROUTINES.proposed.md`

### M3 — 首次晋升演练

- 一刊或 field/causal 达 5–10 + k/n → accumulate
- 主人审 diff → lessons-harvest →（若批准）写入 research-core
- 回顾指标；决定是否让 Academic Bot 创建 weekly routine；是否启用 cloud agent 做批量 dissect；进货源若已澄清再接自动监测

---

## 13. 建议的 vault 目录草图

```
causal-style-vault/
  README.md
  SOURCE.md
  changelog/
  monitor/
    README.md            # 进货契约；source: TBD | <name>
    filters.md
    queue.yaml
    raw/                 # 原始抓取（可 gitignore）；工具未定前可空
    digests/
    ROUTINES.proposed.md # to be created later by Academic Bot
  venues/
    jasa/cards/ ...
    jrssb/cards/
    aos/cards/
    biometrika/cards/
    <slug>/profile.md
  field/
    causal/cards/
    causal/profile.md
  authors/
    hanzhong-liu/
      SOURCE.md
      exemplars.md
      cards/
      profile.md
```

---

## 14. 相关已有能力（执行时先读）

- `skills/style-mine/`（拆攒用、硬规矩、与 quickread 卡衔接）
- `skills/paper-quickread/`（九段 + `--style`）
- `skills/lessons-harvest/`（唯一进 core 的闸门）
- `skills/research-core/` venues & fields（晋升目标，只读直至批准）
- `docs/handoff/supervisor-plus-reading-upgrade-SPEC.md`（读与学总 SPEC；含 AJS 引用约定）
- `docs/handoff/journal-skills-scan-2026-10-16.md`（若存在，期刊 skill 扫描）
- 私有仓 `easygl1der/hanzhong-liu-research`（刘组范文来源）
- MinerU 相关工具（转写）
- 进货工具：**TBD**（勿默认 Apify）

---

## 15. 变更记录

| 日期 | 变更 |
| --- | --- |
| 2026-10-17 | 初稿：架构、vault、刘组仓作者线、节奏、M0–M3、Claude 会话提示 |
| 2026-10-17 | 进货源改为 **TBD**（纠正误听 Apify）；新增 §5 外部风格 skill 调研（borrow vs leave） |
