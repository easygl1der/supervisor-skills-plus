#!/usr/bin/env python3
"""Build or verify data/MANIFEST.tsv (path, bytes, sha256, source, licence,
how_to_fetch, notes).

Usage:
    python manifest.py build  <data_dir> [--root .] [--manifest data/MANIFEST.tsv]
                              [--lfs-mb 5]
    python manifest.py verify [--root .] [--manifest data/MANIFEST.tsv]
                              [--data-dir <dir>]

Paths in the manifest are relative to --root (the repository root).

build: hashes every file under <data_dir>, keeps the source, licence,
how_to_fetch and notes columns of rows already in the manifest, keeps rows
for files that are not present locally (external data), and lists files
larger than --lfs-mb that need Git LFS or an external host.

verify: checks bytes and sha256 of every row whose file is present; a row
whose file is absent passes only if how_to_fetch is filled (external data);
rows with empty source or licence are warnings; with --data-dir, files on
disk that are missing from the manifest are errors.

Exit 1 on any error (mismatch, absent without how_to_fetch, unlisted file).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path

COLS = ["path", "bytes", "sha256", "source", "licence", "how_to_fetch", "notes"]
SKIP = {".DS_Store", "MANIFEST.tsv", ".gitkeep"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read(manifest: Path) -> dict[str, dict]:
    if not manifest.exists():
        return {}
    with manifest.open(newline="") as fh:
        return {r["path"]: {c: (r.get(c) or "") for c in COLS}
                for r in csv.DictReader(fh, delimiter="\t") if r.get("path")}


def write(manifest: Path, rows: dict[str, dict]) -> None:
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for k in sorted(rows):
            w.writerow(rows[k])


def files_under(d: Path):
    for p in sorted(d.rglob("*")):
        if p.is_file() and p.name not in SKIP and ".git" not in p.parts:
            yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "verify"])
    ap.add_argument("data_dir", nargs="?")
    ap.add_argument("--root", default=".")
    ap.add_argument("--manifest", default="data/MANIFEST.tsv")
    ap.add_argument("--data-dir", dest="check_dir")
    ap.add_argument("--lfs-mb", type=float, default=5.0)
    a = ap.parse_args()
    root = Path(a.root).resolve()
    manifest = root / a.manifest
    rows = read(manifest)
    errors = 0

    if a.cmd == "build":
        if not a.data_dir:
            ap.error("build needs <data_dir>")
        big = []
        for p in files_under((root / a.data_dir).resolve() if not Path(a.data_dir).is_absolute() else Path(a.data_dir)):
            rel = str(p.relative_to(root))
            row = rows.get(rel, {c: "" for c in COLS})
            row.update(path=rel, bytes=str(p.stat().st_size), sha256=sha256(p))
            rows[rel] = row
            if p.stat().st_size > a.lfs_mb * 1024 * 1024:
                big.append(rel)
        write(manifest, rows)
        print(f"manifest: {len(rows)} rows written to {manifest.relative_to(root)}")
        for rel in big:
            print(f"LARGE      {rel}  > {a.lfs_mb:g} MB: Git LFS or an external host; fill how_to_fetch")
        for rel, r in sorted(rows.items()):
            if not (r["source"] and r["licence"]):
                print(f"FILL       {rel}  source/licence empty")
        return 0

    if not rows:
        print(f"verify: no manifest at {manifest}")
        return 1
    for rel, r in sorted(rows.items()):
        p = root / rel
        if not p.exists():
            if r["how_to_fetch"]:
                print(f"EXTERNAL   {rel}  not present; fetch: {r['how_to_fetch']}")
            else:
                print(f"MISSING    {rel}  not present and no how_to_fetch")
                errors += 1
            continue
        size = str(p.stat().st_size)
        if size != r["bytes"] or sha256(p) != r["sha256"]:
            print(f"CHANGED    {rel}  bytes {r['bytes']} -> {size} or sha256 differs")
            errors += 1
        if not (r["source"] and r["licence"]):
            print(f"FILL       {rel}  source/licence empty")
    if a.check_dir:
        for p in files_under((root / a.check_dir).resolve()):
            rel = str(p.relative_to(root))
            if rel not in rows:
                print(f"UNLISTED   {rel}")
                errors += 1
    print(f"verify: {len(rows)} rows, {errors} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
