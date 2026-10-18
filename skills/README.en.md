# Skills: twelve groups, one name to remember per task

[中文](README.md)

Since ADR 0021 the library is organised as twelve **groups**. Each group
has one entry skill `sv-<group>` that the agent may pick on its own, and
several **sub-commands** `sv-<group>-<name>` that run only when you call
them by name. A shared library, `research-core`, holds the rules every
group loads.

| You want to | Say or type |
|---|---|
| let the agent pick | describe the task; the matching `sv-<group>` routes it and tells you which sub-command it chose |
| choose exactly | `/sv-write-polish`, `/sv-study-paper`, `/sv-figure-plot`, ... |

Names are the same in Claude Code and Cursor. Only the 12 entries and
`research-core` sit in the agent's skill list; the 50 sub-commands do not,
so adding precision does not crowd the list.

## Where this file sits

| Entry point | For |
|---|---|
| [`../README.en.md`](../README.en.md) | Why the project exists, the handbook, installation |
| [`../handbook/`](../handbook/) / [`../handbook-en/`](../handbook-en/) | The methodology the skills are distilled from |
| **This file** | Which group and sub-command fits a task |
| `SKILL.md` in each folder | The executable spec for the agent |
| [`../docs/adr/0021-sv-skill-groups.md`](../docs/adr/0021-sv-skill-groups.md) | Why the library is grouped this way, and the old-to-new name map |

## The twelve groups

| Group | Sub-commands | What it covers |
|---|---|---|
| [`sv-supervisor`](sv-supervisor/SKILL.md) | `-brief` `-init` `-records` `-harvest` | Session brief and routing, project start-up, STATUS / TODO / ADRs / logs, lessons into research-core |
| [`sv-quickread`](sv-quickread/SKILL.md) | `-card` `-style` | Nine-section five-minute card of one paper; optional style card |
| [`sv-study`](sv-study/SKILL.md) | `-quick-explain` `-paper` `-chapter` `-visual-explain` `-drill` `-bridge` | Understanding-first study with restatement and diagnosis; bridge to the project |
| [`sv-idea`](sv-idea/SKILL.md) | `-evaluate` `-fatal-flaws` | Full idea evaluation, or the early fatal-flaws gate only |
| [`sv-litreview`](sv-litreview/SKILL.md) | `-survey` `-map` | Survey-grade literature review; map of what you have read |
| [`sv-proposal`](sv-proposal/SKILL.md) | `-kaiti` `-grant` `-statement` | Thesis proposal, grant application, research statement |
| [`sv-experiment`](sv-experiment/SKILL.md) | `-freeze` `-runs` `-numbers` `-replication` | Frozen inputs, runs log, traceable numbers, replication artifact |
| [`sv-write`](sv-write/SKILL.md) | `-skeleton` `-intro` `-section` `-polish` `-translate` `-critique` `-humanize-paper` `-humanize-report` `-humanize-slides` `-humanize-letter` `-humanize-audit` `-style-mine` `-style-apply` | Everything about prose: plan, draft, polish, translate, critique, de-AI by scenario, venue style |
| [`sv-figure`](sv-figure/SKILL.md) | `-design` `-drawio` `-plot` `-tikz` `-html` `-poster` `-explain` | Every kind of figure, from design advice to draw.io reconstruction and code plots |
| [`sv-review`](sv-review/SKILL.md) | `-once` `-loop` | Read-only pre-submission audit; bounded multi-round check |
| [`sv-feedback`](sv-feedback/SKILL.md) | `-revise` `-guidance` `-rebuttal` | Tracked revisions from comments, expert guidance records, rebuttal plans |
| [`sv-slides`](sv-slides/SKILL.md) | `-weekly` `-talk` | Beamer decks for group meetings |
| [`research-core`](research-core/SKILL.md) | (not a command) | Core rules, field and venue profiles, checklists, AI-collaboration rules, templates |

## Typical chains

**Technique or benchmark paper.** `sv-idea-evaluate` → `sv-write-skeleton`
→ `sv-write-intro` → `sv-write-section` → `sv-figure-design` →
`sv-write-polish` → `sv-review-loop` → `sv-review-once`.

**Empirical study, any field.** `sv-supervisor-init` → `sv-experiment-freeze`
→ `sv-experiment-runs` → `sv-experiment-numbers` → `sv-write-section`
(empirical skeleton) → `sv-figure-plot` → `sv-review-loop` →
`sv-experiment-replication` → `sv-review-once`.

**Reading into research.** `sv-quickread-card` → `sv-study-paper` →
`sv-study-bridge` → `sv-idea-evaluate` or `sv-experiment-freeze`; many
cards → `sv-litreview-map`; a plan → `sv-proposal`.

**Review round.** `sv-feedback-revise` (response table) →
`sv-feedback-rebuttal` → `sv-write-humanize-letter` → `sv-review-loop`.

**Group meeting.** `sv-supervisor-brief` → `sv-slides-weekly` →
`sv-write-humanize-slides` → `sv-supervisor-records` (meeting log).

## Handbook cross-reference

| Handbook chapter | Groups |
|---|---|
| 1 Preliminary | `sv-review-once` |
| 2 Idea generation | `sv-idea`, `sv-litreview` |
| 3 Paper writing | `sv-write` (skeleton, intro, section, polish), `sv-review` |
| 4 Scientific plotting | `sv-figure` |
| 5 Vibe research | `research-core` (`core/ai-collaboration.md`) |
| 6 Case studies | `sv-write-skeleton`, `sv-experiment`, `sv-review` |

## Installing

See [`../INSTALL.md`](../INSTALL.md). With an agent-sync tree, use
`scripts/sync_agent_links.py`; otherwise `scripts/install.sh`.
