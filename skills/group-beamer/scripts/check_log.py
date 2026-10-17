#!/usr/bin/env python3
"""Parse a XeLaTeX/latexmk .log for overfull and underfull boxes.

Maps warnings to shipout page numbers using [N markers. Severity:
  hbox > 10pt  -> critical
  hbox 1-10pt  -> warn
  hbox < 1pt   -> ignore
  underfull    -> info, unless badness == 10000 (then warn)

Also flags undefined control sequence, undefined citation, undefined
reference, and multiply defined labels as critical.

Usage:
  check_log.py <file.log>
  check_log.py --selftest
Exit 0 if no critical issues, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

OVERFULL_RE = re.compile(
    r"^(Overfull|Underfull) \\([hv])box \("
    r"(?:(?P<pt>\d+(?:\.\d+)?)pt too (?:wide|high)|badness (?P<badness>\d+))\)"
    r"(?: in paragraph at lines (?P<p1>\d+)--(?P<p2>\d+)"
    r"| in alignment at lines (?P<a1>\d+)--(?P<a2>\d+)"
    r"| detected at line (?P<d1>\d+)"
    r"| has occurred while \\output is active)?",
)
SHIPOUT_RE = re.compile(r"\[(\d+)(?:\s|\])")
UNDEF_CS = re.compile(r"Undefined control sequence")
UNDEF_CITE = re.compile(r"Citation [`'].*[`'] on page \d+ undefined")
UNDEF_REF = re.compile(r"Reference [`'].*[`'] on page \d+ undefined")
MULTIDEF = re.compile(r"Label [`'].*[`'] multiply defined")


def page_map(text: str) -> list[tuple[int, int]]:
    """Return list of (char_index, page_number) from [N shipout markers."""
    marks: list[tuple[int, int]] = []
    for m in SHIPOUT_RE.finditer(text):
        marks.append((m.start(), int(m.group(1))))
    return marks


def page_at(marks: list[tuple[int, int]], pos: int) -> int | None:
    current: int | None = None
    for idx, page in marks:
        if idx <= pos:
            current = page
        else:
            break
    return current


def classify_overfull(kind: str, box: str, pt: float | None, badness: int | None) -> str | None:
    if kind == "Overfull":
        if pt is None:
            return "warn"
        if pt > 10:
            return "critical"
        if pt >= 1:
            return "warn"
        return None
    # Underfull
    if badness == 10000:
        return "warn"
    return "info"


def parse_log(text: str) -> list[dict[str, object]]:
    marks = page_map(text)
    issues: list[dict[str, object]] = []
    for i, line in enumerate(text.splitlines()):
        m = OVERFULL_RE.match(line)
        if m:
            pt = float(m.group("pt")) if m.group("pt") else None
            badness = int(m.group("badness")) if m.group("badness") else None
            sev = classify_overfull(m.group(1), m.group(2), pt, badness)
            if sev is None:
                continue
            pos = text.find(line)
            issues.append(
                {
                    "severity": sev,
                    "kind": f"{m.group(1).lower()}-{m.group(2)}box",
                    "pt": pt,
                    "badness": badness,
                    "page": page_at(marks, pos if pos >= 0 else 0),
                    "line": i + 1,
                    "text": line,
                }
            )
            continue
        if UNDEF_CS.search(line):
            issues.append(
                {
                    "severity": "critical",
                    "kind": "undefined-cs",
                    "page": None,
                    "line": i + 1,
                    "text": line.strip(),
                }
            )
        elif UNDEF_CITE.search(line):
            issues.append(
                {
                    "severity": "critical",
                    "kind": "undefined-cite",
                    "page": None,
                    "line": i + 1,
                    "text": line.strip(),
                }
            )
        elif UNDEF_REF.search(line):  # backup-slide hyperlinks break silently otherwise
            issues.append(
                {
                    "severity": "critical",
                    "kind": "undefined-ref",
                    "page": None,
                    "line": i + 1,
                    "text": line.strip(),
                }
            )
        elif MULTIDEF.search(line):
            issues.append(
                {
                    "severity": "critical",
                    "kind": "multiply-defined",
                    "page": None,
                    "line": i + 1,
                    "text": line.strip(),
                }
            )
    return issues


def report(issues: list[dict[str, object]]) -> int:
    if not issues:
        print("check_log: no box or reference issues")
        return 0
    critical = 0
    for item in issues:
        page = item.get("page")
        page_s = f"p.{page}" if page is not None else "p.?"
        extra = ""
        if item.get("pt") is not None:
            extra = f" {item['pt']}pt"
        print(
            f"{item['severity']}: {item['kind']}{extra} {page_s} log:{item['line']}"
        )
        if item["severity"] == "critical":
            critical += 1
    print(f"check_log: {len(issues)} issue(s), {critical} critical")
    return 1 if critical else 0


def selftest() -> int:
    sample = (
        "This is XeTeX, Version\n"
        "[1 {/usr/local/texlive/2026/texmf-var/fonts/map/pdftex/updmap/pdftex.map}]\n"
        r"Overfull \hbox (12.5pt too wide) in paragraph at lines 10--12" + "\n"
        r"Overfull \hbox (2.0pt too wide) in paragraph at lines 20--21" + "\n"
        r"Overfull \hbox (0.4pt too wide) detected at line 30" + "\n"
        r"Underfull \hbox (badness 10000) in paragraph at lines 40--41" + "\n"
        r"Underfull \vbox (badness 1234) has occurred while \output is active" + "\n"
        "[2]\n"
        r"! Undefined control sequence." + "\n"
        "Citation `foo' on page 2 undefined\n"
        "Label `bar' multiply defined\n"
        "LaTeX Warning: Reference `fig:x' on page 2 undefined on input line 9.\n"
    )
    issues = parse_log(sample)
    kinds = [i["kind"] for i in issues]
    sevs = [i["severity"] for i in issues]
    pages = [i["page"] for i in issues]
    assert "overfull-hbox" in kinds
    assert sevs[0] == "critical" and issues[0]["pt"] == 12.5
    assert issues[0]["page"] == 1
    assert sevs[1] == "warn"
    # 0.4pt ignored
    assert not any(i.get("pt") == 0.4 for i in issues)
    assert any(i["kind"] == "underfull-hbox" and i["severity"] == "warn" for i in issues)
    assert any(i["kind"] == "underfull-vbox" and i["severity"] == "info" for i in issues)
    assert "undefined-cs" in kinds
    assert "undefined-ref" in kinds
    assert "undefined-cite" in kinds
    assert "multiply-defined" in kinds
    assert pages[0] == 1
    print("check_log: selftest ok")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if len(argv) != 1 or argv[0].startswith("-"):
        print("usage: check_log.py <file.log> | --selftest", file=sys.stderr)
        return 2
    path = Path(argv[0])
    if not path.is_file():
        print(f"check_log: not found: {path}", file=sys.stderr)
        return 2
    return report(parse_log(path.read_text(errors="replace")))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
