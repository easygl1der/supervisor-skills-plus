# study 作图：HTML 方案调研 + 工具包（2026-10-16）

## 结论
- **HTML（SVG + KaTeX）可以完全替代 TikZ 和 Mermaid 做学习用图**：TikZ 复刻图约 0.9 秒出 PNG，肉眼基本一致；10 个节点的因果 DAG 在浏览器内用 elkjs 或 dagre 自动布局，约 1.0–1.2 秒，**不需要 Graphviz**。Graphviz 只在节点非常多（几十个）时作备选。
- 没有现成的、专门画「学术或教学图」的 HTML skill。最值得借鉴的是 nicobailon/visual-explainer（★10.5k，MIT，10/15 还在更新），它画通用解释页，规则写得很好。所以按我们的需求自己做了一套工具包：`/workspace/study-kit/`。

## A. 调研（以下链接都用 curl 确认能打开，返回 200）
**Skill 类**
| 项目 | 说明 | 借什么 |
|---|---|---|
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer)（★10466，MIT） | 让 agent 把解释写成自包含 HTML 页面，支持 Claude Code、Cursor、Codex 等；SKILL.md 已通读 | ①「每个事实先在图里找到位置（标签、边、图注）再写成句子」②图都手写 SVG，Mermaid 只在用户要求时用 ③反「AI 模板感」清单：不用霓虹、渐变、紫色，不只用 Inter 或系统字体 ④字号下限：标签 ≥12px ⑤KaTeX 里的 `<` 要写成 `&lt;` ⑥交付前逐项勾选的检查清单 ⑦quick 模式：先出 JSON spec，再用 render.mjs 渲染。我们的「数据块 + render」就是照这个思路做的 |
| [anthropics/skills · frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 官方前端设计 skill | 先写设计方案，回头检查是不是「换个题目也会这么画」的通用默认样式；只有确实是顺序时才用编号 |
| [anthropics/skills · canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) / [algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | 海报和艺术图，输出 PNG 或 PDF | 偏艺术，教学图用处不大 |
| [antvis/Infographic](https://github.com/antvis/Infographic)（★7003，MIT） | 声明式信息图引擎，面向 AI 生成 | 以后可试一下「场景卡片」能不能直接用它的模板生成 |

**库类**（都能离线 vendor 进来）
- 布局：[elkjs](https://github.com/kieler/elkjs)、[dagre](https://github.com/dagrejs/dagre)（已 vendor 并实测）、[cytoscape.js](https://github.com/cytoscape/cytoscape.js)（适合交互式大图）。
- 数学和交互：[KaTeX](https://github.com/KaTeX/KaTeX)（已 vendor）、[JSXGraph](https://github.com/jsxgraph/jsxgraph)（几何和函数作图）、[Mafs](https://github.com/stevenpetryk/mafs)（★3444，基于 React，2025-03 后没再更新）、[mathbox](https://github.com/unconed/mathbox)（3D，太重）。
- 声明式图解：[Penrose](https://github.com/penrose/penrose)（★7993，CMU，按「数学含义 + 样式」自动出图，适合集合和几何概念图，学习成本高）、[Bluefish](https://github.com/bluefishjs/bluefish)（★156，关系式图解，比较小众）。
- 手绘风：[rough.js](https://github.com/rough-stuff/rough)（已 vendor，四格漫画边框用的就是它）；[D3](https://github.com/d3/d3) 是底层通用库。
- 因果：[dagitty](https://github.com/jtextor/dagitty)（★352，GPL-2.0，10/09 还在更新），能在浏览器里算调整集、找后门路径。GPL 协议不宜打包进 MIT 仓库，只作为可选的外部 CDN 引用。
- Explorable explanations：[Idyll](https://github.com/idyll-lang/idyll)、[distill template](https://github.com/distillpub/template)，两个都基本不维护了，只适合借版式思路。

未逐个打开 README 的：Penrose、Bluefish、dagitty、Infographic 只看了 GitHub 元数据和已知用法；X 上没专门搜。

## B. 复刻与自动布局（v3 目录）
- `/workspace/study-visual-demos/v3/html_tikz_replica.png`（HTML 原件也在同目录），原图复制为 `t1_tikz_original.png`，左右对比图 `compare_tikz_vs_html_v2.png`。渲染 3 次分别是 0.86、0.92、0.90 秒（含启动 Chrome）。
- `html_elk_10node.png`（elkjs，1.16 秒）和 `html_dagre_10node.png`（dagre，1.04 秒）：10 个节点（基因、年龄、教育、收入、距离、睡眠、咖啡、医疗、血压、寿命），只写了谁指向谁，没写坐标。elk 版有 1 处轻微交叉（G→Y 穿过 I→H）。

## C. 工具包 `/workspace/study-kit/`
- `references/visuals.md`：选型表、不编数字等内容规则、配色和中文字体、渲染→截图→自检循环、各环境说明。
- `templates/`：`textbook-dag`、`auto-dag-elk`、`auto-dag-dagre`、`scene-cards`、`comic-4panel`、`mind-map`。心智模型图的叶子按「你原来就对 / 被纠正 / 新补充」三色着色，正好对上诊断后重画的那一步。只需改模板顶部的数据块。
- `render.sh` / `render.mjs`：用 playwright-core 加系统 Chrome，2 倍分辨率截取 `#fig`，并自动检查文字重叠、溢出、KaTeX 报错、JS 报错和未填的占位符，有问题时退出码为 2。做过一次反例测试：故意让节点重叠，成功报出重叠警告。
- `vendor/`（3.1 MB）：KaTeX 及字体、rough.js、elkjs、dagre，加上 kit.js 和 kit.css，全部离线可用。
- 6 个模板都已渲染通过，每个约 1 秒，没有警告。

## 遗留和注意
- 踩过的坑：在已有的 `<svg>` 上用 innerHTML 写 `stroke="var(--x)"` 时颜色不生效，已经写进规范。
- 心智模型图是按角度摆的固定布局，叶子超过 4 个时可能挤在一起，需要换成 elk 布局。
- 合进 supervisor-skills-plus 时要在 THIRD_PARTY 里写明 KaTeX、rough.js、elkjs、dagre 都是 MIT；dagitty 是 GPL，不能打包进去。
