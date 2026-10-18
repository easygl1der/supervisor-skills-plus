# 第 4 章练习（MLE 这条线）

目标是理解，不是刷题：每题先自己试，卡住再一级一级展开提示。书中没有给解答，下面的解都是「自解，待核」。

## 1. Exercise 4.1：高斯的 MLE

证明 $\hat\mu=\frac1N\sum y_n$（Eq. 4.247），$\hat\sigma^2=\frac1N\sum(y_n-\hat\mu)^2$（Eq. 4.248）。

<details><summary>提示 1（方向）</summary>写出对数似然，分别对 μ 和 σ² 求偏导、令为零。</details>
<details><summary>提示 2（关键事实）</summary>对数似然是 $-\frac N2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum(y_n-\mu)^2$；对 σ² 求导时把 σ² 当成一个整体变量 v。</details>
<details><summary>提示 3（部分步骤）</summary>对 μ：$\frac1{\sigma^2}\sum(y_n-\mu)=0$。对 v：$-\frac N{2v}+\frac1{2v^2}\sum(y_n-\mu)^2=0$。</details>
<details><summary>解（自解，待核）</summary>由提示 3 第一式得 μ̂ = ȳ；代入第二式得 v̂ = (1/N)Σ(y_n − ȳ)²。二阶条件：对数似然在 μ 上是凹的，在 v 上于驻点处二阶导为 −N/(2v̂²) &lt; 0，是最大值。</details>

## 2. Exercise 4.7：方差的 MLE 有偏

证明 $\mathbb E[\hat\sigma^2_{\rm MLE}]\ne\sigma^2$。

<details><summary>提示 1（方向）</summary>把 $\sum(x_n-\bar x)^2$ 拆成 $\sum(x_n-\mu)^2-N(\bar x-\mu)^2$。</details>
<details><summary>提示 2（关键事实）</summary>$\mathbb E[(x_n-\mu)^2]=\sigma^2$，$\mathbb V[\bar x]=\sigma^2/N$。</details>
<details><summary>提示 3（部分步骤）</summary>$\mathbb E\big[\sum(x_n-\bar x)^2\big]=N\sigma^2-\sigma^2$。</details>
<details><summary>解（自解，待核）</summary>除以 N 得 E[σ̂²] = (N−1)σ²/N，与 Eq. 4.234 一致。</details>

## 3. Exercise 4.8：已知 μ 时的方差估计

<details><summary>提示 1（方向）</summary>和 4.1 一样求导，但 μ 不再是未知量。</details>
<details><summary>提示 2（关键事实）</summary>不用 x̄，所以没有“用掉一个点”。</details>
<details><summary>解（自解，待核）</summary>σ̂² = (1/N)Σ(x_n − μ)²，期望为 σ²，无偏。和 4.7 对比：偏差完全来自用 x̄ 代替 μ。</details>

## 4. Exercise 4.9：MSE 的比较（原文疑有误）

先证 Eq. 4.258，再算两个估计量的 MSE。**注意**：书中给出的两个 MSE 结果我们认为下标对调了，见 `notes.md` 第 5 节。请自己算，看你得到哪个。

<details><summary>提示 1（方向）</summary>MSE = 方差 + 偏差²。</details>
<details><summary>提示 2（关键事实）</summary>Eq. 4.259：$\frac{N-1}{\sigma^2}\sigma^2_{\rm unb}\sim\chi^2_{N-1}$，方差 $2(N-1)$；$\sigma^2_{\rm mle}=\frac{N-1}N\sigma^2_{\rm unb}$。</details>
<details><summary>解（自解，待核）</summary>MSE(σ²_unb) = 2σ⁴/(N−1)；MSE(σ²_mle) = 2(N−1)σ⁴/N² + σ⁴/N² = (2N−1)σ⁴/N²。后者更小。</details>

## 5. 补题：MLE 与最小二乘（为 SDID 准备）

设 $y_n=w^\top x_n+\varepsilon_n$，$\varepsilon_n\sim\mathcal N(0,\sigma^2/c_n)$，$c_n>0$ 已知。证明 $w$ 的 MLE 就是以 $c_n$ 为权重的加权最小二乘。

<details><summary>提示 1（方向）</summary>写出 NLL，去掉和 w 无关的项。</details>
<details><summary>提示 2（关键事实）</summary>第 n 项是 $\frac{c_n}{2\sigma^2}(y_n-w^\top x_n)^2$ 加常数。</details>
<details><summary>解（自解，待核）</summary>NLL(w) = const + (1/2σ²)Σ c_n (y_n − wᵀx_n)²，argmin 即加权最小二乘。所以 SDID 的 Eq. 1.1 可以读成“误差方差与 1/(ω_i λ_t) 成正比时的高斯 MLE”；这只是读法，SDID 的论证并不依赖这种噪声假设。</details>
