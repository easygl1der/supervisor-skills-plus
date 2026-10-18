#!/usr/bin/env python3
"""Check checklist items in research-core.

Scans skills/research-core/references/{checklists,fields,venues}/**/*.md for
items of the form

    ### <ID> <title>
    - [ ] Check: ...
    - Why: ...
    - Status: confirmed | candidate | deprecated...
    - Scope: ...
    - Owner: skill-a, skill-b
    - Src: ...

Rules:
- IDs match [A-Z]{2,3}-[0-9]{2,3} (an optional extra segment like FS-01 is fine)
  and are unique across all scanned files.
- Each item has Check, Status, Scope, Owner and Src lines.
- Status is confirmed, candidate, or starts with deprecated.
- Every Owner is an existing skill directory or a planned skill.

Exit 0 when clean, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "skills" / "research-core" / "references"
SCAN_DIRS = ["checklists", "fields", "venues"]

ITEM_HEAD = re.compile(r"^###\s+([A-Z]{2,3}(?:-[A-Z]{2,3})?-\d{2,3})\b")
FIELD = re.compile(r"^-\s+(?:\[[ xX]\]\s+)?(Check|Why|Status|Scope|Owner|Src):\s*(.*)$")
REQUIRED = ["Check", "Status", "Scope", "Owner", "Src"]

# Skills that DESIGN.md plans but that may not exist yet during Phase 4.
PLANNED = {
    "research-core", "experiment-workflow", "proposal-writer",
}


def known_skills() -> set[str]:
    skills_dir = ROOT / "skills"
    return {p.name for p in skills_dir.iterdir() if (p / "SKILL.md").exists()} | PLANNED


def parse(path: Path):
    items = []
    current = None
    for no, line in enumerate(path.read_text().splitlines(), 1):
        m = ITEM_HEAD.match(line)
        if m:
            current = {"id": m.group(1), "line": no, "fields": {}}
            items.append(current)
            continue
        if line.startswith("#"):
            current = None
            continue
        if current is not None:
            f = FIELD.match(line.strip())
            if f:
                current["fields"][f.group(1)] = f.group(2).strip()
    return items


def main() -> int:
    errors: list[str] = []
    seen: dict[str, str] = {}
    skills = known_skills()
    total = 0
    for sub in SCAN_DIRS:
        for path in sorted((CORE / sub).rglob("*.md")):
            rel = path.relative_to(ROOT)
            for item in parse(path):
                total += 1
                where = f"{rel}:{item['line']} {item['id']}"
                if item["id"] in seen:
                    errors.append(f"{where}: duplicate ID (first in {seen[item['id']]})")
                else:
                    seen[item["id"]] = str(rel)
                for key in REQUIRED:
                    if not item["fields"].get(key):
                        errors.append(f"{where}: missing '{key}:'")
                status = item["fields"].get("Status", "")
                if status and not (status in ("confirmed", "candidate") or status.startswith("deprecated")):
                    errors.append(f"{where}: bad Status '{status}'")
                for owner in re.split(r"[,\s]+", item["fields"].get("Owner", "")):
                    if owner and owner not in skills:
                        errors.append(f"{where}: unknown Owner skill '{owner}'")
    for e in errors:
        print(e)
    if errors:
        print(f"check_checklists: {len(errors)} problem(s) in {total} item(s)")
        return 1
    print(f"check_checklists: {total} item(s) clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
