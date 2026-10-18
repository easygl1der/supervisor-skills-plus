#!/usr/bin/env python3
"""Review open actions in expert guidance records and feedback tables.

Usage:
    python guidance_review.py <project_dir> [--today YYYY-MM-DD]

Reads docs/guidance/*.md (format: research-core/assets/templates/guidance-record.md)
and docs/feedback/*.md (response tables). For guidance records it joins the
"Actions" table with the "Follow-up check" table by action id and reports:
- open actions, overdue ones first (Due column parsed as YYYY-MM-DD when possible)
- actions marked done without evidence
For feedback tables it reports rows whose Verified column is not "by diff".
Exit 1 if any action is overdue or any done item lacks evidence, else 0.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


def tables(text: str) -> list[tuple[str, list[dict]]]:
    """Return (section heading, rows) for each markdown table."""
    out, heading, lines = [], "", text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            head = [c.strip() for c in line.strip("|").split("|")]
            rows, i = [], i + 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                rows.append(dict(zip(head, cells)))
                i += 1
            out.append((heading, rows))
            continue
        i += 1
    return out


def parse_date(s: str):
    m = re.search(r"\d{4}-\d{2}-\d{2}", s or "")
    return dt.date.fromisoformat(m.group(0)) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    ap.add_argument("--today", default=None)
    a = ap.parse_args()
    root = Path(a.project_dir)
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    problems = 0

    for rec in sorted((root / "docs" / "guidance").glob("*.md")):
        actions, follow = {}, {}
        for heading, rows in tables(rec.read_text()):
            for r in rows:
                aid = r.get("Action id", "")
                if not aid or aid.startswith("G-<"):
                    continue
                if heading.lower().startswith("actions"):
                    actions[aid] = r
                elif heading.lower().startswith("follow-up"):
                    follow[aid] = r
        for aid, r in actions.items():
            f = follow.get(aid, {})
            status = (f.get("Status (open / done / dropped)") or f.get("Status") or "open").lower()
            evidence = f.get("Evidence (commit, run id, file)") or f.get("Evidence") or ""
            due = parse_date(r.get("Due", ""))
            if status.startswith("done") and not evidence:
                print(f"NO-EVIDENCE {rec.name} {aid}: {r.get('What', '')}")
                problems += 1
            elif status.startswith("open"):
                overdue = due is not None and due < today
                tag = "OVERDUE" if overdue else "open"
                problems += overdue
                print(f"{tag:11} {rec.name} {aid} due {r.get('Due', '?')} owner {r.get('Owner', '?')}: {r.get('What', '')}")

    for tab in sorted((root / "docs" / "feedback").glob("*.md")):
        for _, rows in tables(tab.read_text()):
            for r in rows:
                fid = r.get("ID", "")
                if not fid.startswith("FB-"):
                    continue
                ver = (r.get("Verified") or "").lower()
                if "diff" not in ver:
                    print(f"UNVERIFIED  {tab.name} {fid}: {r.get('Decision', '')} {r.get('Change made', '')}")

    print(f"guidance_review: {problems} blocking problem(s) as of {today}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
