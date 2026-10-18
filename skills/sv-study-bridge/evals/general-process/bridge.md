---
status: scratch
kind: bridge
mode: general
source: "personal experiment-log habit (ad-hoc Colab / local notebooks); no paper card"
project: none
date: 2026-10-17
---
# 学以致用（通用模式）：随手实验记录 → experiment-workflow

> Eval run 3 of research-bridge, **non-estimator / process** mode. No `research.yaml`. The skill asked one question: 「当前项目是什么？」 Simulated user: 「还没定；我想把以前在 Colab 里跑完把数字贴到聊天记录的习惯，迁到现在的实验流程。」 This card shows the skill is not limited to causal or statistical estimators. Learner level: can describe the habit; does not yet know `experiment-workflow` freeze / gold / runs-log rules.

## 1. 可移植的核心（一句话，不带领域词）
先冻结「用了什么数据、什么代码、什么接受标准」，再看结果；每个印到论文里的数字能指回一次有记录的运行。

## 2. 适合的项目长什么样（结构条件）
| 条件 | 为什么 | 出处 |
|---|---|---|
| 会多次改数据、提示词、种子或模型后再报一个数 | 没有冻结点，后见的选择会看起来像事先计划 | experiment-workflow Steps 1–3（补：映射到该 skill，不是论文定理） |
| 人或模型在标注、生成后再改金标准 | 「先看输出再改 gold」会让协议失效 | experiment-workflow Step 2 |
| 论文或附录要复现 | 需要 runs 日志、numbers 文件与可匿名的 artifact | experiment-workflow Steps 3–4 |

## 3. 不适合的情形（会断的地方）
| 情形 | 会怎样 | 出处 |
|---|---|---|
| 纯理论推导、没有运行产物 | 没有可冻结的 corpus / run；只记笔记即可 | experiment-workflow Overview（数学项目只用 runs/numbers/artifact） |
| 一次性探索、明确不进论文 | 全套冻结成本高于收益 | 补：先标 exploratory，不进 numbers 文件 |
| 把聊天记录当唯一日志 | 无法核对脚本、种子、数据快照 | 补：聊天没有 manifest |

## 4. 任何项目都要先查的假设
| 假设（出处） | 在你的项目里成立？ | 怎么查 | 不成立会怎样 | 对策 |
|---|---|---|---|---|
| 数据有可复述的快照（截止时间、计数、筛选） | 要问：现在的 CSV / API dump 还能按同一规则重拉吗？ | 对照 `data/MANIFEST.tsv` 或现有文件日期 | 数字无法复现 | 先写 freeze ADR，再跑 |
| 接受标准写在看结果之前 | 要问：bar / SESOI / 样本量是跑之前定的吗？ | 看脚本或笔记时间戳 | 看起来像 p-hacking | 把 bar 写进 run 脚本，失败就停 |
| 金标准在模型输出前冻结 | 要问：有没有改过 held-out 标签？ | 对比 gold 版本与第一次模型输出时间 | 协议失效 | 新版本 gold + 新 ADR，旧 run 标 superseded |
| 随机种子与 API 契约固定 | 要问：库版本、端点字段、默认种子是否写入？ | 对照环境锁文件与一次重跑 | 同脚本不同数 | 锁依赖；schema 变了当新实验 |

可检验：重跑能否对上 numbers 文件。只能靠论证：探索性工作是否承诺不进正文。

## 5. 最便宜证伪测试模板
- 问题：现有「笔记本 + 聊天贴数」习惯，能不能在不改分析结论的前提下，对上 experiment-workflow 的最小记录（freeze + 一次 run 行 + 一个印出的数）？
- 数据：已有的一次笔记本运行（不新采）。
- 步骤与指标：
  1. 从笔记本还原：数据文件哈希或行数、脚本或 notebook 版本、种子、打印的那个数。
  2. 按 experiment-workflow 模板写一行 `docs/runs.md` 和一条 numbers 记录。
  3. 用同一输入再跑一次（或只重算同一单元格）。
- 要试的变体：原笔记本；按 workflow 重跑。只这两个，全部报告。
- 预期结果：重跑得到同一数字（方向：相等）；若环境未锁，允许记录「不能复现」而不是改数。
- 失败判据（kill criterion）：还原不出数据快照，或重跑数字对不上且找不到已记录的原因 → **暂不**把该习惯当正式实验流程；先补 freeze，不把该数写入论文。
- 结果不明时：能还原输入但不能重跑（API 已变）→ 标 `[to verify]` / 不用该数，或只作初步结果并写清范围。
- 预算：约 1–2 小时（示意）；复用现有笔记本，不写新估计量。

## 6. 要变成具体建议，请告诉我
你的项目里，现在是哪个数字已经进了草稿或幻灯片、它来自哪次笔记本或脚本？有 `research.yaml` 的话走项目模式，裁决会落到五档之一（常见是 **改造后用**：保留探索笔记本，但进论文的数必须经 freeze + runs 日志）。

## 6b. 交接
- experiment-workflow：冻结数据、把 bar 写进脚本、记 run。
- research-records：freeze / gold 版本用 ADR。
- idea-evaluator / deep-research / study：不需要。
