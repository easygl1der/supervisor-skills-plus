你在私有仓库 `easygl1der/supervisor-skills-plus` 的 **main 分支**上工作。任务：给这个 research skill 库加上「读与学」这一层，并做一次合并重构。完整规格在 `docs/specs/2026-10-16-reading-upgrade.md`（我已经放进仓库；如果不在，就在我给你的路径里找 `supervisor-plus-reading-upgrade-SPEC.md`，并把它复制到这个位置，跟随第一个 commit 提交）。HTML 画图套件 `study-kit` 我会放在 `skills/study/kit/`（或者给你 `study-kit.tar.gz`，你解压到这里；不要提交 node_modules）。

**先通读 SPEC，再动手。** SPEC 的 §3 是已经敲定的决策，照做，不要重新讨论；§2 列了被否掉的方案，不要再捡回来；§11 是留给你自己调研、自己决定的问题。

## 精神（任何细节拿不准时，按这些来）
- study 的目标是**为了做研究而真正理解**，不是考试、刷卡片。动机 → 大白话 → 合适就举例（不硬凑）→ 连到我已经懂的概念 → 生动的图 → **我必须复述** → 按心智模型三层（机制 / 条件 / 边界）诊断 → 顺着我自己的联想纠正 → 重画图。默认给提示不给答案；一次只问一个问题；回复要短。
- 不编造：数字、公式、引文照抄原文并标出处；原文没有就写「原文未给出」；图上的数字要么有出处，要么标「示意」；自己补的推导步骤标「补」。
- PDF 只走 MinerU（`mineru_parse_documents_smart`，复用 journal-adapt 现有的 Step 2），失败就报错停止，不回退到其他解析器。
- 跨工具：Cursor、Claude Code、Codex、Claude.ai 都要能用，并写清各环境怎么降级。
- 反堆叠：能并进现有 skill 的就不新建；风格记忆只有一套。文字按终稿口吻写，变更只写进 CHANGELOG。
- 遵守仓库约定：frontmatter；Overview / When to use / When NOT to use / Step 0 加载 research-core / Workflow / Checklist / Outputs / Handoff；来源标 `[src:...]`；general core 加 per-field profile；progressive disclosure。
- 默认输出中文，术语保留英文。

## 工作顺序
1. **读仓库**：仓库里没有 AGENTS.md。先读 `DESIGN.md`、`skills/README.md`、`notes/09-implementation-conventions.md`，再读 `skills/research-supervisor`、`skills/research-core`（含 `references/fields/`、`assets/templates/claim-ledger.md`）、`skills/journal-adapt`（尤其是 `references/style-card.md`）、`skills/deep-research`、`skills/idea-evaluator`、`skills/figure-designer`、`skills/paper-writer`，以及 `scripts/` 下的 lint 脚本。跑一次 `rg -n "journal-adapt"`，列出所有引用位置。
2. **二次调查**（SPEC §11.2）：把候选仓库的 SKILL.md 读全文，核对 learning-science 里的引用和关键数字（核不到就删掉，或标「未核」），再联网看看 2026 年有没有更好的同类做法。只吸收说得清理由的部分。
3. **按 SPEC 实现，并分成下面这些逻辑 commit 提交到 main**：
   1. journal-adapt 改名合并为 `style-mine`（`git mv`，按拆 / 攒 / 用三环节重写 SKILL.md，留一个 `journal-adapt` stub），并更新全仓引用；
   2. `paper-quickread`（固定 9 节、篇幅表、先评估再写、index.json 只追加、`--style` 产出标准 A–L Style Card）；
   3. `study`（主 SKILL.md 保持短，子模块放在 `references/`，加上 kit、学习档案 `study-vault` 的结构和读写规则、会话自动落盘）；
   4. deep-research 加文献地图模式；
   5. `research-bridge`；
   6. `proposal-writer`；
   7. research-supervisor 加「读与学」路由，更新 causal.md / stats.md（AJS 的内容只作为 candidate，标注来源），更新 README（skills/README 现在写的是 11 个，实际是 21 个，要改对）、`README*.md`、`llms.txt`、`install.sh`（如果它有名单）、THIRD_PARTY.md、CHANGELOG.md，并写 ADR。
4. **实测**（SPEC §11.2 第 4 点）：用 1 篇因果论文跑 quickread（含 `--style`）和 study 论文模式，完整走一轮概念协议，其中模拟一次含错误的复述；再用 1 章教材（比如 Murphy PML 的一章）跑 study 教材模式。每张图都跑 `render.sh`，确认没有警告，并打开 PNG 看一遍；至少用一次「概念讲解页」（`explainer-page.html`，`--full --figures`）和一次 stepper（证明或算法，`--steps`），检查逐步 strip。产物存进 `skills/study/evals/`（如果仓库有约定，就按约定放）。实测发现的问题要回头修进 skill。
5. **检查**：跑 `scripts/lint_skills.py`、`check_sources.py`、`check_checklists.py`、`check_shared_sync.py`（依赖见 `requirements-lint.txt`），必须全部通过；再逐条对照 SPEC §12 的验收清单。
6. 本地 commit 全部完成、检查也通过后，push 到 origin/main。不要 force push，不要改写历史。

## 拿不准时
按 SPEC §11.3 的标准排优先级：精神和已定决策 > 我的时间成本 > 跨工具 > 不重复 > 实测效果。先按你认为最好的方案实现，把决定写成 ADR，列进最终报告的「待讨论」清单，不要停下来等我。

## 最后给我一份报告（中文）
1. 每个 commit 做了什么（附 hash）；
2. 你做的决定，各附 ADR 链接；
3. 借鉴清单：哪些内容借自哪个仓库、用的什么许可，哪些是新写的；
4. 两个实测样例的产物路径，以及你看到的问题；
5. lint 结果；
6. 需要和我讨论的问题、没完成的事项和已知风险。


**画图补充（2026-10-16，吸收 nicobailon/visual-explainer）**：SPEC §6.7.1–6.7.7 是新增的画图规则、概念讲解页模式、stepper 动画（取代“HTML 动画→GIF”，GIF 只是 `--steps --gif` 的导出物）和跨领域场景目录（因果、编程、流程、证明、ML、读论文）。kit 里已有 `explainer-page.html`、`stepper*.html`、`vendor/ve/`（MIT，保留 LICENSE/NOTICE 并登记 THIRD_PARTY.md）。**不要**把 visual-explainer 作为 study 的必装依赖；不要引入 Google Fonts CDN；结构图不用 emoji，场景卡/漫画保留。把场景目录放进 `skills/study/references/visual-scenarios.md`，并在 research-supervisor / paper-quickread / research-bridge / deep-research 里需要画流程或对比时引用它。SPEC §11.x 的画图二次调查也要做。
