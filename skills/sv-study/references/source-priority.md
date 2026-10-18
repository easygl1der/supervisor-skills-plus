# Source priority

`/study` teaches from the official paper. `summary.md`, `transcript.md`,
and `quickread.md` in a repo folder are secondary aids. This file wins
over `paper-mode.md` section 2 step 1 when they disagree about what may
fix a claim or a number.

## Contents

1. Source stack
2. Paper-mode workflow
3. Secondary aids
4. Conflicts
5. Session opener
6. Assigned-readings packs

## 1. Source stack

Higher row wins.

| Priority | Source | Role |
|---|---|---|
| 1 | Official paper. Publisher PDF, else the arXiv PDF, else the PDF the user or the reading list names. A publisher HTML page of that version only when no PDF exists. | Primary evidence: claims, definitions, assumptions, equations, numbers, algorithms. |
| 2 | MinerU Markdown of that same file, written this session or reused from `source/paper.md` when the route and the PDF path are on record. | The only text read from priority 1. Citations use the paper's section, equation, table, figure, and page labels. |
| 3 | arXiv TeX of the same paper. | Corroboration when MinerU damaged an equation or a table. Download only with the user's agreement. |
| 4 | Repo aids: `summary.md`, `transcript.md`, `quickread.md`, and `quickread-en.md` when present. | Orientation and cross-links. |
| 5 | Memory, web abstracts, slides, other cards, prior session notes, model knowledge. | Where to look next. Never a number, year, theorem, or quotation. |

Inside priority 1, if the publisher PDF and the arXiv PDF differ, load the
version the user or the reading list names. If neither names one, load the
publisher PDF and say so in the opener.

## 2. Paper-mode workflow

Run this before the protocol and before any formula or number.

1. **Resolve the PDF path.** Record publisher or arXiv, the DOI or arXiv
   id, and the absolute path. Section 6 covers assigned-reading packs.
2. **MinerU, research-core only.** Follow
   `research-core/references/core/inputs-mineru.md` (route order, token
   handling, failure stop, readability gate). Record the route, the page
   range, and any damaged region. If no route works, stop. Priority 4
   does not replace the paper.
3. **Cite the paper.** Every copied formula and every number carries a
   section, equation, table, figure, or page label from the original.
   MinerU's internal numbering is not a citation. Mark steps you insert.

Reuse `source/paper.md` only when it was produced from this PDF and the
route is on record. A `transcript.md` whose header says MinerU was not
rerun is priority 4.

## 3. Secondary aids

Open `summary.md`, `transcript.md`, or `quickread.md` for two jobs:

- **Orientation.** Which concepts the folder already flags, and a sensible
  order for the protocol.
- **Cross-links.** Pointers to `TASKS.md`, other papers in the pack, vault
  notes, and open questions.

They are not sole evidence for any of the following:

- a claim, theorem, assumption, or definition;
- an equation, estimator, or algorithm step;
- a number, sample size, rate, or table cell;
- a page, section, or equation citation;
- a correction of the learner's restatement.

If the PDF cannot be resolved, say so in the opener and stop the paper
session.

## 4. Conflicts

The official PDF wins.

A clash between the MinerU text and the same page of the PDF is a
conversion failure. Repair that span from the PDF or, with consent, from
priority 3. Leave the damaged span unquoted.

When a priority 4 file disagrees with the PDF (equation number, dropped
assumption, year, or a claim the paper does not make), teach the PDF and
add one line to the session file under the material header:

```
Source note: <file> disagrees with the PDF at <location>: <one sentence>. PDF kept.
```

Leave the aid unedited during the study session.

## 5. Session opener

The first message of a paper session names the primary source before any
teaching:

- mode `paper`;
- title and version (publisher PDF or arXiv id);
- path loaded;
- MinerU route and page range, or `reused source/paper.md` plus the route
  already recorded there.

Example: "Paper mode. Primary source: publisher PDF of Rubin (1974),
`<path>`, MinerU route 2, pages 1-8."

If no priority 1 file was loaded, the opener says that and does not enter
the protocol.

## 6. Assigned-readings packs

Subagent note. In an assigned-readings pack the official PDF often is not
beside `summary.md`. The git folder may contain only `transcript.md`,
`summary.md`, and `quickread.md`. The PDF may sit in the source zip, or
the filename and arXiv id may be on the `TASKS.md` row (and in `SOURCE.md`
when that ledger exists). Resolve that path, then run section 2.

Treat `transcript.md` in these packs as priority 4 even when the header
mentions MinerU. This session re-extracts the official PDF.
