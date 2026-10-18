---
name: sv-quickread-card
description: >-
  Writes the nine-section quick-read card for one paper: problem, core idea,
  a field-specific method block, results copied with locations,
  contributions tagged proved, empirical or conjectured, a claim-evidence
  table, limitations, and the link to the reader's research. Text through
  MinerU only; checked and indexed. Use when the user wants one paper
  summarized quickly or triaged.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-quickread-card

Load `../sv-quickread/references/procedure.md` and run Step 0 (reading
root), Steps 1 to 5 and the checklist.

| Step | Load |
|---|---|
| 2 and 3, assess and write | `template-9.md`, `field-method-blocks.md` |
| 4, self-check | `python skills/sv-quickread/scripts/check_quickread.py <quickread.md>` |
| 5, index | `python skills/sv-quickread/scripts/index_append.py` (append only) |

See: ../sv-quickread/references/procedure.md
See: ../sv-quickread/references/template-9.md
See: ../sv-quickread/references/field-method-blocks.md
