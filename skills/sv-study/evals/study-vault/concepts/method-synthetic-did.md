---
concept: synthetic difference in differences
aliases: [SDID, 合成双重差分]
status: 理解中
related: [[method-difference-in-differences]], [[method-synthetic-control]], [[method-event-study]]
sources: ["Arkhangelsky et al., arXiv:1812.09970, §1–§4.1"]
updated: 2026-10-16
---
# 合成双重差分（SDID）

## 一句话直觉
只在和处理组走势相像的对照单位、和处理后相像的处理前年份上做 DID。

## 动机与来历
DID 需要全体对照组平行，常不成立；SC 能拼走势，但要求拼得重合、没有单位固定效应。SDID 把两者写成同一个加权双向固定效应回归的不同权重（Eq. 1.1–1.3）。

## 原理
例子：加州 1989 年加税，五种估计差很多（Table 1）。一般：加权 TWFE 回归。定义：Eq. 1.1；单位权重 Eq. 2.1（带截距、正则 Eq. 2.2）；时间权重 Eq. 2.3（处理后等权）。

## 图
![图 1：两组权重各管一件事，最后进入同一个加权回归](../../reading/papers/2026-10-16_arkhangelsky_sdid/fig-sdid-explainer-fig1.png)
![图 2：纠正后的心智模型](../../reading/papers/2026-10-16_arkhangelsky_sdid/fig-sdid-mental-v2.png)

## 和已知概念的关系
| 已知概念 | 相同 | 不同 | 类比在哪里失效 |
|---|---|---|---|
| DID | TWFE 回归 | 加权 | 平行趋势只对加权后的对照组 |
| SC | 处理前拟合选权重 | 截距、正则、时间权重、单位固定效应 | 不要求重合 |
| event study | 关注处理前各期 | 权重由数据定 | event study 常只用最后一期 |

## 复述与诊断记录
见 sessions/2026-10-16_synthetic-did.md：第 1 轮 机制 1/3、条件 0/3、边界 0/2；第 2 轮 机制 3/3、条件 2/3、边界 1/2。

## 待解决的问题
- [ ] placebo 标准误（§5）
- [ ] 定理中的信噪比条件
