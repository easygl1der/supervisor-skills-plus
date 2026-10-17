# 自评：kaiti.md 对照 proposal-writer Checklist 与 reviewer lens

评测对象：同目录 `kaiti.md`（Draft）。结论先行：骨架（spine）站得住，最大风险是核心 Aim 的新颖性未检索；文献综述过度依赖一篇论文。

## Checklist

| 项 | 结果 | 证据 |
|---|---|---|
| PW-01 Call sheet sourced | unknown | §0 学校模板、字数、评议表全部 unknown，已列为待用户提供；没有凭记忆填限制 |
| PW-02 Question answerable | pass | RQ1–RQ3 各自写明对象、比较与证据（§1） |
| PW-03 Aims independent | pass | §1 级联检验表：A2 有 block 子样本替代输入，A3 只用对照单位 |
| PW-04 Feasibility shown | pass（有缺口） | A1、A3 以原文 Algorithm 1、Table 2–3 设计为依据；A2 无试点数据，已在表中写明并以 M2.1 为第一个里程碑 |
| PW-05 Falsifiable milestones | pass（修订后） | 初稿 M1.1 写成“无明显偏差”“同量级”，不可证伪；已改为阈值 T1–T3 + 何时由谁写入 ADR。此问题已回写进 skill（timeline-risk.md §1） |
| PW-06 Risks paired with fallbacks | pass | R1–R4 均有早期信号、缓解、备选与决定时点；R2 的敏感性方法仍是 [待查] |
| PW-07 Gap claims scoped | pass（Draft） | §3.5 声明“限定在已检索、已阅读范围”；但实际只读了一篇论文，未跑检索。Final 前必须完成 M0 |
| PW-08 Contributions checkable | pass | §7 三个创新点各对应一个 Aim、一个轴、一个交付物 |
| PW-09 Register | pass | 计划用将来时（“将”“拟”），原文结果用过去/现在时并标 Table；无把计划写成发现的句子 |
| PW-10 Reviewer criteria answered | unknown | 无学院评议表 |
| PW-11 Limits; no markers in Final | n/a | Draft 模式；共 14 处 [待查] |
| CI-01 Estimand before estimator | pass | RQ1 先问 estimand，再谈估计量 |
| WR-21 Causal words need a causal design | pass | “效果”只用于估计目标；未对 SE 工具效应下任何结论 |
| WR-24 Novelty scoped | pass（Draft） | 创新点一写明“前提：R1 不成立” |
| WR-28 Every citation supports its sentence | pass（已有部分） | 所有原文引用均可在 quickread/insights/reflection/method 中找到对应 §/Eq./Table；其余为 [待查] |
| TH-08 Alternative explanations named | pass | R2（分配依赖冲击）、R3（无交互项时 DID 更好） |

## Reviewer pass（通用 lens）

- Skim test：只读 §1 能说出问题、缺口、做法；“为什么是这个申请人”答不出（§8 只有阅读进度）。
- Heilmeier 第 6 问（资源）只有“待确认”。

最可能导致不通过的三点：

1. **核心 Aim 的新颖性未核（R1）**。若交错采纳版本已存在，研究内容一要整体改写。修正：开题前完成 M0，而不是开题后。已回写进 skill：Phase 2 在起草前做核心 Aim 的新颖性检索（借 idea-evaluator F1 的方法）。
2. **综述依赖单一来源**。§3.1–3.3 全部来自一篇论文，§3.4 全是 [待查]，评审会认为对领域掌握不足。修正：交 deep-research（文献地图模式）补交错 DID 与 SE 工具评估两条线。已回写进 skill：reviewer-lens 增加 “Single-source gap”。
3. **A2 的工具与结果变量未定**（“某工具”“开发指标”）。修正：在 M2.1 之前选定一种工具与一个结果变量，并做一周试点。

## 对 skill 的回写

| 发现 | 改动 |
|---|---|
| 里程碑判据容易写成形容词 | timeline-risk.md §1：未定阈值写成命名符号 + 由谁、何时写入 ADR |
| 新颖性检索放在开题之后代价最大 | SKILL.md Phase 2：起草前对核心 Aim 做检索；无检索能力时把它设为第一个里程碑 |
| 阅读笔记的覆盖范围（读到 §4.1、定理条件未核）需要带进提案 | SKILL.md Phase 3：覆盖范围写入 ledger；超出范围的陈述算 gap claim 或 [to verify] |
| 缺口只靠一篇论文 | reviewer-lens.md §5 新增 “Single-source gap” |

## 未做

- 未生成技术路线图与 Gantt 的 PNG（study kit 可做，P2/P7）。
- 未跑 paper-writer 的独立引用核查（只有一篇真实引用，其余是 [待查]）。

## 事后核对（2026-10-17）

R1 在原文自己的附录 §8 命中：作者已给出交错采纳下按日期分组再加权的 SDID。初稿只读到 §4.1，正好是 Phase 3 “阅读覆盖范围进账本”要防的情况：没读到的部分只能算缺口假设，不能当作缺口事实。
