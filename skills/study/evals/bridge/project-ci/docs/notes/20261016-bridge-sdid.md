---
status: scratch
kind: bridge
source: "arXiv:1812.09970 (SDID); files: reading/papers/2026-10-16_arkhangelsky_sdid/{quickread,method,insights,reflection}.md, study-vault/concepts/method-synthetic-did.md, study-vault/profile/knowledge.yaml"
project: ci-bugfix (fictional eval project)
date: 2026-10-16
verdict: 改造后用
---
# 学以致用：SDID → ci-bugfix

> Eval run 1 of research-bridge, project mode. Project is fictional (`../../research.yaml`, `../STATUS.md`). Reading root: `research.yaml` `reading.dir` → `skills/study/evals/reading/`. Learner level for SDID: `proficiency_ai: can-use`（knowledge.yaml），够用，不先转 study。

## 0. 一句话结论
**改造后用**：按 adoption cohort 分别做 SDID 再聚合，和现有 TWFE DID 并列报告；因为 SDID 正好针对「对照池整体不平行」这个痛点（单位权重只要求加权后平行，Eq. 2.1），但原文只覆盖 block assignment（Eq. 4.2），而 placebo 标准误依赖单位间同方差（Algorithm 4）。最便宜的证伪测试：在处理前数据上做 placebo-in-time，看假处理日的估计是否远离 0、权重是否压在一两个 repo 上。

## 1. 来源与目标
| | 来源（SDID） | 我的项目 |
|---|---|---|
| 研究问题 | 加州 1989 年加烟草税对人均卷烟消费的效应（quickread §5, Table 1） | RQ1：采用 CI 工具是否缩短 bug 修复时间（STATUS） |
| 痛点 | DID 的平行趋势在原始数据里常不成立；SC 通常只用于极少处理单位、没有单位固定效应（quickread §2, §1） | event-study 处理前系数漂移；处理 repo 少，cluster-robust SE 不可靠（STATUS Blockers） |

两个痛点都在来源的射程内，桥成立，继续。

## 2. 结构映射（source → target）
| 元素 | 来源 | 我的项目 | 类比在哪里断 |
|---|---|---|---|
| Unit | 州；38 个对照州 + 加州（quickread §5, Table 1） | repository | repo 规模、活跃度差异远大于州间差异（补）；影响单位间同方差（见 §3 A3） |
| Treatment / timing | 所有处理单位同一时刻开始（block assignment，Eq. 4.2 前定义） | 首次加入 CI 配置的月份，各 repo 不同（staggered） | **断**，但作者给了桥：正文估计量与定理只覆盖 block；附录 §8 建议按采用日期各做一次 SDID 再加权平均 |
| Outcome | 人均卷烟消费（包/人/年，Table 1） | repo-月 的 bug 修复时间中位数 | 修复时间右偏、低活跃月份可能缺失（补）；更要紧的是 CI 可能改变「什么算 bug、何时关闭」本身（见 §3 新增 B1） |
| Comparison | 单位权重 ω 选出的加权对照州，只要求与处理组平行（Eq. 2.1，截距 ω₀） | 从不采用的 repo 池，加权 | 对照池里需要有与处理 repo 走势相像的 repo；没有的话权重做不到平行（reflection Q3） |
| Time structure | 年度，1970–2000（Table 1） | 月度 | 月度噪声更大、序列相关更强（补）；A4 要求序列相关「不能太强」（quickread §4） |
| Estimand | 处理组在处理后各期的平均效应 τ（Eq. 4.2） | 采用者在采用后的平均效应（ATT 型） | 不外推到从不采用的 repo；分 cohort 后还要定聚合权重（补） |
| Inference | placebo 法（Algorithm 4，从对照抽 N_tr 个做假处理；依赖单位间同方差）；jackknife 在 N_tr=1 时无定义（Algorithm 3） | 处理 repo 少 | 少量处理单位正是 placebo 法的使用场景；但同方差在异质 repo 上存疑 |
| Scale | 1 个处理单位、38 个对照（Table 1 条件列） | 少量处理、大量对照（STATUS，具体数未冻结） | 对照多是好事；处理少意味着推断主要靠 placebo |

## 3. 假设迁移检查
| 假设（出处） | 在我这里成立？ | 证据 / 怎么查 | 不成立会怎样 | 对策 |
|---|---|---|---|---|
| A1 结果模型 $Y=L+W\circ\tau+E$，$L$ 低秩因子结构（Eq. 4.1, 3.2） | 未知 | 补：对照 repo 处理前矩阵做 SVD，看前几个奇异值是否占主导 | 权重无法同时平衡 L，偏差残留 | 只做稳健性检验 |
| A2 分配可依赖 $L$ 但不依赖噪声 $E$（Eq. 3.5） | **未知，最脆弱** | 补：查采用前几个月是否有 bug 修复时间异常上升（“修 bug 太慢 → 引入 CI”）；对应 reflection Q2 的加税例子 | 分配依赖冲击，权重再好也去不掉偏差（reflection Q2） | 只能靠论证 + 处理前异常检查；进 threats |
| A3 单位间误差独立，单位内可序列相关，跨单位同方差（§3, §4；placebo 依赖同方差，Algorithm 4） | 独立：基本是（补，需查共享贡献者）；同方差：**否，可能性大** | 补：按 repo 规模分层看处理前残差方差 | placebo SE 失真 | 结果变量取对数或按活跃度分层（补）；SE 方法换 bootstrap 需 N_tr 足够（Algorithm 2，条件待核） |
| A4 信噪比、序列相关不太强、Γ 随时间稳定（§4 正文；正式条件在转写范围外） | 未知 | 原文条件未核（quickread §4、method §5） | 理论保证不成立 | 先 study §4.3 定理条件，或接受只有模拟证据 |
| Block assignment（Eq. 4.2 前定义） | **否** | STATUS：adoption 月份各异 | 原文估计量不直接适用 | 按 cohort 分别做 SDID 再聚合：这正是原文附录 §8 的做法（权重为各批次处理单元占比）；Stata `sdid` 的实现覆盖 staggered adoption [lit:clarke2024]；该做法的推断原文未给定理 |
| 新增 B1：CI 不改变结果变量的定义（bug 标签、关闭流程） | 未知 | 补：比较采用前后 bug 标签使用率、自动关闭比例 | 测到的是记录方式变化而非修复速度 | 换结果定义（如只看人工关闭）或在 threats 中限定 |
| 新增 B2：采用 CI 时没有同期的其他流程变化 | 未知 | 补：同月是否同时引入 code review bot、迁移仓库等 | 效应混入其他变化（quickread §8：作者也要求用历史背景排除同期冲击，§4） | 排除同期变化的 repo，或作为 threats |

可检验：A1（处理前矩阵结构）、A3 同方差、B1、处理前平衡。只能靠论证：A2、B2 的一部分 → 进 threats 节（`threats.md` TH-08 alternative explanations）。

## 4. 结论与怎么用
- 判定：**改造后用**，因为痛点匹配（§1），而 timing 断（§2 Treatment 行）与同方差存疑（§3 A3）都有可操作的改造；A2 不可检验，但对 TWFE DID 同样成立，不构成偏向现方法的理由。
- 改动的管线步骤：之前「TWFE DID 单一 post 指示变量」→ 之后「TWFE DID 与 per-cohort SDID 并列，报告单位权重 ω 与时间权重 λ（quickread §9 建议）」。
- 论文主张：从「CI 缩短修复时间」变成「在采用 CI 的 repo 上，相对于加权可比 repo，采用后修复时间变化 X」：scope 限于采用者（Eq. 4.2 的 estimand），不推广到所有 repo。
- 它不能给你的：对 A2（因 bug 激增而采用）的保护；异质处理效应下的偏差，原文模拟未直接检验（quickread §8，「我们的判断」）；它也不一定比 DID 更好：没有交互结构时 DID 的 RMSE 略低（Table 2 “No M” 行，DID 0.014 vs SDID 0.016）。
- 和已有 ADR 的关系：无 ADR，无冲突。
- Method-shopping 提醒：这次桥接的动机是现方法的处理前趋势不好看（STATUS Blockers）。因此两种估计量都在跑之前写定，**都报告**，不按结果挑。

## 5. 最小验证实验（2026-10-16 写定，运行前）
- 问题：在本项目数据上，SDID 的加权对照能否在处理前做到平行，且在没有真实处理的地方给出接近 0 的估计？（测 §2 Comparison 行、§3 A1/A3；不测 A2）
- 数据：只用现有面板中各处理 repo **采用前**的月份，以及对照池。不新采集。
- 步骤与指标：
  1. Placebo-in-time：每个 cohort 把假采用日设在真实采用前 k 个月（k 事先定，补），只用假采用日之前的数据算权重，跑 SDID（Eq. 1.1，Algorithm 1）。指标：假效应估计及其 placebo SE（Algorithm 4）。
  2. 权重诊断：ω 的有效对照数（补：$1/\sum\omega_i^2$）、最大单个权重。
  3. Known-answer 检查（补）：在对照 repo 的后期人为加上一个已知效应（大小 = 下面的 SESOI），看 SDID 能否回收。
- 要试的变体（全部列出，全部报告）：SDID、TWFE DID；结果取原值与取对数；k 只取一个值。不再加其他估计量。
- 预期结果：placebo 估计方向上无系统偏离 0；known-answer 能大致回收注入效应。量级：原文没有可迁移的数字，不写。
- 失败判据（kill criterion）：任一条成立就降级为「只做稳健性检验」或「不用」：(a) 多数 cohort 的 placebo 估计绝对值 ≥ SESOI；(b) 权重集中在一两个 repo；(c) known-answer 检查回收不到注入效应的方向。SESOI：由团队在跑之前根据「多少天的修复时间变化对开发者有意义」写定并给理由（Lakens et al. 2018 的思路），本卡不替团队定数。
- 结果不明时（placebo 估计小但 SE 很大）：保留为稳健性检验，不作主结果；记录原因。
- 各结果的下一步：通过 → experiment-workflow 冻结数据与 cohort 定义，正式跑；失败 → research-records 写 ADR「不采用 SDID 作主方法」并保留 TWFE + 其他 staggered 估计量；不明 → 只在附录报告。
- 预算：约半天到一天（示意）；复用现有面板和 synthdid / sdid 软件包，不写新估计代码。

## 6. 交接
- experiment-workflow：冻结面板快照与 cohort 定义；把 SESOI 和 kill criterion 写进 run 脚本的 bar；在 `docs/runs.md` 记 placebo run。
- research-records：验证结束后写 ADR「主方法：TWFE DID + per-cohort SDID 并列」，拒绝的备选写清（只用 TWFE；只用 SDID）。
- deep-research：核对 staggered SDID 的聚合方式与推断（Clarke et al. 2024；arXiv 版附录 §8 已有按日期分组的做法，2026-10-17 核对；推断性质未核）；查 MSR 里 CI 采用效应的既有研究（novelty）。
- study：A4 的正式条件（§4.3 Theorem 1）还没核；若要在论文里引定理，先补这一块（concept note 的「待解决的问题」已列）。
- idea-evaluator：不需要；研究问题没变，只换估计策略。

## Sources
- lit:clarke2024: Clarke, D., Pailañir, D., Athey, S., and Imbens, G. (2024). Synthetic difference-in-differences estimation. Stata Journal, 24(4), 557-598 (IZA DP 15907, 2023). Verified 2026-10-16 via the IZA listing: covers single and staggered adoption.
- lit:lakens2018: see `skills/research-bridge/references/transfer-checks.md` §8.
