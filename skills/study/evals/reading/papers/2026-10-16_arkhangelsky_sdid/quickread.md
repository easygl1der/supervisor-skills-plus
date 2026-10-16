---
paper: Synthetic Difference in Differences
authors: Dmitry Arkhangelsky, Susan Athey, David A. Hirshberg, Guido W. Imbens, Stefan Wager
venue: arXiv preprint (version July 2021)
id: arXiv:1812.09970
type: method
field: causal
tags: [panel-policy-evaluation, synthetic-control-weighting]
source: MinerU official CLI, flash-extract pp. 1-20 then precision extract all 69 pp., 2026-10-16; flash merged Table 1 cells (column order checked against §2.2), precision kept the table intact and agrees
read: 2026-10-16
---

# SDID 速读

## 1. 一句话
把合成控制的单位权重和时间权重放进双向固定效应回归，得到 SDID 估计量；在加州控烟案例和两组校准过的安慰剂模拟里，它的偏差和 RMSE 普遍不差于 DID 与 SC（§2–§3）。
标签：`panel-policy-evaluation` `synthetic-control-weighting`

## 2. 问题与动机
DID 靠平行趋势，原始数据里这条假设常常不成立；SC 靠重加权匹配处理前趋势，但通常只用于极少数处理单位，且回归里没有单位固定效应（§1）。两者被当成适用场景不同的工具，作者认为它们背后的假设其实很接近（§1）。

## 3. 核心想法
单位权重 ω 让加权对照组的处理前走势与处理组**平行**（允许截距 ω₀，不要求重合）；时间权重 λ 让加权的处理前时期能预测处理后均值；再把两组权重放进普通的双向固定效应回归（Eq. 1.1）。和 DID（Eq. 1.2）比多了「局部化」权重，和 SC（Eq. 1.3）比多了单位固定效应和时间权重。

## 4. 方法
- 估计量：加权 TWFE 回归 $\hat\tau^{\rm sdid}$（Eq. 1.1）；ω 由带 $\ell_2$ 正则的 (2.1) 求，ζ 取 (2.2)；λ 由不带正则的 (2.3) 求；步骤见 Algorithm 1（§2.1）。
- Estimand：处理组在处理后各期的平均效应 τ（Eq. 4.2，block assignment，即所有处理单位同一时刻开始处理）。
- 假设：A1 结果模型 $Y=L+W\circ\tau+E$，$L$ 为低秩因子结构（Eq. 4.1, 3.2）；A2 $E[E\mid W,L]=0$，分配可依赖 $L$ 但不能依赖 $E$（§3）；A3 单位之间误差独立，单位内可序列相关，跨单位同方差（§3, §4）；A4 信噪比条件、$E$ 序列相关不能太强、Γ 随时间稳定（§4 正文，正式条件在转写范围外）。编号为补。
- 推断：placebo 法标准误（Table 1 注；§5 Algorithm 4：从对照组抽 $N_{\rm tr}$ 个单位做安慰剂处理，取 B 次估计的方差；依赖单位间同方差）。可检验部分：处理前时期的平衡程度（§4）。

## 5. 结果
| 结果 | 数值 | 条件 / 数据 | 出处 |
|---|---|---|---|
| 加州提税效应（包/人/年），SDID / SC / DID / MC / DIFP | −15.6 / −19.6 / −27.3 / −20.2 / −11.1 | 1970–2000，38 个对照州 | Table 1；列序按 §2.2 正文核对 |
| 对应标准误 | 8.4 / 9.9 / 17.7 / 11.5 / 9.5 | placebo 法 | Table 1 |
| CPS 安慰剂 RMSE（baseline），SDID / SC / DID / MC / DIFP | 0.028 / 0.037 / 0.049 / 0.035 / 0.032 | 1000 次模拟，最低工资法分配 | Table 2 |
| PWT 安慰剂 RMSE（Democracy），SDID / SC / DID / MC / DIFP | 0.031 / 0.038 / 0.197 / 0.058 / 0.039 | N=111，T=48，1000 次模拟 | Table 3 |
| 去掉交互项 M 时的 RMSE，SDID / DID | 0.016 / 0.014 | CPS，“No M” 行 | Table 2 |

## 6. 贡献
- 【实证】在 CPS 与 PWT 两组校准安慰剂模拟中，SDID 的偏差与 RMSE 优于或接近 DID、SC、MC、DIFP（Table 2–3）。
- 【实证】加州案例中 SDID 的标准误小于 DID（Table 1）。
- 【证明】给出一致性与渐近正态的条件（Abstract，§4.3；定理已转写，条件未逐条核）。
- 【猜想】“SC 与 SDID 不一致时，后者通常更可信”（§2.2，为论证而非证明）。

## 7. 主张与证据对照
| 主张 | 证据与出处 | 强度 | 疑点 |
|---|---|---|---|
| SDID 稳健性好 | 模拟 Table 2–3；定理（§4） | 中 | 模拟的分配只依赖 $L$ 不依赖 $E$（Eq. 3.5），且全是零效应设计 |
| 加权还能提高精度 | Table 1 标准误；Table 2 Random 行 | 中 | 作者自己说异质性小时加权可能更差（§1）；Table 2 “No M” 行 DID 更好 |
| SC、SDID 不一致时 SDID 更可信 | §2.2 论证 + 模拟 | 弱 | 加州只是单一案例，没有真值可对照 |

## 8. 局限
| 作者承认 | 我们的判断 |
|---|---|
| 信噪比、序列相关、Γ 稳定等是 “nontrivial assumptions”（§4） | 只适用 block assignment；交错开始处理不在本文设定内（Eq. 4.2 前定义） |
| 系统异质性小时，加权可能降低精度（§1） | 模拟评估的是零效应安慰剂，异质处理效应下的偏差没有直接检验 |
| 需要历史背景排除同期其他冲击（§4） | 本次只读到 §4.1，§5 推断与正式定理未核 |

## 9. 与我方向的关联
如果项目做的是少量处理单位、平行趋势存疑的面板政策评估，SDID 可以作为 DID 和 SC 的并列稳健性检验，并报告单位与时间权重。用之前先确认处理是否同时开始。当前项目的 RQ 还不知道，告诉我后可以写得更具体。
