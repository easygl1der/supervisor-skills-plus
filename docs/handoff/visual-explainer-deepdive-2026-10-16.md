# visual-explainer 深度调研（2026-10-16）

仓库：https://github.com/nicobailon/visual-explainer · v0.12.0 · ~10.5k★ · MIT（© 2025 Nico Bailon）· 最近 push 2026-10-15 14:20 SGT · 开放 issue 1 个（`$$` 渲染误改写、输出目录 symlink 检查、npx video 缺 bin）。最近 commit：状态机逐事件 replay(#118)、**#105「全部手画 SVG，Mermaid 改为 opt-in」**、live figure、打包成 Agent Plugins 1.0.0。

## 1. 架构
```
plugins/visual-explainer/
  SKILL.md (14KB，核心规则)        commands/  diff-review fact-check generate-slides generate-video
  references/ style-guide.md(16KB) diagrams.md(15KB) plans.md slides.md themes.md video.md
  templates/ page.html(33KB 参考实现) plan.html slide-deck.html
  quick/ render.mjs + schema.json + base.css   (JSON→HTML 快速模式)
  plan/  render.mjs plan.js plan.css            (可在页面里作答的交互计划)
  pptx/export.mjs  video/render.mjs(playwright+ffmpeg→MP4)  mcp/server.mjs  extension.ts(Pi)
configs/ cursor(.mdc) codex copilot opencode openclaw antigravity pi   examples/replay-job-queue.html
```
- 安装：Claude Code `/plugin marketplace add` + `/plugin install visual-explainer@visual-explainer-marketplace`；Cursor 把 `plugins/visual-explainer/` 拷到 `~/.cursor/skills/visual-explainer`（或工作区 `.cursor/skills/`），configs/cursor 有可选 .mdc；Codex 拷到 `~/.codex/skills/`，commands 可放 `~/.codex/prompts/`；Pi 有原生工具；另有本地 stdio MCP（只写输出目录 jail）。
- 命令：`/generate-web-diagram`（一句话结论+图，`--quick`）、`/diff-review`（结论/文件图/前后对比 SVG/风险表）、`/plan-review`（逐条 accept/reject 的计划页）、`/generate-visual-plan`、`/project-recap`、`/fact-check`（逐条核对 claim，顶部加核验条）、`/generate-slides`（`--pptx`）、`/generate-video`（MP4，可配音）。
- 输出：**单个自包含 HTML**，默认 `~/.agent/diagrams/<name>.html`（`VISUAL_EXPLAINER_OUTPUT_DIR` 可改）；CSS/JS/SVG 内联，「CDN only for fonts and libraries」（page.html 走 Google Fonts）。写完 `open` 到浏览器。Markdown 伴随文件仅在用户要求时写；**没有 PNG 导出**（只有 video 的 `--stills`）。
- 自检：交付前 16 项 checklist（无 console 错误、首屏=图+一句话、图多于段落、每个数字有图、figcaption「Fig. N」+ role=img/aria-label、1280/390px 无横向溢出、深浅双色、对比度 4.5:1……）；video 要求「run --stills, read every PNG, fix」；fact-check 是事后核对环。**没有自动化重叠检测脚本**（我们的 render.sh 有）。

## 2. 设计规则（摘录）
- 核心理念：“Turn what you know into something a person understands in ten seconds.” “The default output is one HTML page whose spine is figures. Text is caption, not content.”
- Show, don't tell 九条：One claim per figure；Figures lead, words label；**First viewport = the answer**（教概念时可以是问题+框架图）；**Draw the mechanism, not the name. Label every arrow with a verb**；Draw the difference；Encode state in form（never color alone）；Every number gets a picture（跨度用尺寸线）；Cases become small multiples；Give every fact a place。
- 页型：Concept explainer = question → intuition picture → mechanism (stepper) → edge cases → what to remember。
- 文字：约 80% ASD-STE100 简化技术英语；标题写结论（“Cache hits skip Postgres”）不写主题。
- 四种 register：Instrument（Geist，评审/指标）、Blueprint（IBM Plex，架构）、**Paper（Newsreader + Atkinson Hyperlegible，概念/长读，墨蓝 #2c4cd0）**、Editorial。每种给深浅两套 11 色 token。Topic motif：从主题借 2–3 处点缀。
- 排版：7 级字号、间距只用 scale、65ch、正文 ≥16px、标签 ≥12px、真破折号/减号/×、tabular-nums、`text-wrap: balance`。
- 反 AI 模板：“Never: Inter, Roboto, Arial, or system-ui as the only font; violet or fuchsia Tailwind accents; neon; glassmorphism; gradient text, backgrounds, or blobs; clip-art, mascots, or emoji markers; centered everything; an accent bar on a rounded card; 01/02/03 when order does not matter.” 「Quiet ground, one signal」：90% 中性色，强调色 ≤10%。
- 图：**“Draw every diagram by hand… Use Mermaid only when the user asks for it.”** 先 ASCII 草图再换坐标；节点间距 ≥40；正交边；>12 节点拆总览+细节；形状表语义（圆柱=存储）；边语言：实线同步/虚线可选/加粗发光=本图主角/红✕=阻断；Stepper/scene player（打开先显示全图，不自动播放）；callout 编号圆圈 3–6 个；linked highlighting（`data-ref`）；live figure（滑块）；three.js 只用于真有空间数据。
- 无障碍：role="img"+aria-label、4.5:1 对比、可见焦点环、prefers-reduced-motion 显示终态、@media print。
- Known traps：KaTeX 中 `<` 写 `&lt;`；`file://` 下 `history.replaceState` 要 try/catch；Mermaid 读不到 CSS 变量。

## 3. 实测（因果：咖啡/长寿 混杂 + 距离作 IV）
按其 Concept explainer 页型 + Paper register token + 手画 SVG（dot-grid 舞台、key node 高亮、红色虚线「热边」、每条边一个动词、Fig. N 结论句图注、small multiples 卡片、“要记住的”）写成 `study-visual-demos/ve/coffee-iv.html` → `coffee-iv.png`。
- 耗时：撰写约 2–3 分钟（LLM 生成 ~170 行 HTML，单张图主体约 60 行），渲染截图 2.2 s，零 JS 报错，一次过。改用我们 kit 的 KaTeX 离线版；中文回退到 Noto CJK。
- 观感：比我们的 scene-cards 更「专业/安静」，比 textbook-dag 更有信息层次（一页讲完：问题→混杂图→分层→IV 三条件→LATE→要点）。缺点：不如 scene-cards/四格漫画「生动」（它明令禁止 emoji 与插画）；英文字体栈对中文无效；整页长图嵌 Markdown 偏长，适合「概念页」不适合单图。

## 4. 我们该怎么用
- **原样拷**（MIT，需保留 LICENSE 版权声明，放 THIRD_PARTY.md）：style-guide 的 Paper register token/字号/间距 scale；diagrams.md 的节点/边/callout/stepper CSS+JS 片段；交付前 checklist（翻成中文并删软件评审专属项）；Known traps。
- **改编进 study kit**：新增「概念讲解页」模式 `explainer-page.html`（区别于单图）；Show-don't-tell 九条中 1/2/3/4/6/8/9 写进 visuals.md；stepper 代替 GIF 演示推导（成本更低，可交互）；`/fact-check` 思路→「图注/数字核对」步骤；quick 模式的「JSON spec→渲染」思路与我们模板顶部数据块一致，可以借它的 schema 校验思路。
- **冲突**：①它禁 emoji/插画 → 我们保留 scene-cards/四格漫画讲 motivation，VE 规则只管结构图与概念页；②CDN 字体 → 我们离线 vendored + 中文字体栈；③英文 STE100 → 中文写作规则（结论式标题、一句一意）；④无 PNG 导出 → 我们坚持 html+png 双份，并按 section 切图；⑤Mermaid 立场一致（都 opt-in）；⑥深色/浅色双 scheme → 我们只做浅色（截图稳定）。
- **依赖方式**：**vendor 部分，不作为必装 skill 依赖**。理由：study 要跨 Cursor/Claude Code/Claude 网页，VE 输出目录、命令、英文规则都与 study-vault 不符；它迭代很快（周更），规则会漂移。可在 README 里「推荐另装 visual-explainer 用于 diff/plan review」，但 study 不调用它。vendor 时记录上游 commit `69cd739`。
