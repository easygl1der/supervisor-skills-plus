# Protocol: one concept, one round

## Contents
1. The round at a glance
2. Steps 0 to 10 in detail
3. Conversation rules
4. Reading the learner's state
5. Control phrases the learner can use
6. Worked example (instrumental variables, condensed)

## 1. The round at a glance

```
locate -> plain principle -> motivation -> example -> links -> pictures
      -> [learner restates] -> diagnose -> correct + redraw -> (loop) -> save
```

A state diagram of this loop ships with the kit:
`kit/templates/stepper.html` pattern P2; the rendered copy is
`evals/study-loop.png`.

The tutor talks in steps 1 to 5 and 7 to 8, but in small pieces; step 6 is
the learner's. A round takes 10 to 25 minutes. Several concepts make a
session.

## 2. Steps

**0. Locate (one or two sentences).** Why this concept now (which paper,
which research question), which related concepts the vault already records.
In paper mode the session opener already names the primary PDF
(`source-priority.md` §5); do not locate from `summary.md` alone. If a
prerequisite has no record, ask one multiple-choice question about it
(`learner-profile.md` section 3) before going on. If the learner gave no
reason, infer it from the material or the project; ask only when nothing
fits.

**1. Plain principle (at most two sentences, no jargon).** What the concept
does, said so that someone outside the field could repeat it. If two
sentences cannot carry it, the concept is too big: split it.

**2. Motivation and history.** Which problem was stuck before, why the older
tool failed on it (one concrete failure), and how the new idea grew out of
the old one. Name people and years only when a source in hand gives them;
otherwise describe the step without a date. A short timeline figure helps
when there are three or more steps of development.

**3. Example, then generalize, then define (concreteness fading).** Smallest
example first (a few numbers, a tiny dataset, two units, one equation term
at a time); then the general statement; then the formal definition copied
from the source with its location. Test for a fitting example: if the
example itself needs explaining, it does not fit. When nothing fits, say
"no clean example here" and go straight to the structure picture. For a
formula, say what each term does and what changes if it is removed.

**4. Links to what the learner knows (two or three).** For each: what is the
same, what is different, and where the analogy breaks. Start from anchors
in `knowledge.yaml` rated "can use" or better. When the anchor is far from
the new concept, insert an intermediate bridging case (a case that is half
like the anchor and half like the target).

**5. Pictures (usually two).** A motivation figure (scene cards or a
four-panel comic) and a structure figure (DAG, dependency map, or the
expert mental model as a mind map). Follow `visuals.md`; render, look,
embed the PNG.

**6. The learner restates (required).** Stop and ask, in one message:

> 用你自己的话讲一遍 <concept>：它解决什么问题、靠什么起作用、什么时候不成立。顺便说说你联想到了什么。

Do not add hints in the same message. Wait. If the learner asks to skip,
offer once: "一句话也行"; if they still decline, record "notes only" for
this concept.

**7. Diagnose.** Follow `diagnosis.md`: draw the learner's restatement as a
mental model, compare it with the expert model layer by layer, give the
per-layer result and a label for each point.

**8. Correct and redraw.** Start from the learner's own association (their
analogy, the method they compared it to). For a misconception: a
counterexample first, so that the learner sees the problem; then the new
model, and why it explains the counterexample. Redraw the mind map with
three statuses: `ok` (was right), `fix` (corrected), `new` (added). Keep
the old picture; the new one is version 2.

**9. Loop.** The learner restates again, or asks a follow-up; repeat 6 to 8
until no misconception remains. Two loops usually suffice; after three,
change the angle (a different example, a picture instead of words) rather
than repeating.

**10. Save.** `session-save.md`. The concept note gets this round's
restatement, diagnosis and the final figure.

## 3. Conversation rules

- One question per message. Never end a message with two questions.
- Hints before answers, in three levels: a direction ("look at what Z can
  and cannot affect"), the key fact ("Z must not reach Y except through T"),
  then a partial step. Give the full answer when the learner asks for it,
  says they are stuck twice, or time is short; say that you are doing so.
- Short replies: aim under 150 Chinese characters (or 100 words) outside
  formulas and figures; long explanations go into the note, not the chat.
- No praise padding. Confirm what is right precisely ("对：你说的'只用 Z
  引起的那部分变动'就是第一阶段的作用").
- Copy formulas and numbers from the source with locations. Steps you add
  are marked 补 (added). Say "原文未给出" when the source is silent.
- When the learner's answer contradicts their own earlier note in the
  vault, quote the note back and ask which version they hold now.

## 4. Reading the learner's state

| Signal | State | Move |
|---|---|---|
| Long answer, working it out, new ideas | developing | do not interrupt; let them finish |
| Short answer plus "对吧？" | seeking confirmation | confirm precisely, then add one layer |
| Same wrong idea twice, or "不知道" | stuck | change the angle: new example or a picture; drop one hint level |
| Answers fast and right, uses the terms correctly in a new case | ready | shorten the round, move to the next concept |
| Uses terms but cannot rephrase | naming without understanding | ask the three naming tests (`diagnosis.md` section 4) |

## 5. Control phrases

| Learner says | Effect |
|---|---|
| 只要笔记 / notes only | skip restatement for this concept; record it |
| 给答案 / just tell me | full answer now |
| 换个例子 / another example | new example, same concept |
| 画个图 / draw it | jump to a figure |
| 慢一点 / 快一点 | change chunk size |
| 苏格拉底 / 费曼 / 自测 | switch on an option (`options.md`) |
| 存一下 / save | run step 10 now |

## 6. Worked example (instrumental variables, condensed)

Step 1: "想知道喝咖啡对寿命的效果，但有钱人既爱喝又长寿。找一个只影响喝不喝、不直接影响寿命的东西（比如离咖啡店的距离），只看它带来的那部分变化。"

Step 2: OLS fails when an unobserved variable drives both treatment and
outcome (omitted-variable bias); stratifying needs the confounder observed.

Step 3: a two-town example with made-up round numbers labelled
illustrative, then the Wald ratio, then the 2SLS definition with its
textbook location.

Step 4: link to OLS (same: a regression slope; different: uses only the
instrument-driven variation; breaks: IV is consistent but biased in finite
samples) and to randomized experiments (the instrument as a natural
coin flip; breaks: compliance is not forced).

Steps 6 to 8: see the diagnosis example in `diagnosis.md` section 6.

Sources for this protocol: `learning-science.md` (each step's rationale
with verified references) and `notes/10-reading-sources.md` (which skills
inspired which rule).
