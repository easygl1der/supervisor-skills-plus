# Diagnosis: comparing mental models

## Contents
1. The expert model in three layers
2. The learner's model
3. Labels per point and the per-layer result
4. Naming versus understanding
5. Correction moves
6. Worked example (instrumental variables)
7. Output format

## 1. The expert model in three layers

Before asking for the restatement, write the expert model of the concept
(it also becomes the mind map, `kit/templates/mind-map.html`):

| Layer | Question | IV example |
|---|---|---|
| Mechanism | How does it work? | use an outside push Z on T, and only the part of T's variation that Z causes |
| Conditions | What must hold? | relevance (Z moves T), exclusion (Z reaches Y only through T), independence (Z unrelated to unobserved confounders) |
| Boundaries and consequences | What can and cannot it answer? | estimates a local effect for compliers (LATE), not the population average; weak instruments give large bias |

Three to six points in total. Each point cites the source location
(definition, theorem, section) it comes from.

## 2. The learner's model

Map each sentence of the restatement to a point of the expert model, to a
wrong point, or to nothing. Draw it as the same mind-map shape so the two
can be compared side by side. Missing branches are empty, wrong edges are
drawn as the learner stated them.

## 3. Labels and per-layer result

| Label | Meaning | Move |
|---|---|---|
| ✅ core right | captures the mechanism or purpose of a point | confirm and name the matching part of the definition |
| 🟡 partly right | right direction, missing a condition, scope or boundary | add the condition; one counterexample shows why it is needed |
| ❌ misconception | contradicts the definition, or reverses a direction | counterexample first, then the new model (section 5); give its level |
| 🔗 missing link | each piece fine, but not connected to the motivation or to a known concept | add the bridge as an edge in the redrawn figure |

Misconception levels (from research on conceptual change):

1. **Isolated false belief**: one wrong fact; fix the sentence.
2. **Flawed mental model**: the parts are wired wrongly; rebuild the
   relevant layer, not just one sentence.
3. **Category mistake**: the concept is treated as the wrong kind of thing
   (an estimator treated as an assumption, a process treated as an object,
   an estimand confused with an estimator); rebuild the frame.

Per-layer result, in one line: "机制层 ✅；条件层 1/3；边界层缺". Then one line
per point with its label. Do not compress the result into a single score.

Optional scoring frame for a quick read of a restatement: solid / imprecise
/ missing per layer. Push on an imprecise point by stating its logical
consequence ("如果真是这样，那么 Z 直接影响 Y 也没关系了？").

## 4. Naming versus understanding

A restatement full of correct terms can still be naming without
understanding. Three tests, one at a time:

1. Say it again without the terms (no "排他性", no "LATE").
2. Answer the same question asked differently ("Z 可以和 Y 相关吗？").
3. Use it once in a new case the learner has not seen.

Failing two of the three means the point is labelled 🟡 at best, whatever
the vocabulary.

## 5. Correction moves

- Start from the learner's own association: their analogy, the method they
  compared it with, their example. Keep what is right in it and say so.
- For ❌: present a counterexample where the learner's model predicts the
  wrong thing; let the learner see it; then give the new model and show how
  it handles the counterexample. Do not just state the right answer.
- For level 2 and 3 misconceptions, rebuild the layer: redraw that branch of
  the mind map from scratch.
- When the learner contradicts their own earlier note, quote it.
- Keep a running list of the pairs the learner confuses (estimator vs
  estimand, consistency vs unbiasedness) in `misconceptions.md`; next time a
  related concept comes up, check that pair first.
- Redraw: `ok` for points that were right, `fix` for corrected ones, `new`
  for added ones; the figure's caption gives the per-layer result.

## 6. Worked example (instrumental variables)

Restatement: "IV 就是找一个和 X 相关的变量，替换掉 X 来回归，这样就没有偏了，有点像 2SLS 的第一阶段预测值。"

| Point | Label | Why |
|---|---|---|
| "和 X 相关" | ✅ core right | the relevance condition |
| "像 2SLS 第一阶段" | 🔗 missing link | right association, but not why the fitted values: they keep only the part of X driven by Z, which is free of the confounder |
| "替换掉 X 就没有偏" | ❌ flawed mental model (level 2) | drops exclusion and independence: if Z reaches Y directly, the bias stays |
| "没有偏" | 🟡 partly right | IV is consistent, but biased in finite samples, badly so with weak instruments |

Per layer: mechanism 🔗 (the idea is there, the reason is missing),
conditions 1 of 3, boundaries missing.

Correction, from the learner's "first stage": draw Z -> X -> Y with U -> X
and U -> Y; ask what the fitted value of X can depend on (only Z). Then add
a red dashed edge Z -> Y and ask what the fitted-value regression now picks
up (the direct path too): the counterexample to "no bias". Redraw with
relevance `ok`, first-stage reason `new`, exclusion and independence `fix`,
LATE and weak instruments `new`.

## 7. Output format

```markdown
### 第 <n> 轮（<date>）
> 复述：<learner's words, verbatim>

- 分层：机制 <..>；条件 <k/m>；边界 <..>
- ✅ <point>（对应 <definition / Thm, location>）
- 🟡 <point>：补 <condition>；反例 <one line>
- ❌ <point>（层级：心智模型缺陷）：反例 <...>；新理解 <...>
- 🔗 <point>：桥接 <edge added>
- 纠正后的图：![图 <n>：<conclusion>](fig-<concept>-mental-v<n>.png)
```

Sources: `learning-science.md` (conceptual change, self-explanation,
knowledge integration, misconception levels); answer-case and
elaboration ideas credited in `notes/10-reading-sources.md`.
