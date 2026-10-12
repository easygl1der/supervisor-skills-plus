#!/usr/bin/env python3
"""Search a directory for identity leaks before an anonymous release.

Usage:
    python anon_grep.py <dir> [--terms "Name,Lab,handle"] [--terms-file f]
                        [--allow "noreply@example.org,anonymous.4open.science"]
                        [--git-log] [--json]

Reports file:line for:
- user terms (case-insensitive): names, affiliations, lab names, handles,
  personal domains, venue name if the artifact must stay venue-neutral
- e-mail addresses
- home paths: /Users/<name>/, /home/<name>/, C:\\Users\\<name>\\
- account URLs: github.com/<account>, gitlab.com/<account>,
  bitbucket.org/<account>, huggingface.co/<account>, <account>.github.io,
  orcid.org ids
- author fields in metadata: LICENSE / COPYING copyright lines, CITATION.cff
  authors, package.json "author", pyproject / setup.py / setup.cfg authors,
  Cargo.toml, DESCRIPTION, .zenodo.json creators, codemeta.json
- PDF metadata (/Author, /Creator) in .pdf files
- rendered pages (index.html and other .html): listed, since project pages
  carry names in templates and metadata
- .git/config: [user] section and remote URLs; with --git-log, the distinct
  commit authors (a mirror built from a clone carries its history)

Not checked here (do by hand and keep a note): the hosting account name, the
repository description and topics, image EXIF data, the anonymous mirror's
rendered copy after each refresh.

Exit 1 when anything is found, else 0.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
HOME = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\\\?Users\\\\?)([A-Za-z0-9._-]+)")
ACCOUNT = re.compile(
    r"(?:(?:github|gitlab)\.com|bitbucket\.org|huggingface\.co)[/:]([A-Za-z0-9_.-]+)"
    r"|([A-Za-z0-9-]+)\.github\.io|orcid\.org/(\d{4}-\d{4}-\d{4}-\d{3}[\dX])")
GENERIC_HOME = {"runner", "user", "username", "name", "me", "you", "shared", "ubuntu", "root", "anonymous"}
GENERIC_ACCOUNT = {"features", "settings", "orgs", "topics", "about", "pricing", "login", "datasets", "models",
                   "spaces", "docs", "anonymous", "your-account", "user", "username", "org"}
META_FILES = {
    "license", "license.md", "license.txt", "copying", "citation.cff", "package.json", "pyproject.toml",
    "setup.py", "setup.cfg", "cargo.toml", "description", ".zenodo.json", "codemeta.json", "authors",
    "authors.md", "contributors", "contributors.md", "notice", "mkdocs.yml", "_config.yml", "conf.py",
}
AUTHOR_LINE = re.compile(
    r"(copyright|\(c\)|©|\bauthors?\b|\bmaintainers?\b|family-names|given-names|creators?|"
    r"\bemail\b|author_email|\"name\"\s*:|^\s*-?\s*name\s*:)", re.I)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".mypy_cache", ".pytest_cache"}
TEXT_LIMIT = 5 * 1024 * 1024


def is_text(p: Path) -> bool:
    try:
        with p.open("rb") as fh:
            chunk = fh.read(4096)
    except OSError:
        return False
    return b"\0" not in chunk


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--terms", default="")
    ap.add_argument("--terms-file")
    ap.add_argument("--allow", default="")
    ap.add_argument("--git-log", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = Path(a.dir).resolve()
    terms = [t.strip() for t in a.terms.split(",") if t.strip()]
    if a.terms_file:
        terms += [t.strip() for t in Path(a.terms_file).read_text().splitlines()
                  if t.strip() and not t.startswith("#")]
    allow = [s.strip().lower() for s in a.allow.split(",") if s.strip()]
    term_pat = re.compile("|".join(re.escape(t) for t in terms), re.I) if terms else None
    hits: list[dict] = []

    def add(kind, path, line, text):
        low = text.lower()
        if any(x in low for x in allow):
            return
        rel = str(path.relative_to(root)) if isinstance(path, Path) else path
        hits.append({"kind": kind, "file": rel, "line": line, "text": text.strip()[:160]})

    for p in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts) or not p.is_file():
            continue
        name = p.name.lower()
        if p.suffix.lower() in (".html", ".htm"):
            add("rendered-page", p, 0, "rendered page in the artifact; prefer a complete README")
        if p.suffix.lower() == ".pdf":
            raw = p.read_bytes()[:TEXT_LIMIT]
            for m in re.finditer(rb"/(Author|Creator|Producer)\s*\(([^)]{0,120})\)", raw):
                val = m.group(2).decode("latin-1", "replace")
                if m.group(1) == b"Author" or (term_pat and term_pat.search(val)):
                    add("pdf-metadata", p, 0, f"/{m.group(1).decode()} ({val})")
            continue
        if p.stat().st_size > TEXT_LIMIT or not is_text(p):
            continue
        meta = name in META_FILES or name.startswith("license")
        for no, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
            if term_pat and term_pat.search(line):
                add("term", p, no, line)
            for m in EMAIL.finditer(line):
                add("email", p, no, m.group(0))
            for m in HOME.finditer(line):
                if m.group(1).lower() not in GENERIC_HOME:
                    add("home-path", p, no, m.group(0))
            for m in ACCOUNT.finditer(line):
                acct = (m.group(1) or m.group(2) or m.group(3) or "").lower()
                if acct and acct not in GENERIC_ACCOUNT:
                    add("account-url", p, no, m.group(0))
            if meta and AUTHOR_LINE.search(line):
                add("author-field", p, no, line)

    gitdir = root / ".git"
    if gitdir.is_dir():
        cfg = gitdir / "config"
        section = ""
        if cfg.exists():
            for no, line in enumerate(cfg.read_text(errors="replace").splitlines(), 1):
                s = line.strip()
                if s.startswith("["):
                    section = s
                elif section.startswith("[user") or (section.startswith("[remote") and s.startswith("url")):
                    add("git-config", ".git/config", no, f"{section} {s}")
        if a.git_log:
            out = subprocess.run(["git", "-C", str(root), "log", "--format=%an <%ae>|%cn <%ce>"],
                                 capture_output=True, text=True).stdout
            for who in sorted({w for l in out.splitlines() for w in l.split("|") if w}):
                add("git-author", "git log", 0, who)

    if a.json:
        print(json.dumps(hits, indent=1, ensure_ascii=False))
    else:
        for h in hits:
            print(f"{h['kind']:13} {h['file']}:{h['line']}  {h['text']}")
    counts: dict[str, int] = {}
    for h in hits:
        counts[h["kind"]] = counts.get(h["kind"], 0) + 1
    print("summary:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "no hits",
          "| check by hand: hosting account name, repo description, image EXIF, mirror copy", file=sys.stderr)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
