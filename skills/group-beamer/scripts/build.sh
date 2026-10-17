#!/usr/bin/env bash
# Compile a group-beamer deck with latexmk -xelatex.
# Usage: build.sh [--theme moloch-cjk|simpleplus-cjk|sysu-like] <file.tex>
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
THEME=""
TEX=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --theme)
      THEME="${2:-}"
      shift 2
      ;;
    --help|-h)
      echo "Usage: $0 [--theme moloch-cjk|simpleplus-cjk|sysu-like] <file.tex>"
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      echo "unknown option: $1" >&2
      exit 2
      ;;
    *)
      TEX="$1"
      shift
      ;;
  esac
done

if [[ -z "${TEX}" ]]; then
  echo "usage: $0 [--theme moloch-cjk|simpleplus-cjk|sysu-like] <file.tex>" >&2
  exit 2
fi
if [[ ! -f "$TEX" ]]; then
  echo "build.sh: file not found: $TEX" >&2
  exit 2
fi

need() {
  local cmd="$1"
  local hint="$2"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "build.sh: missing command '$cmd'." >&2
    echo "Install: $hint" >&2
    echo "Do not install a full MacTeX tree from this skill; use tlmgr or brew for the named package only." >&2
    exit 3
  fi
}

need latexmk "tlmgr install latexmk"
need xelatex "install TeX Live (BasicTeX is enough) then tlmgr install latexmk collection-xetex"

detect_theme() {
  local src
  src="$(cat "$TEX")"
  if [[ "$src" == *"groupbeamer-sysu"* ]] || [[ "$src" == *"sysu-like"* ]]; then
    echo "sysu-like"
  elif [[ "$src" == *"groupbeamer-simpleplus"* ]] || [[ "$src" == *"SimplePlus"* ]]; then
    echo "simpleplus-cjk"
  else
    echo "moloch-cjk"
  fi
}

if [[ -z "$THEME" ]]; then
  THEME="$(detect_theme)"
fi

THEME_DIR="$SKILL_DIR/templates/$THEME"
if [[ ! -d "$THEME_DIR" ]]; then
  echo "build.sh: unknown theme '$THEME' (expected moloch-cjk, simpleplus-cjk, or sysu-like)" >&2
  exit 2
fi

require_kpse() {
  local sty="$1"
  local pkg="$2"
  if ! command -v kpsewhich >/dev/null 2>&1; then
    echo "build.sh: missing command 'kpsewhich'. Install TeX Live / BasicTeX." >&2
    exit 3
  fi
  if [[ -n "$(kpsewhich "$sty" 2>/dev/null || true)" ]]; then
    return 0
  fi
  echo "build.sh: TeX package file '$sty' not found." >&2
  echo "Install: tlmgr install $pkg" >&2
  exit 3
}

case "$THEME" in
  moloch-cjk)
    require_kpse beamerthememoloch.sty moloch
    require_kpse ctex.sty ctex
    ;;
  simpleplus-cjk)
    require_kpse ctex.sty ctex
    # Vendored SimplePlus .sty files live in templates/simpleplus-cjk/.
    ;;
  sysu-like)
    require_kpse ctex.sty ctex
    ;;
esac

export max_print_line=10000
export error_line=254
export half_error_line=238
# Theme dir first so wrappers and vendored SimplePlus win; then the .tex dir.
TEX_DIR="$(cd "$(dirname "$TEX")" && pwd)"
TEX_BASE="$(basename "$TEX")"
export TEXINPUTS="${THEME_DIR}:${TEX_DIR}:${SKILL_DIR}/templates:${TEXINPUTS:-}"

cd "$TEX_DIR"
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error \
  "$TEX_BASE"
echo "build.sh: ok $TEX_DIR/${TEX_BASE%.tex}.pdf (theme $THEME)"
