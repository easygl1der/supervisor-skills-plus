<div align="center">

<img src="assets/icon.png" alt="sv-skills" height="240" />

</div>

# sv-skills: Yihua Yue's academic research skill library

English · [中文](README.md)

Agent Skills for Claude Code, Cursor and Codex: twelve `sv-*` groups plus a shared `research-core` of rules, field and venue profiles, and sourced checklists. Each group has one auto-invocable entry and slash-only sub-commands such as `/sv-write-polish`.

Maintainer: [Yihua Yue](https://github.com/easygl1der) (`easygl1der`). Repository: [`easygl1der/supervisor-skills-plus`](https://github.com/easygl1der/supervisor-skills-plus).

This is an independently maintained skill pack. It is not the product page or official fork presentation of HKUSTDial/Supervisor-Skills (HKUST(GZ) DIAL / SuperY). Handbook chapters and some early procedures that skills still cite keep their required attribution in [THIRD_PARTY.md](THIRD_PARTY.md) and [`handbook/README.md`](handbook/README.md).

Install from a clone with [INSTALL.md](INSTALL.md). Usage: [skills/README.en.md](skills/README.en.md). Grouping: [docs/adr/0021-sv-skill-groups.md](docs/adr/0021-sv-skill-groups.md).

<p align="center">
  <a href="https://github.com/easygl1der/supervisor-skills-plus/stargazers"><img src="https://img.shields.io/github/stars/easygl1der/supervisor-skills-plus?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"></a>
</p>

## Layout

```
supervisor-skills-plus/
├── skills/              # installable Agent Skills (the product)
│   ├── sv-supervisor/ … sv-slides/
│   └── research-core/
├── handbook/            # Chinese curriculum cited by skills (see that folder's README)
├── handbook-en/         # English mirror
├── notes/               # evidence notes cited by research-core
├── docs/adr/            # decisions about this library
└── scripts/             # install and lint
```

## Skills

| Group | Covers | Link |
|---|---|---|
| **sv-supervisor** | Session brief and routing, project start-up, STATUS / TODO / ADRs / logs, lessons into research-core | [Open](skills/sv-supervisor/SKILL.md) |
| **sv-quickread** | Nine-section five-minute card of one paper; optional style card | [Open](skills/sv-quickread/SKILL.md) |
| **sv-study** | Understanding-first study of a concept, paper or chapter: restatement, diagnosis, correction; bridge back to the project | [Open](skills/sv-study/SKILL.md) |
| **sv-idea** | Full idea evaluation, or the fatal-flaws gate only | [Open](skills/sv-idea/SKILL.md) |
| **sv-litreview** | Survey-grade literature review with verified citations, or a map of papers already read | [Open](skills/sv-litreview/SKILL.md) |
| **sv-proposal** | Thesis proposals, grant applications (NSFC, NSF, ERC, NIH), research statements | [Open](skills/sv-proposal/SKILL.md) |
| **sv-experiment** | Frozen inputs, runs log, numbers traceable into the paper, replication artifact | [Open](skills/sv-experiment/SKILL.md) |
| **sv-write** | Skeleton, Introduction, sections, polish, Chinese-to-English, critique, de-AI by genre, venue style | [Open](skills/sv-write/SKILL.md) |
| **sv-figure** | Figure design, draw.io reconstruction, code plots, TikZ, HTML, posters, explainers | [Open](skills/sv-figure/SKILL.md) |
| **sv-review** | Read-only pre-submission audit, or a bounded multi-round check | [Open](skills/sv-review/SKILL.md) |
| **sv-feedback** | Tracked revisions from comments, expert guidance records, rebuttal plans | [Open](skills/sv-feedback/SKILL.md) |
| **sv-slides** | Beamer for group meetings: weekly report or paper talk | [Open](skills/sv-slides/SKILL.md) |
| **research-core** | Shared rules, field and venue profiles, checklists, AI-collaboration rules, templates (not a command) | [Open](skills/research-core/SKILL.md) |

## Quick start

```
git clone https://github.com/easygl1der/supervisor-skills-plus.git
```

Then follow [INSTALL.md](INSTALL.md) to link `skills/` into Claude Code / Cursor / Codex. You can also paste:

```
Help me install the skills from https://github.com/easygl1der/supervisor-skills-plus (see INSTALL.md).
```

## Handbook

`handbook/` and `handbook-en/` are source curriculum that skill checklists and field profiles still cite (CC BY-NC-SA 4.0). They are **not** this repository's public brand; see [`handbook/README.md`](handbook/README.md).

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Changes land on `main` through PRs; do not force-push.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Third-party code and handbook provenance: [THIRD_PARTY.md](THIRD_PARTY.md) and [LICENSE](LICENSE).
