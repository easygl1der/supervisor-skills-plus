# Third-party material

This repository is licensed CC BY-NC-SA 4.0 (`LICENSE`). The material below
comes from other projects under their own licences, which still apply to it.
Licences were read from each project's LICENSE file on the date given.

| Material | Where in this repo | Source (commit) | Licence | Copyright | Checked |
|---|---|---|---|---|---|
| Quick-read section skeleton, per-section length table, "assess before writing", append-only index rule, three-level Q&A, four reflection questions (ideas, rewritten) | `skills/paper-quickread/`, `skills/study/references/paper-mode.md` | github.com/alaliqing/claude-paper | MIT | (c) 2026 alaliqing | 2026-10-16 |
| Candidate rules for causal inference and statistics (rewritten) | `skills/research-core/references/fields/causal.md`, `stats.md` | github.com/brycewang-stanford/Awesome-Journal-Skills @ 932eb23 | MIT | (c) 2026 Bryce Wang | 2026-10-16 |
| Paper register tokens, figure/node/edge/callout styling, stepper `data-s` idea, delivery checklist, known traps (adapted) | `skills/study/kit/vendor/ve/`, `skills/study/references/visuals.md` | github.com/nicobailon/visual-explainer @ 69cd739 (v0.12.0) | MIT (`kit/vendor/ve/LICENSE`) | (c) 2025 Nico Bailon | 2026-10-16 |
| KaTeX 0.16 (JS, CSS, fonts), unmodified | `skills/study/kit/vendor/katex.min.*`, `auto-render.min.js`, `fonts/` | github.com/KaTeX/KaTeX | MIT | (c) 2013-2020 Khan Academy and other contributors | 2026-10-16 |
| rough.js, unmodified | `skills/study/kit/vendor/rough.js` | github.com/rough-stuff/rough | MIT | (c) 2019 Preet Shihn | 2026-10-16 |
| dagre, unmodified | `skills/study/kit/vendor/dagre.min.js` | github.com/dagrejs/dagre | MIT | (c) 2012-2014 Chris Pettitt | 2026-10-16 |
| elkjs, unmodified bundle | `skills/study/kit/vendor/elk.bundled.js` | github.com/kieler/elkjs | **EPL-2.0** (secondary GPL-3.0); notice kept in the file header; source at the URL to the left | Eclipse ELK contributors (see file header) | 2026-10-16 |
| Pattern catalog and editing contract (adapted) | `skills/deai-writing/` (`LICENSE-avoid-ai-writing.txt`) | avoid-ai-writing | MIT | (c) Conor Bronsdon | 2026-10-13 |
| drawio-reconstruction skill | `skills/drawio-reconstruction/` (`LICENSE`) | sxy1499894281/drawio-reconstruction-skill via upstream | MIT | see the skill's LICENSE | upstream |
| style-mine (formerly journal-adapt), the owner's own skill | `skills/style-mine/` (`README.md`) | owner | MIT | the owner | 2026-10-16 |

Not bundled on purpose:

- **dagitty** (GPL-2.0): adjustment sets and backdoor paths in the browser.
  It may be loaded from its own site by the user; it is never copied into
  this repo.
- **visual-explainer** as a whole: recommended as a separate install for
  diff and plan reviews; `study` does not depend on it.
- Code from claude-paper (PDF parsing, web reader, demos): not used; PDF
  input goes through MinerU only.

The upstream Supervisor-Skills project (HKUSTDial) is CC BY-NC-SA 4.0; see
`LICENSE` and `README.md`.
