# research-bridge / proposal-writer 调研结论（给用户）

**一句话**：这两个 skill **已经够用，不是薄草稿**；建议 **保留架构 + 轻量打磨**，不要推倒重写。

## 判决

| Skill | 判断 | 动作 |
|---|---|---|
| research-bridge | v1 成熟 | Keep + light polish |
| proposal-writer | v1 成熟 | Keep + light polish |

## 为什么说「不薄」

- **research-bridge**：完整「映射 → 假设迁移 → 五档裁决 → 先验 kill criterion」流程；引用了类比结构映射、外部效度/可迁移性、预注册与 forking paths；有两份真评测（SDID→项目、MLE 通用模式），质量高。
- **proposal-writer**：Call sheet → Heilmeier spine → 证据账本 → 时间线/风险 → 提案语体 → 评审透镜；覆盖开题 / PhD / NSFC / NSF / ERC / NIH；有 ADR 0016（Draft 允许 `[待查]`）；开题评测还自我抓虫并回写进 skill。

相对当初 SPEC 里各写四行的草图，SG 上的 Claude **已经超额完成**。

## 还差什么（只打磨这些）

1. 评测文件还塞在 `study/evals/` 下，应归到各自 skill。  
2. 不少出处标着 candidate；NSFC 2026「三部制」要用官方模板再核。  
3. 缺「刘汉中式 / 中文开题」语体短参考（结构句式，不是抄书）。  
4. bridge 缺一份非估计量（coding/流程）示范。  
5. 可选：补一张 study kit 出的路线图/前后对比 PNG。

## 不要做什么

不要 deep rewrite；不要并进 idea-evaluator；不要整包换成网上 grant skill；不要凭记忆填学校字数；不要把预算/CV 拉进 scope。

## 交给 SG Claude 的文件

- `/workspace/bridge-proposal-upgrade-SPEC.md`（完整打磨规格）  
- `/workspace/bridge-proposal-upgrade-PROMPT.md`（可直接粘贴的执行提示词）  
- 本摘要  

把 SPEC/PROMPT 拷进仓库 `docs/handoff/` 后，在 SG 上 `git pull`，再把 PROMPT 正文贴给 Claude 即可。本轮**不要**由调研 agent 直接 push 业务改动（除非你另有指示）。

## 外部对照（借检查项，不替换）

- DARPA Heilmeier：https://www.darpa.mil/about/heilmeier-catechism  
- Pearl & Bareinboim transportability（Statistical Science 2014）  
- 开源 grant-proposal / research-grants 类 Claude skill（NSF Broader Impacts、NSFC 创新点编号等）  
