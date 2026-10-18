# Learner profile: the study vault

## Contents
1. Why a separate repository
2. Finding the vault
3. Layout
4. knowledge.yaml
5. Asking about prerequisites, a little at a time
6. Privacy

## 1. Why a separate repository

The learner's records (what they know, how they misunderstood things, every
session) must survive skill upgrades, be shared across machines and tools,
and stay private. So they live in a private git repository, `study-vault`
(suggested: `easygl1der/study-vault`), never inside this skill or
`research-core`. [src: user:2026-10-16] (confirmed)

## 2. Finding the vault

`python skills/sv-study/scripts/vault.py where` resolves, in order:

1. environment variable `STUDY_VAULT`;
2. the path written in `~/.config/study/vault` (one line);
3. `~/study-vault` if it exists;
4. otherwise `./reading/` in the current directory, with a warning that
   nothing will be shared across projects.

First use: `python skills/sv-study/scripts/vault.py init ~/study-vault` creates
the layout below, an empty `knowledge.yaml`, a README and a git repository;
then the learner adds a private remote
(`gh repo create easygl1der/study-vault --private --source ~/study-vault --push`)
and records the path with `vault.py where --set ~/study-vault`.

## 3. Layout

```
study-vault/
  profile/
    knowledge.yaml        one entry per concept (section 4)
    sources.yaml          books, courses, papers: how far, which chapters
    misconceptions.md     misunderstandings and how they were corrected; confused pairs
  concepts/<prefix>-<kebab-name>.md     def- thm- lem- method- ex-
  sessions/<YYYY-MM-DD>_<concept>.md
  papers/<YYYY-MM-DD>_<firstauthor>_<short-title>/
  books/<book-slug>/progress.md, chNN-<slug>/
  style/<venue>/cards/    optional: style cards from sv-quickread --style
  index.json              append-only (sv-quickread/scripts/index_append.py)
```

Concept file names: English kebab-case after the prefix, for example
`method-instrumental-variables.md`, `thm-gauss-markov.md`. A concept that
appears again in another source is appended to its existing note, never
duplicated (search `concepts/` and the `aliases` field first).

## 4. knowledge.yaml

```yaml
- concept: instrumental variables
  aliases: [IV, 工具变量]
  field: causal
  proficiency_self: can-use          # not-studied | studied-rusty | can-use | can-explain
  proficiency_ai: studied-rusty      # from the last diagnosis
  sources: ["Angrist & Pischke, MHE, ch. 4", "Ding, A First Course in Causal Inference, ch. 21"]
  prereqs: [method-ols, def-confounding]
  last_restatement: {date: 2026-10-16, result: "mechanism ok; conditions 1/3; boundaries missing", note: concepts/method-instrumental-variables.md}
  notes: confuses consistency with unbiasedness
```

- `proficiency_self` is what the learner says; `proficiency_ai` is the last
  diagnosis. Keep both. When they differ by two levels or more, ask one
  question about it at the start of the next related session.
- `sources` are what the learner actually used, in their words (book and
  chapter, course and lecture); never filled in by guess.
- Write only through the session-save step; never rewrite other entries.

## 5. Asking about prerequisites, a little at a time

No placement test. When the protocol needs a prerequisite that has no
entry, ask one question:

> 讲 <concept> 要用到 <prereq>。你对它：
> A 没学过　B 学过但生疏　C 能用　D 能讲给别人听
> 如果学过，是在哪本书 / 哪门课？

- In Claude Code use the question tool when available; in Cursor, Codex and
  Claude.ai use the lettered text form.
- A or B: give a three-minute version of the prerequisite (plain principle,
  one example) before continuing, or offer to study it first.
- Record the answer immediately (self level and source).
- Ask at most two such questions per session; the vault fills, and the
  questions become rare.

## 6. Privacy

The vault holds personal learning records. Keep it private; do not copy its
content into project repositories or shared skill files. Sessions store
structured summaries, not verbatim transcripts.
