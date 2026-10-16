# alaliqing/claude-paper 深度拆解（2026-10-16）

仓库：https://github.com/alaliqing/claude-paper ，克隆在 /tmp/claude-paper。node_modules 和截图以外的文件已全部读过。

## 1. 架构与安装
- 本质上是一个 Claude Code 插件，带一个本地 Web 阅读器。v1.2.1，2026-08 又加了跨 agent 分发（Codex / OpenCode / DeepSeek-harness）。
- 核心文件：
  - `plugin/skills/summary/SKILL.md`（8 KB）：速读
  - `plugin/skills/study/SKILL.md`（10 KB）：精读加学习材料
  - `plugin/skills/webui/SKILL.md` 和 `plugin/commands/webui.md`：启动 Nuxt 服务，端口 5815
  - `plugin/skills/study/scripts/`：`download-pdf.cjs`（arXiv abs→pdf）、`parse-pdf.js` 和 `parse-pdf-core.js`（**pdf-parse**）、`extract-images.py`（PyMuPDF）
  - `plugin/hooks/check-install.sh`：SessionStart 时创建 ~/claude-papers/
  - `plugin/src/web/`：Vue/Nuxt 阅读器，带卡片、标签和文件树。仓库里误提交了 node_modules，约 39 MB
  - `skills/claude-paper-*`、`.agents/skills/*`：脚本 `sync-agent-adapters.mjs` 生成的跨 agent 副本，只改了 frontmatter 名称和 `CLAUDE_PAPER_PLUGIN_ROOT` 变量
  - `.opencode/commands/*`、`bin/claude-paper.mjs`、`scripts/install-agent-adapters.mjs`、`tests/*.test.mjs`
- 安装方式二选一：`/plugin marketplace add alaliqing/claude-paper` 加 `/plugin install claude-paper`，或者 `npx --yes @zlzliqing/claude-paper@latest install --target claude-code|codex|opencode|all`。首次运行会执行 `npm install` 并装 pymupdf。
- 产出目录是 `~/claude-papers/papers/{slug}/`，另有 `~/claude-papers/index.json`。

## 2. 工作流
### summary 模式（/claude-paper:summary）
0. 检查依赖。
1. 是 URL 就下载到 /tmp/claude-paper-downloads。然后 `node parse-pdf.js <pdf> --output-dir`，得到 `meta.json`（标题取首行，摘要用正则抓，正文预览截断到 5 万字）和 `paper.txt`（全文）。
2. 把 PDF、txt、meta 拷进 slug 目录，写 `quick-summary.md`。
3. 往 index.json 里追加一条（原文："Read existing index.json first, then append… Never overwrite"）。
4. 重启 webui。
5. 展示摘要，引导用户去用 study。

模板原文：
```
# Quick Summary: [Paper Title]
## One Sentence
## Problem
## Core Idea
## Key Contributions   (- 3–5 条)
## Main Results        | Metric | Value | Dataset/Benchmark |
## Why It Matters
## Limitations         (- 2–3 条)
```
篇幅规则：
| 节 | 篇幅 |
|---|---|
| One Sentence | 1 句 |
| Problem | 2–3 句 |
| Core Idea | 2–3 句 |
| Contributions | 3–5 条 |
| Results | 1 张表 |
| Why It Matters | 2–3 句 |
| Limitations | 2–3 条 |

总篇幅约 300–500 词，不含表。原文还要求 "readable in under 5 minutes"、"Focus on conceptual clarity over technical details"。语言按用户输入自动检测，中文提问就出中文。

### study 模式
1. 同上解析，原文："Use paper.txt as the source… Search it and read relevant sections as needed"。
2. 先做**评估**：难度分 Beginner/Intermediate/Advanced/Highly Theoretical，性质分 Theoretical/Architecture/Empirical-heavy/System/Survey，方法复杂度另评一档。评估结果决定写不写 method.md 和 notebook。
2.5. 必须生成**恰好 2 个标签**，一个领域、一个方法，不能用 paper/ai 这种泛词。
3. 必写文件：
   - README.md：难度、预计学习时间、导航
   - summary.md：背景、问题、贡献、结果、量化指标
   - **insights.md**（原文 "Most Important"）：核心想法、为什么有效、概念转变、取舍、局限、和前人工作的比较
   - qa.md：15 题，基础、中级、高级各 5，用 `<details>` 折叠答案
   
   条件文件：
   - method.md：组件、算法流程、ASCII 架构图、伪代码、实现坑、超参敏感性、复现风险
   - mental-model.md
   - reflection.md：可扩展方向、脆弱假设、可能失败的场景
4. **强制**至少一个可运行的代码 demo，放在 code/。
5. 单文件交互式 HTML，原文："Uses real data from the paper… never invent numbers"。
6. PyMuPDF 抽图。图少于 3 张时，把前 3 页渲染成图。
7–8. 更新索引，启动 webui。
9. 交互追问，追问内容另存成 deep-dive-*.md。

## 3. PDF 解析
- 用的是 **pdf-parse（Node，纯文本）**。元数据全靠正则：标题取第一行，作者用 `^[A-Z][a-z]+ [A-Z][a-z]+` 匹配，摘要匹配 `Abstract … Introduction`。公式、表格、阅读顺序全丢，双栏论文会串行，数学和统计论文基本没法用。
- 硬编码程度：两个 SKILL.md 的 Step 1b 都写死了 `node …/parse-pdf.js`，产物契约是 `meta.json` 加 `paper.txt`。下游只读这两个文件，所以替换只需要动这一步。
- **已有先例**：PR #10（hugooole，2026-06）提出用 `mineru-open-api` 替换 pdf-parse 和 PyMuPDF，**作者没合并就关了**。思路可以参考，但它走的是 MinerU 云 API CLI，不是我们的 MCP。
- 我们改成 MinerU 的具体做法：
  1. Step 1b 改成调用 MCP `mineru_parse_documents_smart`，输入本地 PDF 或 arXiv PDF URL，产出 `paper.md` 和 images/。
  2. 用 `paper.md` 取代 `paper.txt`，并且**保留章节标题**，方便后面按章节引用。
  3. 元数据（标题、作者、年份、arXiv id）改从 arXiv API 或 MinerU 的首个 H1 取，不再用正则。
  4. 删掉 extract-images.py，图片直接用 MinerU 抽出来的。
  5. 去掉 50k 截断。长文按 `##` 章节分块读。
  6. MinerU 失败时**报错停止**，不回退到 pdf-parse（这是用户的规定）。

## 4. 优劣
优点：
- 速读骨架简洁，每节都有篇幅上限。
- study 模式先评估论文性质再决定写哪些文件。
- insights 和 reflection 两份的视角好。
- QA 分三档难度。
- index 文件只追加不覆盖，这个纪律做得对。

缺点：
- **防幻觉弱**：summary 模板没有要求数字照抄原文，结论也不用标出处章节。只有 HTML 那一步写了 "never invent numbers"。示例 Limitations 里有一条 "Requires large amounts of training data"，原文其实没这么说，等于示范了编造。
- 不区分证明、实证和猜想，没有识别假设和估计量，也不把主张和证据对照。所以对**数学、统计、因果**论文帮助不大。代码 demo 和 Results 表都是按 ML 论文的口径设计的：理论论文没有 Metric/Dataset 可填，硬塞一个 demo 也是负担。
- SE 论文勉强能用，但没有 RQ 结构、威胁效度这些节。
- **完全没有文风或引言分析**。
- 依赖重：Node、Nuxt、npm、PyMuPDF，还在 5815 端口起服务。中文提问时会出中文。
- 已知问题：issue #6 反映有时不会自动触发。

## 5. 许可与活跃度
- MIT，© 2026 alaliqing。
- ★347，27 fork。2026-02-10 创建，最后一次 push 在 2026-08-14（UTC）。
- 10 个 issue/PR 全部已关闭：#8 新增 summary；#9 npx skills；#10 MinerU PR 未合并就关了；#2、#7 是改进建议。
- 3 月以后基本只有一次分发功能的更新，算低频维护。

## 6. 并入 supervisor-skills-plus 的方案
现状：仓库已有 `skills/research-core`（含 `references/fields/{ai-ml,causal,math,se,stats}.md`、`_template.md`，模板里有 claim-ledger.md）和 `skills/journal-adapt`（references 下有 style-card.md、style-profile.md、method-card.md）。

- **原样照抄**（MIT 允许，需在 THIRD_PARTY.md 里保留版权声明）：
  - summary 的节骨架和篇幅表
  - study 的"先评估难度、性质、复杂度"
  - QA 三档加 `<details>` 的格式
  - reflection 的四个问题
  - index 只追加不覆盖的规则
- **重写**：
  - 解析换成 MinerU MCP
  - 模板改成我们的 9 节，按"元信息→问题→核心想法→方法→结果→贡献→主张与证据→局限→与我方研究的关系"排列。方法节按 fields 档案加内容：causal 写识别假设、估计量和估计方法，stats 写模型、渐近性质和模拟设计，math 写定理链和证明思路，SE 写 RQ 和威胁效度
  - 结果节的数字必须**照抄原文**，并标明出自哪个表或哪一节
  - 贡献逐条标【证明/实证/猜想】
  - 主张与证据写进 claim-ledger 格式
  - 局限分开写"作者承认"和"我方判断"
  - 去掉 webui、代码 demo 和 HTML
  - 产出写 Notion「因果/LLM 文献精读」或 research-records
- **新增 `--style`**：拆引言的修辞步骤（CARS 那几步）、每段的作用和过渡、可复用句式模板、hedging 语气。结果写进 journal-adapt 的 style-card 或 style-profile，不另建一套格式。
- 建议放在 `skills/paper-quickread/`：SKILL.md、references/template-9.md、references/style-mode.md、THIRD_PARTY.md。

（可选的实测这次没做：原版依赖 pdf-parse，跑出来的结果不能代表 MinerU 版本的效果。等我们的版本写好后，再拿一篇 arXiv 论文的 MinerU 输出来测。）
