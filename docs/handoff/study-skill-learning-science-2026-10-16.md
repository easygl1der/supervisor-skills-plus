# study skill 设计调研：学习科学 + 现有工具 + 方案（2026-10-16）

> 核实说明：第二部分的链接已通过搜索确认存在。第一部分的经典文献是公认的标准引用（作者、年份、期刊、DOI），本轮没有逐篇打开原文。

## 一、学习科学依据（按对本 skill 的价值排序）

| # | 原理 | 关键文献 | 机制 | LLM 导师里怎么落地 | 适合数学证明吗 |
|---|---|---|---|---|---|
| 1 | 提取练习 / 测试效应 | Roediger & Karpicke 2006, *Psych Sci* 17(3):249（doi:10.1111/j.1467-9280.2006.01693.x）；Karpicke & Blunt 2011, *Science* 331:772 | 主动提取会强化记忆痕迹，效果胜过重读，也胜过画概念图 | 每节读完出题，先答后看；「闭卷复述定义和定理条件」 | ★★★ 默写定理条件，判断去掉哪个条件会失效 |
| 2 | 间隔重复 | Cepeda et al. 2006, *Psych Bull* 132(3):354；Cepeda et al. 2008, *Psych Sci* 19(11):1095；SM-2（Wozniak 1990）；FSRS（Ye et al., KDD 2022；open-spaced-repetition） | 间隔增大、复习时接近遗忘点，长期保持最好 | review-queue.md 记每张卡的到期日；会话开头先过到期卡 | ★★ 适合定义、条件、反例；整篇证明用「重构」卡代替 |
| 3 | 精细加工 / 自我解释 | Chi et al. 1989, *Cog Sci* 13:145；Chi et al. 1994, *Cog Sci* 18:439 | 逐步解释「为什么这一步成立」，补全推理链 | 每一步证明都问「这一步用了哪条引理或假设？」 | ★★★ 这是读证明的核心方法 |
| 4 | 交错练习 | Rohrer & Taylor 2007, *Instr Sci* 35:481；Kornell & Bjork 2008, *Psych Sci* | 混合题型，迫使学习者先判断该用什么方法 | 复习时混入其他章节的题；「这题该用 IV、DiD 还是 RD？」 | ★★ 选方法、选证明技巧 |
| 5 | 生成效应 | Slamecka & Graf 1978, *JEP:HLM* 4:592 | 自己生成的内容比读到的记得牢 | 读证明前先自己猜证明思路或定理结论 | ★★★ 先猜再看 |
| 6 | 合意困难 | Bjork 1994（*Metacognition: Knowing about Knowing*，MIT Press）；Bjork & Bjork 2011 | 短期内更难，长期效果更好（提取、间隔、交错都属于此类） | 总原则：默认不直接给答案，给分级提示 | ★★★ |
| 7 | 双重编码 | Paivio 1971/1986；Mayer《Multimedia Learning》 | 语言和图像两条通道互相补充 | 概念图、DAG 图、几何直观图用 mermaid 画 | ★★ 因果 DAG、收敛示意图 |
| 8 | 样例 + 认知负荷 | Sweller 1988, *Cog Sci* 12:257；Sweller & Cooper 1985；Kalyuga 2003 专长反转效应 | 新手先看完整样例比直接解题负荷低，熟练后应逐步撤除样例（fading） | 新章节先给样例，后面的题依次少给步骤（完成题 → 独立题） | ★★★ 证明的 fading：留空关键步让你补 |
| 9 | 费曼技巧 | 业界方法，没有单一的实证文献；接近「向他人讲解」效应（Fiorella & Mayer 2013/2014） | 用简单语言讲给别人听，能暴露缺口 | explain-back：你讲，它挑出含糊处和跳步 | ★★ 讲证明直觉 |
| 10 | 苏格拉底式辅导 | Graesser et al. 1995（tutoring dialogue）；AutoTutor | 用问题引导学生自己推出答案 | 一次只问一个问题，等回答后再继续 | ★★ 卡住时逐步收窄提示 |
| 11 | Bloom 2σ / 掌握学习 | Bloom 1984, *Educational Researcher* 13(6):4 | 一对一辅导加掌握学习，效果约 +2σ。注意：后来的复现幅度更小（VanLehn 2011 约 0.79σ） | 每个概念达标（例如答对率 ≥80% 且信心校准良好）才进入下一个 | ★★ |
| 12 | 概念图 | Novak & Gowin 1984；Nesbit & Adesope 2006, *RER* | 显式表示概念之间的关系 | 每章画「定义 → 引理 → 定理 → 例子」的依赖图 | ★★★ 定理依赖图 |
| 13 | Zettelkasten / 原子笔记 | Luhmann；Ahrens 2017《How to Take Smart Notes》（实践方法，实证有限） | 一条笔记只讲一个概念，用链接组织成网络 | concepts/ 下一个概念一个文件，用双链互相引用 | ★★★ 定义、定理各自成为一个节点 |
| 14 | 康奈尔笔记 | Pauk《How to Study in College》 | 分线索栏、笔记栏、总结栏；线索栏用于自测 | 每章笔记末尾放「线索问题」，可以直接转成卡片 | ★ 轻量借用 |
| 15 | 元认知 / 信心校准 | Dunning-Kruger 等；Koriat 1997；Kornell & Bjork 2008 | 学习者常高估自己的掌握程度；评信心再对照对错，可以纠正 | 每题先打 1–5 分信心再作答，统计「高信心答错」并优先复习 | ★★★ 「我以为懂了」是读证明最常见的坑 |
| 16 | Dunlosky 2013 综述 | Dunlosky et al. 2013, *Psych Sci Public Interest* 14(1):4–58 | 10 种学习技巧的效用评级：**高**＝练习测试、分散练习；**中**＝精细提问、自我解释、交错练习；**低**＝总结、划重点、关键词记忆法、意象法、重读 | 设计原则：笔记（总结）本身是低效用的，一定要配提取练习和间隔复习 | — |

**AI 辅导的实证警示**：Bastani et al. 2025, *PNAS*「Generative AI without guardrails can harm learning」（[链接](https://www.pnas.org/doi/10.1073/pnas.2422633122)）。不加限制的 GPT-4 让练习成绩提高 48%，但撤掉 AI 后考试成绩比对照组**低 17%**；改为只给提示、不给答案的 GPT Tutor 基本消除了这个负面效应。→ 我们的 skill 默认应该「先让你想」。

## 二、现有 skill、提示词和产品

| 名称 | 链接 | 做什么 | 可借用 |
|---|---|---|---|
| ChatGPT Study Mode 系统提示词（已泄露） | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/0bc4c25f/OpenAI/Study%20and%20learn.md)；[Simon Willison 解读](https://simonwillison.net/2025/Jul/29/openai-introducing-study-mode/) | 先了解用户；连接已有知识；不直接给答案，一次只问一个问题；难点讲完后要求复述；回复要短 | 「一步一问、等回答」的规则，以及「数学题第一轮不解」。HN 报道称 OpenAI 已悄悄下线这个模式 |
| Claude Code Learning 输出风格 | [官方文档](https://code.claude.com/docs/en/output-styles)；[learning-output-style 插件](https://github.com/anthropics/claude-code/tree/main/plugins/learning-output-style) | 在设计决策点留 `TODO(human)` 让用户自己写，加 Insight 块 | 证明重构可以照这个做：在关键步留 `TODO(you)` |
| Anthropic Learning Mode（Claude for Education） | [Education Report](https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude) | 苏格拉底式，重概念理解，不直接给答案 | 只有理念，提示词没有公开 |
| Anthropic claude-for-legal 的 socratic-drill | [SKILL.md](https://github.com/anthropics/claude-for-legal/blob/main/law-student/skills/socratic-drill/SKILL.md) | 「drill me / quiz me」触发；先读用户的弱项配置；不断追问；「答案和你自己的笔记矛盾时才指出」 | 官方的 skill 写法范本：弱项文件加触发词 |
| Google LearnLM | [arXiv 2407.12687](https://arxiv.org/abs/2407.12687)；[arXiv 2412.16429](https://arxiv.org/abs/2412.16429)；[博客](https://blog.google/products-and-platforms/products/education/google-learnlm-gemini-generative-ai/) | 五原则：主动学习、管理认知负荷、适应学习者、激发好奇、深化元认知；附录有教学评分 rubric | 用五原则当 skill 自检清单，可以借 rubric 写 eval |
| lfnovo/open-cognition | [GitHub](https://github.com/lfnovo/open-cognition) | Claude skill 加 MCP：苏格拉底陪练、费曼会话、卡片需用户批准、SM-2、追踪疑问和难卡 | 「卡片需经批准」「doubts 列表」「费曼会话流程」 |
| mordor-forge/study-skill | [GitHub](https://github.com/mordor-forge/study-skill) | 兼容 Agent Skills；FSRS-6（Go 二进制）；会话开头最多复习 3 张、不超过 5 分钟；有书目目录和 PDF 支持；无打卡、不催促 | 最接近我们需求：会话开头热身复习，可重启的会话状态。缺点是要装 Go |
| F1veYearPlan/deckhand | [GitHub](https://github.com/F1veYearPlan/deckhand) | 把笔记转成只用 cloze 的 Anki 卡，输出带 header 指令的 TSV；有 subagent 复核 | Anki 导出格式直接照抄（Anki ≥2.1.54 的 TSV header） |
| bevibing/socrates-skill | [GitHub](https://github.com/bevibing/socrates-skill) | 读 → 评估 → 引导 → 调整 → 确认五步；问题从澄清依次推进到反例 | 问题递进阶梯 |
| malkreide/socratic-method-skill | [SKILL.md](https://github.com/malkreide/socratic-method-skill/blob/main/SKILL.md) | 苏格拉底状态机（假设检验 → 困惑 → 深化）和问题分类 | 卡住时的状态处理 |
| open-spaced-repetition/py-fsrs | [GitHub](https://github.com/open-spaced-repetition/py-fsrs) | FSRS 的 Python 实现，`pip install fsrs` | 用一个小脚本更新 review-queue，不必让 LLM 手算间隔 |
| Khanmigo | khanacademy.org/khan-labs（本轮未打开） | 苏格拉底式辅导、不给答案 | 理念同上，提示词没有公开 |

## 三、study skill 设计方案

### 3.1 模式（自动识别，可用 `--mode` 覆盖）
- **paper**：arXiv 或期刊 PDF，有 abstract 和 references，篇幅不超过约 60 页。
- **book**：有目录、按章节组织，或者用户说「第 N 章」。按章推进。
- 两种模式的输入都只用 MinerU 的转写结果。数字和公式照抄原文并标出处（§、Thm、Eq、页码）。自己补的推导步骤标「补」。

### 3.2 一次会话的流程（默认，约 30–60 分钟）
1. **热身**：读 review-queue.md，先过到期卡，最多 5 张（间隔重复 + 交错）。
2. **预测**：看完标题和摘要或章节导读后，让你先猜要解决什么问题、可能怎么证（生成效应）。
3. **分块讲读**：每块讲一个概念或一个定理。先给样例，后面逐步撤除步骤（fading）。每块之后问一个「为什么这一步成立」（自我解释）。
4. **块末检测**：1–2 道题，先打信心分 1–5 再作答，然后批改（提取练习 + 校准）。
5. **收尾**：写笔记，生成候选卡片（你批准后才进队列），更新 progress.md 里的薄弱点。

### 3.3 交互选项（开关）
| 选项 | 默认 | 说明 |
|---|---|---|
| `quiz` | 开 | 题型：默写定义和条件、判断真假并给反例、「去掉假设 X 会怎样」、计算、选方法（交错）。批改分「对 / 部分对 / 错」，并给错因 |
| `confidence` | 开 | 每题打 1–5 分信心；「高信心答错」进入 misconceptions.md，并优先复习 |
| `socratic` | 卡住时自动启用 | 一次只问一个问题，提示分三级（方向 → 关键引理 → 部分步骤），不直接给答案，除非你明确说「给答案」 |
| `feynman` | 可选 | 你用自己的话讲一遍，它标出含糊词、跳步和循环论证 |
| `proof` | 数学和统计默认开 | 证明重构：给出定理和证明骨架，关键步留 `TODO(you)`；你写完后逐步核对。另有「找出每一步用到的假设」练习 |
| `review` | 开 | 写 review-queue.md；可选用 py-fsrs 脚本计算到期日，没装就退回固定间隔 1/3/7/16/35 天 |
| `anki` | 可选 | 导出 cards.tsv（deckhand 格式，cloze 加 Basic，数学公式用 MathJax `\( \)`） |
| `notes-only` | 可选 | 只写笔记、不互动（例如赶时间时用）。在笔记里注明这是「低效用模式」 |

### 3.4 目录与笔记结构（Markdown，用相对链接）
```
reading/
  index.md                         # 所有材料的总表（只追加）
  review-queue.md                  # 全局复习队列：| card | source | due | interval | last_grade |
  misconceptions.md                # 高信心答错的条目
  concepts/                        # 原子概念笔记，跨材料共享
    def-potential-outcomes.md
    thm-backdoor-adjustment.md
    lem-...md
  papers/2026-10-16_ding-li_principal-stratification/
    00-overview.md                 # quickread 的九节
    method.md  qa.md  reflection.md  deep-dive-<topic>.md
  books/murphy-pml1/
    progress.md                    # 每章状态、薄弱点、遗留问题
    ch03-probability-multivariate/
      notes.md                     # 康奈尔式：正文 + 线索问题 + 一段总结
      concept-map.md               # mermaid 依赖图
      exercises.md                 # 3–5 题，提示分级，解答标「自解，待核」
```
- 命名规则：概念笔记以 `def- / thm- / lem- / ex- / method-` 为前缀，后接英文 kebab-case；论文目录为 `日期_作者_短题名`；书按章编号。
- 每个原子笔记包含：一句话陈述、条件和假设、直觉、最小例子和反例、出处（原文 § 或页码）、「被谁用到 / 用到谁」的双链、对应卡片 id。
- 同一概念在别的材料里再次出现时，追加到已有笔记，不新建（Zettelkasten 的做法）。

### 3.5 默认与可选
- **默认开**：quiz、confidence、热身复习、原子概念笔记、progress.md，以及数学和统计材料的 proof 重构。
- **可选**：socratic 全程模式、feynman、Anki 导出、FSRS 脚本、Notion 同步（之后由 Grok Bot 定时同步，skill 本身不管）。
- **不做**：打卡和连续天数、网页阅读器、代码 demo（编程内容由 Learning 输出风格负责）。

### 3.6 给 Claude Code 的要点
- 写一份 `references/learning-science.md`，把上表压缩成每条一行、带引用，作为设计依据。
- 用 LearnLM 五原则加 Bastani 2025 的「不给答案」规则当 eval rubric；写 2 个 eval：一章教材（PML ch3）和一篇因果论文。
- 卡片必须经用户批准才进队列（open-cognition 的做法）。
- 会话状态全部放在文件里，中断后可以接着读（study-skill 的做法）。
