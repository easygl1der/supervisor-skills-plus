#!/usr/bin/env python3
"""Structural linter for this library's SKILL.md files.

Enforces the hard rules for SKILL.md structure:
 - SKILL.md body (after frontmatter) is at most 500 lines
 - description is 40..80 words, third person, contains at least one "Use when" clause
 - no em-dash in SKILL.md or references/*.md
 - no CJK characters in SKILL.md
 - every "See: references/X.md" and "See: ../<skill>/references/X.md" pointer resolves
 - no nested references (references/X.md may not link to references/Y.md)
 - references/*.md longer than 100 lines must have a table of contents in the first 20 lines
 - no Claude or Anthropic attribution strings
 - ADR 0021 groups: an entry `sv-<group>` is auto-invocable, its description
   is at most 60 words and its body at most 120 lines; every sub-command
   `sv-<group>-<name>` sets `disable-model-invocation: true`, has a body of
   at most 100 lines (sv-figure-drawio excepted), and is named in its
   entry's body; every `sv-<group>-...` name an entry mentions exists

Exit 0 on clean, 1 on any violation. Prints one line per violation.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError as exc:
    raise SystemExit(
        "PyYAML is required; run 'python -m pip install -r requirements-lint.txt'"
    ) from exc

SKILL_ROOT = Path("skills")

EM_DASH = "\u2014"
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
REF_POINTER = re.compile(r"See:\s+references/([A-Za-z0-9_\-./]+\.md)")
# Pointer into another skill's references (ADR 0021 groups share one folder).
SIBLING_POINTER = re.compile(r"See:\s+\.\./([a-z0-9][a-z0-9\-]*)/references/([A-Za-z0-9_\-./]+\.md)")
REF_LINK = re.compile(r"\[[^\]]+\]\((?:\./)?references/([A-Za-z0-9_\-./]+\.md)\)")
BANNED_ATTRIB = [
    "Co-Authored-By: Claude",
    "Generated with [Claude Code]",
    "🤖 Generated with",
    "Anthropic SDK",  # only flags as attribution in skill files, not in script strings themselves
]


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Return (frontmatter dict, body). Raises ValueError on malformed."""
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing YAML frontmatter closer '---'")
    fm_text = text[4:end]
    body = text[end + 5 :]

    try:
        parsed = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        problem = getattr(exc, "problem", None) or str(exc)
        mark = getattr(exc, "problem_mark", None)
        location = f" at line {mark.line + 1}, column {mark.column + 1}" if mark else ""
        raise ValueError(f"invalid YAML frontmatter{location}: {problem}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("YAML frontmatter must be a mapping")
    if not all(isinstance(key, str) for key in parsed):
        raise ValueError("YAML frontmatter keys must be strings")
    return parsed, body


def check_description(desc: str) -> list[str]:
    errors: list[str] = []
    clean = desc.replace(">-", "").replace(">", "").replace("\n", " ").strip()
    words = [w for w in clean.split() if w]
    if not (40 <= len(words) <= 80):
        errors.append(f"description has {len(words)} words; must be 40..80")
    first_person = re.search(r"\b(I|my|we|our|us)\b", clean, re.IGNORECASE)
    if first_person:
        errors.append(
            "description contains first-person pronoun; must be third person"
        )
    if "Use when" not in clean and "use when" not in clean:
        errors.append("description must contain at least one 'Use when' clause")
    return errors


def check_body(body: str, max_lines: int = 500) -> list[str]:
    errors: list[str] = []
    lines = body.splitlines()
    if len(lines) > max_lines:
        errors.append(f"body has {len(lines)} lines; must be <= {max_lines}")
    if EM_DASH in body:
        first = body.find(EM_DASH)
        line_no = body[:first].count("\n") + 1
        errors.append(f"em-dash found at body line {line_no}")
    m = CJK.search(body)
    if m:
        line_no = body[: m.start()].count("\n") + 1
        errors.append(
            f"CJK character {m.group()!r} found at body line {line_no}; SKILL.md is English-only"
        )
    for banned in BANNED_ATTRIB:
        if banned in body:
            errors.append(f"banned attribution string found: {banned!r}")
    return errors


def check_pointers(skill_dir: Path, body: str) -> list[str]:
    errors: list[str] = []
    targets: set[str] = set()
    for m in REF_POINTER.finditer(body):
        targets.add(m.group(1))
    for m in REF_LINK.finditer(body):
        targets.add(m.group(1))
    for target in targets:
        ref = skill_dir / "references" / target
        if not ref.exists():
            errors.append(f"pointer to missing reference: references/{target}")
    for m in SIBLING_POINTER.finditer(body):
        if not (skill_dir.parent / m.group(1) / "references" / m.group(2)).exists():
            errors.append(f"pointer to missing reference: ../{m.group(1)}/references/{m.group(2)}")
    return errors


def check_reference_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        errors.append(f"{path}: not valid UTF-8")
        return errors
    if EM_DASH in text:
        first = text.find(EM_DASH)
        line_no = text[:first].count("\n") + 1
        errors.append(f"{path}: em-dash at line {line_no}")
    for banned in BANNED_ATTRIB:
        if banned in text:
            errors.append(f"{path}: banned attribution {banned!r}")
    # nested references check
    for m in REF_POINTER.finditer(text):
        errors.append(
            f"{path}: nested reference pointer 'See: references/{m.group(1)}' is forbidden"
        )
    # ToC check for files > 100 lines
    lines = text.splitlines()
    if len(lines) > 100:
        head = "\n".join(lines[:20]).lower()
        if (
            "table of contents" not in head
            and "## contents" not in head
            and "toc" not in head
        ):
            errors.append(
                f"{path}: file has {len(lines)} lines but no table of contents in first 20 lines"
            )
    return errors


def lint_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors

    try:
        text = skill_md.read_text()
    except UnicodeDecodeError:
        errors.append(f"{skill_md}: not valid UTF-8")
        return errors

    try:
        fm, body = parse_frontmatter(text)
    except ValueError as e:
        errors.append(f"{skill_md}: {e}")
        return errors

    if "name" not in fm:
        errors.append(f"{skill_md}: frontmatter missing 'name'")
    elif not isinstance(fm["name"], str):
        errors.append(f"{skill_md}: frontmatter 'name' must be a string")
    else:
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-]{0,62}[a-z0-9]", fm["name"]):
            errors.append(
                f"{skill_md}: name {fm['name']!r} must be kebab-case, 2..64 chars, [a-z0-9-]"
            )
        if fm["name"] != skill_dir.name:
            errors.append(
                f"{skill_md}: frontmatter name {fm['name']!r} must match directory name {skill_dir.name!r}"
            )

    if "description" not in fm:
        errors.append(f"{skill_md}: frontmatter missing 'description'")
    elif not isinstance(fm["description"], str):
        errors.append(f"{skill_md}: frontmatter 'description' must be a string")
    else:
        errors.extend(f"{skill_md}: {e}" for e in check_description(fm["description"]))

    errors.extend(f"{skill_md}: {e}" for e in check_body(body))
    errors.extend(f"{skill_md}: {e}" for e in check_pointers(skill_dir, body))

    ref_dir = skill_dir / "references"
    if ref_dir.is_dir():
        for ref_md in sorted(ref_dir.rglob("*.md")):
            errors.extend(check_reference_file(ref_md))

    return errors


# ADR 0021: drawio-reconstruction was kept verbatim at the owner's request.
BODY_CAP_EXEMPT = {"sv-figure-drawio"}
SV_NAME = re.compile(r"`(sv-[a-z0-9-]+)`")


def read_skill(skill_dir: Path) -> tuple[dict[str, object], str] | None:
    try:
        return parse_frontmatter((skill_dir / "SKILL.md").read_text())
    except (OSError, ValueError, UnicodeDecodeError):
        return None  # lint_skill already reports these


def lint_groups(skill_dirs: list[Path]) -> list[str]:
    """Check the sv- group conventions of ADR 0021 across all skills."""
    errors: list[str] = []
    parsed = {d.name: read_skill(d) for d in skill_dirs if (d / "SKILL.md").exists()}
    parsed = {k: v for k, v in parsed.items() if v is not None}
    names = set(parsed)
    sv = {n for n in names if n.startswith("sv-")}
    # Structure decides the role, not the flag: an entry has no sv- parent.
    entries = {n for n in sv if not any(n.startswith(p + "-") for p in sv if p != n)}

    def entry_of(name: str) -> str | None:
        owners = [e for e in entries if name.startswith(e + "-")]
        return max(owners, key=len) if owners else None

    for name in sorted(names):
        if not name.startswith("sv-"):
            continue
        fm, body = parsed[name]
        lines = len(body.splitlines())
        where = f"skills/{name}/SKILL.md"
        if name in entries:
            if fm.get("disable-model-invocation"):
                errors.append(f"{where}: group entry must stay auto-invocable (no disable-model-invocation)")
            words = len(str(fm.get("description", "")).split())
            if words > 60:
                errors.append(f"{where}: entry description has {words} words; must be <= 60")
            if lines > 120:
                errors.append(f"{where}: entry body has {lines} lines; must be <= 120")
            for m in SV_NAME.finditer(body):
                ref = m.group(1)
                if ref.startswith(name + "-") and ref not in names:
                    errors.append(f"{where}: routes to missing sub-command {ref}")
            continue
        owner = entry_of(name)
        if fm.get("disable-model-invocation") is not True:
            errors.append(f"{where}: sub-command must set disable-model-invocation: true")
        if lines > 100 and name not in BODY_CAP_EXEMPT:
            errors.append(f"{where}: sub-command body has {lines} lines; must be <= 100")
        if f"`{name}`" not in parsed[owner][1]:
            errors.append(f"{where}: not named in the routing table of {owner}")
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)

    if not SKILL_ROOT.is_dir():
        print(f"lint: SKILL_ROOT {SKILL_ROOT} does not exist; nothing to lint.")
        return 0

    skill_dirs = [p for p in sorted(SKILL_ROOT.iterdir()) if p.is_dir()]
    if not skill_dirs:
        print(f"lint: no skills under {SKILL_ROOT}; nothing to lint.")
        return 0

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(lint_skill(skill_dir))
    all_errors.extend(lint_groups(skill_dirs))

    if all_errors:
        print(f"lint: {len(all_errors)} violation(s)")
        for e in all_errors:
            print(f"  {e}")
        return 1

    print(f"lint: {len(skill_dirs)} skill(s) clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
