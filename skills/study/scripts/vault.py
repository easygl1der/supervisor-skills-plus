#!/usr/bin/env python3
"""Find, create and save the study vault (the learner's private records).

Usage:
    python vault.py where [--set PATH]   print the vault path (and record it with --set)
    python vault.py init PATH            create the layout and a git repo at PATH
    python vault.py save [-m MSG]        git add/commit in the vault; push if a remote exists
    python vault.py --selftest

Resolution order for `where`: $STUDY_VAULT, the path in ~/.config/study/vault,
~/study-vault, else ./reading (printed with a warning on stderr).
`save` never discards changes: if the push fails, the commit stays local and
the command to retry is printed.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

CONF = Path.home() / ".config" / "study" / "vault"
DIRS = ["profile", "concepts", "sessions", "papers", "books", "style"]
README = """# study-vault

Private learning records used by the `study` skill (supervisor-skills-plus).
Layout: profile/ (knowledge.yaml, sources.yaml, misconceptions.md), concepts/,
sessions/, papers/, books/, style/, index.json (append-only).
"""


def where() -> tuple[Path, bool]:
    env = os.environ.get("STUDY_VAULT")
    if env:
        return Path(env).expanduser(), True
    if CONF.exists() and CONF.read_text().strip():
        return Path(CONF.read_text().strip()).expanduser(), True
    home = Path.home() / "study-vault"
    if home.exists():
        return home, True
    return Path.cwd() / "reading", False


def git(path: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True)


def init(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for d in DIRS:
        (path / d).mkdir(exist_ok=True)
        keep = path / d / ".gitkeep"
        if not any((path / d).iterdir()):
            keep.touch()
    files = {
        "README.md": README,
        "profile/knowledge.yaml": "# one entry per concept; see skills/study/references/learner-profile.md\n[]\n",
        "profile/sources.yaml": "# books, courses, papers studied: title, chapters done, notes\n[]\n",
        "profile/misconceptions.md": "# Misconceptions\n\n| Date | Concept | Misconception | Level | Correction that worked |\n|---|---|---|---|---|\n",
        "index.json": "[]\n",
    }
    for rel, text in files.items():
        f = path / rel
        if not f.exists():
            f.write_text(text)
    if not (path / ".git").exists():
        git(path, "init", "-q")
    print(f"vault ready at {path}")


def save(msg: str) -> int:
    path, found = where()
    if not found or not (path / ".git").exists():
        print(f"vault.py: {path} is not a git vault; run `vault.py init <path>` first", file=sys.stderr)
        return 1
    git(path, "add", "-A")
    if not git(path, "status", "--porcelain").stdout.strip():
        print("vault.py: nothing to save")
        return 0
    c = git(path, "commit", "-q", "-m", msg)
    if c.returncode != 0:
        print("vault.py: commit failed:\n" + c.stderr, file=sys.stderr)
        return 1
    remotes = git(path, "remote").stdout.split()
    if not remotes:
        print("vault.py: committed locally (no remote configured)")
        return 0
    p = git(path, "push", "-q", "-u", remotes[0], "HEAD")  # -u: first push to a new remote sets upstream
    if p.returncode != 0:
        print(f"vault.py: committed locally; push failed ({p.stderr.strip()[:200]}). Retry: git -C {path} push")
        return 0
    print("vault.py: committed and pushed")
    return 0


def selftest() -> None:
    with tempfile.TemporaryDirectory() as d:
        v = Path(d) / "vault"
        init(v)
        assert (v / "profile" / "knowledge.yaml").exists() and (v / ".git").exists()
        os.environ["STUDY_VAULT"] = str(v)
        git(v, "config", "user.email", "t@t")
        git(v, "config", "user.name", "t")
        assert where() == (v, True)
        assert save("test") == 0 and git(v, "log", "--oneline").stdout.count("\n") == 1
        (v / "sessions" / "x.md").write_text("x")
        bare = Path(d) / "nowhere.git"
        git(v, "remote", "add", "origin", str(bare))  # remote that does not exist: push must fail softly
        assert save("second") == 0
        assert git(v, "log", "--oneline").stdout.count("\n") == 2
    print("vault selftest ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
    elif a[:1] == ["where"]:
        if "--set" in a:
            CONF.parent.mkdir(parents=True, exist_ok=True)
            CONF.write_text(str(Path(a[a.index("--set") + 1]).expanduser()) + "\n")
        p, ok = where()
        print(p)
        if not ok:
            print("warning: no study vault found; using ./reading (not shared across projects)", file=sys.stderr)
    elif a[:1] == ["init"] and len(a) == 2:
        init(Path(a[1]).expanduser())
    elif a[:1] == ["save"]:
        sys.exit(save(a[a.index("-m") + 1] if "-m" in a else "study: save session"))
    else:
        print(__doc__)
        sys.exit(2)
