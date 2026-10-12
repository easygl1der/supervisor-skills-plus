#!/usr/bin/env python3
"""Compare the numbers printed in LaTeX sources with a numbers file.

Usage:
    python numbers_check.py <numbers.json> <tex file or dir> [...]
                            [--key-macro val] [--all-ints] [--strict] [--json]

numbers.json holds {key: value}. A value is a number, a string such as
"0.78" or "12.3%", or an object {"value": 0.123, "scale": 100}. Keys that
start with "_" are metadata; "_meta" should name "code_sha" and "data_sha"
(or "data_version"); missing or placeholder SHAs are reported.

What is checked:
- A marker comment "%num:key" (several allowed: "%num:a,b"). The numbers on
  the code part of that line (or, if the line is only the comment, of the
  next non-empty line) must include the key's value. A printed value may be
  rounded from the stored one (0.7812 printed as 0.78 passes as "rounded").
- A key macro such as \\val{key} (pass --key-macro val): the key must exist.
- Every other number in the text that has no key: decimals, percentages and
  numbers with thousands separators (plus integers >= 10 with --all-ints)
  are listed as warnings. Numbers inside \\cite, \\ref, \\label, \\url,
  lengths (0.5\\linewidth, 3pt) and years are skipped.

Exit 1 on a mismatch, an unknown key or a missing SHA; warnings exit 0
unless --strict.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

NUM = re.compile(r"(?<![\w.])(-?\d{1,3}(?:(?:,|\{,\}|\\,|~)\d{3})+(?:\.\d+)?|-?\d+\.\d+|-?\.\d+|-?\d+)(\s*\\?%)?")
MARKER = re.compile(r"%\s*num:([\w.,:-]+)")
SKIP_ARGS = re.compile(
    r"\\(?:cite\w*|ref|eqref|autoref|cref|Cref|label|url|href|input|include|"
    r"includegraphics|begin|end|usepackage|documentclass|bibliography\w*|"
    r"setlength|vspace|hspace|newcommand|renewcommand|definecolor|color)"
    r"\*?(?:\[[^\]]*\])*\{[^}]*\}")
LENGTH = re.compile(r"-?\d*\.?\d+\s*(?:\\(?:line|text|column|paper)width|\\(?:base)?lineskip|pt|cm|mm|em|ex|in|bp)\b")
PLACEHOLDER = re.compile(r"^(|todo|tbd|xxx+|none|null|\[.*\]|<.*>)$", re.I)


def to_dec(s: str) -> Decimal | None:
    s = re.sub(r"\{,\}|\\,|~|,", "", s.strip()).replace("\\%", "").replace("%", "").strip()
    try:
        return Decimal(s)
    except InvalidOperation:
        return None


def expected(v) -> Decimal | None:
    if isinstance(v, dict):
        base = expected(v.get("value"))
        if base is None:
            return None
        return base * Decimal(str(v.get("scale", 1)))
    if isinstance(v, bool) or v is None:
        return None
    return to_dec(str(v))


def strip_comment(line: str) -> tuple[str, str]:
    m = re.search(r"(?<!\\)%", line)
    return (line[: m.start()], line[m.start():]) if m else (line, "")


def numbers_in(code: str, all_ints: bool) -> list[tuple[str, Decimal, bool]]:
    code = SKIP_ARGS.sub(" ", code)
    code = LENGTH.sub(" ", code)
    out = []
    for m in NUM.finditer(code):
        raw, pct = m.group(1), bool(m.group(2))
        d = to_dec(raw)
        if d is None:
            continue
        has_sep = bool(re.search(r",|\{,\}|\\,|~", raw))
        is_dec = "." in raw
        is_int = not is_dec and not has_sep
        if is_int and 1900 <= d <= 2099:
            reportable = False
        elif pct or is_dec or has_sep:
            reportable = True
        else:
            reportable = all_ints and abs(d) >= 10
        out.append((raw + ("%" if pct else ""), d, reportable))
    return out


def matches(printed: Decimal, want: Decimal) -> str | None:
    if printed == want:
        return "ok"
    exp = printed.as_tuple().exponent
    if not isinstance(exp, int):
        return None
    try:
        if want.quantize(Decimal(1).scaleb(min(exp, 0))) == printed:
            return "rounded"
    except InvalidOperation:
        return None
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("numbers")
    ap.add_argument("tex", nargs="+")
    ap.add_argument("--key-macro", action="append", default=[])
    ap.add_argument("--all-ints", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    data = json.loads(Path(a.numbers).read_text())
    meta = data.get("_meta", {}) if isinstance(data.get("_meta"), dict) else {}
    keys = {k: v for k, v in data.items() if not k.startswith("_")}
    want = {k: expected(v) for k, v in keys.items()}
    values = {}
    for k, d in want.items():
        if d is not None:
            values.setdefault(d, []).append(k)

    findings: list[dict] = []

    def add(kind, file="", line=0, **kw):
        findings.append({"kind": kind, "file": file, "line": line, **kw})

    for f in ("code_sha",):
        if PLACEHOLDER.match(str(meta.get(f, "")).strip()):
            add("NO-SHA", detail=f"_meta.{f} missing or placeholder")
    data_id = meta.get("data_sha") or meta.get("data_version") or ""
    if PLACEHOLDER.match(str(data_id).strip()):
        add("NO-SHA", detail="_meta.data_sha (or data_version) missing or placeholder")

    files: list[Path] = []
    for t in a.tex:
        p = Path(t)
        files += sorted(p.rglob("*.tex")) if p.is_dir() else [p]
    used: set[str] = set()
    macro_pat = (re.compile(r"\\(" + "|".join(map(re.escape, a.key_macro)) + r")\{([^}]+)\}")
                 if a.key_macro else None)

    for path in files:
        lines = path.read_text(errors="replace").splitlines()
        claimed: set[int] = set()
        for i, line in enumerate(lines):
            code, comment = strip_comment(line)
            if macro_pat:
                for m in macro_pat.finditer(code):
                    used.add(m.group(2))
                    if m.group(2) not in keys:
                        add("UNKNOWN-KEY", str(path), i + 1, key=m.group(2), detail=f"\\{m.group(1)}{{{m.group(2)}}}")
            mk = MARKER.search(comment)
            if not mk:
                continue
            target = i
            if not code.strip():
                target = next((j for j in range(i + 1, len(lines)) if strip_comment(lines[j])[0].strip()), i)
            claimed.add(target)
            nums = numbers_in(strip_comment(lines[target])[0], True)
            for key in [k for k in mk.group(1).split(",") if k]:
                used.add(key)
                if key not in keys:
                    add("UNKNOWN-KEY", str(path), target + 1, key=key, detail="marker names a key not in numbers file")
                    continue
                w = want[key]
                hit = next((r for raw, d, _ in nums if (r := matches(d, w))), None) if w is not None else None
                if hit:
                    add("OK" if hit == "ok" else "ROUNDED", str(path), target + 1, key=key, expected=str(w))
                else:
                    add("MISMATCH", str(path), target + 1, key=key, expected=str(w),
                        printed=[raw for raw, _, _ in nums])
        for i, line in enumerate(lines):
            if i in claimed:
                continue
            for raw, d, rep in numbers_in(strip_comment(line)[0], a.all_ints):
                if not rep:
                    continue
                cand = values.get(d) or [k for k, w in want.items() if w is not None and matches(d, w) == "rounded"]
                if cand:
                    add("UNMARKED", str(path), i + 1, printed=raw, detail=f"equals key(s) {', '.join(cand[:3])}; add %num:{cand[0]}")
                else:
                    add("NO-KEY", str(path), i + 1, printed=raw, detail="number with no key in numbers file")

    for k in sorted(set(keys) - used):
        add("UNUSED", key=k, detail="key never marked in the TeX")

    if a.json:
        print(json.dumps(findings, indent=1))
    else:
        for f in findings:
            loc = f"{f['file']}:{f['line']}" if f["file"] else "-"
            extra = " ".join(f"{k}={v}" for k, v in f.items() if k not in ("kind", "file", "line"))
            print(f"{f['kind']:11} {loc}  {extra}")
    count = {}
    for f in findings:
        count[f["kind"]] = count.get(f["kind"], 0) + 1
    print("summary:", ", ".join(f"{k}={v}" for k, v in sorted(count.items())) or "nothing found", file=sys.stderr)
    errors = sum(count.get(k, 0) for k in ("MISMATCH", "UNKNOWN-KEY", "NO-SHA"))
    warns = sum(count.get(k, 0) for k in ("NO-KEY", "UNMARKED", "UNUSED"))
    return 1 if errors or (a.strict and warns) else 0


if __name__ == "__main__":
    sys.exit(main())
