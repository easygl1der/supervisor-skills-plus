#!/usr/bin/env python3
"""Refuse a sync that would overwrite someone else's edits.

Usage:
    python sync_guard.py <repo_dir> <remote> <branch> [--no-fetch]

Fetches <remote>/<branch> and checks that it is an ancestor of the local
HEAD (a fast-forward push is then safe). If the remote has commits that HEAD
does not contain, prints them with author, time and diffstat and exits 1:
merge or rebase first, never force or copy over.

Typical use before pushing to an Overleaf git remote:
    python sync_guard.py paper overleaf master
"""
from __future__ import annotations

import subprocess
import sys


def git(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        print(__doc__)
        return 2
    repo, remote, branch = args
    if "--no-fetch" not in sys.argv:
        f = git(repo, "fetch", remote, branch)
        if f.returncode != 0:
            print(f"sync_guard: fetch failed: {f.stderr.strip()}")
            return 2
    ref = f"{remote}/{branch}"
    if git(repo, "rev-parse", "--verify", ref).returncode != 0:
        print(f"sync_guard: {ref} not found")
        return 2
    if git(repo, "merge-base", "--is-ancestor", ref, "HEAD").returncode == 0:
        ahead = git(repo, "rev-list", "--count", f"{ref}..HEAD").stdout.strip()
        print(f"sync_guard: OK, {ref} is contained in HEAD; push is a fast-forward ({ahead} new commit(s))")
        return 0
    log = git(repo, "log", "--format=%h %an %ad %s", "--date=iso", f"HEAD..{ref}").stdout
    stat = git(repo, "diff", "--stat", f"HEAD...{ref}").stdout
    print(f"sync_guard: STOP. {ref} has commits that HEAD does not contain:")
    print(log.rstrip())
    print("Files changed on the remote side since the common base:")
    print(stat.rstrip())
    print("Merge or rebase onto the remote first. Do not force-push or copy files over.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
