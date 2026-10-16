# SDID 方法拆解

公式照抄原文并标号；标「补」的是我们补的步骤。

## 1. 估计量（Eq. 1.1）

$$\left(\hat\tau^{\rm sdid},\hat\mu,\hat\alpha,\hat\beta\right)=\arg\min_{\tau,\mu,\alpha,\beta}\Big\{\sum_{i=1}^N\sum_{t=1}^T\big(Y_{it}-\mu-\alpha_i-\beta_t-W_{it}\tau\big)^2\,\hat\omega_i^{\rm sdid}\hat\lambda_t^{\rm sdid}\Big\}$$

| 项 | 作用 | 去掉会怎样 |
|---|---|---|
| $\alpha_i$（单位固定效应） | 吸收各州之间的常数差 | 就成了 SC 式回归（Eq. 1.3），常数差要靠权重完全拟合 |
| $\beta_t$（时间固定效应） | 吸收所有州共同的年度冲击 | 共同冲击会混进 $\tau$ |
| $\hat\omega_i$ | 让对照组与处理组走势平行 | 回到 DID（Eq. 1.2），不像的州同样有发言权 |
| $\hat\lambda_t$ | 让处理前年份能预测处理后 | 所有处理前年份等权，早期不像的年份也算进来 |

## 2. 单位权重（Eq. 2.1, 2.2）

$\ell_{unit}(\omega_0,\omega)=\sum_{t=1}^{T_{\rm pre}}\big(\omega_0+\sum_{i=1}^{N_{\rm co}}\omega_iY_{it}-\frac1{N_{\rm tr}}\sum_{i=N_{\rm co}+1}^NY_{it}\big)^2+\zeta^2T_{\rm pre}\|\omega\|_2^2$，约束 $\omega\ge0$、$\sum_{i\le N_{\rm co}}\omega_i=1$（Eq. 2.1）。

- 补：$\omega_0$ 是截距，所以最优解只要求两条线在处理前**相差一个常数**，这正是“平行”的意思。
- $\zeta=(N_{\rm tr}T_{\rm post})^{1/4}\hat\sigma$，$\hat\sigma$ 取对照组处理前一期变动的标准差（Eq. 2.2）。
- 去掉 $\omega_0$ 且 $\zeta=0$，就退化为 Abadie 等人（2010）在单个处理单位时的权重（§2.1）。

## 3. 时间权重（Eq. 2.3）

$\ell_{time}(\lambda_0,\lambda)=\sum_{i=1}^{N_{\rm co}}\big(\lambda_0+\sum_{t=1}^{T_{\rm pre}}\lambda_tY_{it}-\frac1{T_{\rm post}}\sum_{t=T_{\rm pre}+1}^TY_{it}\big)^2$，约束 $\lambda\ge0$、处理前权重和为 1、**处理后各年 $\lambda_t=T_{\rm post}^{-1}$**。

- 补：处理后的权重被约束固定，优化只在处理前年份里分配权重。这一点正是模拟复述里的误解所在（见会话记录）。
- 不加正则：作者用允许单位内相关、单位间独立的设定来解释这一选择（§2.1）。

## 4. 等价写法（Eq. 2.4, 2.5）

$\hat\tau=\hat\delta_{\rm tr}-\sum_{i=1}^{N_{\rm co}}\hat\omega_i\hat\delta_i$，其中 SDID 的 $\hat\delta_i=\frac1{T_{\rm post}}\sum_{t>T_{\rm pre}}Y_{it}-\sum_{t\le T_{\rm pre}}\hat\lambda_tY_{it}$。

- 补：把 $\hat\lambda$ 换成等权 $1/T_{\rm pre}$、$\hat\omega$ 换成 $1/N_{\rm co}$，就得到 DID 的 $\hat\delta^{\rm did}$（Eq. 2.5 第二行）。

## 5. 设定与目标（§3–§4）

- 结果模型 $Y=L+W\circ\tau+E$（Eq. 4.1），$L=\Gamma\Upsilon^\top$ 低秩。
- 分配：$D_i$ 可依赖 $\alpha_i$ 和 $M_i$，但独立于 $E_i$（Eq. 3.5 与脚注 6 前的说明）。
- Estimand：处理组处理后各期效应的平均（Eq. 4.2，block assignment）。
- 正式的一致性与渐近正态定理在 §4.3（Theorem 1），已转写，条件未逐条核。
- 推断（§5）：bootstrap（Algorithm 2）、jackknife（Algorithm 3，$N_{\rm tr}=1$ 时无定义）、placebo（Algorithm 4，依赖单位间同方差）。
- 原文疑点（待核）：Table 4 图注说前三列是 Placebo、最后三列是 bootstrap，而表头顺序是 Bootstrap / Jackknife / Placebo。
