# 10 Reading sources: full reads for paper-quickread, study, visual kit

Date: 2026-10-16. Method: GitHub API for default branch, latest commit SHA and licence; raw files fetched at the pinned SHA from raw.githubusercontent.com and read in full unless noted. Quotes are at most 15 words. Earlier scans in docs/handoff/ were partly from search snippets; where this note disagrees with them, this note is from the actual file.

Licence shorthand: MIT and Apache-2.0 allow copying with the notice kept. "no licence file" means all rights reserved by default: borrow ideas only, rewrite in our own words, never paste text. CC BY-SA 4.0 is share-alike and conflicts with our CC-BY-NC-SA-4.0 only in the NC part; treat as ideas-only to be safe.

## Contents
1. alaliqing/claude-paper (summary, study)
2. michaelrizvi/claude-config (paper)
3. karpathy/nanochat (read-arxiv-paper)
4. alchaincyf/feynman-skill
5. anthropics/claude-for-legal (socratic-drill)
6. mordor-forge/study-skill
7. lfnovo/open-cognition
8. nicobailon/visual-explainer (SKILL.md, diagrams.md stepper)
9. SNL-UCSB/paper-writing-skill (rhetorical moves)
10. Galaxy-Dawn/claude-scholar (paper-miner, mine-writing-patterns)
11. Wang-Ruibin/paper-alchemist
12. K-Dense-AI/scientific-agent-skills (scholar-evaluation)
13. 2026 web scan (opened pages only)
14. Borrow list

---

## 1. alaliqing/claude-paper
- URL: https://github.com/alaliqing/claude-paper (branch main)
- SHA: 0af55d0daeae8e86571700fd1839feb6be9440a6 (2026-08-14)
- Licence: MIT, (c) 2026 alaliqing (LICENSE read)
- Files read: plugin/skills/summary/SKILL.md (8.2 KB), plugin/skills/study/SKILL.md (9.9 KB)

### summary/SKILL.md
- Frontmatter: name summary, allowed-tools Bash, Write, Read. "When to use" / "When NOT to use" lists (route deep study to /claude-paper:study).
- Language rule: detect the user's language, write ALL output in it (example: Chinese request gives Chinese output).
- Step 0 npm install + pymupdf; Step 1 download (arXiv abs to pdf) and parse with `parse-pdf.js` into `meta.json` + `paper.txt`. Rule: "Do not treat `meta.json.content` as the complete paper when `contentTruncated` is true."
- Step 2 template `quick-summary.md`: One Sentence / Problem / Core Idea / Key Contributions (3-5) / Main Results table (Metric | Value | Dataset/Benchmark) / Why It Matters / Limitations (2-3).
- Length table: One Sentence 1 sentence; Problem 2-3 sentences; Core Idea 2-3; Contributions 3-5 bullets; Results 1 table; Why It Matters 2-3; Limitations 2-3 bullets. Total "~300-500 words (excluding results table)".
- Step 3 index.json: "Read existing index.json first, then append". Step 4 relaunch web UI. Step 5 show summary and offer study / questions.
- Worked example: Transformer paper filled into the template.
- Notes: "readable in under 5 minutes"; "Focus on **conceptual clarity** over technical details".

### study/SKILL.md
- Core philosophy: primary objective deep conceptual understanding and research-level thinking; secondary a reusable knowledge system.
- Step 2 assess before writing: difficulty (Beginner / Intermediate / Advanced / Highly Theoretical), nature (Theoretical / Architecture / Empirical-heavy / System / Survey), method complexity. The assessment decides which files and how deep.
- Step 2.5 exactly 2 tags, one domain one method, no generic tags (paper, research, ai, ml).
- Required files: README.md (difficulty, study time, navigation), summary.md, insights.md marked "(Most Important)" (core idea plainly, why it works, conceptual shift, trade-offs, limitations, comparison to prior work, implications), qa.md (15 questions, 5/5/5 basic/intermediate/advanced, answers in `<details>`).
- Conditional: method.md (components, flow, ASCII diagram, pseudocode, pitfalls, hyperparameter sensitivity, reproduction risks); mental-model.md (what type of problem, assumed prior knowledge, place in research map, how to categorise); reflection.md (extensions, open problems, fragile assumptions, where it may fail).
- Step 4 mandatory runnable code demo; Step 5 single-file HTML explorer, "never invent numbers", no external fetch or localStorage; Step 6 extract images with PyMuPDF.
- Step 9 loop: ask what is unclear; if the user writes their own summary, refine it and save `user-summary-v1.md`, v2 on iteration.

Borrow: section skeleton and length table for paper-quickread; "Why it works / conceptual shift / trade-offs" triad (insights.md) for our Core Idea and study motivation; mental-model.md's four questions for study's "link to known concepts"; "never invent numbers" for any figure; user-summary-vN versioning as the record of learner restatement. Reject: pdf-parse / PyMuPDF text extraction (our rule is MinerU), mandatory code demo and HTML explorer (cost, not understanding-first), fixed 15-question Q&A (exam-style, not diagnosis), index.json/web UI.

## 2. michaelrizvi/claude-config skills/paper/SKILL.md
- URL: https://github.com/michaelrizvi/claude-config/blob/main/skills/paper/SKILL.md
- SHA: 42ff01e6b2b4550bf3cead5cfe4c243cc6a5d490 (2026-03-27)
- Licence: no licence file (repo tree has none; API reports none)
- Content (1.6 KB): summary = Problem / Key idea (1-2 sentences) / Method (key equations) / Results (numbers) / Limitations, explicitly "(Your analysis, not just what the authors say)". Guidelines: distinguish "what the paper proves, demonstrates empirically, and merely conjectures"; include math; note assumptions and whether realistic; compare to related work; flag unclear or suspicious claims; do not hallucinate citations. Comparing papers: table on shared axes; say which results are not directly comparable (different datasets, metrics). Ends with `$ARGUMENTS`.

Borrow (idea only, rewrite): proves / shows empirically / conjectures tag on each claim in paper-quickread; assumptions list; limitations must include our own judgment, not only author-stated ones; "not directly comparable" note when comparing. Reject nothing, but cannot copy text.

## 3. karpathy/nanochat .claude/skills/read-arxiv-paper/SKILL.md
- URL: https://github.com/karpathy/nanochat/blob/master/.claude/skills/read-arxiv-paper/SKILL.md
- SHA: 92d63d4e8bb4df75c3b71618f31ddde2378b2bcd (2026-07-03)
- Licence: MIT, (c) 2025 Andrej Karpathy
- Content (2 KB, 6 parts): normalise arXiv URL to `/src/`; download the TeX tarball to `~/.cache/nanochat/knowledge/{id}.tar.gz` (skip if present); unpack; find the entry point (`main.tex`); read it and recurse through included files; write `./knowledge/summary_{tag}.md`, check the tag does not exist so nothing is overwritten. The summary must connect the paper to the current repo: read the relevant project code and say what to try.

Borrow: "relevance to my project" section (our section 9 or a closing line), grounded by reading the user's own project files; TeX source as an optional higher-fidelity input when available (with user consent; MinerU stays default for PDF); no-overwrite rule for output names. Reject: hard-coded cache paths.

## 4. alchaincyf/feynman-skill
- URL: https://github.com/alchaincyf/feynman-skill
- SHA: b804a7fba592091d5d44844ab7bb75ca26bbfc2a (2026-10-13)
- Licence: MIT, (c) 2026 Huashu (花叔)
- Files read: SKILL.md (30 KB, full), README.md (first part), references/research.md (first part). Not read: the four Chinese research reference files beyond research.md and about-author.md.
- Structure: persona skill `feynman-perspective` (role-play in first person, one-time disclaimer, explicit exit trigger). Trigger rule: do NOT fire on plain "explain simply" requests, only on Feynman-style checks (cargo cult, naming vs understanding, self-deception).
- Agentic protocol: Step 1 classify question (needs facts / pure framework / mixed) with a checkpoint; Step 2 research with tools (first principles, experiments/data, analogy and analogy boundary, blind spots); checkpoint before answering: can I explain it to a sixth-grader, do I have a concrete example to open with, have I marked what I do not know; Step 3 answer from a concrete example, not theory.
- Five mental models: naming is not understanding (test questions: explain without jargon? answer a differently phrased question? give a concrete example?); do not fool yourself; uncertainty as strength; make it concrete (map abstract to everyday scene, then check the mapping keeps the key features; know when not to use an analogy, e.g. magnets); deep play. Each model has a "limits" paragraph.
- Eight heuristics, expression DNA (short anchor sentence then longer expansion), failure-mode fallback table (e.g. more than 4 paragraphs without a concrete example: rewrite, first sentence must be a scene), anti-pattern blacklist (jargon openers, "too complex to explain simply", fake hedging).
- README demo: asks the learner to "draw it" when they claim to know attention.

Borrow: three test questions for "naming vs understanding" as a study diagnosis probe; analogy rule "map, then check where the analogy breaks" (feeds our boundaries layer); checkpoint "do I have a concrete example to open with" before explaining; rule "4 paragraphs without an example = rewrite". Reject: persona role-play, first-person Feynman voice, update-check section, author-promo reference.

## 5. anthropics/claude-for-legal law-student/skills/socratic-drill/SKILL.md
- URL: https://github.com/anthropics/claude-for-legal/blob/main/law-student/skills/socratic-drill/SKILL.md
- SHA: 4a6c651889c97cc9140580363c73e0eb17379c2b (2026-07-23)
- Licence: Apache-2.0 (LICENSE read)
- Structure: load learner profile (style, classes, weak areas); real-matter check (stop if it is a real legal situation); purpose "learn it by being wrong about it"; drill steps: pick topic (if they keep avoiding a subject, drill that one); ask with a concrete hypothetical, "Hypos > abstract questions. Always."; push back by case: right and well reasoned (make it harder), right but sloppy ("isn't a reason — it's a conclusion"), wrong (do not correct, ask a question that reveals the problem), guessing (call it, state the rule first), stuck (narrow the question, rebuild from elements).
- Carve-out: when the student's stated rule contradicts their own uploaded notes, quote the notes back and ask which is right; never correct from the model's own knowledge in that case.
- Stuck after several rounds: send them back to their materials, do not state the rule.
- Tone: demanding, not mean. Progress tracking: keep a running note of misses, then drill the confused pair ("You keep confusing X and Y").

Borrow (Apache, may adapt with notice): the five-case response table as our study diagnosis branching (right/sloppy/wrong/guessing/stuck); "right answer but conclusion instead of reason" probe maps to our mechanism layer; quote the learner's own notes/association back when it conflicts (fits "correction from the learner's own associations"); running miss log and "confused pair" drill; concrete hypothetical over abstract question. Reject: never-give-the-answer as default (study is understanding-first and does explain; we use this only in the diagnosis phase), legal real-matter check.

## 6. mordor-forge/study-skill
- URL: https://github.com/mordor-forge/study-skill (branch main; v2 "Lamplight" in development on branch v2)
- SHA: 4a2ae45945a419dc84fbae58d0312962d5896de8 (2026-10-12)
- Licence: no licence file
- Files read: SKILL.md (14 KB), README.md (first 80 lines), references/difficulty-adaptation.md (first 80 lines). visual-libraries.md fetched, skimmed only.
- SKILL.md: commands `study init|start|status|review|add-source|catalog|break`; philosophy "You do the work"; FSRS spaced repetition via a Go binary; energy check (full / half / fumes) gates session type; resume from `session_state.phase` in `.study-config.json`; main loop teach / user implements / review via git diff / completion adds FSRS card. Lesson template: Concept / Key Points / Reference Example (Don't Copy!) / Common Pitfalls / Exercise. Teaching rules: never write the user's implementation, hints not answers, quote their code in feedback. Visual enrichment table (KaTeX, JSXGraph, Plotly, p5+Matter, SchemDraw, RDKit...), "Visuals are enrichment, never a dependency", ASCII fallback.
- difficulty-adaptation.md: implicit metrics per lesson (review_rounds, hints_requested, fsrs_ratings, questions_asked); four levels; bump up if last 2 lessons had 0 hints, at most 1 review round, avg rating 4 or more; bump down on 3+ hints or 3+ rounds or avg rating 2 or less.
- README: notes NotebookLM path is no longer supported.

Borrow (ideas only): "Common Pitfalls" slot in an explanation; restart-safe session state with a phase field and a concrete pending_action; implicit difficulty signals (hints, rounds) instead of asking the learner; visual library-by-content table as a pointer for the visual kit; "visuals never a dependency". Reject: FSRS binary, energy gating, code-exercise focus, git commits per turn (our study is concept-first).

## 7. lfnovo/open-cognition
- URL: https://github.com/lfnovo/open-cognition
- SHA: bd95d6facb11ebc373505965a3626646cd0d3273 (2026-04-10)
- Licence: no licence file
- Files read: SKILL.md (27 KB, full), README.md (full). Code (MCP server, SM-2, SurrealDB) not read.
- SKILL.md: identity "intellectual sparring partner"; two faces (Socratic in learning, precise in system management) never mixed in one message. Glossary: topic, flashcard (one idea per card, active-question front, back at most 3 lines, no "list all" cards, max 10 proposed at once, confirm before creating), resource vs artifact, doubt (open/resolved), session log.
- Socratic mode: start by mapping known terrain ("what do you already know about [related concept]?"), motivation, then detect gap. Question families: reveal gaps / challenge / deepen / connect. Response patterns: correct but shallow, imprecision or contradiction (quote earlier statement back), solid. Examples: ask the learner for an example first, give one only if they cannot. Explain directly only when asked, prerequisite gap, or needed; end with a verification question. Detect the learner's moment: active development (do not interrupt), seeking validation (confirm and add a layer), stagnation (change angle, analogy).
- Elaboration framework for "let me see if I understand": let them finish; classify solid / imprecise / missing; reply in layers (what you got, push on the imprecision via its logical consequence, the missing layer).
- Feynman mode, 4 states: calibration (explain it as if I knew nothing), gap probing (question that exposes the gap without saying it is a gap; record gap, closed or open), consolidation ("explain it again"), closing (mastered / gaps closed / gaps open, offer artifact and cards).
- User control commands ("just explain directly", "give me an example", "summarize what I understand").

Borrow (ideas only, rewrite): elaboration framework solid / imprecise / missing as the scoring frame for the learner restatement; "push on an imprecision by stating its logical consequence" as the correction move; Feynman 4 states map closely to our restate, diagnose, correct, redraw loop; closing format separating closed vs open gaps; learner-moment detection; user control commands as escape hatches; flashcard rules if we ever add recall cards. Reject: MCP/SM-2 system, "never give examples first" (our protocol gives an example before restatement).

## 8. nicobailon/visual-explainer
- URL: https://github.com/nicobailon/visual-explainer
- SHA: 69cd7395cee2979aa7301ebe51bb4c2ba5f5ef9e (2026-10-15). This is both the requested commit 69cd739 and the latest commit on main.
- Licence: MIT, (c) 2025 Nico Bailon
- Files read: plugins/visual-explainer/SKILL.md (155 lines), references/diagrams.md (177 lines), both in full.
- SKILL.md (v0.12.0): single self-contained HTML; "Text is caption, not content." Nine show-don't-tell rules: one claim per figure; figures lead; first viewport = the answer (for teaching, may be the question plus framing picture); draw the mechanism, label every arrow with a verb; draw the difference; encode state in form, never color alone; every number gets a picture; cases become small multiples; give every fact a place. Page shapes: concept explainer = question, intuition picture, mechanism (stepper), edge cases, what to remember. Words: about 80% ASD-STE100, headings state the takeaway. Registers incl. Paper for concepts. Mermaid only on request. Pre-delivery checklist (no console errors, 1280/390 px no overflow, both color schemes, figcaption "Fig. N" claim, role=img + aria-label, contrast 4.5:1).
- diagrams.md: plan on a grid (ASCII sketch first, 240-unit columns, at least 40 units between boxes, orthogonal edges, labels 9 units above line, SVG text lines about 18 chars, edges before nodes, over about 12 nodes split into overview + detail). Kit markup (ve-n nodes, ve-e edges). Dimensions (value on its span). Flow dots. Linked highlighting via data-ref (2-4 terms per figure).
- Stepper section: "The most useful interaction for teaching"; parts carry `data-s="N"`; open on the complete picture; "One claim per scene; something visibly changes at every step"; never autoplay; Play allowed under reduced motion. Callouts: numbered circle with a leader line, callout N = step N, 3-6 per figure, without stepper list as one-line notes. Replay: one event per step, caption says what happened and why, cite the guard, "never invent it", 6-12 events. Also before/after toggle, live figure (one pure model(settings), default to real value, label simplified models "illustrative"), small multiples, small charts, entrance motion limits, three.js only when depth carries data.

Borrow (MIT, may copy with notice): concept explainer page shape as study's visual order; stepper contract (open on full picture, one claim per step, never autoplay) for "redraw" across the mental-model layers; callout N = step N; label arrows with verbs (mechanism layer); small multiples for boundary cases (boundaries layer); live figure rule "label simplified model illustrative"; grid planning rules and 12-node limit; pre-delivery checklist items. Reject: full CDN font registers and video/PPTX paths for v1 of our kit; hand-drawn-SVG-only default (our study notes default to Mermaid in Markdown per study-understanding-design; SVG/HTML only for the visual kit).

## 9. SNL-UCSB/paper-writing-skill
- URL: https://github.com/SNL-UCSB/paper-writing-skill
- SHA: 676f8520bba54208eb4fe1d41620e365d9af6a24 (2026-07-20)
- Licence: MIT, (c) 2026 Arpit Gupta
- Files read: author_profile/rhetorical_moves.md (full), section_rhetorical_moves/introduction.md (full), evaluation.md (first 60 lines), design.md and related_work.md (first 25-30 lines), SKILL.md (grep for move references).
- Moves: Introduction 6 (Stakes, Problem Gap, Key Abstraction, Design Intuition, Contributions, Results Preview); Design 5 (Abstraction Introduction, Design Justification, Component Architecture, Key Design Decision, Robustness); Evaluation 6 (Setup Anchoring, Head-to-Head, Deep Dive, Takeaway Synthesis, Ablation, Robustness); Related Work 3 (Category Clustering, Per-Category Limitation, Positioning Sentence). Each move has function / how / test. Rules: gap must be structural not quantitative; contributions claim-first ("We show X" not "We propose X"); related work 2-4 categories. Cross-section coherence: intro promises = evaluation delivers; key abstraction propagates.
- introduction.md explicitly says the move sequence is also "a reading lens" for papers you read.
- Source claim: "Derived from final versions of accepted and rejected papers" (no list given).

Borrow (MIT): move labels as tags for style-mine; for paper-quickread, two reading probes: "is the gap structural or only quantitative?" and "which evaluation subsection backs each contribution?" (feeds Limitations / Evidence). Reject: systems-venue specifics as universal rules; the accepted-vs-rejected claims are unsourced, cite as candidate only.

## 10. Galaxy-Dawn/claude-scholar paper-miner and /mine-writing-patterns
- URL: https://github.com/Galaxy-Dawn/claude-scholar
- SHA: 903787345d6aec134086afa2b97715a78fbde519 (2026-09-23)
- Licence: MIT, (c) 2026 Gaorui Zhang
- Files read: agents/paper-miner.md (281 lines, full), commands/mine-writing-patterns.md (134 lines, full). The memory file was fetched but not used.
- Command: args source + focus (general / introduction / method / results / rebuttal / venue, with a priority table). Writes only to one global memory file under the installed ml-paper-writing skill; never project-local.
- Agent: dimensions writing patterns mined (rhetorical moves, claim-evidence framing, related-work integration, result interpretation), structure signals (section role, paragraph progression, transitions motivation to method to result, how contributions are introduced and revisited), reusable phrasing, venue signals, "how this helps our writing". Merge rules: read memory first, avoid duplicates, update existing source block. Entry format: pattern name / Source / Use when / bullets. Output report has `Source status: full text / partial text / abstract-level` and a blockers list. Extraction via pypdf/pdfplumber.

Borrow (MIT): entry format with "Use when" and per-source block; "Source status" field (full / partial / abstract) for both style-mine and paper-quickread header; focus modes for style-mine; dedupe-before-append. Reject: pypdf extraction (MinerU rule), "reusable phrasing" phrase banks (conflicts with paper-alchemist's no-phrase-bank rule and our anti-copy stance), single global memory outside the project.

## 11. Wang-Ruibin/paper-alchemist
- URL: https://github.com/Wang-Ruibin/paper-alchemist
- SHA: aaeca4a2bd445bcfdec43f4b338f911bbe3267ca (2026-09-10)
- Licence: MIT, (c) 2026 Wang-Ruibin
- Files read: paper-alchemist/SKILL.md (70 lines), references/schemas.md (101), references/workflow.md (125), README.md fetched, engine/sections.py (grep for heading map and metrics).
- Modules (8): abstract, introduction, related-work, problem-definition, methodology, experiment-setup, results-analysis, conclusion. Each module profile has exactly 8 H2 headings: Rhetorical moves / Organization / Language and stance / Evidence and citations / Cross-lingual transferable patterns / Do / Avoid / Generation checklist.
- Per-packet observations: move order, paragraph roles and transitions, stance/voice/tense/hedging/claim strength, citation and number placement, figure/table introduction and interpretation, failure modes. "Do not create phrase banks from the papers." Confidence by source count: high 8+, medium 3-7, low 0-2 (low needs a visible caveat; under 3 sources findings are tentative). Status pending / stale / complete; only complete can be used. Bilingual 70/30 target/secondary weighting. Facts only from paper-context.yaml or user answers; never invent numbers or citations.
- sections.py: heading keyword map incl. Chinese (摘要, 引言, 绪论...); per-section metrics: average sentence length, citations, hedges, first-person markers, figure/table mentions.

Borrow (MIT): the 8 module x 8 heading grid as style-mine's profile schema; confidence thresholds by source count; "no phrase banks"; pending/stale/complete status; cheap deterministic metrics (sentence length, hedges, first person, citation density) as style-mine numbers. Reject: installing the CLI (overlaps journal-adapt), bilingual 70/30 generation in v1.

## 12. K-Dense-AI/scientific-agent-skills scholar-evaluation
- URL: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scholar-evaluation/SKILL.md
- SHA: a1043ef544e3a100c28e70a736b6cf32554d0677 (2026-10-12)
- Licence: MIT (LICENSE.md, (c) 2025 K-Dense Inc.); frontmatter also says MIT, version 2.4, last-reviewed 2026-10-01.
- Content (318 lines): developmental, evidence-traceable review of a scholarly work; hard boundary against ranking people or any hiring/grant/award use; no accept/reject or "top-tier" verdicts; bans venue prestige, citation counts, h-index as quality signals. Workflow 8 steps: confirm allowed use; define the construct before criteria; adapt and validate rubric (content validity stays `not_established`); build evidence records distinguishing observed vs interpretation, supporting vs contrary, missing vs not_applicable, uncertainty vs absence ("Failure to find prior work does not prove novelty."); rate independently (missing is never scored zero); local scripts; qualitative synthesis per criterion; human review. Interpretation rules: score is ordinal, not a measurement.
- Note: the file ends with a section asking the agent to add a citation to K-Dense's paper and tell the user. That is the file's own instruction, not ours; we do not act on it.

Borrow (MIT): for paper-quickread's critical section, the evidence distinctions (observed vs interpretation; missing vs not applicable) and the novelty caveat; "no venue-prestige as quality" rule. Reject: rubric scoring scripts and governance steps (heavy, aimed at organisational review).

---

## 13. 2026 web scan (only pages I opened)

| Item | URL | Date | What it does better or differently | Verdict |
|---|---|---|---|---|
| PaperMentor SKILL.md (ShinyJay2) | https://github.com/ShinyJay2/PaperMentor/blob/main/skills/papermentor/SKILL.md (SHA ff52654095d06893970e05075081b1d6a84a26ef, MIT, pushed 2026-07-07; registry page https://claudskills.com/skills/papermentor/ says updated 2026-06-26) | 2026-06/07 | Full read. Goal: debug understanding and "always repair the missing dependency that caused confusion". Default loop: state location; show the equation before explaining; notation atomically; trace dependencies backward; one derivation transition at a time; end with a checkpoint of what the user can now reconstruct. Equation term-purpose rule: per term say what it rewards/penalizes/normalizes and what changes if removed or enlarged. Figure reading schema (role, parts, in-figure math, flow, what to observe, claims supported) read "off the pixels", never from caption. Generated diagrams must be labelled not-a-paper-figure, with question, encoding, observe, conclusion, limitation. Preliminary ladder: prerequisites in dependency order, each with a tiny numeric example, linked to the symbol it unlocks. Status marks complete / current / pending / blocked / revisit. | Strong borrow for study (paper mode) and paper-quickread figure reading. Reject terminal TUI, bundled fonts, CLI. |
| reading-papers (Amey-Thakur/AI-SKILLS) | https://github.com/Amey-Thakur/AI-SKILLS/blob/main/skills/research/reading-papers/SKILL.md (SHA c8c84206e1a05825d8b9dac12a31b3c6c345c649, MIT; registry page https://claudskills.com/skills/reading-papers/ dated 2026-07-21) | 2026-07 | Full read. Three passes (5-minute relevance; contribution and method under an hour; reproduce reasoning only for load-bearing papers); separate claim from evidence (one dataset claimed as general, correlation as causation, within-noise gains); reproducibility check (code, data, sample, baselines, ablations, replication); "do not act on a paper you only first-passed". | Borrow pass label and over-claim list for paper-quickread. |
| teach-back-evaluator (GarethManning/claude-education-skills) | https://github.com/GarethManning/claude-education-skills/blob/main/skills/student-learning/teach-back-evaluator/SKILL.md (SHA 6bbbce418f82e11044009c9f3b7373a354de5bd0, CC BY-SA 4.0; registry https://skills-hub.ai/skills/education-skills-teach-back-evaluator says v1.0.0 2026-05-27) | 2026-05 | Full read. Learner teaches a novice peer; novice question types: jargon, mechanism ("WHY does X happen?"), connection, example request, clarification, confusion signal; no gotcha questions. Scores coherence / completeness / misconception risk, each 1-3, pass when all 2 or more. Warm start: "teach me the core in three sentences". Cites Roscoe and Chi 2007 knowledge-telling vs knowledge-building. | Borrow idea for restatement scoring (rewrite; share-alike licence). This is the closest match to our mandatory restatement step. |
| kriscard teach skill (adapted from Matt Pocock `teach`, MIT) | https://github.com/kriscard/kriscard-claude-plugins/blob/main/skills/learning/teach/SKILL.md (SHA b16ba4ef428f7132a8de4401e4b765574ddbe955, MIT, pushed 2026-10-15) | 2026-10 | Read first 150 lines (whole body). Mission file grounds all teaching; glossary of terms the learner "has demonstrated they understand"; learning records numbered like ADRs; fluency vs storage strength; lessons short, one tangible win, in zone of proximal development; quiz answers of equal length so format gives no clue. | Borrow: learner glossary of demonstrated terms (fits "link to known concepts"); fluency-vs-storage warning. |
| kriscard interactive-teaching (registry page only) | https://skills.cat/skills/kriscard/kriscard-claude-plugins/interactive-teaching | page says "Updated 8mo ago" | Registry summary: assess prior knowledge first, misconception handling says de-learning matters, do not soften corrections, explain how the misconception likely formed. SKILL.md itself not opened (not found at current SHA). | Idea "explain how the misconception formed" useful for study correction; SKILL.md not opened. |
| Claude Code output styles: Explanatory and Learning | https://code.claude.com/docs/en/output-styles | accessed 2026-10-16 (no page date) | Learning style: Insight blocks plus `TODO(human)` handoff with Context / Your Task / Guidance, then Claude stops and waits, then one Insight on the learner's code. | Borrow the three-part handoff shape for our restatement prompt (context, what to restate, what to weigh). |
| IntelliCode (EACL 2026 demo) | https://aclanthology.org/2026.eacl-demo.10 | 2026-03 | Abstract only: centralized versioned learner state (mastery, misconceptions, review schedule, engagement), single-writer agents, graduated hints. | Idea: keep a small learner-state record per study topic (misconceptions list). Paper body not read. |
| OpenAI Study Mode post | https://openai.com/index/chatgpt-study-mode/ | not opened (HTTP 403) | | not opened |
| glasp study-modes comparison | https://glasp.co/articles/ai-study-modes-compared | not opened (HTTP 403) | | not opened |
| LearnLM / Gemini 2026 update | search only | no 2026 LearnLM item found; search results were 2025 | | not opened |

Conclusion of the scan: PaperMentor (dependency repair, equation term-purpose, figure reading) and teach-back-evaluator (restatement scoring) do things our draft does not yet do. No 2026 vendor learning-mode change was verified from an opened page.

---

## 14. Borrow list

| Item | From (repo@sha, licence) | Goes into | Copied text or rewritten idea |
|---|---|---|---|
| Section skeleton One Sentence / Problem / Core Idea / Contributions / Results table / Why It Matters / Limitations, with per-section length table and 300-500 word target | alaliqing/claude-paper@0af55d0, MIT | paper-quickread | Rewritten idea; length table may be copied with MIT notice |
| Results table columns Metric / Value / Dataset, "never invent numbers" | alaliqing/claude-paper@0af55d0, MIT | paper-quickread | Rewritten idea |
| Insights triad: why it works, conceptual shift, trade-offs | alaliqing/claude-paper@0af55d0, MIT | paper-quickread; study protocol (motivation) | Rewritten idea |
| Mental-model questions: what type of problem, assumed prior knowledge, place in research map | alaliqing/claude-paper@0af55d0, MIT | study protocol (link to known concepts) | Rewritten idea |
| Versioned learner summary (user-summary-v1, v2) | alaliqing/claude-paper@0af55d0, MIT | study protocol (restatement record) | Rewritten idea |
| Claim tag proves / shows empirically / conjectures; assumptions list; own-judgment limitations; "not directly comparable" | michaelrizvi/claude-config@42ff01e, no licence file | paper-quickread | Rewritten idea only (no text) |
| "Relevance to my project" grounded in reading the user's own files; TeX source as optional input; no-overwrite output names | karpathy/nanochat@92d63d4, MIT | paper-quickread | Rewritten idea |
| Naming-vs-understanding test questions (no jargon? different phrasing? concrete example?) | alchaincyf/feynman-skill@b804a7f, MIT | study diagnosis | Rewritten idea |
| Analogy rule: map, then state where it breaks | alchaincyf/feynman-skill@b804a7f, MIT | study protocol (example, link); study diagnosis (boundaries) | Rewritten idea |
| Five answer cases right / sloppy / wrong / guessing / stuck with matching moves | anthropics/claude-for-legal@4a6c651, Apache-2.0 | study diagnosis | Rewritten idea (adapt; keep Apache notice if text reused) |
| Quote the learner's own notes back when they contradict | anthropics/claude-for-legal@4a6c651, Apache-2.0 | study diagnosis (correction from own associations) | Rewritten idea |
| Running miss log, drill the confused pair | anthropics/claude-for-legal@4a6c651, Apache-2.0 | study diagnosis | Rewritten idea |
| Common Pitfalls slot; restart-safe phase + pending_action; implicit difficulty signals | mordor-forge/study-skill@4a2ae45, no licence file | study protocol | Rewritten idea only |
| Elaboration framework solid / imprecise / missing; push via logical consequence; closed vs open gaps closing | lfnovo/open-cognition@bd95d6f, no licence file | study diagnosis | Rewritten idea only |
| Feynman 4 states calibration, probe, consolidation (explain again), closing | lfnovo/open-cognition@bd95d6f, no licence file | study protocol (restate, diagnose, redraw) | Rewritten idea only |
| Learner-moment detection and user control commands | lfnovo/open-cognition@bd95d6f, no licence file | study protocol | Rewritten idea only |
| Concept explainer shape: question, intuition picture, mechanism stepper, edge cases, what to remember | nicobailon/visual-explainer@69cd739, MIT | study visuals | May copy with MIT notice |
| Stepper contract: open on full picture, one claim per step, never autoplay, callout N = step N | nicobailon/visual-explainer@69cd739, MIT | study visuals (redraw) | May copy with MIT notice |
| Label every arrow with a verb; small multiples for cases; "illustrative" label on simplified live figures | nicobailon/visual-explainer@69cd739, MIT | study visuals (mechanism / boundaries) | May copy with MIT notice |
| Grid planning: ASCII first, 40-unit gaps, about 18 chars per SVG line, split above about 12 nodes | nicobailon/visual-explainer@69cd739, MIT | study visuals | May copy with MIT notice |
| Move labels per section (intro 6, design 5, evaluation 6, related work 3) | SNL-UCSB/paper-writing-skill@676f852, MIT | style-mine | May copy labels with MIT notice |
| Reading probes: structural vs quantitative gap; each contribution maps to an evaluation part | SNL-UCSB/paper-writing-skill@676f852, MIT | paper-quickread | Rewritten idea |
| Entry format pattern / Source / Use when; Source status full / partial / abstract; focus modes; dedupe | Galaxy-Dawn/claude-scholar@9037873, MIT | style-mine; paper-quickread header (source status) | Rewritten idea |
| 8 modules x 8 headings profile grid; confidence by source count (8+ / 3-7 / 0-2); no phrase banks; pending/stale/complete | Wang-Ruibin/paper-alchemist@aaeca4a, MIT | style-mine | Rewritten idea; headings may be copied with MIT notice |
| Deterministic metrics: sentence length, hedges, first person, citation and figure mentions | Wang-Ruibin/paper-alchemist@aaeca4a, MIT | style-mine | Rewritten idea |
| Observed vs interpretation; missing vs not applicable; failure to find prior work is not proof of novelty; no venue prestige | K-Dense-AI/scientific-agent-skills@a1043ef, MIT | paper-quickread (critique) | Rewritten idea |
| Repair the missing dependency; show equation first; one transition at a time; end with a reconstruct checkpoint | ShinyJay2/PaperMentor@ff52654, MIT | study protocol (paper mode) | Rewritten idea |
| Equation term-purpose: what each term rewards/penalizes, what changes if removed | ShinyJay2/PaperMentor@ff52654, MIT | study protocol; study diagnosis (mechanism) | Rewritten idea |
| Figure reading schema read from pixels; generated diagram labelled not-from-paper with limitation line | ShinyJay2/PaperMentor@ff52654, MIT | paper-quickread; study visuals | Rewritten idea |
| Preliminary ladder with tiny numeric example per prerequisite | ShinyJay2/PaperMentor@ff52654, MIT | study protocol (plain principle, example) | Rewritten idea |
| Three-pass reading and over-claim checklist | Amey-Thakur/AI-SKILLS@c8c8420, MIT | paper-quickread | Rewritten idea |
| Restatement scored on coherence / completeness / misconception risk, novice question types, three-sentence warm start | GarethManning/claude-education-skills@6bbbce4, CC BY-SA 4.0 | study diagnosis | Rewritten idea only (share-alike) |
| Glossary of terms the learner has shown they understand | kriscard/kriscard-claude-plugins@b16ba4e, MIT (Matt Pocock teach, MIT) | study protocol (link to known concepts) | Rewritten idea |
| Restatement handoff shape Context / Task / Guidance, then stop and wait | code.claude.com output-styles (docs, accessed 2026-10-16) | study protocol | Rewritten idea |
| Learner-state record with misconceptions list | IntelliCode EACL 2026 demo (abstract only) | study diagnosis | Rewritten idea |
| OpenAI Study Mode behaviours | openai.com | n/a | not opened |
| Gemini / LearnLM 2026 changes | n/a | n/a | not opened (no 2026 item found) |
| kriscard interactive-teaching misconception section | skills.cat registry page only | study diagnosis | not opened (SKILL.md); registry summary only |
