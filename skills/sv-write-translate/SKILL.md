---
name: sv-write-translate
description: >-
  Rewrites a Chinese academic draft, or English with heavy Chinese-English
  residue, into submission-quality English by extracting each sentence's
  meaning first, restoring implicit logic, keeping terminology stable and
  fixing common residues, without inflating claims. Obeys the shared
  faithfulness rules. Use when the user asks to translate a Chinese
  manuscript, thesis chapter or paragraph into publishable English.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-write-translate

Formerly the Chinese-to-English section of `paper-polish`. Before starting,
load the shared faithfulness rules, and follow the Step 0 of
`../sv-write-polish/references/procedure.md` (research.yaml, field and venue
profiles, term table).

See: ../sv-write/references/faithfulness.md
See: ../sv-write-polish/references/procedure.md

## Rewriting Chinese drafts into English

When the source is Chinese, or English with heavy Chinese-English residue, do
not translate line by line.

- **Extract the meaning first, then write the sentence.** Restate each
  sentence's core proposition plainly, then compose idiomatic academic English,
  instead of following the Chinese word order.
- **Restore the omitted logic.** Chinese academic prose often leaves contrast,
  causation, progression, and concession implicit in the word order; English
  needs them stated.
- **Keep terminology stable.** Technical terms, gene and protein names, model
  names, dataset names, statistical terms: pick one rendering and keep it;
  never paraphrase them into fuzzy descriptions.
- **Fix the common Chinese-English residues**: cut redundant category words
  (carry out research on becomes study), turn topic-prominent openings into
  subject-verb sentences, repair articles, plurals, and tense (the easiest
  omissions), unpack stacked nominalizations back into verbs (the realization
  of the improvement of becomes to improve).
- **Do not inflate while translating.** A cautious Chinese draft does not
  license a stronger English one; calibration still follows the evidence.

## Delivery

Follow the sections "Working on files versus pasted text", "Long
documents", "Content you cannot read", "How to deliver" and "Output
language" of `../sv-write-polish/references/procedure.md`.

## Hand-offs

- A language pass on the English result: `sv-write-polish`.
- AI tone in the result: `sv-write-humanize-paper`.
- Content gaps found while translating: `sv-write-section`.
