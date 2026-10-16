# supervisor-skills-plus 覆盖度审计 + 补缺候选（2026-10-16）

来源：用 cursor-github MCP 读取私有仓库 easygl1der/supervisor-skills-plus 的 main（git tree + skills/README.md）。只读，没有改动，也没有提 PR。

## 1. 当前 skill 清单（21 个）

### A. 上游 HKUSTDial（12 个，fork 里强化了 8 个）
| skill | 用途 | 层级 |
|---|---|---|
| idea-evaluator | 四层 idea 体检：致命缺陷 → 能力匹配 → 五维打分 → 范式跃迁 | general（带 domain-evaluation-frameworks） |
| deep-research | 综述级调研：冻结 RQ、多视角检索、逐条核验引用 | general |
| tech-paper-template | 技术论文逻辑骨架（挑战—模块—贡献互锁） | SE/AI 偏 |
| benchmark-paper-template | Benchmark 论文六阶段编排 | SE/AI |
| intro-drafter | 六段式 Intro 正文，引用先检索后写 | SE/AI 偏 |
| paper-writer | 证据门控正文写作，含独立引用核查（另有 math-paper.md） | general + math 参考 |
| figure-designer | 三张承重图的设计 | SE/AI |
| drawio-reconstruction | 参考图 → 可编辑 drawio | general 工具 |
| paper-polish | 忠于原意的润色、中译英 | general |
| pre-submission-reviewer | 五维审稿式终审 | general（顶会视角） |
| rebuttal-guidance | rebuttal 策略与回复 | general |
| vibe-research-workflow | 人机协作守则（coding/figure/writing） | general |

### B. Plus 新增（9 个）
| skill | 用途 | 层级 |
|---|---|---|
| research-supervisor | 入口：初始化、判断阶段、阻塞项、分派 | general core |
| research-core | 通用规则 + field profiles（se / ai-ml / math / stats / causal，其中 stats、causal 只有空框架）+ venue profiles + 9 份 checklist + 风格 overlay | core + field |
| experiment-workflow | 冻结语料/金标、prompt/模型版本、runs 日志、数字可追溯、匿名复现包 | general（偏 SE/LLM 实证） |
| journal-adapt | 从范文生成风格 skill 和 venue/field profile | general |
| deai-writing | 按意图去 AI 味，另有只报告的审查模式 | general |
| check-loop | 设轮数上限的多轮检查（研究 → 风格 → 语言） | general |
| feedback-to-revision | 意见编号、一条意见对应一处改动、diff 核实、回复表 | general |
| research-records | STATUS/TODO/ADR/日志，可选 Linear 镜像 | general |
| lessons-harvest | 把意见沉淀成带出处的规则 | general |

## 2. 按研究流程看覆盖
| 环节 | 状态 | 说明 |
|---|---|---|
| 选题/开题 | 部分 | idea-evaluator 和 deep-research 很强。缺开题报告/proposal、研究计划和里程碑模板 |
| 文献检索收集 | 部分 | deep-research 偏一次性综述。缺持续追踪（arXiv 日报、Zotero/BibTeX 库管理、去重） |
| 精读笔记 | 缺失 | 没有单篇精读模板（Notion 范式目前在 skill 外）。转写按约定只用 MinerU，应写进 skill |
| 文献整理/综述 | 已覆盖 | deep-research + paper-writer 的 Related Work |
| 读教材 | 缺失 | 没有章节学习、习题、证明复述类 skill |
| 实验设计 | 部分 | experiment-workflow 管冻结和日志，但没有功效分析、消融矩阵、统计检验计划 |
| 跑实验（Colab/GPU） | 缺失 | 没有算力调度、任务排队、checkpoint、长作业监控 |
| 工程实现写代码 | 部分 | 只有 vibe-research-workflow 守则。缺研究代码的 TDD、review、worktree 流程 |
| 数据管理/可复现 | 已覆盖 | experiment-workflow 加 research-records |
| 结果分析作图 | 部分 | figure-designer 讲设计。缺数据 → 图的执行（matplotlib 风格、统计显著性标注） |
| 写作/润色/去 AI 味 | 已覆盖（强） | paper-writer、intro-drafter、paper-polish、deai-writing、check-loop、journal-adapt |
| 投稿前审稿 | 已覆盖 | pre-submission-reviewer。缺多 persona 模拟审稿和 meta-review |
| rebuttal | 已覆盖 | rebuttal-guidance + feedback-to-revision |
| 组会汇报/幻灯片 | 缺失 | 没有 Beamer/PPT、组会周报、海报、talk 稿 |
| 与导师/合作者沟通 | 部分 | feedback-to-revision 有指导记录。缺周报和会前议程模板 |
| 项目管理（Linear） | 部分 | research-records 里有可选的 Linear 镜像 |
| 学术诚信 | 部分 | 引用核验、不编造做得很强。缺预注册、标注一致性（kappa）、AI 使用披露模板、查重 |
| 领域 profile | 部分 | stats/causal 是空框架，跟用户主方向（因果/统计）不匹配，优先级最高 |

## 3. 补缺候选（链接都已用 curl 确认返回 200；stars 和最近 push 时间来自 GitHub API）
| # | 候选 | 补哪个缺口 | 理由 | 建议 |
|---|---|---|---|---|
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) ★52k，今天还有 push | 全流程 research→review→revise | 很活跃，用户多，可以对照我们的 pipeline | 借鉴改写（挑 review/revise 部分，别整包装，避免和现有 skill 叠在一起） |
| 2 | [fcakyon/phd-skills](https://github.com/fcakyon/phd-skills) ★423，10/11 | 论文复现、实验设计、结果对比 | 垂直于 PhD 场景，体量小，好吸收 | 借鉴改写 → 并进 experiment-workflow |
| 3 | [claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback) ★502，10/15 | 投稿前多角度审稿 | 学者本人维护，偏经济/社科审稿视角，适合给 stats profile 用 | 借鉴改写（放进 field-specific） |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) ★5.8k，9/23 | Zotero 精读笔记、results-report、slides/poster；支持 Codex | 文献库 → 笔记 → 报告的闭环正好是我们缺的 | 借鉴 /zotero-notes 和 results-report |
| 5 | [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) ★411，2/27（不太活跃） | literature-search（S2/arXiv/OpenAlex 脚本）、self-review 三 persona、slide-generation（Beamer） | 脚本可以直接用 | 借鉴脚本和 Beamer 生成，其他跳过 |
| 6 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) ★13.6k，10/11 | GPU 实验：Modal/SkyPilot/Lambda、W&B/MLflow、lm-eval、vLLM | 有真实复现 demo（LoRA Without Regret） | 按需直接引入单个 skill（Modal、W&B、lm-eval） |
| 7 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) ★51k，10/15 | 统计/数据分析、DataLad 可复现、GPU 加速 | 支持 Agent Skills 标准，Cursor/Codex 都能用 | 只挑 statsmodels/统计、DataLad 等少数 skill 引入。生物医药部分跳过 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) ★181k | pptx/docx/xlsx：组会幻灯片、表格 | 官方维护，格式稳定 | 直接引入 pptx（组会） |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) ★300k | 研究代码工程化：brainstorm → plan → TDD → review | 工程流程最成熟 | 直接引入工程子集，在 vibe-research-workflow 里引用 |
| 10 | [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) ★2.2k，7/3 | 去 AI 味（含基金申请书） | 可以拿来对照 deai-writing 的规则表 | 只借鉴规则，不引入（避免两个去 AI 味 skill 叠加） |
| 11 | [ShZhao27208/Aut_Sci_Write](https://github.com/ShZhao27208/Aut_Sci_Write) ★210，8/13 | 多源检索、Zotero 同步、PPT | 中文作者，PDF 抽取跟 MinerU 约定冲突 | 只借鉴 sci-search 和 sci-zotero，PDF 部分跳过 |
| 12 | [franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills) ★223，9/18 | 经济/金融/社科实证（计量、因果） | 可以填 stats/causal profile | 借鉴改写成 causal.md / stats.md |
| — | delibae/claude-prism ★1.8k | LaTeX 写作工作区 | 是独立应用，不是 skill | 跳过 |
| — | XiaontOVO/autoresearch-plugin | 全自动 pipeline | 只有 1 star，没有用户反馈 | 跳过 |

X 搜索：这次结果基本是营销号和泛 AI 工具榜单，没有找到研究类 skill 的高质量推荐，没有采信。YouTube 这轮没有单独深挖。

## 4. 落地建议（按用户偏好）
- **普适 core 和领域风格分开**：新能力（lit-tracker、reading-notes、slides、compute-runner）放在 general 层。审稿视角和计量规范进 field profile，先把 stats.md 和 causal.md 填实。
- **技能源统一放在 ~/.codex/skills**：外部 skill 先 vendor 到 fork 的 `skills/`，写清出处和许可证（参照 drawio-reconstruction 的做法），再用 install.sh 同步。
- **反堆叠**：每个缺口只引入一个 skill。去 AI 味和审稿只改写现有 skill，不新增平行 skill。
- **文献转写只用 MinerU**：reading-notes 和 lit-tracker 里明确禁止 pypdf/外部 PDF 抽取脚本（候选 4、5、11 里的这部分不要引入）。

## 5. 建议新增 skill（优先级）
1. 填实 stats/causal field profile（参考 12、3）
2. reading-notes：单篇精读，MinerU → Notion 范式（参考 4）
3. lit-tracker：arXiv/S2 持续追踪 + BibTeX/Zotero 库（参考 5、11）
4. compute-runner：Colab/Modal 作业、checkpoint、监控（参考 6）
5. group-meeting：周报 + Beamer/PPT（参考 8、5）
6. proposal-drafter：开题报告和研究计划
7. textbook-study：教材精读、习题、证明复述
8. integrity-pack：预注册、标注一致性、AI 使用披露
