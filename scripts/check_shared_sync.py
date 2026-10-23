#!/usr/bin/env python3
"""Shared-reference sync checker for this skill library.

Some reference files are shared across skills. Because every skill
directory must stay self-contained (a user may copy a single skill
folder), shared files are duplicated per consuming skill: one copy is
canonical, the others carry a header comment pointing at it.

This script verifies that every copy is byte-identical to its canonical
after stripping the leading HTML comment header from both sides, so the
headers may differ ("Canonical copy..." versus "Copy...") while the
content may not.

Exit 0 when all pairs match, 1 on any divergence. Prints one line per
violation.
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path("skills")

# canonical (relative to SKILL_ROOT) -> list of copies (same)
# ADR 0021 collapsed the sv-write copies into one shared folder; add pairs here
# only if a reference is ever duplicated across skill folders again.
SHARED: dict[str, list[str]] = {}


def strip_header(text: str) -> str:
    """Drop one leading HTML comment block (the canonical/copy header)."""
    stripped = text.lstrip()
    if stripped.startswith("<!--"):
        end = stripped.find("-->")
        if end != -1:
            return stripped[end + 3 :].lstrip("\n")
    return text


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    errors: list[str] = []

    for canonical_rel, copies in SHARED.items():
        canonical = repo_root / SKILL_ROOT / canonical_rel
        if not canonical.exists():
            errors.append(f"canonical missing: {canonical_rel}")
            continue
        canonical_body = strip_header(canonical.read_text())
        for copy_rel in copies:
            copy = repo_root / SKILL_ROOT / copy_rel
            if not copy.exists():
                errors.append(f"copy missing: {copy_rel}")
                continue
            if strip_header(copy.read_text()) != canonical_body:
                errors.append(
                    f"out of sync: {copy_rel} differs from canonical {canonical_rel}"
                )

    if errors:
        print(f"shared-sync: {len(errors)} violation(s)")
        for e in errors:
            print(f"  {e}")
        return 1

    n_pairs = sum(len(v) for v in SHARED.values())
    print(f"shared-sync: {n_pairs} copy(ies) in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
