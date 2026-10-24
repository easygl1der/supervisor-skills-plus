# Install and use this skill library

One copy of this repo serves Claude Code, Codex and Cursor. The skills are
linked, not copied, so `git pull` updates every tool. The library is twelve
`sv-` groups plus `research-core` (ADR 0021); see
[skills/README.en.md](skills/README.en.md).

## 1. Install

### As a plugin (Claude Code, Cursor)

The repo is a plugin named `sv-skills` (manifests: `plugin.json`,
`.cursor-plugin/plugin.json`, `.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json`). Skill names stay flat (`sv-study`,
`sv-study-paper`, ...); Claude Code may show them prefixed with the plugin
name.

- **Claude Code** (2.1.275+):
  `/plugin install sv-skills --marketplace easygl1der/supervisor-skills-plus`
  (older: `/plugin marketplace add easygl1der/supervisor-skills-plus`, then
  `/plugin install sv-skills@supervisor-skills-plus`).
- **Cursor**: Customize > Plugins > import from GitHub, enter
  `https://github.com/easygl1der/supervisor-skills-plus`. Cursor reads
  `.cursor-plugin/plugin.json`.
- **Codex / GPT**: no plugin import; use the symlink path below
  (`scripts/install.sh --targets codex`, or `sync_agent_links.py`).
- Other agents that read Agent Plugins (agent-plugins.org) use the root
  `plugin.json`.

Do not combine plugin install with the symlink install in the same tool:
you would get every skill twice.

### As symlinks (all tools)

```bash
git clone git@github.com:easygl1der/supervisor-skills-plus.git ~/Projects/supervisor-skills-plus
cd ~/Projects/supervisor-skills-plus
```

### With an agent-sync tree (the owner's machines)

When `~/.claude/skills`, `~/.codex/skills` and `~/.cursor/skills` are links
into `~/agent-sync/skills`, do not run `install.sh`; it would write into the
agent-sync tree. Instead:

```bash
python3 scripts/sync_agent_links.py            # dry run: prints the plan
python3 scripts/sync_agent_links.py --apply    # writes the links
cd ~/agent-sync && git status && git add skills .gitignore && git commit -m "link supervisor-skills-plus"
```

The script keeps one per-machine link that agent-sync ignores,
`~/agent-sync/external/supervisor-skills-plus` (to this checkout), and one
committed relative link per skill, `skills/<name> ->
../external/supervisor-skills-plus/skills/<name>`. The committed links
resolve on every machine whatever its home directory is. On another
machine, clone this repo, `git pull` in agent-sync, and run the script with
`--apply`: the skill links are already committed, so it only adds the
external link.

### Without agent-sync

```bash
scripts/install.sh --dry-run          # see what will happen
scripts/install.sh                    # claude, codex and cursor
scripts/install.sh --targets claude   # only Claude Code
```

The script links every `skills/<name>` into the tools' skill folders, moves
an existing folder of the same name to `~/.<tool>/skills-backup/<date>/`,
removes links into this repo whose skill no longer exists (the 26 names
retired by ADR 0021), and moves the older local skills this library merged
(se-paper-*, deai-paper-writing, avoid-ai-writing, humanize-paper,
parse-pdf-comments, collaborative-review-notes, drawio-figure-replication,
tikz-diagram-review, anti-accretive-docs, architecture-decision-records,
research-docs-linear-lifecycle, paper) to the backup folder; skip that with
`--no-backup-retired`. `--uninstall` removes only links into this repo.

Restart the agent tools afterwards.

### Optional dependencies

| For | Install |
|---|---|
| Repo checks (`scripts/lint_skills.py`) | `python3 -m pip install -r requirements-lint.txt` (PyYAML) |
| PDF comment extraction (`sv-feedback-revise`) | `python3 -m pip install pymupdf` |
| draw.io reconstruction (`sv-figure-drawio`) | draw.io desktop or CLI; see the skill |
| HTML figures (`sv-figure-explain`, `sv-figure-html`) | Node and Chrome; `npm i` once in `skills/sv-figure-explain/kit` |
| Group-meeting Beamer (`sv-slides`) | TeX Live or BasicTeX plus `tlmgr install latexmk moloch beamertheme-simpleplus ctex`; `pymupdf` for page renders. Do not install a full MacTeX tree from the skill. |

## 2. Use

Describe the task and let the matching group route it, or call a
sub-command directly: `/sv-write-polish`, `/sv-study-paper`,
`/sv-figure-plot`. Only the twelve entries and `research-core` are in the
agent's skill list; sub-commands run when named.

| Stage | Groups |
|---|---|
| Start of a session, what next | `sv-supervisor` |
| Reading and learning | `sv-quickread`, `sv-study`, `sv-litreview` |
| Idea, design, proposal | `sv-idea`, `sv-litreview`, `sv-proposal` |
| Experiments | `sv-experiment`, `sv-supervisor-records` |
| Writing | `sv-write` |
| Figures | `sv-figure` |
| Feedback and reviews | `sv-feedback` |
| Before submission | `sv-review` |
| Group meetings | `sv-slides` |
| After each paper | `sv-supervisor-harvest` |

## 3. Start a new project

1. In the project repo, run `/sv-supervisor-init`. It interviews you and
   writes `research.yaml` (from
   `skills/research-core/assets/templates/research.yaml`) and `docs/`
   (STATUS, TODO, ADR 0001 for the sources of truth, logs, runs).
2. Every skill reads `research.yaml` first and loads the core rules, the
   field profile (`se`, `ai-ml`, `math`, `stats`, `causal`) and the venue
   profile from `research-core`.
3. `/sv-supervisor-brief` at the start of a session shows the stage,
   blockers, open reviewer notes, overdue guidance and the next skills.

## 4. Update

```bash
cd ~/Projects/supervisor-skills-plus && git pull
```

Links follow the repo. When skills were added, renamed or removed, rerun
`scripts/sync_agent_links.py --apply` (agent-sync) or `scripts/install.sh`.

## 5. Keep the library growing

After a submission, after reviews, or after expert advice, run
`/sv-supervisor-harvest` in the project. It proposes rule changes for
`research-core` on a `learn/<source>` branch, each with its source; you
approve before merge.

## 6. Checks

```bash
python scripts/lint_skills.py        # skill conventions and the sv- group rules
python scripts/check_shared_sync.py  # duplicated reference copies (none at present)
python scripts/check_checklists.py   # checklist item format and owners
python scripts/check_sources.py      # every [src: ...] resolves
```

`check_sources.py` resolves `arc:` citations against the private evidence
archive (`$EVIDENCE_ARCHIVE` or `~/Projects/supervisor-skills-msr-tpa`) and
skips them when it is absent. `skill:` citations keep the name a rule came
from; names retired by ADR 0021 resolve to their new folders, and a skill
outside this library that is not installed locally is skipped, not failed.
`up:` citations resolve to files in this repo (handbook chapters, notes,
skill references).
