# study 配图风格对比 v2（2026-10-16）

场景：喝咖啡与长寿，混杂因素是收入；另附工具变量（IV）示例。所有文件在 `study-visual-demos/v2/`。
渲染时间 = 源文件写好之后到 PNG 生成的墙钟时间（box 上测量，包含 Chrome/Python 冷启动）。编写工作量 = agent 写源文件的大致耗时。

| # | 工具 | 风格 | 渲染时间 | 编写工作量 | Cursor md 预览（嵌 PNG） | 结论 |
|---|---|---|---|---|---|---|
| h1 | HTML/CSS → 无头 Chrome | 扁平插画卡片 | 1.1 s | 低（约 40 行） | ✅ PNG；HTML 也能在浏览器里打开 | ⭐ 默认场景图，干净，emoji 清楚 |
| h2 | HTML/CSS | 四格漫画分镜 | 1.0 s | 低 | ✅ | ⭐ 讲“故事和 motivation”最好 |
| h3 | HTML + rough.js（CDN） | 手绘草图 DAG | 1.2 s | 中（要写坐标） | ✅ | ⭐ 手绘感好，可读；需要联网加载 CDN |
| h4 | HTML/CSS | 深色信息图 | 1.0 s | 低 | ✅ | 好看，但数字是示意性的，必须来自真实计算；底部有留白 |
| h5 | HTML/SVG | 教科书极简 DAG | 0.9 s | 中（坐标） | ✅ | 正式、清楚，适合笔记正文 |
| h6 | HTML/CSS | IV 场景卡片 | 1.1 s | 低 | ✅ | 可用；收入和 Z 的“无关”没有画成边，只写在文字里 |
| e1 | Excalidraw MCP（mindmap 模板） | 手绘概念图 | 约 1.7 s 下载 + MCP 调用 | 低 | ✅ PNG；可在 excalidraw.com 编辑 | ❌ 模板把“咖啡”放在中心，结构不对；emoji 变成乱码；箭头压住文字。要自定义元素 JSON 才可用；导出在公开 URL 上 |
| g1 | Graphviz dot | 配色、圆角、cluster | 0.13 s | 低 | ✅ | ⭐ 最快最稳，布局自动，排版紧凑 |
| d1 | D2 0.7.1 --sketch → SVG → Chrome | 手绘草图 | 1.2 s | 很低 | ✅ | 字体中英混排不统一，布局偏向一边、右侧大片空白；D2 原生 PNG 需要 playwright 驱动（404，已绕开） |
| m1 | Mermaid（mmdc 12）+ ELK | 五层分层结构 | 1.6 s | 低 | ✅ PNG；源码在 Cursor/GitHub 里能原生渲染 | 无重叠；但 ELK 忽略了子图的 direction LR，图又窄又高 |
| m2 | Mermaid mindmap | 概念思维导图 | 1.1 s | 很低 | ✅ | ⭐ 结构丰富、彩色，适合概念总览 |
| m3 | Mermaid timeline | Neyman→Rubin→Pearl→DML | 0.9 s | 很低 | ✅ | 清楚；年份是常用书目年份，正式用前要核对 |
| p1 | matplotlib xkcd + 霞鹜文楷 | 手绘风数据图 | 0.9 s | 中（模拟数据） | ✅ | ⭐ 统计直觉最佳：合并后斜率 2.4、分组后接近平 |
| p2 | Plotly + kaleido | 交互散点 + 静态导出 | 3.0 s | 低 | ✅ PNG；HTML 可交互 | 可用，但没有回归线，信息量不如 p1/p3 |
| p3 | Vega-Lite（vl-convert） | 分组回归线 + 合并虚线 | 0.9 s | 中 | ✅ | ⭐ 辛普森/混杂的直观展示最清楚 |
| t1 | TikZ（pdflatex + CJKutf8） | 教科书 DAG + IV | 0.8 s | 中（TeX 调试；ctex/standalone 缺包） | ✅ | 出版级质量；依赖完整的 TeX 环境，跨工具可移植性差 |
| a1 | HTML/CSS 动画 → Playwright 逐帧截图 → ffmpeg | 4.5 秒动画（mp4 + gif） | 6.7 s | 中 | GIF 能在 md 预览里播放；mp4 不行 | 可用，比 Manim 快得多；红色相关线的虚线效果丢了 |
| — | 免费 AI 插画 | — | — | — | — | 跳过：box 上没有不需要付费 key 的生图工具 |

## 建议
- 默认组合：Graphviz 或 Mermaid mindmap 画结构，h1/h2 风格的 HTML 场景卡片讲 motivation，p1/p3 讲统计直觉。全部秒级出图，导出 PNG 嵌进 Markdown。
- 动画：HTML/CSS 动画转 GIF，约 7 秒，不用 Manim。
- 不推荐：Excalidraw 模板（结构错、emoji 坏）、D2 sketch（中文排版差）、需要完整 TeX 的 TikZ（仅在出版时用）。
