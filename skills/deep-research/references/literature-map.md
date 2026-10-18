# Literature-map mode

## Contents

1. What this mode is
2. Inputs: finding the cards
3. Step 1: node inventory (read versus cited-only)
4. Step 2: edges and their types
5. Step 3: the evolution map figure
6. Step 4: comparison table
7. Step 5: gap list and the evidence bar
8. Step 6: next reads by citation chaining
9. Verification
10. Outputs and checklist

## 1. What this mode is

The survey mode searches outward from research questions. This mode works
inward from what the user has already read: a batch of `sv-quickread`
cards and `sv-study` notes becomes (a) an evolution map that links papers by
problem, method and assumption, (b) a comparison table, (c) a gap list
where every gap names the cards that show it, and (d) a short list of what
to read next. It is the bridge between reading single papers and writing a
related-work section or a proposal.

It reuses the survey machinery: the extraction fields of the synthesis
framework (core finding, method signature, conditions, relations), the
citation protocol, and the hedge ladder. It does not replace a full survey:
a map built from five cards is a map of five cards, and says so.

Output language follows the user (default Chinese with English terms), as
in the cards.

## 2. Inputs: finding the cards

Resolve the reading root exactly as `sv-quickread` Step 0 does:
`research.yaml` `reading.dir`; else `<project>/reading/` inside a research
project; else the study vault (`$STUDY_VAULT`, then `~/.config/study/vault`,
then `~/study-vault`, as resolved by the study skill's `vault.py where`); else `./reading/`. Say which root was used.

Read `<reading-root>/index.json`. It is append-only: several records may
share an `id`; take every record per id (one per artifact: `quickread`,
`sv-study`, `style-card`), not only the latest, because each points to a
different file. The user may restrict the batch by tag, field, date or an
explicit list of ids; default is every `kind: paper` entry.

For each paper load, in this order and only what exists: `quickread.md`
(sections 2 to 8), `reflection.md` (its comparison with prior work),
`insights.md`, `method.md`. The paper's converted Markdown under
`source/` (MinerU output) is read only for the related-work section and the
bibliography, to find cited-only works. If a needed source is a PDF with no
Markdown yet, convert it with MinerU per
`skills/research-core/references/core/inputs-mineru.md`; never another
extractor.

Fewer than three read cards: run anyway, but state in the first line of
the map that most nodes are cited-only and the gap list is thin.

## 3. Step 1: node inventory (read versus cited-only)

A node is one work, or one tight family of works when the cards always
cite them together (for example "synthetic control: two founding papers").
Every node gets a status:

| Status | Meaning | Drawn as |
|---|---|---|
| read | has a quickread card or study notes in the index | solid outline, accent fill |
| cited-only | appears only in a read card's related work, introduction or bibliography | dashed grey outline, labelled 未读 |

Claims about a cited-only node are claims made by the citing paper, and the
map says whose words they are ("according to SDID section 6"). A
cited-only node never contributes results numbers of its own.

Keep a node table: short id, full reference copied from the citing
paper's bibliography, status, where it is cited (section), verification
grade (section 9).

## 4. Step 2: edges and their types

Edges are directed from the earlier or more general work to the later or
more specific one. Four types cover most relations; use one of them or
leave the edge out:

| Type | Read as | Example |
|---|---|---|
| extends | B adds a component to A | adds time weights |
| relaxes assumption of | B drops or weakens an assumption A needs | no known rank |
| competes with | A and B target the same estimand or problem with different routes | compared in the same table |
| applies to | A is carried into a new setting B | staggered adoption |

Each edge carries a verb phrase of at most five Chinese characters (or
three English words) saying what changes, and a source: the card section,
or the citing paper's section for cited-only nodes. An edge without a
source does not go on the map.

Edges also record the axis they belong to (problem, method, assumption);
the comparison table and the gap list are read off these axes.

## 5. Step 3: the evolution map figure

Follow `skills/sv-figure-explain/references/visuals.md` (render loop, visual rules)
and `skills/sv-figure-explain/references/visual-scenarios.md` (P1 structure, P7
timeline).

- Default up to about 20 nodes: copy the ELK template with
  `python skills/sv-figure-explain/scripts/newfig.py auto-dag-elk <map-dir>/fig-lit-map.html`
  and edit only the data block. Make each edge's verb a borderless label
  node in the layout (edge A to label without arrowhead, label to B with
  arrowhead); ELK then reserves room for the text and labels stop sitting
  on other edges. Colour encodes the edge type and is never the only cue:
  the verb names the change and the edge table states the type.
- More than about 20 nodes, or a map that keeps changing between sessions:
  Graphviz `dot -Tsvg` embedded in HTML, as visuals.md allows for large
  graphs; or split into an overview plus one figure per branch.
- A timeline (P7) only when every year is checked against a source; years
  from memory are not drawn.
- Not Mermaid by default, no Manim, no hand-placed coordinates beyond six
  nodes.

Render with `skills/sv-figure-explain/kit/render.sh fig-lit-map.html fig-lit-map.png`;
fix until the warning list is empty, then open the PNG and check arrow
directions, label placement and that the caption states a conclusion
("图 1" plus one sentence). Embed the PNG in `map.md`; keep the HTML next
to it.

## 6. Step 4: comparison table

Rows are works, columns are comparison dimensions:

| Column | Content |
|---|---|
| method | the method signature in a few words |
| key assumptions | identifying or modelling assumptions |
| data / setting | data, design, sample sizes |
| results | numbers copied from a card, each with its location |
| source | card file and section, or citing paper section |

Rules from the synthesis framework apply: the caption states the
conclusion; missing cells read "原文未给出" or "未读"; never a blank cell,
never a number from memory. Numbers about a cited-only method that were
produced by a read paper (for example the read paper re-implements the
older method in its own table) are allowed and labelled as such: they are
that paper's implementation, not the original authors' results.

## 7. Step 5: gap list and the evidence bar

A gap is a missing combination on one of the axes (a setting no method
covers, an assumption nobody relaxes, a comparison nobody runs). Every gap
is marked candidate and carries its evidence.

The bar for listing a gap:

- at least two read cards show it independently, or
- one read card plus an explicit statement by that paper's authors (quote
  the location: "results ... are currently not available", section 6).

Our own judgement in a card (a reflection.md item, a "我们的判断"
limitation) does not reach the bar alone; such items go to a separate list
"线索（未达门槛）". A gap stated by the authors of an older paper may
already be closed by later work: mark it "需前向追引核实" until a forward
citation search says otherwise. Wording follows the hedge ladder: "在已读
的 N 篇里没有看到", never "nobody has done".

## 8. Step 6: next reads by citation chaining

Snowballing in both directions, after Wohlin's guidelines
[src: lit:Wohlin 2014, Guidelines for snowballing in systematic literature studies, EASE] (candidate):

- **Backward**: candidates from the read cards' reference lists. Rank by
  (1) how many read cards cite the work, (2) how many map edges touch the
  node, (3) whether reading it would test a listed gap.
- **Forward**: works citing the read papers (Semantic Scholar or OpenAlex
  citations API, or a scholarly search tool). Needed for every gap marked
  "需前向追引核实". If no retrieval is available, say forward chaining was
  not done.

Give at most eight next reads, each with one line on why and which gap or
edge it would confirm or overturn. A reading list is not a verdict: it
names the question each read answers.

## 9. Verification

Every work that appears in the map, the table or the next-read list goes
through `citation-protocol.md`: existence by title search (Crossref,
Semantic Scholar, arXiv or DBLP), then quote accuracy. Grades as there. A
cited-only work whose title changed between the preprint in the
bibliography and the published version is MINOR: keep the bibliography
entry, note the published version. UNVERIFIABLE works leave the map.

## 10. Outputs and checklist

```
<reading-root>/maps/<YYYY-MM-DD>_<slug>/
  map.md            scope note, figure, node table, edge table,
                    comparison table, gaps, clues, next reads, verification
  fig-lit-map.html  ELK source (or Graphviz SVG wrapped in HTML)
  fig-lit-map.png   embedded in map.md
```

Checklist (pass, fail or n/a with evidence):

- Reading root and the index records used are named.
- Every node has a status; cited-only nodes are dashed grey and labelled.
- Every edge has a type, a verb and a source.
- render.sh warnings empty; PNG opened and checked; caption is a
  conclusion.
- Comparison table: no blank cell, every number has a location.
- Every gap meets the evidence bar and is marked candidate; sub-bar items
  sit under clues.
- Next reads give backward and forward status; forward marked not done if
  no retrieval.
- Every listed work has a citation-protocol grade.

Example on real data: `skills/sv-study/evals/reading/lit-map/map.md` (one read
card, so mostly cited-only nodes).
