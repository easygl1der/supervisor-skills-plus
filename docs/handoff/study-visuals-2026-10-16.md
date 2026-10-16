# study 出图调研与 demo（2026-10-16）

## A. Demo（场景：喝咖啡 vs 长寿，混杂因素＝收入/生活习惯）
目录：/workspace/study-visual-demos/
1. `1_dag.png`：Mermaid 因果图（源文件 dag.mmd，用 mmdc 渲染，约 2 秒）。任何环境都能显示，适合讲结构，不够生动。
2. `2_scatter.png`：matplotlib 模拟数据。左图不分组时斜率约 3.1 岁/杯；右图按收入分层后组内斜率约 0，直观看到混杂造成的虚假相关（辛普森式）。这就是 matplotlib 的用处：用数据讲直觉。
3. `3_scene.png`：手写 SVG/HTML 场景图（emoji 图标、带标注的箭头、后门路径说明），用 headless Chrome 截图，约 1 秒。生活化、生动，零成本，不需要任何图像 API。
4. 动画：没做（时间优先）。可以把 3 改成 HTML/CSS 分步动画（先亮混杂，再亮两条箭头，最后划掉虚线），也可以走 live-panel 的 JSON→mp4。

## B. 现成工具与 skill（链接都打开过，返回 200）
- excalidraw 手绘风：coleam00/excalidraw-diagram-skill（会渲染、自己看截图修布局，能用于任何读取 skills 的 agent）https://github.com/coleam00/excalidraw-diagram-skill ；robonuggets/excalidraw-skill（走 MCP 的实时画布）https://github.com/robonuggets/excalidraw-skill ；官方 https://github.com/excalidraw/excalidraw-mcp 。几秒到几十秒，需要文件系统或 MCP，Claude.ai 只能通过 MCP 用。
- 图像生成式解释图：ericblue/visual-explainer-skill（白板、信息图、思维导图，可把 Mermaid 直接转成信息图，后端用 Gemini Nano Banana 2 或 OpenAI）https://github.com/ericblue/visual-explainer-skill 。Gemini 免费额度可用，十几秒一张，但图里的文字和数字可能出错，不适合放公式。
- 信息图排版：remybroun/infographic（52 种版块，HTML/PDF，有字数预算校验）https://github.com/remybroun/infographic 。偏「深度版」，较重。
- nicobailon/visual-explainer（HTML 解释页）https://github.com/nicobailon/visual-explainer ；anthropics/skills 里有 canvas/artifacts 类示例 https://github.com/anthropics/skills 。
- 因果 DAG：dagitty（网页版，还能自动给出调整集）https://www.dagitty.net ；ggdag（R）https://github.com/r-causal/ggdag 。适合严谨的 DAG，生动性不足。
- 其他图表：D2 https://github.com/terrastruct/d2 ；Napkin AI（文本转图，网页 SaaS，有免费额度，不能被 agent 调用）https://www.napkin.ai 。
- 动画：Remotion（React→mp4）https://github.com/remotion-dev/remotion ；Motion Canvas https://github.com/motion-canvas/motion-canvas ；Lottie https://github.com/lottie-animation-community/lottie-spec ；本机 live-panel（JSON→mp4）。都比 Manim 稳，但渲染要几十秒到几分钟。
未覆盖：X、YouTube 没有专门去搜。

## 推荐默认栈
- 快速生动回答（默认，跨 Cursor、Claude Code、Claude.ai）：Mermaid DAG + emoji 场景图（SVG/HTML；在 Claude.ai 里用 artifact）+ 需要时补一张 matplotlib 模拟数据图。都是秒级、免费，文字准确。
- 深度可视化（用户要求时才做）：excalidraw skill 画手绘概念图；visual-explainer + Gemini 免费额度出插画式场景图（文字必须核对）；HTML/CSS 或 Remotion/live-panel 做分步动画；dagitty 核对调整集。Manim 不用。

## C. 让 Mermaid 更生动、结构更丰富（追加）
同一张咖啡因果图出了三个版本，可以对比：
- 原版：study-visual-demos/1_dag_plain.png（文件 1_dag.png 内容相同）
- 美化版：1_dag_styled.png。用了 handDrawn 手绘风、theme: base 加 themeVariables、classDef 配色、子图分层（背景 / 观察到的）、emoji 和 linkStyle 红色虚线。
- 结构版：1_dag_rich.png。纵向五层子图：生活场景 → 变量 → DAG（附后门路径说明）→ 估计策略（分层、倾向得分、敏感性分析）→ 结论。
已知缺陷：handDrawn 模式下中文会提前换行，两条边的标签有一处重叠；结构版图很高，在第 ③ 层里 T 和 Z 之间的边有些挤。可以改用 ELK 布局，或者加宽节点。

美化相关的资源（都打开过，返回 200）：
- 主题和 themeVariables：https://mermaid.js.org/config/theming.html
- 布局（ELK、handDrawn look）：https://mermaid.js.org/config/layouts.html
- 图标：architecture-beta 可以用 iconify 图标包 https://mermaid.js.org/syntax/architecture.html ，图标库在 https://icon-sets.iconify.design
- beautiful-mermaid（多套精美主题的渲染器，可以输出 SVG 或 ASCII）：https://github.com/lukilabs/beautiful-mermaid
- Mermaid 转 Excalidraw（转成手绘风后可以继续编辑）：https://github.com/excalidraw/mermaid-to-excalidraw
- 官方在线编辑器和示例：https://www.mermaidchart.com/
- 注意：github.com/mermaid-js/awesome-mermaid 返回 404，不存在。

flowchart 以外值得用的图类型（官方文档有示例）：
- mindmap，适合概念地图：https://mermaid.js.org/syntax/mindmap.html
- block-beta，适合分层结构：https://mermaid.js.org/syntax/block.html
- timeline，适合概念演化史，例如 Rubin → Pearl → DML：https://mermaid.js.org/syntax/timeline.html
- quadrantChart，适合方法对比，例如按「假设强弱 × 数据需求」画四象限：https://mermaid.js.org/syntax/quadrantChart.html
- sankey，适合样本流失或分组流向：https://mermaid.js.org/syntax/sankey.html
建议：study 默认用「分层子图 + classDef 语义配色 + emoji」，讲概念演化时配 timeline，比较方法时配 quadrantChart。美化项目只用纯 Mermaid 语法，才能保证跨工具都能渲染；beautiful-mermaid 和 Excalidraw 转换留给需要精修的时候。
