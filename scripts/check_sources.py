#!/usr/bin/env python3
"""Resolve source citations in skill files.

Finds `[src: ...]` blocks and `- Src: ...` lines in skills/**/*.md and checks
each citation whose prefix can be resolved locally:

  note:nNN...            notes/NN-*.md exists
  up:<path>              <repo>/<path> exists
  skill:<name>           ~/.claude/skills/<name>, the archive's 03-skills/<name>,
                         or skills/<name> in this repo exists
  arc:msr:<sha>          a patch file *_<sha>.patch under patches-msr-tpa/
  arc:ol:<sha>           a patch file *_<sha>.patch under patches-overleaf/
  arc:res:<sha>          sha appears in research-repo-commits.tsv
  arc:chat:group@<ts>    a message with that minute in the group messages.jsonl
  arc:<path>[:line]      the file exists in the archive
  arc:@<alias>[:line]    a role-based alias (ALIASES) for a name-bearing path
  arc:<ID>@v2            the ID appears in the archived master checklist v2

The private archive is found via $EVIDENCE_ARCHIVE or
~/Projects/supervisor-skills-msr-tpa. When it is absent, arc: citations are
skipped (reported as skipped, not failed). lit:, venue:, user:, proj: are
not checked here.

Exit 0 when no resolvable citation failed, 1 otherwise.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = Path(os.environ.get("EVIDENCE_ARCHIVE", Path.home() / "Projects" / "supervisor-skills-msr-tpa"))
LOCAL_SKILLS = Path.home() / ".claude" / "skills"
# skill: citations are provenance and keep the name the rule came from; names
# retired by ADR 0021 resolve to the folder that now holds that skill.
RENAMED = {
    "paper-writer": "sv-write-section", "intro-drafter": "sv-write-intro",
    "tech-paper-template": "sv-write-skeleton", "benchmark-paper-template": "sv-write-skeleton",
    "paper-polish": "sv-write-polish", "deai-writing": "sv-write", "style-mine": "sv-write-style-mine",
    "pre-submission-reviewer": "sv-review-once", "check-loop": "sv-review-loop",
    "feedback-to-revision": "sv-feedback", "rebuttal-guidance": "sv-feedback-rebuttal",
    "research-supervisor": "sv-supervisor", "research-records": "sv-supervisor-records",
    "lessons-harvest": "sv-supervisor-harvest", "vibe-research-workflow": "research-core",
    "figure-designer": "sv-figure-design", "drawio-reconstruction": "sv-figure-drawio",
    "study": "sv-study", "paper-quickread": "sv-quickread", "research-bridge": "sv-study-bridge",
    "idea-evaluator": "sv-idea", "deep-research": "sv-litreview", "proposal-writer": "sv-proposal",
    "experiment-workflow": "sv-experiment", "group-beamer": "sv-slides",
}

SRC_BLOCK = re.compile(r"\[src:\s*([^\]]+)\]")
SRC_LINE = re.compile(r"^\s*-\s+Src:\s*(.+)$", re.M)
# Role-based aliases for archive paths whose real names contain people's names.
ALIASES = {
    "@senior-a-comments": "02-comments-hao/comments_hao.md",
    "@advisor-glimpse": "04-comms/20260926-jimmy-advisor-paper-glimpse/README.md",
    "@threats-pivot": "04-comms/20260910-zhimin-d4d5-threats/README.md",
    "@senior-b-1on1": "04-comms/past-chat-jimmy/raw",
}
TOKEN = re.compile(r"(arc|note|up|skill):[^\s;,)]+")


def split_tokens(text: str) -> list[str]:
    return [m.group(0).rstrip(".") for m in TOKEN.finditer(text)]


class Resolver:
    def __init__(self) -> None:
        self.have_archive = ARCHIVE.is_dir()
        self._chat = None
        self._v2 = None
        self._res = None

    def chat_minutes(self) -> set[str]:
        if self._chat is None:
            self._chat = set()
            for f in (ARCHIVE / "04-comms").rglob("messages.jsonl"):
                for m in re.finditer(r'"ts":\s*"(\d{4}-\d\d-\d\dT\d\d:\d\d)', f.read_text()):
                    self._chat.add(m.group(1))
        return self._chat

    def v2_text(self) -> str:
        if self._v2 is None:
            p = ARCHIVE / "01-checklist" / "FULL-PAPER-CHECKLIST.md"
            self._v2 = p.read_text() if p.exists() else ""
        return self._v2

    def res_text(self) -> str:
        if self._res is None:
            p = ARCHIVE / "11-mining-github-issue-audit" / "research-repo-commits.tsv"
            self._res = p.read_text() if p.exists() else ""
        return self._res

    def check(self, tok: str) -> str:
        """Return 'ok', 'skip', or an error message."""
        kind, _, rest = tok.partition(":")
        if kind == "note":
            m = re.match(r"n(\d\d)", rest)
            if not m:
                return f"bad note id {tok}"
            return "ok" if list((ROOT / "notes").glob(f"{m.group(1)}-*.md")) else f"missing note {tok}"
        if kind == "up":
            return "ok" if (ROOT / rest).exists() else f"missing upstream path {tok}"
        if kind == "skill":
            name = rest.split("/")[0]
            name = RENAMED.get(name, name) if not (LOCAL_SKILLS / name).exists() else name
            for base in (LOCAL_SKILLS, ARCHIVE / "03-skills", ROOT / "skills"):
                if (base / name).exists():
                    return "ok"
            return f"unknown skill {tok}"
        if kind != "arc":
            return "skip"
        if not self.have_archive:
            return "skip"
        if rest.startswith("msr:") or rest.startswith("ol:"):
            sub = "patches-msr-tpa" if rest.startswith("msr:") else "patches-overleaf"
            sha = rest.split(":", 1)[1][:7]
            hits = list((ARCHIVE / "07-overleaf-history" / sub).glob(f"*_{sha}*.patch"))
            return "ok" if hits else f"no patch for {tok}"
        if rest.startswith("res:"):
            return "ok" if rest[4:11] in self.res_text() else f"no research commit {tok}"
        if rest.startswith("chat:group@"):
            ts = rest.split("@", 1)[1][:16]
            return "ok" if ts in self.chat_minutes() else f"no group message at {tok}"
        if rest.startswith("chat:"):
            return "skip"  # 1on1 and raw chats have no uniform index
        m = re.match(r"([A-Z]{2}-\d\d)@v2", rest)
        if m:
            return "ok" if f"### {m.group(1)} " in self.v2_text() else f"no v2 item {tok}"
        path = re.split(r":(?=\d)", rest)[0]
        if path.startswith("@"):
            if path not in ALIASES:
                return f"unknown alias {tok}"
            path = ALIASES[path]
        return "ok" if (ARCHIVE / path).exists() else f"missing archive file {tok}"


def main() -> int:
    r = Resolver()
    errors, ok, skipped = [], 0, 0
    for path in sorted((ROOT / "skills").rglob("*.md")):
        text = path.read_text()
        chunks = SRC_BLOCK.findall(text) + SRC_LINE.findall(text)
        for chunk in chunks:
            for tok in split_tokens(chunk):
                res = r.check(tok)
                if res == "ok":
                    ok += 1
                elif res == "skip":
                    skipped += 1
                else:
                    errors.append(f"{path.relative_to(ROOT)}: {res}")
    for e in sorted(set(errors)):
        print(e)
    note = "" if r.have_archive else " (archive not found: arc: citations skipped)"
    print(f"check_sources: {ok} resolved, {skipped} skipped, {len(set(errors))} failed{note}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
