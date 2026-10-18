---
concept: maximum likelihood estimation
aliases: [MLE, 最大似然估计]
status: 能用
related: [[def-kl-divergence]], [[method-map]], [[method-ols]], [[method-synthetic-did]]
sources: ["Murphy, PML 1, §4.2, §4.7.6 (PDF pp. 137–196)"]
updated: 2026-10-16
---
# 最大似然估计（MLE）

## 一句话直觉
选一个参数，让手里这批数据在模型下“最不意外”；等价地，让模型分布尽量贴近数据的经验分布。

## 动机与来历
需要一个通用的“从数据到参数”的规则。MLE 有两个理由：均匀先验下的后验众数（Eq. 4.9），以及最小化到经验分布的 KL（Eq. 4.13–4.15）。

## 原理
例子：抛硬币 $\hat\theta=N_1/N$（Eq. 4.25）。一般：iid 下似然拆成乘积，取负对数变成求和（Eq. 4.3–4.6）。定义：$\hat\theta=\arg\min_\theta\text{NLL}(\theta)$（Eq. 4.7）。

## 图
![图 1：第 4 章概念图](../books/murphy-pml1/ch04-statistics/fig-ch04-concept-map.png)
![图 2：KL 推导五步](../books/murphy-pml1/ch04-statistics/fig-mle-kl-proof-strip.png)

## 和已知概念的关系
| 已知概念 | 相同 | 不同 | 类比在哪里失效 |
|---|---|---|---|
| OLS | 高斯噪声下解相同（Eq. 4.59） | OLS 是损失，MLE 是概率模型 | 噪声非高斯时不再相同 |
| 无偏估计 | 都是估计量的好坏标准 | MLE 不保证无偏 | 高斯方差（Eq. 4.234） |
| MAP | 都是取一个点 | MAP 多一个先验项（Eq. 4.9） | 小样本时差别大 |

## 常见误解
- “MLE 总是无偏” → 高斯方差 MLE 除以 N，偏小（§4.7.6.1）。会话：`sessions/2026-10-16_mle.md`。
- 易混：一致性（N→∞ 时收敛）与无偏性（每个 N 期望都对）。
