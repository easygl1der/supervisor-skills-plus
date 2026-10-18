# Quickread template: nine fixed sections

## Contents
1. Length budget
2. The template (copy this)
3. What each section must and must not contain
4. Section labels in English output
5. Sources of this design

## 1. Length budget

| # | Section | Budget | Must contain |
|---|---|---|---|
| 1 | 元信息 + 一句话 + 2 个标签 | 1 sentence + exactly 2 tags | title, authors, venue/year, arXiv/DOI, MinerU route and pages |
| 2 | 问题与动机 | 2 to 3 sentences | what was broken or unknown before; why it matters |
| 3 | 核心想法 | 2 to 3 sentences | the one move that makes the method work; position against 3 to 6 prior methods if the paper does so |
| 4 | 方法（按领域） | at most 150 Chinese characters (or 100 words) plus formulas | the field method block (`field-method-blocks.md`) |
| 5 | 结果表 | 1 table | only numbers printed in the paper, each with its location |
| 6 | 贡献 | 3 to 5 bullets | each tagged 【证明】【实证】【猜想】 or 【引用】 |
| 7 | 主张与证据对照 | 1 table | claim, evidence and location, strength, doubt |
| 8 | 局限 | 2 columns | 作者承认 (with location) and 我们的判断 |
| 9 | 与我方向的关联 | 2 to 3 sentences | link to the reader's current project or open question |

Body text outside tables: target 700 Chinese characters (or 450 English
words), hard limit 900 (600 words). Tables and formulas do not count.
[src: up:docs/handoff/claude-paper-deepdive-2026-10-16.md] (candidate)

## 2. The template

```markdown
---
paper: <title>
authors: <First Author, Second Author, ...>
venue: <venue, year>        # or "arXiv preprint, <year>"
id: <arXiv id or DOI>
type: <theory | method | empirical | system | benchmark | survey | position>
field: <causal | stats | math | se | ai-ml | other>
tags: [<problem-domain-tag>, <method-tag>]
source: <MinerU route, pages converted, date>
read: <YYYY-MM-DD>
---

# <short title>

## 1. 一句话
<one sentence: what the paper shows, for whom, under which conditions>
标签：`<problem-domain-tag>` `<method-tag>`

## 2. 问题与动机
<2 to 3 sentences>

## 3. 核心想法
<2 to 3 sentences; optional comparison line: 比 <A> 强在 <x>（§n）；比 <B> 弱在 <y>（§m）>

## 4. 方法
<field method block; formulas copied with (Eq. n); added steps marked 补>

## 5. 结果
| 结果 | 数值 | 条件 / 数据 | 出处 |
|---|---|---|---|
| <what> | <copied value> | <setting> | Table n / §n / Fig. n caption |
<theory papers: | 定理 | 结论（照抄要点） | 条件 | Thm n, §n |>

## 6. 贡献
- 【证明】<...>（Thm n）
- 【实证】<...>（Table n）
- 【猜想】<...>（§n，原文未给证明）

## 7. 主张与证据对照
| 主张 | 证据与出处 | 强度 | 疑点 |
|---|---|---|---|
| <claim as the paper states it> | <proof / experiment / citation, location> | 强 / 中 / 弱 | <what is missing or could break it> |

## 8. 局限
| 作者承认 | 我们的判断 |
|---|---|
| <limitation>（§n） | <our judgement, labelled as such> |

## 9. 与我方向的关联
<2 to 3 sentences tied to the current project or open question; if unknown, one line asking for it>
```

## 3. Section rules

**1. 一句话 and tags.** The sentence states the result with its scope, not
the topic ("Shows that X is consistent under A and B", not "Studies X").
Exactly two tags: one problem domain, one method. No generic tags
(`statistics`, `ai`, `paper`). [src: up:docs/handoff/claude-paper-deepdive-2026-10-16.md] (candidate)

**2. 问题与动机.** What prior practice did, where it failed (one concrete
failure), why the failure matters. No praise words.

**3. 核心想法.** The one move. If the paper compares itself with 3 to 6 named
methods, add one line saying which it beats and where, with locations
(literature positioning). [src: guide:AJS/jbes-literature-positioning] (candidate)

**4. 方法.** Use the field block. Every assumption the method needs is
listed, numbered as in the paper when it numbers them. Formulas are copied;
a step you add to make a formula follow is marked 补. [src: user:2026-10-16] (confirmed)

**5. 结果.** Copy numbers exactly as printed (same rounding, same units).
Each row names its table, section, or figure caption. A value visible only
in a plot is not copied; write "图中可见趋势，原文未给数值". For theory
papers the table lists the main theorems instead. [src: user:2026-10-16] (confirmed)

**6. 贡献.** Tags: 【证明】 proved in this paper; 【实证】 shown by experiments
or data in this paper; 【猜想】 stated without proof or evidence here;
【引用】 a result proved elsewhere and used here. The distinction between
proved, assumed and cited follows the theory-paper reading habit of
econometrics and mathematics. [src: guide:AJS/ecta-writing-style; skill:paper] (candidate)

**7. 主张与证据对照.** Same idea as the research-core claim ledger, applied to
someone else's paper: each headline claim, the evidence and where it is,
strength (强 direct proof or experiment; 中 indirect or narrow; 弱 asserted or
cited only), and the doubt (missing evidence, a hidden assumption, a scope
jump from the experiment to the claim). Flag at least the weakest claim.
[src: up:skills/research-core/assets/templates/claim-ledger.md] (confirmed)

**8. 局限.** Left column only what the authors wrote, with location. Right
column is ours and says so. Do not move our judgement into the authors'
column. [src: up:docs/handoff/claude-paper-deepdive-2026-10-16.md] (candidate)

**9. 与我方向的关联.** What the reader could reuse, test or avoid in the
current project, named concretely (a dataset, an estimator, an assumption to
check). Use only what the reader or `docs/STATUS.md` says about the project.
[src: up:docs/handoff/paper-quickread-skill-scan-2026-10-16.md] (candidate)

When a section does not apply, write one line saying why ("理论论文，无实验
数值；见第 5 节定理表"), never pad it.

## 4. English output labels

1 One sentence and tags; 2 Problem and motivation; 3 Core idea; 4 Method;
5 Results; 6 Contributions (tags: proved, empirical, conjectured, cited);
7 Claims and evidence; 8 Limitations (stated by authors / our judgement);
9 Relevance to my work. `check_quickread.py` accepts both label sets.

## 5. Sources of this design

- Section skeleton and per-section length table: claude-paper `summary`
  (MIT, see `THIRD_PARTY.md`), reordered and extended.
- Proved / empirical / conjectured tags and the assumption list: the owner's
  `paper` skill and michaelrizvi's paper skill.
- Section 9: Karpathy's read-arxiv-paper ("what can we borrow").
- Claim-evidence table: K-Dense scholar-evaluation idea, in the format of
  research-core's claim ledger.
Details and licences: `notes/10-reading-sources.md`.
