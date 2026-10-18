#!/usr/bin/env bash
# 用法: ./render.sh fig.html [fig.png]   需要 node + playwright-core + Chrome（CHROME=路径 可覆盖）
# 退出码 0=干净，2=有自检警告（重叠/溢出/KaTeX 错误/JS 错误/未填占位符），需修后重渲染
DIR="$(cd "$(dirname "$0")" && pwd)"; NODE_PATH="$DIR/node_modules" exec node "$DIR/render.mjs" "$@"
