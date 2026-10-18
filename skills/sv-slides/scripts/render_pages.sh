#!/usr/bin/env bash
# Render each PDF page at 150 dpi for visual inspection in batches of 3.
# Prefers pdftoppm (poppler). Falls back to PyMuPDF if installed.
# Usage: render_pages.sh <file.pdf> [outdir]
set -euo pipefail

PDF="${1:-}"
if [[ -z "$PDF" || ! -f "$PDF" ]]; then
  echo "usage: $0 <file.pdf> [outdir]" >&2
  exit 2
fi
OUT="${2:-${PDF%.pdf}-pages}"
mkdir -p "$OUT"

if command -v pdftoppm >/dev/null 2>&1; then
  pdftoppm -png -r 150 "$PDF" "$OUT/page"
  echo "render_pages: pdftoppm 150 dpi -> $OUT/page-*.png"
  echo "Inspect in batches of 3. After a recompile, discard this snapshot."
  exit 0
fi

if python3 - <<'PY'
import sys
try:
    import pymupdf  # noqa: F401
except ImportError:
    try:
        import fitz  # noqa: F401  older PyMuPDF
    except ImportError:
        sys.exit(1)
sys.exit(0)
PY
then
  python3 - "$PDF" "$OUT" <<'PY'
import sys
from pathlib import Path
try:
    import pymupdf as fitz
except ImportError:
    import fitz  # older PyMuPDF

pdf = sys.argv[1]
out = Path(sys.argv[2])
doc = fitz.open(pdf)
# 150 dpi: zoom = 150/72
zoom = 150 / 72
mat = fitz.Matrix(zoom, zoom)
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=mat, alpha=False)
    pix.save(str(out / f"page-{i:02d}.png"))
print(f"render_pages: PyMuPDF 150 dpi -> {out}/page-*.png")
PY
  echo "Inspect in batches of 3. After a recompile, discard this snapshot."
  exit 0
fi

echo "render_pages: missing pdftoppm and PyMuPDF." >&2
echo "Install: brew install poppler" >&2
echo "Or: python3 -m pip install pymupdf" >&2
exit 3
