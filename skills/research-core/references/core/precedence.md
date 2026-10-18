# Precedence, sources and formats

## Contents
1. What wins when rules conflict
2. Source formats
3. Rule line format
4. Checklist item format
5. Status lifecycle

## 1. What wins when rules conflict

From strongest to weakest:

1. The official venue call (page limits, template, anonymity, required
   sections). Fetch it and keep a dated copy; do not trust a remembered
   deadline. [src: arc:10-requirements/venue/fse-2027-requirements.md; note:n04§1.1]
2. A decision the authors recorded for this project in `docs/adr/`
   (for example, "print agreement values only when they pass the bar").
3. The venue profile (`references/venues/<venue>.md`).
4. The field profile (`references/fields/<field>.md`).
5. Core rules (`references/core/`).
6. Style overlays the project switched on.
7. Suggestions made by a skill while it works.

A checklist item beats a skill's suggestion when they conflict. The team in
the evidence project wrote the same rule into their own skill folder.
[src: arc:03-skills/README.md]

When two sources at the same level disagree (two co-authors, two exemplar
papers), do not average them. Show both positions, propose one option, and
record the choice in an ADR. [src: note:n05§5.4; note:n02§11.1]

## 2. Source formats

| Prefix | Resolves to | Example |
|---|---|---|
| `arc:msr:<sha>` | Paper-repo commit in the private evidence archive, patch under `07-overleaf-history/patches-msr-tpa/` | `arc:msr:9809b8c` |
| `arc:ol:<sha>` | Overleaf-repo commit, patch under `07-overleaf-history/patches-overleaf/` | `arc:ol:214cc0c` |
| `arc:res:<sha>` | Research-repo commit, `11-mining-github-issue-audit/research-repo-commits.tsv` | `arc:res:de95735` |
| `arc:chat:group@<ts>` | Group chat message, `04-comms/20260929-1007-wechat-group/messages.jsonl` | `arc:chat:group@2026-10-03T19:42` |
| `arc:chat:1on1@<ts>` | One-to-one chat between the student and senior co-author B (alias `@senior-b-1on1`) | `arc:chat:1on1@2026-09-28T23:15` |
| `arc:<path>[:line]` | Any file in the archive | `arc:@senior-a-comments:40-43` |
| `arc:<ID>@v2` | Item in the archived master checklist v2 | `arc:CF-23@v2` |
| `note:nNN§x` | Evidence note in this repo, `notes/NN-*.md` | `note:n06§2.4` |
| `up:<path>` | Upstream Supervisor-Skills file in this repo | `up:skills/sv-write/references/ai-tone-guardrails.md` |
| `skill:<name>` | A former local skill merged into this library | `skill:se-paper-refinement` |
| `lit:<key>` | Published work, full reference in the file's Sources section | `lit:wohlin2012` |
| `venue:<url>@<date>` | Official venue page with fetch date | |
| `user:<date>` | A decision the library owner made | `user:2026-10-12` |
| `proj:<project>/<path>` | A file in another of the owner's project repos | |

Archive paths that contain a person's name are cited through role-based
aliases, resolved by `scripts/check_sources.py`:

| Alias | Meaning |
|---|---|
| `arc:@senior-a-comments[:line]` | Senior co-author A's written comment file |
| `arc:@advisor-glimpse` | Notes on the advisor's relayed reading of the draft |
| `arc:@threats-pivot` | Notes on the threats-to-validity pivot decision |
| `arc:@senior-b-1on1` | One-to-one chat export with senior co-author B |

The evidence archive is private. Its sources are cited by id so that the
rules stay checkable without copying private material into this library.
Never write a person's name in a rule; use roles (student, senior co-author,
advisor, reviewer).

## 3. Rule line format

In profiles and core files, every rule is one bullet that ends with its
sources:

```
- Results paragraphs open with the finding in bold, then a sentence that
  cites the figure or table, then detail. [src: arc:msr:0f96193; note:n06§2.4] (confirmed)
```

The trailing status is `(confirmed)`, `(candidate)` or `(deprecated: reason)`.
A rule without a source goes to the profile's "Unknown" section instead.

## 4. Checklist item format

```
### WR-07 Finding-first results paragraphs
- [ ] Check: Each results paragraph opens with the finding in bold, then a
  sentence citing a figure or table, then detail.
- Why: Readers come for the results; the senior co-author asked for this layout.
- Status: confirmed
- Scope: field:se
- Owner: sv-write-section, sv-write-polish, check-loop
- Src: arc:msr:0f96193; note:n06§2.4
```

- IDs: two or three capital letters, a dash, two digits. Prefixes per file:
  `MA` master, `WR` writing, `FG` figures, `TH` threats, `DB` double-blind,
  `AR` artifact, `VS` venue-submission, `IN` integrity, `RC` records. Field
  additions use the field code (`SE-`, `ML-`, `MT-`, `ST-`, `CI-`).
- `Scope`: `core`, `field:<code>`, `venue:<name>`, or `paper-type:<type>`.
- `scripts/check_checklists.py` enforces unique IDs and the presence of
  `Check`, `Status`, `Scope`, `Owner` and `Src`.

## 5. Status lifecycle

| Status | Meaning | Enforced? |
|---|---|---|
| `candidate` | Seen in one project or stated by one expert | Advisory only |
| `confirmed` | Seen in two or more projects, or stated by a published guide or the venue, or decided by the owner | Yes |
| `deprecated` | Contradicted later; keep the reason | Skipped |

Evidence from one project can still be `confirmed` when the owner decides it
(`user:<date>`) or a published guide states it. Everything else from the
first evidence project starts as `candidate`, except venue rules quoted from
the official call.

On 2026-10-13 the owner promoted items from the first evidence project whose
failure had a clear bad outcome (desk-reject risk, research integrity, lost
or overwritten work, anonymity leak, claims contradicted by the paper's own
data) from `candidate` to `confirmed`. Their `Src` ends with
`user:2026-10-13 (promoted: ...)`. Other first-project items stay candidates
until a second project or a published guide supports them.

