#!/usr/bin/env python3
"""Check a quickread.md against the nine-section template.

Usage: python check_quickread.py <quickread.md> [--max-chars 900] [--selftest]

Checks (exit 1 on any failure, warnings exit 0):
- nine "## n." headings in order 1..9, none empty
- exactly two tags (frontmatter `tags: [a, b]`)
- body length outside tables, code and formulas: CJK chars + English words
  <= max (default 900 Chinese characters, or 600 words for an English card;
  the targets 700 and 450 are reported as warnings)
- results table (section 5): every data row has a non-empty last column
- contributions (section 6): 3 to 5 bullets, each with a tag
  【证明】【实证】【猜想】【引用】 or [proved]/[empirical]/[conjectured]/[cited]
- limitations (section 8): a two-column table
"""
from __future__ import annotations

import re
import sys

TAGS = re.compile(r"【(证明|实证|猜想|引用)】|\[(proved|empirical|conjectured|cited)\]", re.I)


def sections(text: str) -> dict[int, str]:
    parts = re.split(r"^## (\d)\.", text, flags=re.M)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out[int(parts[i])] = parts[i + 1]
    return out, [int(parts[i]) for i in range(1, len(parts) - 1, 2)]


def body_len(text: str) -> int:
    text = re.sub(r"^---.*?^---", "", text, flags=re.S | re.M)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "", text, flags=re.S)
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("|") and not l.startswith("#"))
    cjk = len(re.findall(r"[\u3400-\u9fff]", text))
    words = len(re.findall(r"[A-Za-z][A-Za-z\-']*", text))
    return cjk + words


def is_english(text: str) -> bool:
    return len(re.findall(r"[\u3400-\u9fff]", text)) < len(re.findall(r"[A-Za-z][A-Za-z\-']*", text))


def table_rows(sec: str) -> list[list[str]]:
    rows = [l for l in sec.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not re.match(r"^\s*\|[\s:\-|]+\|\s*$", r)]
    return [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows[1:]]


def check(text: str, max_chars: int | None = None) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    # English cards are counted in words: target 450, limit 600 (template-9.md)
    target, default = (450, 600) if is_english(text) else (700, 900)
    max_chars = max_chars or default
    secs, order = sections(text)
    if order != list(range(1, 10)):
        errs.append(f"headings '## 1.'..'## 9.' expected in order, found {order}")
    for n, s in secs.items():
        if not s.strip().splitlines()[1:] and len(s.strip()) < 3:
            errs.append(f"section {n} is empty")
    m = re.search(r"^tags:\s*\[(.*?)\]", text, flags=re.M)
    tags = [t.strip() for t in m.group(1).split(",") if t.strip()] if m else []
    if len(tags) != 2:
        errs.append(f"exactly 2 tags required, found {len(tags)}")
    n = body_len(text)
    if n > max_chars:
        errs.append(f"body length {n} > {max_chars}")
    elif n > target:
        warns.append(f"body length {n} above target {target}")
    if 5 in secs:
        rows = table_rows(secs[5])
        if not rows:
            errs.append("section 5 has no table")
        for r in rows:
            if not r[-1] or r[-1] in ("-", "?"):
                errs.append(f"section 5 row without source: {r}")
    if 6 in secs:
        bullets = [l for l in secs[6].splitlines() if l.lstrip().startswith("- ")]
        if not 3 <= len(bullets) <= 5:
            errs.append(f"section 6 needs 3-5 contributions, found {len(bullets)}")
        for b in bullets:
            if not TAGS.search(b):
                errs.append(f"contribution without tag: {b.strip()[:60]}")
    if 8 in secs:
        rows = [l for l in secs[8].splitlines() if l.strip().startswith("|")]
        if not rows or rows[0].count("|") != 3:
            errs.append("section 8 must be a two-column table")
    return errs, warns


def selftest() -> None:
    good = """---
tags: [synthetic-control, panel-causal]
---
## 1. 一句话
结论。
## 2. 问题与动机
问题。
## 3. 核心想法
想法。
## 4. 方法
方法。
## 5. 结果
| 结果 | 数值 | 条件 | 出处 |
|---|---|---|---|
| RMSE | 0.5 | sim | Table 1 |
## 6. 贡献
- 【证明】a（Thm 1）
- 【实证】b（Table 1）
- 【猜想】c（§5）
## 7. 主张与证据对照
| 主张 | 证据 | 强度 | 疑点 |
|---|---|---|---|
| a | Thm 1 | 强 | none |
## 8. 局限
| 作者承认 | 我们的判断 |
|---|---|
| x（§6） | y |
## 9. 与我方向的关联
关联。
"""
    e, _ = check(good)
    assert not e, e
    bad = good.replace("Table 1 |\n## 6", " |\n## 6").replace("- 【猜想】c（§5）\n", "")
    e, _ = check(bad)
    assert any("without source" in x for x in e) and any("3-5" in x for x in e), e
    long_en = good + "\nwords " * 650
    e, _ = check(long_en)
    assert any("> 600" in x for x in e), e
    print("check_quickread selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit(0)
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    mx = int(sys.argv[sys.argv.index("--max-chars") + 1]) if "--max-chars" in sys.argv else None
    errs, warns = check(open(sys.argv[1], encoding="utf-8").read(), mx)
    for w in warns:
        print("WARN", w)
    for e in errs:
        print("FAIL", e)
    print("check_quickread:", "clean" if not errs else f"{len(errs)} problem(s)")
    sys.exit(1 if errs else 0)
