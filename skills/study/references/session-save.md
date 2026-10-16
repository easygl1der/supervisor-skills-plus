# Saving a session

## Contents
1. What is written
2. Session file template
3. Concept note template
4. Commit and push
5. Environments that cannot write files

## 1. What is written

At the end of every session (or when the learner says "save"):

1. `sessions/<YYYY-MM-DD>_<concept>.md`: a structured summary (section 2),
   not a transcript.
2. `concepts/<prefix>-<name>.md`: create, or append a new round to the
   existing note (section 3).
3. `profile/knowledge.yaml`: the entry for each concept touched
   (`proficiency_ai`, `last_restatement`, new `sources`).
4. `profile/misconceptions.md`: each misconception found, its level, and the
   correction that worked.
5. `index.json`: one appended entry per new session or note
   (`../paper-quickread/scripts/index_append.py`).
6. Figures: `fig-<concept>-<type>.html` and `.png` next to the note that
   embeds them.

## 2. Session file

```markdown
---
date: <YYYY-MM-DD>
mode: paper | book | concept
material: <title, chapter, section, or none>
concepts: [<concept>, ...]
duration_min: <approx>
---
# <concept>（<date>）

## 为什么学
## 讲了什么
- 大白话：
- 动机：
- 例子：（或：没有贴切的例子）
- 连接：
## 复述与诊断
（diagnosis.md section 7 format, one block per round）
## 图
![图 1：<结论>](../concepts/fig-<concept>-scene.png)
## 留下的问题
- [ ] ...
```

## 3. Concept note

```markdown
---
concept: <name (English)>
aliases: [<abbrev>, <中文名>]
status: 理解中 | 已理解 | 有疑问
related: [[method-ols]], [[def-confounding]]
sources: [<book ch./§, paper §>]
updated: <YYYY-MM-DD>
---
# <name>

## 一句话直觉
## 动机与来历
## 原理
（example -> general -> formal definition; formulas with locations; added steps marked 补）
## 图
![图 1：<结论句>](fig-<concept>-scene.png)
![图 2：<结论句>](fig-<concept>-dag.png)
## 和已知概念的关系
| 已知概念 | 相同 | 不同 | 类比在哪里失效 |
|---|---|---|---|
## 复述与诊断记录
### 第 1 轮（<date>）
...
## 待解决的问题
- [ ] ...
```

Appending rules: new rounds go under "复述与诊断记录"; the intuition and
principle sections are rewritten only when the understanding changed, and
then the change is recorded in the round, not as a stacked correction.

## 4. Commit and push

`python skills/study/scripts/vault.py save -m "study: <concept> (<date>)"`
stages the vault, commits, and pushes when a remote is configured. If the
push fails (offline, no remote, authentication), the commit stays local and
the script prints what to run later; it never discards changes.

- Claude Code: run it at the end; a background agent may run it so the
  learner is not interrupted.
- Cursor and Codex: run the same command in the terminal tool.
- If the vault is not a git repository, the script says so and exits after
  writing nothing.

Nightly sync of new sessions to Notion is done outside this skill (by the
owner's own bot); nothing here depends on it.

## 5. Environments that cannot write files

Claude.ai (web) cannot write the vault. At the end, print the session file,
the concept note round and the `knowledge.yaml` entry as ready-to-paste
Markdown blocks, each with its target path. Reading the vault there works
through Project knowledge (upload `profile/` and the related `concepts/`).
