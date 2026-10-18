#!/usr/bin/env python3
"""Copy a kit template to a new figure file, fixing the vendor paths.

Usage:
    python newfig.py <template-name> <out.html>
    python newfig.py --list
    python newfig.py --selftest

Templates live in skills/sv-figure-explain/kit/templates/ and load ../vendor/...; the copy
points to kit/vendor/ by a path relative to <out.html>, so figures can sit
next to the notes that embed them (vault, paper folder, evals).
Refuses to overwrite an existing file.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent / "kit"
TPL = KIT / "templates"


def newfig(name: str, out: Path) -> Path:
    src = TPL / (name if name.endswith(".html") else name + ".html")
    if not src.exists():
        raise SystemExit(f"newfig: no template {src.name}; use --list")
    out = out.resolve()
    if out.exists():
        raise SystemExit(f"newfig: {out} exists; not overwriting")
    rel = os.path.relpath(KIT / "vendor", out.parent).replace(os.sep, "/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(src.read_text().replace("../vendor/", rel + "/"))
    return out


def selftest() -> None:
    with tempfile.TemporaryDirectory() as d:
        o = newfig("mind-map", Path(d) / "a" / "fig-x-mental.html")
        t = o.read_text()
        assert "../vendor/" not in t and "/vendor/kit.js" in t
        assert (o.parent / t.split('src="')[1].split('"')[0]).resolve().exists()
        try:
            newfig("mind-map", o)
        except SystemExit:
            pass
        else:
            raise AssertionError("overwrite not refused")
    print("newfig selftest ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
    elif a == ["--list"]:
        print("\n".join(sorted(p.stem for p in TPL.glob("*.html"))))
    elif len(a) == 2:
        print(newfig(a[0], Path(a[1])))
    else:
        print(__doc__)
        sys.exit(2)
