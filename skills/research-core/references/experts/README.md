# Expert notes

Anonymized digests of expert guidance that shaped rules in this library.

## Layout

```
experts/
  <field>/
    <source-id>.md
```

`<source-id>` is `<yyyy-mm>-<kind>-<short-topic>`, where `<kind>` is one of
`advisor`, `coauthor`, `reviewer`, `guide` (published writing guide, talk or
blog), or `self` (the owner's own lessons).

## Digest format

```
# <source-id>
Kind: advisor | coauthor | reviewer | guide | self
Field: <code>      Project: <project slug or none>
Raw record: proj:<project>/docs/guidance/<file>.md  (private; or URL for guides)
Date: <date>

## Context
What was shown or asked (paper stage, experiment state).

## Points (paraphrased, short quotes only)
1. <point> -> rule candidate: <file and rule or checklist ID>

## Outcome
Which points became rules, which were project-only, which were declined.
```

## Rules

- Roles, never names. Published guides may name their author in Sources.
- Paraphrase; quotes under 25 words.
- Raw notes stay in the private project repo (`docs/guidance/`); this folder
  holds only what generalizes.
- `lessons-harvest` writes these digests and the rule candidates they produce.

No digests yet. The first evidence project's guidance is cited directly from
the private archive in the core files and the SE profile.
