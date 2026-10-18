#!/usr/bin/env python3
"""Plan or apply the agent-sync links for this library (ADR 0021, "安装").

agent-sync keeps one live skills tree, `<agent-sync>/skills/`, which
~/.codex, ~/.claude and ~/.cursor point at. This script keeps one relative
link per skill there:

    <agent-sync>/skills/<name> -> ../external/supervisor-skills-plus/skills/<name>

and one per-machine link that agent-sync ignores:

    <agent-sync>/external/supervisor-skills-plus -> <this repo's main checkout>

Because every committed link stays inside the agent-sync tree, the same
commit resolves on every machine whatever its home directory is.

Default is a dry run that changes nothing. --apply writes the links (and
adds `external/` to agent-sync's .gitignore); committing in agent-sync is
left to the owner. Entries that are not links into external/ are never
touched; a name clash is reported instead.

Usage:
    python scripts/sync_agent_links.py [--agent-sync ~/agent-sync] [--repo PATH] [--apply]
    python scripts/sync_agent_links.py --selftest
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

EXTERNAL = "supervisor-skills-plus"
PREFIX = f"../external/{EXTERNAL}/skills/"


def main_checkout(start: Path) -> Path:
    """The main checkout of this repo, also when run from a worktree."""
    out = subprocess.run(
        ["git", "-C", str(start), "rev-parse", "--path-format=absolute", "--git-common-dir"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return Path(out).parent


def plan(agent_sync: Path, repo: Path) -> list[tuple[str, str]]:
    """Return (action, detail) pairs; actions: external, link, unlink, clash, ignore, ok."""
    steps: list[tuple[str, str]] = []
    ext = agent_sync / "external" / EXTERNAL
    if ext.is_symlink():
        if Path(os.readlink(ext)) != repo:
            steps.append(("clash", f"{ext} points to {os.readlink(ext)}, not {repo}"))
    elif ext.exists():
        steps.append(("clash", f"{ext} exists and is not a link; left alone"))
    else:
        steps.append(("external", f"{ext} -> {repo}"))
    gi = agent_sync / ".gitignore"
    if "external/" not in (gi.read_text().split() if gi.exists() else []):
        steps.append(("ignore", "add 'external/' to .gitignore"))

    wanted = sorted(p.name for p in (repo / "skills").iterdir() if (p / "SKILL.md").exists())
    live = agent_sync / "skills"
    for name in wanted:
        dest, target = live / name, PREFIX + name
        if dest.is_symlink() and os.readlink(dest) == target:
            steps.append(("ok", name))
        elif dest.exists() or dest.is_symlink():
            steps.append(("clash", f"{dest} exists and is not our link; left alone"))
        else:
            steps.append(("link", f"{name} -> {target}"))
    for dest in sorted(live.iterdir()) if live.is_dir() else []:
        if dest.is_symlink() and os.readlink(dest).startswith(PREFIX) and dest.name not in wanted:
            steps.append(("unlink", f"{dest.name} (no longer in this library)"))
    return steps


def apply(agent_sync: Path, repo: Path, steps: list[tuple[str, str]]) -> None:
    for action, detail in steps:
        if action == "external":
            (agent_sync / "external").mkdir(exist_ok=True)
            (agent_sync / "external" / EXTERNAL).symlink_to(repo)
        elif action == "ignore":
            gi = agent_sync / ".gitignore"
            text = gi.read_text() if gi.exists() else ""
            gi.write_text(text + ("" if text.endswith("\n") or not text else "\n")
                          + "# per-machine links to other repos (supervisor-skills-plus ADR 0021)\nexternal/\n")
        elif action == "link":
            name = detail.split(" ", 1)[0]
            (agent_sync / "skills" / name).symlink_to(PREFIX + name)
        elif action == "unlink":
            (agent_sync / "skills" / detail.split(" ", 1)[0]).unlink()


def report(steps: list[tuple[str, str]], applied: bool) -> int:
    counts: dict[str, int] = {}
    for action, detail in steps:
        counts[action] = counts.get(action, 0) + 1
        if action != "ok":
            print(f"{action:8} {detail}")
    print("summary:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if not applied:
        print("dry run: nothing changed; rerun with --apply to write the links")
    else:
        print("next: cd <agent-sync> && git status && git add skills .gitignore && git commit")
    return 1 if counts.get("clash") else 0


def selftest() -> None:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        repo, sync = root / "repo", root / "sync"
        for name in ("sv-a", "sv-a-b"):
            (repo / "skills" / name).mkdir(parents=True)
            (repo / "skills" / name / "SKILL.md").write_text("x")
        (sync / "skills").mkdir(parents=True)
        (sync / "skills" / "other").mkdir()
        (sync / "skills" / "old").symlink_to(PREFIX + "old")
        steps = plan(sync, repo)
        assert ("unlink", "old (no longer in this library)") in steps, steps
        apply(sync, repo, steps)
        assert (sync / "skills" / "sv-a-b" / "SKILL.md").read_text() == "x"
        assert not (sync / "skills" / "old").is_symlink() and (sync / "skills" / "other").is_dir()
        assert "external/" in (sync / ".gitignore").read_text().split()
        assert {a for a, _ in plan(sync, repo)} == {"ok"}
        # a real folder at external/<name> is a clash, never overwritten
        (sync / "external" / EXTERNAL).unlink()
        (sync / "external" / EXTERNAL).mkdir()
        steps = plan(sync, repo)
        assert any(a == "clash" and "not a link" in d for a, d in steps), steps
        apply(sync, repo, steps)
        assert (sync / "external" / EXTERNAL).is_dir() and not (sync / "external" / EXTERNAL).is_symlink()
    print("sync_agent_links selftest ok")


def cli() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--agent-sync", type=Path, default=Path.home() / "agent-sync")
    ap.add_argument("--repo", type=Path, help="checkout to link to (default: this repo's main checkout)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    agent_sync = a.agent_sync.expanduser().resolve()
    repo = (a.repo or main_checkout(Path(__file__).resolve().parent)).resolve()
    if not (agent_sync / "skills").is_dir():
        print(f"no skills/ under {agent_sync}", file=sys.stderr)
        return 2
    steps = plan(agent_sync, repo)
    if a.apply:
        apply(agent_sync, repo, steps)
    return report(steps, a.apply)


if __name__ == "__main__":
    sys.exit(cli())
