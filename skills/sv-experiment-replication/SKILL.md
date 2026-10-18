---
name: sv-experiment-replication
description: >-
  Prepares where data lives and the replication artifact: data placement
  and compute backend, a manifest of data files that can be rebuilt and
  verified, an anonymized artifact checked for identity leaks, and the
  mirror for double-blind review. Use when deciding data storage, packaging
  a replication artifact, or checking an anonymous mirror.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-experiment-replication

Load `../sv-experiment/references/procedure.md`, follow Step 0, Step 8 and
Step 9, with `data-and-backends.md` and `replication-artifact.md`. Scripts,
from the repository root:

- `python skills/sv-experiment/scripts/manifest.py build data/` and `verify --data-dir data/`
- `python skills/sv-experiment/scripts/anon_grep.py artifact/ --terms-file private/identity-terms.txt`

See: ../sv-experiment/references/procedure.md
See: ../sv-experiment/references/data-and-backends.md
See: ../sv-experiment/references/replication-artifact.md
