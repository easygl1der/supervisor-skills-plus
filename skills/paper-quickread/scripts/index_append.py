#!/usr/bin/env python3
"""Append an entry to a reading index (index.json), never rewriting history.

Usage:
    python index_append.py <index.json> '<json entry>'
    python index_append.py --selftest

Entry fields: id (required, e.g. arXiv id, DOI, or book slug), kind
(paper | book | concept), title, path (relative to the index), date
(YYYY-MM-DD), and optional tags, field, artifact (quickread | study |
style-card | session ...).

Rules:
- The file is a JSON list. Existing entries are never modified or removed.
- If an entry with the same id and kind exists, a new event is appended to
  "events" of a NEW record line instead of editing the old one; readers take
  the latest record per id. This keeps the file append-only for git diffs.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REQUIRED = ("id", "kind", "title", "path", "date")


def append(index: Path, entry: dict) -> str:
    missing = [k for k in REQUIRED if not entry.get(k)]
    if missing:
        raise SystemExit(f"index_append: missing fields {missing}")
    data = json.loads(index.read_text()) if index.exists() else []
    if not isinstance(data, list):
        raise SystemExit("index_append: index.json must be a JSON list")
    before = json.dumps(data, ensure_ascii=False, sort_keys=True)
    seen = [e for e in data if e.get("id") == entry["id"] and e.get("kind") == entry["kind"]]
    entry = dict(entry, seq=len(data) + 1, supersedes=seen[-1]["seq"] if seen else None)
    data.append(entry)
    # append-only guard: the old prefix must be byte-identical after the write
    assert json.dumps(data[:-1], ensure_ascii=False, sort_keys=True) == before
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    return "updated" if seen else "added"


def selftest() -> None:
    with tempfile.TemporaryDirectory() as d:
        idx = Path(d) / "index.json"
        e = {"id": "arXiv:1812.09970", "kind": "paper", "title": "SDID", "path": "papers/x/quickread.md", "date": "2026-10-16"}
        assert append(idx, e) == "added"
        first = idx.read_text()
        assert append(idx, dict(e, artifact="study", date="2026-10-17")) == "updated"
        data = json.loads(idx.read_text())
        assert len(data) == 2 and data[1]["supersedes"] == 1
        assert json.loads(first)[0] == data[0]
        try:
            append(idx, {"id": "x"})
        except SystemExit:
            pass
        else:
            raise AssertionError("missing fields not rejected")
    print("index_append selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif len(sys.argv) == 3:
        print(append(Path(sys.argv[1]), json.loads(sys.argv[2])))
    else:
        print(__doc__)
        sys.exit(2)
