# 调查附录：因果风格监测进货、外部 skill、刘组语料（2026-10-17）

> **Outcome 2026-10-17:** the recommended stack (Crossref + OpenAlex, Semantic Scholar optional) was adopted as skill-local API calls in `skills/style-mine/scripts/intake_search.py`, not through academic-mcp. The evidence below is unchanged.

> 附属 `2026-10-17-causal-style-mining-and-monitor.md`。本文件只记调查证据与建议，不改 skill、不建 vault、不创建 routine、不晋升 `research-core`。  
> 调查日：2026-10-17。环境：supervisor-skills-plus Cloud Agent；GitHub MCP 可读 `easygl1der/hanzhong-liu-research`（private）。

## 1. 结论先行

1. **进货不要用 Apify（或任何通用爬虫）做默认。** 四大刊都有 Crossref ISSN 与 OpenAlex source；DOI 级监测用元数据 API 即可。Apify 没有独特收益，且碰到付费墙 / ToS。
2. **推荐默认栈（v1）**：**Crossref polite pool 做刊级新文发现** + **OpenAlex 补摘要/概念/OA 链接** + **人工关键词初筛** + 队列。RSS 仅作 JASA 的低延迟旁路。
3. **academic-mcp 不宜当四大刊 TOC 主源**（live discovery 本会话失败；工具描述以 dblp 为主，统计刊覆盖弱）。作者消歧 / 单篇详情可作辅路，前提是 MCP 恢复。
4. **刘老师范文不要手编列表。** 权威清单是刘组仓 `papers/publications.json`（`updated: 2026-08-28`，38 条）。`catalog.json` 不是刘 CV。远程 Git 不含 PDF（gitignore）。
5. **style-mine 已覆盖拆/攒/用。** 外部 journal skill 只借检查维度与 author+venue 叠用思路；统计四大刊仍无现成 pack。

---

## 2. 进货源排序（四大刊因果新文）

ISSN（本会话 Crossref `/journals?query=` 核实）：

| slug | 刊 | print / electronic ISSN | 出版商 | OpenAlex source（`/sources/issn:{eISSN}`） |
| --- | --- | --- | --- | --- |
| jasa | JASA | 0162-1459 / **1537-274X** | Informa UK (ASA) | `S4394736638` |
| jrssb | JRSS-B Statistical Methodology | 1369-7412 / **1467-9868** | OUP | `S145009937` |
| aos | Annals of Statistics | 0090-5364 / **2168-8966** | IMS | `S119757635` |
| biometrika | Biometrika | 0006-3444 / **1464-3510** | OUP | `S172180718` |

注意：Crossref 另有历史刊名 *JRSS-B (Methodological)*（ISSN 0035-9246）与 *Annals of Applied Statistics*、*Annals of Mathematical Statistics*。过滤器必须钉 **上表 eISSN**，避免 AoAS / 旧系列污染。

### 2.1 排名

| 秩 | 源 | 角色 | 本会话证据 | 适合 v1？ |
| ---: | --- | --- | --- | --- |
| **1** | **Crossref REST** `filter=issn:{ISSN},from-pub-date:,type:journal-article` | **刊级发现主源** | polite `mailto=` 后 JASA `query.title=causal` 自 2026-01-01 返回 total=10（例：10.1080/01621459.2025.2585561 *Causal Inference in Pharmaceutical Statistics*）。无密钥。429 出现在未带 mailto、连续打 `/journals` 之后。 | **是。默认。** |
| **2** | **OpenAlex** `works?filter=primary_location.source.issn:…` + `search=` | **补全**：摘要、concepts、`open_access.oa_status` / `oa_url`、作者 OpenAlex id | JASA 1537-274X + 2025-01-01 + `causal OR identification OR "treatment effect"` → **count=132**，前几条大量假阳性（激素替代、空间图模型、Deep Transformation）。hybrid 的 `oa_url` 常是 T&F `needAccess=true`，**不是合法全文**。green 才可能指向 arXiv pdf。 | **是。enrichment，不作唯一过滤器。** |
| **3** | **期刊 RSS** | 低延迟「刚上线」 | **JASA** `https://www.tandfonline.com/feed/rss/uasa20` → **200 `application/xml`**（RSS 1.0 RDF）。OUP JRSSB/Biometrika 猜测路径 404；`/biometrika/advance-articles/feed` **403 Cloudflare**。Project Euclid / imstat.org 返回 bot HTML。Hyndman 2015 OPML 已过时，只作线索。 | **仅 JASA 旁路。** 不要把 OUP/IMS RSS 写成必选。 |
| **4** | **Unpaywall / Crossref license + 作者主页 / arXiv** | DOI 已知后找 **合法 OA** | OpenAlex 已带 oa 字段；付费墙 PDF 禁止绕过。MinerU 只吃已有合法副本或 OA。 | **是。在 queue 的 `oa_url` 字段。** |
| **5** | **Semantic Scholar Graph** | 刘老师作者线辅核（已有 `authorId` 48447276） | 刘组 `s2-author.json`：`paperCount` **27**，而 `publications.json` **38** 条。PROFILE 写明 S2 年表不完整、year 常是 arXiv 年。公开 Graph 现多需 key。 | **作者消歧辅路，不作刊 TOC。** |
| **6** | **academic-mcp** | 已有 MCP：`academic_search`、`author_search`（OpenAlex+dblp）、`paper_detail` | 本会话 namespace **error**（live tool discovery 失败）。`academic_search` 描述以 **dblp / SPARQL** 为先；dblp 对 JASA/AoS/Biometrika **覆盖差**。 | **MCP 修好后作单篇 enrich / 刘老师 OpenAlex 消歧；不当四大刊监测主环。** |
| **7** | **arXiv `stat.ME` / `stat.TH` new** | 预印本雷达 | 高召回、低精度「是否已是四大刊」；可与 Crossref DOI 日后对齐。 | **可选第二队列，不与 venue cards 混计数。** |
| **8** | **人工 DOI/TOC** | 证明管线 | 计划原文已定：M1 先手动 1 篇。 | **M1 必做。** |
| **—** | **Apify / 通用 HTML 爬刊站** | 无 | 元数据 API 已覆盖发现；爬 T&F/OUP/Project Euclid 易踩 ToS 与付费墙。 | **不采用，除非主人书面指定且只抓公开 landing 元数据。** |

### 2.2 建议的 queue 契约（仍不实现）

`monitor/queue.yaml` 每条建议字段：

- `doi`（主键）、`title`、`venue_slug`、`issn`、`issued`
- `source`: `crossref` | `openalex` | `rss:jasa` | `manual`
- `oa_status`、`oa_url`（仅 green/预印本/作者主页；T&F `needAccess=true` 记 `paywall`）
- `filter`: `keyword_hit` | `human_keep` | `human_skip` + `skip_reason`
- `status`: `new | fetched | transcribed | carded | skipped`
- **不存** PDF 字节、不存全文。

**因果过滤（建议 v1 = 关键词 + 人筛，不要分类器）**

- 标题/摘要关键词（可放 vault `monitor/filters.md`）：`causal`, `treatment effect`, `potential outcome`, `identif`, `instrument`, `regression discontinuity`, `difference-in-difference`, `matching`, `propensity`, `randomiz`, `rerandom`, `covariate adjustment`, `interference`, `instrumental variable`, `IV`, `RDD`, `DID`。
- **本会话反例**：OpenAlex 宽检索 132 条里混入非风格目标文；Crossref `query.title=causal` 更严（JASA 2026 起 10 条）但会漏「只在摘要写 identification」的文。
- v1：**机器打标 + 每周人看 skip/keep**。不要上分类器，除非误报让人筛不可承受。

**礼貌与密钥**

- Crossref：每个请求带 `mailto=`；429 则退避。不要无 mailto 连打。
- OpenAlex：可匿名；有 `mailto` 更稳。
- 密钥不进 git。无需 Apify token。

**合法全文**

- 只记录元数据与公开 preprint / 作者主页。
- MinerU 路径与 `research-core` `inputs-mineru.md` 一致；失败停。
- 不把 PDF 推进 supervisor-skills-plus。

---

## 3. 外部风格 / 期刊 skill：借什么

对照本仓已有 `style-mine`（A–L 卡、k/n、永不改事实）与 `docs/handoff/journal-skills-scan-2026-10-16.md`、`paper-quickread-skill-scan-2026-10-16.md`、`notes/10-reading-sources.md`。本轮 GitHub 代码搜索补了几条新候选。

### 3.1 继续借（与 10-16 扫描一致）

| 来源 | LICENSE | 借 | 不借 |
| --- | --- | --- | --- |
| **brycewang-stanford/Awesome-Journal-Skills** | MIT | Econometrica / JoE / JBES **检查维度**（贡献语气、文献定位、识别策略表述）→ candidate，须范文 k/n | 整包当 JASA/JRSSB/AoS/Biometrika 规则；franklee16 无根 LICENSE 拷贝 |
| **WantongC/journal-adapt-writing-skill** | （本仓 style-mine 上游） | 已是主实现；不要再装一份平行 skill | 在本仓再 vendor 一遍 |
| **Galaxy-Dawn/claude-scholar paper-miner** | MIT | focus 模式、`Source status: full/partial/abstract`、Use-when 条目 | pypdf；全局 phrase bank；单文件 writing memory |
| **SNL-UCSB/paper-writing-skill** | MIT | 修辞 move 标签（已部分进 `--style` / CARS） | 把系统会贡献句式当统计刊规 |
| **Wang-Ruibin/paper-alchemist** | MIT | 分节 8×8 网格、无 phrase bank、按源数量标置信 | 再装 CLI；中英 70/30 生成 |

### 3.2 本轮新看到、建议借思路

| 来源 | LICENSE | 借 | 不借 |
| --- | --- | --- | --- |
| **RTCartist/paper-suite `venue-adapt`** | 未在本会话读根 LICENSE；技能正文引用 WantongC | **user/lab exemplar 与 venue overlay 分层**；1–2 篇只算 calibration 不算刊规；动态 skill 8–15 条须有 k/n | PyMuPDF/PyPDF2 抽取；把配色/PPT 层并进 causal vault；引用语料原文当 evidence（违反本仓「不引语料」） |
| **ShaishavMaisuria/research-paper-lifecycle-skills `match-style` / `paper-profile`** | 未核 | **author voice vs venue register 冲突表**写进本地 `.paper-memory`（对应我们 vault 里 author ≠ venue） | 把 memory 上传；在本仓建第二套 profile.yml |
| **fuhaoda/stats-paper-writing-agent-skills `stat-writing`** | **CC0** | Apply/check 阶段可参考：摘要句数、关键词、notation/repro 启发式、response-letter 骨架。期刊无关 + 可选 JDS profile | **不能替代**四大刊 exemplar 挖掘；不要把 JDS 检查项写成 JASA 规则 |

### 3.3 明确不并进 style-mine

- 通用 academic-writing / CRediT / 预注册清单 → proposal-writer / pre-submission。
- 数字孪生营销文风教程。
- 任何「无范文、整包刊规」。
- 统计四大刊：AJS **没有** JASA/JRSSB/AoS/Biometrika pack（10-16 扫描仍成立）。

### 3.4 对本仓 style-mine 的产品缺口（仍只记计划）

现有 accumulate 目标是 venue / field；`style-card.md` 的 corpus role 已有 `user_exemplar`，**没有一等公民 author profile 文件类型**。计划中的 `authors/hanzhong-liu/profile.md` 应：

- 复用 A–L + k/n；
- 另加：`register`（`en-stats` / `zh-academic`）、贡献编号习惯、与 venue 冲突时的 overlay 顺序（venue 体裁 > author 语体，冲突进表不覆盖）；
- 未发表组内稿用 `proj:` 键，不进共享 venue 规则。

扩展标签体系前先写 ADR；默认 **不改 A–L**。

---

## 4. 刘汉中语料：如何找（不另编论文表）

### 4.1 仓库

- **存在且可访问**：`easygl1der/hanzhong-liu-research`（private，`visibility: private`，本会话 GitHub MCP `permissions.pull: true`）。
- 描述：刘汉中组研究笔记与方向（从 `thu-stat-ds/faculty/hanzhong-liu` 迁出）。`clone`: `git@github.com:easygl1der/hanzhong-liu-research.git`。
- 默认分支 `main`；口试包在分支 `interview`，不在科研线根目录。
- 本机：若已有则 `git pull`；Cloud 环境不要为挖风格去克隆 600MB+ 含本地 PDF 的工作树——**元数据已在 git 里**。

### 4.2 以哪个文件为准

| 路径 | 是什么 | 能否当刘老师范文全集 |
| --- | --- | --- |
| **`papers/publications.json`** | 权威结构化书目。`author: Hanzhong Liu`，`updated: 2026-08-28`，`canonical_cv` 系站。`items` **38** 条。 | **是。** 挖 author 档从这里 filter，不要手打。 |
| **`papers/papers.md`** | 同一书目的可读年表（条目 38；本地 PDF 30；LaTeX transcript 30；待 MinerU 8） | 人读；机器用 json |
| **`papers/s2-author.json`** | S2 `authorId` **48447276**，`paperCount` 27，匹配文 *Lasso adjustments…* | **否。** 不完整 |
| **`papers/catalog.json`** | `updated: 2026-09-13`，仅 **6** 条背景（Jiang–Ding AoS、Lin–Ding、丁鹏书、Rosenbaum、Li–Wager） | **否。不是刘 CV** |
| **`papers/papers.json`** | 另一份索引（未在本会话当权威） | 先以 publications.json 为准 |
| **`group/PROFILE.md`** | 消歧、主页、方向、刷新命令 | 流程；不是篇目 |
| **`papers/by-author/liu-hanzhong/`** | `papers/README.md` 写「刘瀚中一作」 | **远程 GitHub 目录列表只有 `ding-peng/` 与 `jiang-zhichao/`**。PDF/e-print/src **gitignore**。夹可能只在主人本机 |

公开核对（PROFILE，勿当第二全集）：

- 系站中文 CV https://www.stat.tsinghua.edu.cn/info/1023/2414.htm （PROFILE：2026-08-28 仍把部分 2024 稿写成 under review）
- Scholar `user=7c0w76MAAAAJ`
- S2 https://www.semanticscholar.org/author/48447276
- arXiv `au:"Hanzhong Liu"`；**排除** `2510.10196`（宫颈病理，同名）

PROFILE 记载刷新脚本 `python3 scripts/enrich_hanzhong_liu.py` 与 `fetch_liu_transcripts.py`。**本会话在该仓 GitHub tree 未找到这些文件**（code search 0）。不要假设 Cloud 上能跑它们。

### 4.3 从 json 筛 author 范文（步骤，不是新编清单）

在克隆或 `gh api` 读到 `publications.json` 后：

1. 读 `items[]`。
2. **Author 档（修辞）优先**：`status == published`（或 in press），且刘老师为一作 / 通讯（姓名含 `Hanzhong Liu*` 或作者[0] 为 Hanzhong Liu）。预印本/在投可进第二盘，**不与四大刊 venue 卡混计数**。
3. **与监测线重叠的「老师已中四大刊」**：`venue` ∈ {`JASA`,`JRSS-B`,`JRSSB`,`Biometrika`,`AoS`,`Annals of Statistics`} 且 `status=published`。
4. 中文综述/计划：`venue` 或 title 含 `in Chinese` → 卡上 `register: zh-academic`。
5. transcript：有 `arxiv` 则优先刘组仓已有 **arXiv LaTeX**（`transcript_kind: arxiv-latex`）；`needs-mineru` 且无合法 PDF 则跳过并记日志。
6. 把 **bib 级字段 + 本地指针** 写入 vault `authors/hanzhong-liu/exemplars.md`；**不要**把 publications.json 全文拷进本 skill 仓。

**本会话对 publications.json 的 filter 结果（SHA `a9aaaeb`，updated 2026-08-28）——这是仓库里的条目，不是新编：**

四大刊 `published`：

| year | venue | title（json 原题） | arxiv |
| ---: | --- | --- | --- |
| 2026 | JRSS-B | Causal inference under uniformly bounded neighbourhood interference | 2408.17205 |
| 2025 | JASA | Tyranny-of-the-minority regression adjustment in randomized experiments | 2210.00261 |
| 2024 | JASA | Randomization-based joint central limit theorem and efficient covariate adjustment in randomized block 2^K factorial experiments | 2103.04050 |
| 2023 | JASA | Rerandomization in stratified randomized experiments | 2011.05195 |
| 2023 | Biometrika | Design-based theory for cluster rerandomization | 2207.02540 |
| 2023 | Biometrika | Lasso-adjusted treatment effect estimation under covariate-adaptive randomization | 2011.09734 |
| 2020 | Biometrika | Regression-adjusted average treatment effect estimates in stratified randomized experiments | 1908.01628 |

**AoS：该快照 0 篇。** 不要把 `catalog.json` 里 Jiang–Ding 的 AoS 算进刘老师 author 档。

其它高频刊（JBES、Biometrics、Statistics in Medicine、PNAS 等）可作 author 语体、**不可**当作 JASA/JRSSB/AoS/Biometrika venue 卡。

中文 register 候选（同一 json）：`Design-based theory for causal inference (in Chinese)` arXiv `2511.22518`（preprint）。

### 4.4 版权

刘组 README / gitignore：PDF、e-print、解开的 `src/`、MinerU 树默认不入库。卡片只写结构与修辞。STYLE 卡与规则不进公开 fork 的全文。

---

## 5. 对本计划里程碑的影响

- **M0**：本调查完成；进货推荐栈写下，**仍等主人点头才接自动监测**（硬约束未破）。
- **M1**：继续人工 DOI 跑通 1 篇；`monitor/README.md` 可把 `source` 写成 `recommended: crossref+openalex; bound: not until owner confirms`。
- **不要**把 OpenAlex 132 条当周任务；人筛预算按 Crossref 严查询 + RSS 新文。
- Author 线 M1/M2：从上面 7 篇四大刊 published + 适量通讯作切入口（仍用 json，不手抄进 skill）。

## 6. 本会话未做 / 限制

- 未克隆刘组仓全文；未打开 PDF。
- academic-mcp 调用失败。
- 未写 `filters.md` / `queue.yaml` 实体（属 M1 vault）。
- 未改 `skills/style-mine` 代码。
- Crossref 无 mailto 时 429；后续测试带 `mailto=` 成功。
- OUP/IMS RSS 在此出口被挡，不代表主人浏览器订阅一定失败。
