# Bridge card template

## Contents
1. Rules for filling the card
2. Template (project mode)
3. Template differences in general mode
4. Length

## 1. Rules for filling the card

- Headings are in Chinese by default (the user's language otherwise);
  technical terms stay in English.
- Every fact about the source carries its location as the source notes
  give it (section, equation, table, algorithm) and the file it was read
  from. Items the notes mark as not checked stay marked.
- Own reasoning is labelled 补 (added); illustrative numbers are labelled
  示意 and never look like data. Expected magnitudes appear only with a
  source.
- Verdict vocabulary (exactly one): 主方法 (main method), 改造后用
  (use with a named modification), 只做稳健性检验 (robustness check
  only), 暂不 (not now; name the missing precondition), 不用 (no).
- The validation test is written, dated, before anything runs. Later
  changes are added below it with a new date; the original stays.

## 2. Template (project mode)

```markdown
---
status: scratch
kind: bridge
source: <paper id or concept>, files: <paths read>
project: <research.yaml project>
date: YYYY-MM-DD
verdict: <one of five>
---
# 学以致用：<source short name> → <project>

## 0. 一句话结论
<verdict> ，因为 <decisive row(s)>。最便宜的证伪测试：<one line>。

## 1. 来源与目标
| | 来源（<source>） | 我的项目 |
|---|---|---|
| 研究问题 | ... (loc) | ... (research.yaml / STATUS) |
| 痛点 | 来源解决什么 | 我的项目卡在哪 |

## 2. 结构映射（source → target）
| 元素 | 来源 | 我的项目 | 类比在哪里断 |
|---|---|---|---|
| Unit | | | |
| Treatment / timing | | | |
| Outcome | | | |
| Comparison | | | |
| Time structure | | | |
| Estimand | | | |
| Inference | | | |
| Scale | | | |

## 3. 假设迁移检查
| 假设（出处） | 在我这里成立？ | 证据 / 怎么查 | 不成立会怎样 | 对策 |
|---|---|---|---|---|
| A1 ... (Eq. x) | 是 / 否 / 未知 | | | |
| 新增：我的项目额外需要的假设 | | | | |

可检验：... 只能靠论证：...（进 threats）

## 4. 结论与怎么用
- 判定：<verdict>，因为 ...
- 改动的管线步骤：之前 → 之后
- 论文里的主张会变成：...（scope words）
- 它不能给你的：...
- 和已有 ADR 的关系：无冲突 / 与 ADR-NNNN 冲突，需要新 ADR

## 5. 最小验证实验（YYYY-MM-DD 写定，运行前）
- 问题：只测哪一条假设或主张
- 数据：
- 步骤与指标：
- 要试的变体（全部列出，全部报告）：
- 预期结果：方向 + 理由（量级只在有出处时写）
- 失败判据（kill criterion）：
- 结果不明时：
- 各结果的下一步：通过 → ... ；失败 → ... ；不明 → ...
- 预算：约 N 小时，复用 ...

## 6. 交接
- sv-idea / sv-experiment / sv-supervisor-records / sv-litreview / study：各一句，说清交什么
```

## 3. Template differences in general mode

Replace sections 1 to 5 with:

```markdown
## 1. 可移植的核心（一句话，不带领域词）
## 2. 适合的项目长什么样（结构条件）
## 3. 不适合的情形（会断的地方）
## 4. 任何项目都要先查的假设（表格，"成立？"一栏留成要问的问题）
## 5. 最便宜证伪测试模板（数据 / 指标 / 失败判据留空位）
## 6. 要变成具体建议，请告诉我：<the one question>
```

## 4. Length

Body text outside tables: at most about 1000 Chinese characters or 650
English words, most of it in the validation test. Tables carry the
content; prose only states the verdict, the how, and the test. In the
hand-off section, say "not needed" for a skill that has nothing to do,
rather than leaving it out.
