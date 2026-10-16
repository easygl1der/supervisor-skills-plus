# study-kit：study skill 的 HTML 作图工具包
- `references/visuals.md`：作图规范（选型、规则、自检循环）
- `templates/`：textbook-dag、auto-dag-elk / auto-dag-dagre、scene-cards、comic-4panel、mind-map（全部离线可用，依赖 `vendor/`）
- `render.sh` / `render.mjs`：headless Chrome 渲染 + 自检。首次运行 `npm i`（只装 playwright-core，用系统 Chrome；`CHROME=/path` 可指定）
- `vendor/`：KaTeX 0.16 + fonts、rough.js、elkjs、dagre（MIT），kit.js / kit.css（本工具包）
复制模板 → 改顶部数据块 → `./render.sh x.html` → 看 PNG → 嵌进笔记。


## 新增（2026-10-16，吸收 visual-explainer）
- 模板：`explainer-page.html`、`stepper.html`、`stepper-proof.html`、`stepper-trace.html`、`stepper-plot.html`
- `vendor/ve/`：`ve.css`、`stepper.js`、上游 `LICENSE`（MIT，© 2025 Nico Bailon）与 `NOTICE.md`（commit 69cd739）
- `render.sh` 参数：`--full` `--figures` `--steps` `--gif`（GIF 需 ffmpeg）
