# study 作图规范（visuals.md）

## Contents
1. 什么时候用哪种模板 · 2. 内容规则 · 3. 视觉规则 · 3b. 结构图视觉 token · 4. 渲染与自检 · 5. 各环境 · 6. 来源

默认：**HTML（SVG + KaTeX）**。每张图产出两份：`<name>.html`（原件，可改、可交互）+ `<name>.png`（嵌进笔记 `![图N：结论句](name.png)`）。
Graphviz 只在节点多、需要自动排版且浏览器内 elkjs/dagre 不够时用（导出 SVG 再嵌进 HTML）。TikZ 只给要进论文的图。不用 Manim、不默认用 Mermaid。

## 1. 什么时候用哪种模板（templates/）
| 场景 | 模板 | 何时用 |
|---|---|---|
| 讲 motivation / 生活场景 | `scene-cards.html` | 3–5 个实体 + 带动词的箭头；第一次见到概念 |
| 讲“它解决了什么问题”的故事 | `comic-4panel.html` | 起-承-转-合：现象 → 直觉错误 → 发现问题 → 新概念 |
| 严谨结构 / 正式笔记 | `textbook-dag.html` | ≤6 个节点、手摆坐标；因果 DAG、定理依赖 |
| 大图 / 结构还在变 | `auto-dag-elk.html`（默认）；`-dagre` 备用 | >6 个节点，只写 nodes/edges，浏览器内自动布局；边按布局算出的路径画成曲线，不会穿过节点。实测 elk 交叉更少。边上有动词时加 `labelsAsNodes:true`（标签变成参与布局的文字节点，不压线）；标签比圈长时加 `fitLabels:true` 或单个节点 `r`；太散或太挤调 `spacing:{node, layer}`（默认 40 / 90）。例：`evals/reading/lit-map/fig-lit-map.html` |
| 几十个节点 | Graphviz `dot -Tsvg`，SVG 嵌进 HTML | 浏览器布局仍乱时才用；边标签多时加 `decorate=true`（标签用细线连到边，不会认错边） |
| 心智模型 / 诊断复述 | `mind-map.html` | 中心概念 + 三层（核心机制 / 成立条件 / 边界与推论）；叶子 status=ok/fix/new 着色 |
| 数据直觉 | matplotlib / Vega-Lite（另生成） | 只有在有真实或明确标注“模拟”的数据时 |
| 演变时间线 | scene-cards 横排或 `stepper.html` 横排 | 年份必须核对出处，否则不写年份 |
| 讲透一个概念（整页） | `explainer-page.html` | 问题→直觉图→机制→边界(small multiples)→要记住的；`--full --figures` |
| 有先后的过程：结构演变 / 流程状态机 | `stepper.html` | 4–8 步，打开即全图；`--steps [--gif]` |
| 证明、推导 | `stepper-proof.html` | 每行一个变形 + 右栏“用到了什么” |
| 算法 / 代码执行 | `stepper-trace.html` | 高亮行 + 数据结构 + 变量面板；状态由页面 JS 实际运行算法生成（`trace()` 记录每步），再加一行 `console.assert` 检查不变式，不手填数组；例：`evals/demo/fig-lomuto-partition.html` |
| 数值过程（优化、收敛） | `stepper-plot.html` | 页面 JS 真实计算，不手填数字 |

一个概念最多 2–3 张图：通常 1 张 motivation（卡片或漫画）+ 1 张结构（DAG / 心智模型）。

## 2. 内容规则（硬性）
- **不编数字**：图上的数字只能来自原文（标 §/Table/Fig）、真实计算，或明确标「示意」。年份、作者凭记忆不写。
- **每个事实先找位置**：节点标签、边上的动词、图注，图注写一句结论（借 visual-explainer “Give every fact a place”）。
- 颜色不单独承载信息：同时用实线/虚线、形状或图例。
- 例子找不到合适的就不画场景图，直接画结构图，不硬凑。
- 数学一律 KaTeX：`$...$` 行内；`<` 写成 `&lt;`；不要用 Unicode 伪公式。SVG `<text>` 里 KaTeX 不生效：不要写 `ω̂`、`τ̂` 这类组合附加符（中文字体下会渲染成 `ω^`，检查脚本查不出来），改写成「ω 的估计」或把公式放进 HTML 图注 / foreignObject。

## 3. 视觉规则
- 字体（离线，不走 Google Fonts CDN）：正文 `Noto Sans CJK SC`（回退 PingFang SC / Microsoft YaHei），标题 `Noto Serif CJK SC`，等宽标签 `Noto Sans Mono CJK SC`；手写感用 `LXGW WenKai`。字体是系统字体，不打包。
- 调色板（`vendor/kit.css`）：墨色 #1f2328，处理 `--c1` 蓝，混杂 `--c2` 橙，结果 `--c3` 绿，强调/错误 `--warn` 红。一张图只有一个强调色焦点。
- 字号：`html{font-size:17px}`，scale .75/1/1.25/1.625rem；正文 ≥16px，SVG 标签 ≥12px；间距只用 .25/.5/.75/1/1.5/2/3/4.5rem。避免霓虹、渐变、紫色模板感。
- 图注一律以「图 N」开头，后面一句结论（不是主题）。
- emoji 只用在场景卡片和漫画里；教科书 DAG 不用。
- 坑：在已存在的 `<svg>` 上用 innerHTML 写 `stroke="var(--x)"` 时不可靠，颜色先用 `getComputedStyle` 取出实际值再写。

## 3b. 结构图/讲解页/stepper 的视觉 token（来自 visual-explainer Paper 风格，见 vendor/ve/）
- 用 `vendor/ve/ve.css`（Paper·light，只做浅色）：`--bg #f7f7f4 --surface #fff --border #e3e3dc --border-bright #8e8e8a --text #17191c --text-dim #575c63 --accent #2c4cd0 --ok #1d7443 --warn #836000 --risk #b3301d --info #1b6a94`；强调色 ≤10%，每屏一个焦点。
- 舞台：dot-grid 背景 + 1px 边框 + 10px 圆角；节点 rx 6、1.5 描边；关键节点浅底 + 2px 描边；边 1.75，主角边 2.75。
- 线型语义：实线 = 因果/流向；虚线 = 被禁止或未观测；红色加粗 = 本图要你看的路径（如后门路径）；红 ✕ = 该路径必须不存在（如排他性）。
- 图原则：一图一论断（图注「图 N」+ 结论句）；画机制不画名字，每条边写动词；状态靠线型/形状+颜色；多情形用 small multiples；每个事实先在图里找位置。
- 禁止：紫色/霓虹/玻璃拟态/渐变/全部居中/卡片彩色侧条；结构图不用 emoji（场景卡和漫画例外）。
- 手画 SVG：先 ASCII 草图再定坐标；节点间距 ≥40；每行 ≤12 个汉字；先画边后画节点；>12 节点拆图或改 elk。`<svg role="img" aria-label>`。
- 动画默认 stepper，GIF 只是它的导出物（`--steps --gif`）。

## 4. 渲染 → 截图 → 自检循环（必须）
1. 写/改 HTML（只改模板顶部的 SPEC / CARDS / PANELS / BRANCHES 数据块）。脚本结束时设 `window.__READY = true`。
2. `./render.sh fig.html fig.png [--full] [--figures] [--steps] [--gif]`（--full 整页；--figures 每个 figure 单独截；--steps 每步截图+竖排 strip；--gif 用 ffmpeg 合成）（headless Chrome，2× 截 `#fig`；Chrome 自动找 macOS/Linux/Windows 默认路径，`CHROME=` 可覆盖）。脚本自动检查：文字框互相重叠（按文字本身的紧边界算）、**线穿过文字**（`text-on-line`，被不透明框或标签底色遮住的部分不算；故意的可加 `data-cross-ok`）、**边穿过节点**（`edge-through-node`）、溢出 `#fig`、KaTeX 错误、JS 报错、未填 `{{占位符}}`。退出码 2 = 有警告，3 = 找不到 Chrome。
3. **打开 PNG 自己看一遍**（能看图的环境必须看）：箭头方向对不对、标签是否贴在正确的边上、有无交叉遮挡、中文有无豆腐块、图意是否一句话说得清。
4. 有问题就改数据再渲染，最多 3 轮；仍不行就换模板（如手摆改 elk 自动布局）。
5. 笔记里嵌 PNG，HTML 放同目录；文件名 `fig-<概念>-<类型>.html/png`。

## 5. 各环境
- Cursor / Claude Code：按上面流程，Markdown 预览直接看 PNG。
- Claude 网页版：没有 Chrome 就直接用 artifact 显示 HTML，并说明 PNG 需回到本地渲染。
- 离线：`vendor/` 已放 KaTeX（含字体）、rough.js、elkjs、dagre；不需要 CDN。

## 6. 来源

- Paper·light token、stepper `data-s`、交付前检查清单、Known traps 改编自 nicobailon/visual-explainer @69cd739（MIT，© 2025 Nico Bailon；`kit/vendor/ve/LICENSE`）。见仓库 `THIRD_PARTY.md`。
- 线穿过文字、边穿过节点两项检查和 elk 路径曲线是 2026-10-16 实测中发现问题后加的：原来的自动布局只取节点坐标、直线连边，边会从别的节点下面穿过去，读起来像多了一条因果链。
