# 动画/交互式 HTML 图：场景目录（2026-10-16）

默认动画 = **HTML stepper**（`kit/vendor/ve/stepper.js`，思路来自 visual-explainer，MIT）：打开先显示全图，◀ ▶ / 播放 / 拖动条逐步看，每步一句说明。嵌进 Markdown 时 `render.sh x.html x.png --full --steps --gif` 产出整页 PNG、逐步 `-stepK.png`、竖排 `-strip.png`、可选 `.gif`（每帧 1.4 s）。**GIF 只是 stepper 的导出物，不再单独做“HTML 动画→录屏”**。

## 图式（pattern）速查
| 代号 | 图式 | 适合 | 模板 |
|---|---|---|---|
| P1 | 结构 stepper（节点/边逐步出现） | 有先后的结构演变 | `stepper.html` |
| P2 | 状态机回放（全图常驻，每步点亮一个状态+触发边，`data-s="0 k"`） | 流程、路由、循环 | `stepper.html` |
| P3 | 推导 stepper（每行一个变形 + 右栏“用到了什么”） | 证明、推导 | `stepper-proof.html` |
| P4 | 执行追踪（代码高亮行 + 数据结构 + 变量面板） | 算法、代码 | `stepper-trace.html` |
| P5 | 数值动画/轨迹（JS 计算真实数值后逐步画） | 优化、采样、收敛 | `stepper-plot.html` |
| P6 | small multiples（同一小图画多遍，只改一个变量） | 对比参数/情形/失败模式 | 任一模板 + `.grid` |
| P7 | 时间线（横轴年份/版本，逐步出现） | 概念演变、修改历史 | `stepper.html` 横排 |
| P8 | 概念讲解页（整页：问题→直觉→机制→边界→要记住的） | 讲透一个概念 | `explainer-page.html` |
| P9 | 流动点（沿边移动的点表示数据/梯度流，VE flow dots） | 数据流、前向/反向传播 | `stepper.html` + CSS offset-path（可选） |

## 场景 → 图式 → 归属 skill
| 领域 | 场景 | 图式 | 归属 skill |
|---|---|---|---|
| 因果 | 混杂/后门路径、IV 三条件、DID 平行趋势、选择偏差 | P8 + P1，P6 比较分层前后 | study |
| 因果 | 识别策略比较（回归调整 vs IV vs RDD vs DID） | P6 | study / deep-research（文献地图） |
| 编程 | git rebase / merge / cherry-pick / reset | P1（**demo**） | study |
| 编程 | 算法执行（二分、排序、DFS/BFS、DP 填表） | P4（**demo**：二分） | study |
| 编程 | 数据结构操作（堆插入、哈希冲突、链表反转） | P4 / P1 | study |
| 编程 | 并发/异步调用顺序 | 序列图 stepper（P1，泳道） | study |
| 流程 | 实验管线（数据→训练→评估→消融） | P2 | experiment-workflow / research-bridge |
| 流程 | 论文修改/投稿/rebuttal 流程 | P2 + P7 | paper-writing 系列 / style-mine |
| 流程 | ACA（自动化学术流程）工作流 | P2 | research-supervisor |
| 流程 | supervisor-skills 路由（按项目阶段推荐下一个 skill） | P2 | research-supervisor（README/DESIGN 图） |
| 流程 | study 概念协议 + study-vault 落盘循环 | P2（**demo**） | study（SKILL 文档自带） |
| 流程 | 多 agent / bot 路由（谁接什么消息、何时交接） | P2 + P9 | 文档用（非 skill 运行时） |
| 数学/统计 | OLS 无偏、CLT、Delta 方法、MLE 渐近正态 | P3（**demo**：OLS） | study（book-mode / paper-mode 的 method.md） |
| 数学/统计 | 估计量分布随 n 收敛（CLT 直观） | P5 + P6 | study |
| ML | 梯度下降/学习率、训练循环 | P5 + P6（**demo**） | study |
| ML | 注意力（Q·K → softmax → 加权 V） | P4 变体（矩阵逐格高亮）+ P9 | study |
| ML | 前向/反向传播 | P9 + P1 | study |
| 读论文 | 论文结构（问题→假设→方法→定理→实验→结论）一页图 | P1（逐节点出现）/ 静态 | paper-quickread |
| 读论文 | 方法 pipeline 逐步 | P2 | paper-quickread / study paper-mode |
| 读论文 | 和前人方法的差异（加了/删了哪条边） | P6 前后对比 | paper-quickread / deep-research |
| 学以致用 | 新方法挂进我的项目管线（哪一步替换） | P6 前后对比 + P2 | research-bridge |
| 综述 | 方法演变时间线 | P7（年份必须核对） | deep-research 文献地图 / proposal-writer |

## 使用规则
1. 只有“有先后”的内容才用 stepper；静态结构用单图。步数 4–8，每步一个变化 + 一句说明。
2. 打开即全图（首屏是答案）；不自动播放；`prefers-reduced-motion` 下无过渡。
3. 数值动画必须由页面 JS 真实计算（如 GD 的 $0.8^5\cdot2.6=0.85$），不手填；否则标「示意」。
4. 笔记里嵌最后一帧 PNG 或 strip；GIF 仅在 Cursor/GitHub 预览需要“会动”时生成。
5. 自检：`render.sh` 对全图做重叠/溢出/KaTeX/JS 检查；逐步帧要人工/模型看 strip 一遍。

## Demo（/workspace/study-visual-demos/ve2/）
| demo | 图式 | 撰写（估） | 渲染全部产物 | 文件 |
|---|---|---|---|---|
| git rebase | P1 | ~2 min | 2.7 s（5 帧+strip+GIF 96 KB） | git-rebase.* |
| 梯度下降 3 学习率 | P5+P6 | ~2 min（修 1 轮出界） | 2.9 s（6 帧，GIF 100 KB） | gradient-descent.* |
| OLS 无偏证明 | P3 | ~1.5 min | 2.5 s（5 帧，GIF 120 KB） | ols-proof.* |
| study 协议循环 | P2 | ~2 min（修 1 处标签重叠） | 3.1 s（7 帧，GIF 132 KB） | study-loop.* |
| 二分查找追踪 | P4 | ~2 min | 3.0 s（6 帧，GIF 100 KB） | code-trace.* |
渲染时间含 headless Chrome 启动、整页截图、逐帧截图、ffmpeg 拼 strip 与 GIF。
