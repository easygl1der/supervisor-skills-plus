# Install and use Supervisor-Skills Plus

One copy of this repo serves Claude Code, Codex and Cursor. Each skill folder
is symlinked into the tools' skill folders, so `git pull` updates all three.

## 1. Install

```bash
git clone git@github.com:easygl1der/supervisor-skills-plus.git ~/Projects/supervisor-skills-plus
cd ~/Projects/supervisor-skills-plus
scripts/install.sh --dry-run          # see what will happen
scripts/install.sh                    # claude, codex and cursor
scripts/install.sh --targets claude   # only Claude Code
```

What the script does:

- links every `skills/<name>` into `~/.claude/skills/`, `~/.codex/skills/`
  and `~/.cursor/skills/`;
- moves an existing folder with the same name to
  `~/.<tool>/skills-backup/<date>/` before linking;
- also moves the old local skills that this library merged (se-paper-*,
  deai-paper-writing, avoid-ai-writing, humanize-paper, parse-pdf-comments,
  collaborative-review-notes, drawio-figure-replication, tikz-diagram-review,
  anti-accretive-docs, architecture-decision-records,
  research-docs-linear-lifecycle, paper) to the backup folder, so agents do
  not pick the old version. Skip this with `--no-backup-retired`.

Restart the agent tools afterwards.

Uninstall: `scripts/install.sh --uninstall` removes only links that point
into this repo. Restore old skills from the backup folder by moving them back.

Optional dependencies:

| For | Install |
|---|---|
| Repo checks (`scripts/lint_skills.py`) | `python3 -m pip install -r requirements-lint.txt` (PyYAML) |
| PDF comment extraction (`feedback-to-revision`) | `python3 -m pip install pymupdf` |
| Figure checks (`drawio-reconstruction`, `figure-designer`) | draw.io desktop or CLI; see each skill |

## 2. Update

```bash
cd ~/Projects/supervisor-skills-plus && git pull
```

Links follow the repo, so nothing else is needed. Run `scripts/install.sh`
again only when new skills were added.

## 3. Start a new project

1. In the project repo, ask the agent: "use research-supervisor to set up
   this project". It interviews you and writes:
   - `research.yaml` (field, venue, paper type, stage, repos, sources of
     truth, data location, experiment backend, comment macros, check-loop
     budget), from `skills/research-core/assets/templates/research.yaml`;
   - `docs/STATUS.md`, `docs/TODO.md`, `docs/adr/` (ADR 0001 records the
     sources of truth), `docs/log/`, `docs/runs.md`.
2. Or copy the template by hand:
   ```bash
   cp ~/Projects/supervisor-skills-plus/skills/research-core/assets/templates/research.yaml .
   ```
   and fill in at least `field`, `venue`, `paper_type`, `stage`.
3. Every skill reads `research.yaml` first and loads the core rules, the
   field profile (`se`, `ai-ml`, `math`, `stats`, `causal`) and the venue
   profile from `research-core`.

Typical flow:

| Stage | Skills |
|---|---|
| Idea and design | idea-evaluator, deep-research |
| Experiments | experiment-workflow, research-records |
| Writing | paper-writer, intro-drafter, journal-adapt, check-loop |
| Figures | figure-designer, drawio-reconstruction |
| Feedback and guidance | feedback-to-revision |
| Before submission | pre-submission-reviewer |
| Reviews | feedback-to-revision, rebuttal-guidance |
| After each paper | lessons-harvest |

At any point: "use research-supervisor" shows the stage, blockers, open
reviewer notes, overdue guidance actions and the next skills.

## 4. Keep the library growing

After a submission, after reviews, or when you get expert advice, run
`lessons-harvest` in the project. It proposes new or updated rules for
`research-core` on a `learn/<source>` branch in this repo, each with its
source; you approve before merge. New fields start from
`research-core/references/fields/_template.md`.

## 5. Sync with upstream HKUSTDial/Supervisor-Skills

```bash
cd ~/Projects/supervisor-skills-plus
git fetch upstream
git checkout -b sync/upstream-$(date +%Y%m%d) main
git merge upstream/main
# resolve conflicts so that our additions survive; then:
python scripts/lint_skills.py && python scripts/check_shared_sync.py \
  && python scripts/check_checklists.py && python scripts/check_sources.py
git checkout main && git merge --no-ff sync/upstream-$(date +%Y%m%d)
git push origin main
```

Record each sync in `CHANGELOG.md`. Never push to `upstream`; its push URL
is disabled in this clone.

## 6. Checks

```bash
python scripts/lint_skills.py        # upstream skill conventions
python scripts/check_shared_sync.py  # shared reference copies identical
python scripts/check_checklists.py   # checklist item format and owners
python scripts/check_sources.py      # every [src: ...] resolves
```

`check_sources.py` resolves `arc:` citations against the private evidence
archive (`$EVIDENCE_ARCHIVE` or `~/Projects/supervisor-skills-msr-tpa`) and
skips them when it is absent.
