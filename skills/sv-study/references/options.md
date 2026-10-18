# Options (all off by default)

Switch on with a phrase ("苏格拉底", "费曼", "自测", "证明重构", "只要笔记",
"导出 Anki") or `--option <name>`.

| Option | What changes | When it helps |
|---|---|---|
| socratic | the whole round is questions: clarify, then assumptions, then evidence, then counterexamples; the tutor explains only when the learner asks or is stuck twice | the learner already half-knows the concept |
| feynman | after the round, the learner explains the concept to an imagined outsider; the tutor marks vague words, skipped steps and circular reasoning | before teaching or presenting the concept |
| self-test | 2 to 3 short questions per concept, each with a confidence rating 1 to 5 before answering; high-confidence wrong answers go to `misconceptions.md` | before an exam or a talk |
| proof | the proof is given as a skeleton with key steps left as `TODO(you)`; the learner fills them; each is checked | mathematics and statistics chapters |
| notes-only | no restatement; the note says it was written without a check | time is short; marked as the low-value mode |
| anki | approved concept notes become cards (cloze and basic, MathJax `\( \)`), exported as a TSV with Anki header lines; nothing enters without the learner's approval | the learner keeps an Anki deck |

Spaced review queues are not part of this skill; the learner's own Anki or
review tool handles them if wanted. [src: user:2026-10-16] (confirmed)

Why off by default: retrieval practice and spacing are among the most
effective techniques for remembering, but the owner's goal is understanding
for research, so the default spends the learner's effort on restatement and
correction instead; see `learning-science.md`.
