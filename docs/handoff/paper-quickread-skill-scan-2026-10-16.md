# 单篇论文速读 / 结构化总结 skill 扫描（2026-10-16）

渠道：GitHub search_repositories、WebSearch、X search_posts_all。所有链接都用 curl 确认返回 200，stars 和最近 push 时间来自 GitHub API。没有改动任何仓库。
提示：没有单独做 GitHub search_code。部分 SKILL.md 的结构是从 WebSearch 抓到的原文片段里读的，没有逐个打开原文件。

## 候选
| # | 候选 | 输出结构 | 文风分析 | PDF 抽取 | ★ / 最近活跃 | 建议 |
|---|---|---|---|---|---|---|
| 1 | [alaliqing/claude-paper](https://github.com/alaliqing/claude-paper) `summary` + `study` | summary：一句话 / Problem / Core Idea / 3–5 贡献 / 结果表 / Why it matters / 2–3 局限，300–500 词，5 分钟读完。study：summary + insights（为什么有效、观念转变、trade-off）+ method（伪代码、复现风险）+ mental-model + Q&A，并强制打 2 个语义 tag | 无 | 自带 PDF 解析（Node），**违反 MinerU 规则** | 347 / 2026-08 | **借鉴**：速读模板的骨架、每节的长度表、两档深度 |
| 2 | [michaelrizvi/claude-config `skills/paper`](https://github.com/michaelrizvi/claude-config/blob/main/skills/paper/SKILL.md) | Problem / Key idea / Method（含公式）/ Results（带数字）/ Limitations（要求自己判断）。另有规范：区分「证明 / 实证 / 猜想」、写出假设、标可疑主张、多篇对比用表 | 无 | 不规定 | 12 / 2026-03 | **借鉴**：「证明 / 实证 / 猜想」分级和假设清单，很适合统计/因果论文 |
| 3 | [karpathy/nanochat `read-arxiv-paper`](https://github.com/karpathy/nanochat/blob/master/.claude/skills/read-arxiv-paper/SKILL.md) | 拉 arXiv **TeX 源码**，从 main.tex 递归读全文 → 写 `summary_{tag}.md`，并联系本项目说明「能借鉴什么」 | 无 | 不用 PDF，读 TeX | 58.7k（仓库）/ 2026-09 | **借鉴**：「与我当前项目的关联」一节。有 TeX 源时可以作为 MinerU 的补充（需要用户确认是否允许） |
| 4 | [Charles-Donne/Research-Paper-Skills `paper-reading-management`](https://github.com/Charles-Donne/Research-Paper-Skills) | Codex skill。每篇论文用一个独立 subagent，产出中文精读报告（带图表标记），生成 note.md / retrieval.md / metadata.json，做结构审计后再更新索引，Zotero 只打 2 个 tag | 无 | pypdf / pdfplumber，**违反规则** | 7 / 2026-09 | **借鉴**：一篇一个 subagent 的隔离、产物审计、目录约定 |
| 5 | [Wang-Ruibin/paper-alchemist](https://github.com/Wang-Ruibin/paper-alchemist) | 从范文**按章节**（摘要 / 引言 / 相关工作 / 问题定义 / 方法 / 实验设置 / 结果分析 / 结论）蒸馏中英双语写作模式 profile。只学组织方式，不抄内容，不编事实 | **有（核心功能）** | 本地处理，具体方式没核实 | 4 / 2026-09，有 CI 和 release | **借鉴**：拆文风那部分的分节维度。跟我们的 journal-adapt 功能重叠，不要直接装 |
| 6 | [Galaxy-Dawn/claude-scholar `paper-miner` / `/mine-writing-patterns`](https://github.com/Galaxy-Dawn/claude-scholar) | 维度：writing patterns / structure signals（段落推进、动机 → 方法 → 结果的过渡）/ reusable phrasing / venue signals / how this helps / source index。支持 focus 模式（intro / method / results / rebuttal / venue），结果累积写进一个全局 writing memory | **有** | 读 PDF/DOCX/arXiv，方式不限定 | 5.8k / 2026-09 | **借鉴**：文风拆解的输出字段和 focus 模式 |
| 7 | [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | 写作向：section_rhetorical_moves（各章节的修辞步骤 + 例子）、craft_reference（句长、三种语域）、机械检查（M1–M18）和语义检查（S1–S31） | **有**（规范，用来对照） | 不涉及 | 240 / 2026-07 | **借鉴**：拿 rhetorical moves 的分类给文风拆解贴标签 |
| 8 | [K-Dense-AI/scientific-agent-skills `scholar-evaluation`](https://github.com/K-Dense-AI/scientific-agent-skills) | 逐条主张对应证据的评估（X 上有用户推荐：「指出哪条主张缺了哪份证据」） | 无 | 视具体 skill 而定 | 51k / 2026-10 | **借鉴**：给速读加一节「主张—证据」表 |
| 9 | [YihengCai/paper-reader_SKILL](https://github.com/YihengCai/paper-reader_SKILL) | Codex arXiv 阅读总结 skill | 无 | 没核实 | 1 / 2026-03 | 跳过（没有用户反馈） |
| 10 | [selfanti/skip-reading](https://github.com/selfanti/skip-reading) | Codex 简洁总结 + 从 arXiv 抽原图 | 无 | 自带抽图 | 0 / 2026-08 | 跳过（只有抽原图这个思路可以参考） |
| 11 | [qiuchenmeng/PaperXRay](https://github.com/qiuchenmeng/PaperXRay) | 「用最少的字给出最充分的理解」 | 没核实 | 没核实 | 0 / 今天刚建 | 先观察 |

X 搜索：结果多是营销号和榜单，有用的只有对 scholar-evaluation 的一条推荐，以及「从老师改稿里提炼 Codex 协作规则」的思路（呼应 lessons-harvest）。YouTube 这轮没找到专门的速读 skill 教程。

## 融合方案（我们自己的 paper-quickread skill）
**输入**：一律用 MinerU 转写，产出 markdown 和图片。不引入候选 1、4、10 的 PDF 解析器。arXiv TeX 源只作为可选旁证，用不用要用户拍板。

**一页输出（固定节，带长度上限，参考 #1）**
1. 元信息 + 一句话总结 + 2 个 tag（问题域 / 方法）（#1、#4）
2. 问题与动机（2–3 句）
3. 核心想法（2–3 句）
4. 方法：步骤或伪代码；统计/因果论文写识别假设和估计量（#2）
5. 结果：一张数字表，只抄原文数字，不估读图里的值（#5）
6. 贡献：3–5 条，每条标「证明 / 实证 / 猜想」（#2）
7. 主张—证据表 + 可疑点（#8、#2）
8. 局限：作者自己承认的和我们的判断分开写
9. 与我的项目/方向的关联（#3）

**可选的文风拆解（`--style`，参考 #6、#5、#7）**
- 开头：摘要和引言第一段的修辞步骤序列（背景 → gap → 本文 → 贡献），给每一步贴 move 标签
- 段落推进：每段一句话概括功能，以及段与段之间的过渡方式
- 句式：3–5 个可复用句型模板（用占位符抽象，不长篇引用原文）、句长和语域、hedging 的用法
- 写进 journal-adapt 的风格 profile，并注明出处。不新建平行的 writing-memory，避免堆叠

**流程纪律**：一篇论文开一个 subagent 隔离上下文，写完做结构自检（#4）。分两档深度：速读（一页）和精读（接现有的 Notion 范式）（#1）。
**归属**：放在普适 core。stats/causal 专属的字段（识别假设、估计量）放进 field profile 的附加段。
