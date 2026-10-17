# research-bridge & proposal-writer 轻量升级 SPEC

**日期**: 2026-10-17  
**仓库**: easygl1der/supervisor-skills-plus @ `0d1f341`（及之后）  
**结论先行（诚实判断）**: 两个 skill **都不是薄稿，不需要重写**。相对 handoff 里各一段的草图，SG Claude 已经做成可交付的 v1，并有真实评测回写。本 SPEC 只做 **light polish（轻量打磨）**，目标是把「候选出处 → 核实」「评测归位」「补两三个缺口」做完，而不是推翻架构。

---

## 0. 判决与证据

### 0.1 判决

| Skill | 成熟度 | 建议 |
|---|---|---|
| `research-bridge` | **可用 / v1 成熟** | **Keep + light polish** |
| `proposal-writer` | **可用 / v1 成熟** | **Keep + light polish** |

**不要 deep rewrite。不要合并进 idea-evaluator。不要从网上 grant skill 整包替换。**

### 0.2 证据：已经做到的（反驳「还很空」）

**research-bridge**（约 24 KB：SKILL 11.7 + refs 12）

- 完整 workflow：Load context → Collect source → Pin target → Structure mapping → Assumption transfer → 五档裁决 → 最小证伪实验（预期 + kill criterion 先验）→ Save / hand-offs。
- 理论锚点写进了 skill：Gentner structure-mapping、Cartwright/Hardie external validity、Pearl & Bareinboim transportability、Nosek preregistration、Gelman & Loken forking paths、Platt strong inference、Lakens SESOI（见 `references/transfer-checks.md`）。
- 五档裁决词汇钉死：主方法 / 改造后用 / 只做稳健性检验 / 暂不 / 不用。
- 卡片模板分项目模式与 general mode；长度预算、`补`/`示意` 标记、ADR 冲突检查齐全。
- **真实评测两份且质量高**：
  - `skills/study/evals/bridge/project-ci/.../20261016-bridge-sdid.md`：SDID → 虚构 SE 面板，映射表断点写清（block vs staggered）、假设迁移含 A2/A3/B1、kill criterion + SESOI、method-shopping 提醒、交接完整。
  - `skills/study/evals/bridge/general-mle/bridge.md`：无项目时的通用模式，可移植核心 + 证伪模板。
- 与路由已接通：`research-supervisor` 触发表、`paper-quickread`/`study` hand-off、`experiment-workflow`/`research-records`/`idea-evaluator`/`deep-research` 边界清楚。
- 可选可视化接到 study kit（P6 before/after + P2）。

**proposal-writer**（约 42 KB：SKILL 16 + 4 refs）

- 七阶段：Call sheet → Spine（Heilmeier + aims 级联检验 + 起草前 novelty 检索）→ Evidence ledger（claim kinds）→ Section map / timeline / risks → Draft register → Reviewer pass → Citations & delivery。
- 文体覆盖：开题 / PhD plan / research statement / NSFC 2026 三部制 / NSF / ERC / NIH Specific Aims（`references/genres.md`）。
- Heilmeier 八问已对齐官方页：https://www.darpa.mil/about/heilmeier-catechism （confirmed）。
- Checklist PW-01…PW-11 + research-core CI/WR/TH；Draft 可见 `[cite needed]`/`[to verify]`/`[待查]`，Final 清零（**ADR 0016**，故意与 paper-writer 零占位符不同）。
- **真实评测 + 自我回写**：`skills/study/evals/proposal/2026-10-16_sdid-staggered-se/{kaiti,review}.md`。评测发现了：里程碑形容词不可证伪、新颖性应在起草前检索、阅读覆盖范围进 ledger、single-source gap——并回写进 `timeline-risk.md` / SKILL Phase 2–3 / `reviewer-lens.md`。事后核对发现附录 §8 已有 staggered SDID，正好验证了「M0 必须在起草前」这条规则。

相对 **handoff SPEC §8–§9**（各约 4 行）和 **audit「缺开题模板」**：已经超额完成。相对 **idea-evaluator**（更多 paradigm 参考、~100 KB refs）：这两个更短，但 workflow 完整度不输，属于「够用的专用 skill」，不是半成品。

### 0.3 真正的缺口（只打磨这些）

1. **评测目录错位**：桥与开题评测放在 `skills/study/evals/{bridge,proposal}/`，应迁到各自 skill 下的 `evals/`（或至少加 README 指针），免得 lint / 发现性差。
2. **出处大量 `(candidate)`**：proposal 的学校开题规则、NSF 页数、ERC 页数、NSFC 填充说明等多处 candidate；bridge 的 lit 条目多数未在正文外再核实 DOI/可获取性。轻量任务：能确认的改 `(confirmed)` + 抓取日；不能确认的写清「以当年 call / 学校模板为准，禁止凭记忆填限制」。
3. **NSFC 2026「三部制」断言**：genres.md 引用新闻联播/新华社类二手源。必须用 NSFC 当年正式指南或模板 PDF 再核一次；核不过就降级为「报道称…，以当年系统模板为准」。
4. **刘汉中式中文综述/计划书语体**：handoff SPEC 提到用户常读刘汉中教材；proposal-writer **没有**中文开题语体示例段（只有结构）。可加短 `references/zh-kaiti-register.md`：选题依据如何「问题先行」、创新点如何按轴编号、技术路线图期望——**原则与句式**，不是抄书。
5. **缺「编码 / 流程」桥接示范**：bridge 评测只有因果方法与 MLE。用户关心 coding、experiment pipeline、supervisor 路由本身。补一份 general 或 project 评测：例如「把 study kit stepper 挂进论文图流程」或「把某 git/实验脚本习惯迁到当前 repo」——证明 skill 不限于因果估计量。
6. **无 skill 内 scripts**：可接受。仓库级 lint 已覆盖；不必为 polish 硬造脚本。可选：`scripts/check_bridge_card.py` 检查 frontmatter `verdict ∈ 五档`、kill criterion 非空——**可选，非必须**。
7. **可选图未出 PNG**：评测注明未渲染 P2/P7。polish 时至少给 proposal 或 bridge 之一跑一张 study kit PNG，路径写进 eval README。
8. **外部对照可借、不可替换**：
   - DARPA Heilmeier（已用）：https://www.darpa.mil/about/heilmeier-catechism
   - NIH Specific Aims 常见结构（已用 Yale/CASRAI 类指南）
   - 开源 Claude skill 如 `wanshuiyin/.../grant-proposal`（NSF Broader Impacts、NSFC 创新点编号、KAKENHI 社会意义）与 `k-dense-ai` / `mzane0803` research-grants：可借「按基金分 register」「创新点编号」检查项，**不要**把预算/biosketch 拉进本 skill（当前 out of scope 正确）。
   - Transportability 文献（Pearl & Bareinboim 2014 等）：bridge 已引用；polish 时在 transfer-checks 加一句「正式 transport formula 需要选择图；本卡只做假设级检查，不做自动 do-calculus」。
   - ARIS / kill-argument 类对抗评审：属于 paper 提交前，**不**并进 bridge；bridge 的 kill criterion 是方法迁移级，不是拒稿 memo。

---

## 1. 原则（升级时遵守）

1. **架构冻结**：七阶段 proposal、五档 bridge、general mode、Draft markers（ADR 0016）、与 idea-evaluator / experiment-workflow 的边界——一律保留。
2. **Skill 文件英语**：SKILL.md 与 references 继续英文；对用户的对话/评测样例可中文（与仓库现有评测一致）。
3. **Call / 学校模板永远优先**：禁止用记忆填写字数、必备标题、评议表；unknown 必须显式保留。
4. **先 spine 后 prose；先证伪后证实**：已有，不得弱化。
5. **数字与缺口不编造**：ledger / bridge 卡继续要求出处或 `[to verify]`。
6. **轻量 diff**：每个文件改动说明「为什么」；禁止无关格式化大扫除。

---

## 2. research-bridge 打磨清单

### 2.1 Keep（不要动）

- 五档裁决、mapping 表八元素、assumption-transfer 列、validation 先验 kill、general mode、hand-offs、理论基础段。

### 2.2 Do（轻量）

| ID | 改动 | 验收 |
|---|---|---|
| RB-P1 | 迁评测到 `skills/research-bridge/evals/`（或 symlink + README）；保留现有 SDID / MLE 内容 | 路径可发现；链接从 SKILL.md Outputs/Evals 指出 |
| RB-P2 | 核对 Sources 里每条 lit：可访问则 `(confirmed)` + 稳定标识（DOI/年卷页）；否则保持 candidate 并写「未核全文」 | `check_sources` 风格与仓库一致 |
| RB-P3 | `transfer-checks.md` §3 增一小段 **coding / process / pipeline** 常见断点（API 契约、数据 schema、实验随机种子、CI 定义漂移），各 3–5 行，标明补 | 与因果/SE/stats 并列，不膨胀成新 skill |
| RB-P4 | 新增一份短评测：非估计量桥（例如「某实验记录习惯 → 当前 experiment-workflow」或「某图示流程 → 论文 figure 管线」），general 或虚构 project 均可 | 证明适用范围 |
| RB-P5 | SKILL.md 顶部加 **Evals** 小节指向评测路径；一句说明「正式 transportability 公式不在本 skill 自动求解」 | 防范围蔓延 |
| RB-P6 | （可选）用 study kit 给 SDID 桥出一张 before/after PNG | 文件进 evals |

### 2.3 Do NOT

- 不要改成打分制 idea-evaluator。
- 不要强制每次出图。
- 不要读 PDF（继续要求 quickread/study 产物）。
- 不要引入 Manim / 外部 grant 整包。

---

## 3. proposal-writer 打磨清单

### 3.1 Keep（不要动）

- Call sheet → spine → ledger → map/timeline/risks → draft → reviewer → delivery。
- PW-01…11、ADR 0016 Draft markers、级联检验、起草前 novelty 检索、single-source gap、Heilmeier、与 style-mine / deep-research / paper-writer 交接。
- 预算/CV/biosketch **继续 out of scope**。

### 3.2 Do（轻量）

| ID | 改动 | 验收 |
|---|---|---|
| PW-P1 | 迁评测到 `skills/proposal-writer/evals/`；保留 kaiti + review（含 2026-10-17 事后核对注） | 可发现 |
| PW-P2 | **核实 NSFC 2026 三部制**：用 NSFC 官方当年申请书填写说明 / 模板；二手新闻降级或删除；genres.md §5 写清核实日与 URL | 无「凭新闻当正式规则」 |
| PW-P3 | NSF/ERC/NIH 页数与标准：凡 candidate，改为「verify against current PAPPG / Information for Applicants / FOA」+ 示例链接；不把过期页数写成硬默认 | 与「call wins」一致 |
| PW-P4 | 新增 `references/zh-kaiti-register.md`（英文文件名，文中可给中英对照句式）：问题先行、文献按「缺口轴」组织、创新点一条一轴、技术路线图期望、进度用交付物而非活动。注明受常见中文开题习惯与用户教材语境启发，**不**大幅引用受版权保护的教材原文 | SKILL Phase 5 链到此文件 |
| PW-P5 | reviewer-lens：开题面板增「学校评议表优先」检查项（已有则强化一句）；确认 frequent weaknesses 含 single-source gap（已有则只加测试） | review.md 模板仍可用 |
| PW-P6 | （可选）为 kaiti 评测渲染 P2 技术路线 + P7 Gantt 各一 PNG | evals 目录 |
| PW-P7 | SKILL.md 加 Evals 小节；Outputs 列表与 ADR 0016 交叉链接 | 一致性 |

### 3.3 Do NOT

- 不要自动填学校字数/必备节（unknown 保留）。
- 不要在 Final 模式留 `[待查]`。
- 不要写预算表、人事、伦理批件正文。
- 不要用 paper-writer 的「零占位符」覆盖 ADR 0016。
- 不要为了「更像网上 grant skill」加入 Broader Impacts 长模板除非用户 call 要求——NSF 已有独立节说明即可。

---

## 4. 互联与回归

- `research-supervisor` 路由表已含二者 → polish 后只确认触发短语未丢。
- `paper-quickread` §9 → bridge；`study` → bridge；`deep-research` 文献地图 → proposal gap；`research-bridge` → idea-evaluator / experiment-workflow；`proposal-writer` → style-mine / paper-polish。
- 回归：重跑（或人工 diff）现有 SDID bridge 卡与 kaiti 评测，确认 polish 未破坏结构；新 RB-P4 / 可选 PNG 各一份。
- Lint：`python scripts/lint_skills.py`、`check_sources.py`、`check_checklists.py`、`check_shared_sync.py` 全过。

---

## 5. 验收标准（做完即停）

- [ ] 判决未被推翻：无大规模重写、无合并 skill。
- [ ] 评测归位或显式指针完成。
- [ ] NSFC 2026 断言已官方核实或已降级措辞。
- [ ] zh-kaiti-register 短文就位并被 SKILL 引用。
- [ ] bridge 有一份非估计量评测。
- [ ] candidate→confirmed 至少处理「能核的一批」；其余标明以 call 为准。
- [ ] lint 全绿；逻辑分 commit；push origin main（no force）。
- [ ] 中文汇报：改了什么、刻意没改什么、评测路径、遗留。

---

## 6. 参考 URL（调研用）

- Heilmeier Catechism: https://www.darpa.mil/about/heilmeier-catechism
- Pearl & Bareinboim transportability (Statistical Science 2014): 常见 PDF / DOI 10.1214/14-STS486
- NIH simplifying review framework: https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
- 开源 grant-proposal skill（对照，勿整包替换）: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/grant-proposal/SKILL.md
- research-grants skill 目录（对照）: https://skills.rest/skill/research-grants-mzane0803 、 https://www.getclaudeskills.com/skills/research-grant-writing-k-dense-ai
- 本仓库评测与 ADR：`skills/study/evals/bridge/**`、`skills/study/evals/proposal/**`、`docs/adr/0016-proposal-draft-markers.md`
- Handoff 原文（已过时的「一段话」规格）: `docs/handoff/supervisor-plus-reading-upgrade-SPEC.md` §8–§9

