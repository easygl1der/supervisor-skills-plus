# Handoff prompt: build `group-beamer` (group-meeting Beamer skill)

Paste everything below into Claude Code at the root of `~/Projects/supervisor-skills-plus`.

---

You are adding a new skill, `skills/group-beamer/`, to supervisor-skills-plus. Work directly on `main`, use normal `git push` (never force), and write everything in English (the slides themselves may be Chinese or English).

## Goal
Produce LaTeX Beamer decks for Yihua's research group meetings in math/statistics, mainly causal inference. Two first-class modes, equally important:
- `weekly-report`: progress report, 6 to 10 slides. `progress` is a longer variant (topic-level status) that lives under it.
- `paper-talk`: critical paper presentation, 12 to 18 slides.

Explore the references below yourself, then propose the design. **Stop after the proposal (Step 2) and wait for Yihua's "continue" before writing files into the repo.**

## Fixed decisions (do not relitigate)
1. **Template**: Moloch (`jolars/moloch`, CC-BY-SA-4.0) is the default theme; SimplePlus (Unlicense) as a minimal alternative; `yxnchen/sysu-beamer-template` (CC0) optional for formal SYSU-branded talks. Vendor into `templates/{moloch-cjk,simpleplus-cjk,sysu}/` with source and license noted. CJK via `ctex`, compile with `latexmk -xelatex`. Mac already has TeX Live 2026, moloch, SimplePlus, ctex, `pdftoppm`.
2. **Audience parameter**: `audience: advisor` (default) or `peer`. Advisor: lead with conclusions, blockers, and decisions needed from the advisor; push technical detail to an appendix. Peer: derivations and experiment details in the main body.
3. **Critical paper-talk**: besides explaining the method, include slides for estimand and identifying assumptions (where they are strong), link to our project, and reproducibility (rerun or simulate under assumption violation). Optionally pull the attack checklist used by the Critic workflow.
4. **Accumulation**: every meeting's `.tex`, rendered PDF, and speaker notes are stored via `research-records` (e.g. `docs/log/<date>-group-meeting.md` plus deck files). The next weekly report automatically loads last week's "next steps" and marks each done / partial / dropped.
5. **Inputs**: weekly report draws on `research-records`, Linear, and git history. Paper talk takes the `paper-quickread` card or MinerU markdown; never extract PDFs with pypdf or other ad hoc scripts.
6. **Math and figures**: native LaTeX math; causal DAGs in TikZ (Graphviz PDF only for large/changing graphs); reuse `figure-designer` outputs.
7. **Speaker notes**: in `\note{}` and also exported as markdown, written from the final rendered pages.
8. Not Marp, not PPTX. Human gate on outline before drafting. No invented numbers; missing data becomes `TODO`.

## References to read (clones may exist under `/tmp/` on Yihua's machine; otherwise clone shallow)
Layout and pipeline:
- `Noi1r/beamer-skill` (MIT): bullet length limits, every slide carries a formula/figure/table/theorem, text-only slides at most ~30%, no `\pause`, outline gate, backup slides, visual check of boxes.
- `Master-cai/Arxiv2beamer` (no license; ideas only, do not copy text): rebuild the paper's section outline first and map sections to slide groups; visual audit against original figures in small batches.
- `moyoo0/paper-to-latex-ppt` (MIT): Chinese group-meeting decks, speaker notes per page (main point, every symbol, figure axes/legend/takeaway, transition), `pdftoppm` self-check.
- `pedrohcgs/claude-code-my-workflow` (MIT): separate visual / pedagogy / proofreading review passes; fix overflow by spacing before font size; `credible-claims` (claims may only be narrowed, never strengthened).
- `takashiishida/paper2slides` (MIT): generate, lint, compile, refine loop.
- Our own `paper-quickread`: its 9-section card, claim-evidence table, and proved/empirical/conjectured tags feed the critique and link-to-project slides.

Statistics and causal talk writing:
- Ramdas Stat-ML talk checklist: https://www.stat.cmu.edu/~aramdas/checklists/aadi-talk-checklist.pdf (one idea per slide, assertion titles, fewer slides than minutes, simple sufficient conditions over most general theorem).
- Method Atlas paper card: https://methodatlas.vercel.app/guides/reading-papers (Question / Estimand / Identification / Key assumption / Main result / Robustness / Biggest threat / External validity). Use as the identification-slide template; an unstated estimand is itself a warning.
- Estimand to identification to estimation (Cornell causal course; Petersen and van der Laan causal roadmap): when the paper is vague, pick one reading, define it with potential outcomes, label it as the presenter's interpretation; the causal-to-statistical gap can only be bounded by sensitivity analysis.
- `rphilipzhang/Reading-Group-2026`: reading-group format with a replication segment.
- Hernán, "The C-Word" (AJPH 2018): say causal when that is the goal; results slides report numbers, the causal reading goes on the discussion slide.
- Notation defaults to Ding, *A First Course in Causal Inference*. Hanzhong Liu's group-meeting preferences: leave a clearly marked slot; Yihua will fill it or it will be mined later with `style-mine` from past `.tex` files.

Humanizer:
- `blader/humanizer` (MIT) and our `deai-writing` (which already includes avoid-ai-writing). Add a `slides` context profile to `deai-writing` rather than a parallel skill: terse bullets are expected, but keep one hedge per claim, no repeating a selling point across title, bullets, and summary, no "not X but Y", no punchy closers, no marketing adjectives. Title verb strength must not exceed the claim level (proved / numerical evidence / causal under stated assumptions / exploratory).
- Slide rules to adopt: assertion titles with evidence bodies; at most 6 bullets of at most 2 lines; numbers copied from source with table/page reference; speaker notes conversational and keep the presenter's own judgment; end slides with a discussion question rather than a slogan.

## Steps
0. Read `PROGRESS.md`, existing skills `research-records`, `paper-quickread`, `deai-writing`, `figure-designer`, `style-mine`, and `research-core` field profiles (causal, stats). Log progress in `PROGRESS.md`.
1. Read the references above; write `docs/handoff/group-beamer-notes.md` with what you borrow from each and license implications.
2. **Propose** the skill layout (SKILL.md triggers, `references/` modules for weekly-report, paper-talk, quality gates, audience; `templates/`; `scripts/` such as compile, render pages, overflow/quality check), the compile-check loop (at most 3 to 5 rounds), and integration points. **STOP and wait for Yihua.**
3. After approval: implement, vendor templates with attribution, add the `slides` profile to `deai-writing`, add an ADR, update README skill lists.
4. Verify: build a sample `weekly-report` (Chinese, advisor) and a sample `paper-talk` on a real causal paper already in the repo's notes, both compiling cleanly with no overfull boxes; render pages and inspect. Run `scripts/lint_skills.py` and `scripts/check_shared_sync.py`.
5. Commit in logical pieces, push to `origin main` (no force), and report what was built, the sample PDFs' paths, and open questions.
