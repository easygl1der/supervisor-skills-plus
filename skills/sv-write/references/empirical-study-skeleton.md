# Empirical study skeleton (RQ-driven)

Skeleton for an RQ-driven empirical paper: a mining study, a survey or a
qualitative study whose contribution is a set of answered research
questions rather than a new technique. Selected when `research.yaml` has
`paper_type: empirical-study`. The field profile (`research-core`
`fields/<field>.md`) and the venue profile override anything here; this file
is the generic shape they specialize.

Origin: one SE/MSR paper traced through its full revision history (the
evidence project), generalized. Project names, counts and findings are left
out on purpose. Rules use the format `[src: ...] (status)`.

## Contents
1. Before drafting
2. Section table with one exemplar's measured lengths
3. Paragraph functions per section
4. RQ answer format (finding paragraphs)
5. Summary box
6. Implications, threats, conclusion, data availability
7. Rewrite patterns seen in the exemplar's history
8. What not to carry over from the exemplar

## 1. Before drafting

- The claim ledger exists for every RQ section before any prose: one row
  per finding with its number, denominator, scope and script. Prose is
  written from the ledger. [src: note:n02§11.5; note:n08§5#28] (confirmed)
- The copyable numbers and tables are in the manuscript before the prose
  around them is drafted, so the writer never fills a gap with a plausible
  value. [src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#28] (candidate)
- You know which figure or table answers each RQ before writing it. If no
  figure answers an RQ, the RQ is not ready to write.
  [src: skill:lecture-paper-revision; note:n06§3] (candidate)
- A term table (term, definition, rejected readings) exists; labels that
  repeat are macros. [src: arc:@senior-a-comments:1-3; note:n06§2.8] (candidate)

## 2. Section table with one exemplar's measured lengths

Measured on one exemplar under an all-in page limit of 18 pages plus 4 for
references (prose only, comments and floats excluded, about 5 percent
error). These are one paper's numbers, a reference point and not targets;
a different venue or page budget changes them. [src: note:n06§3] (candidate)

| # | Section | Words (exemplar) | Floats (exemplar) |
|---|---|---:|---|
| | Abstract | about 190 to 275 | none |
| 1 | Introduction | about 1,100 | one phenomenon figure |
| 2 | Background and related work | about 1,150 | none |
| 3 | Methodology | about 1,850 | workflow figure, codebook table |
| 4 | Results, one subsection per RQ | about 350 to 900 per RQ | one figure or table per RQ |
| 5 | Implications | about 900 | none |
| 6 | Threats to validity | about 700 | none |
| 7 | Conclusion | about 150 to 200 | none |
| | Data Availability (unnumbered) | about 80 | none |

Total in the exemplar: about 8,000 words of body prose with five figures
and two tables. The shortest RQ section (about 350 words) was the one the
senior co-authors asked to expand when pages ran short.
[src: note:n06§3; arc:chat:group@2026-10-02T22:44] (candidate)

## 3. Paragraph functions per section

**Title.** Topic or claim, then "An Empirical Study of ...", or topic first.
[src: note:n06§3] (candidate)

**Abstract** (plain text, no macros or labels when it is pasted into a
submission form): background (1 sentence), gap (1), "To fill this gap, we
study ..." with scope (1), method (1), key findings (one or two, or one per
RQ), recommendation (1, or one per audience).
[src: note:n06§3; arc:chat:group@2026-10-03T18:43] (candidate)

**Introduction**: drafted by `sv-write-intro`, empirical route. In short:
outsider context, phenomenon figure, why the data source matters to the
field, gap with cited assumptions, RQ blocks, one-sentence method,
contributions, roadmap. [src: note:n06§3] (candidate)

**Background and related work**: one roadmap sentence; domain background a
general reader of the venue needs, with components named as they appear
later; "shares concerns with general X, but differs in N respects"; one
subsection per research strand, one sentence per cited study giving its
method, scale and result, then what the strand does not cover; a closing
"Taken together, ..." synthesis and "Our study takes ...".
[src: note:n06§3; arc:msr:9c69675] (candidate)

**Methodology**: an overview paragraph pointing to the workflow figure; one
subsection per figure phase; one bold "Step n" run-in per figure box, in
figure order; each step gives its purpose clause, the procedure, then the
number it produced. The figure is the outline: box names and run-in names
match. Labeling and gold data are method objects described before any
result uses them. Agreement statistics appear only where they pass the bar
stated before the run. [src: note:n06§2.5; arc:msr:b5c0045; note:n06§2.7] (candidate)

**Results**: one subsection per RQ, no sub-subsections; finding paragraphs
(section 4); a summary box at the end (section 5). Results open with the
finding, not with a method reminder: the "why" lives in the intro RQ block
and the methodology step. [src: arc:msr:0f96193; note:n06§2.1] (candidate)

## 4. RQ answer format (finding paragraphs)

Each finding paragraph has three moves:

1. A bold finding stated as a full sentence in words, scoped ("pooled over
   the studied groups", "in the studied repositories"), with at most one
   number.
2. A sentence that cites the figure, table or column and carries one or two
   exact numbers ("Table N shows that ..."). Never a bare pointer sentence.
3. One to three sentences that dig deeper: a breakdown, the exception, a
   robustness check, or a definition the reader needs.

[src: arc:msr:0f96193; arc:msr:9809b8c; note:n06§2.4] (candidate)

Rules around the format:

- Paragraphs with nothing new are merged or cut; order paragraphs by
  importance. [src: arc:msr:0f96193] (candidate)
- State the general pattern before the exception; when a pooled result
  does not hold in every group, the same sentence says so.
  [src: skill:se-paper-refinement; arc:msr:24d8c65] (candidate)
- No recommendations inside Results; they belong in Implications and cite
  the RQ. [src: skill:se-paper-refinement; note:n02§11] (candidate)
- Hedge the interpretation, never the measured value. An explanation the
  study did not test is labelled as such ("one possible reason, which our
  data do not test"). [src: skill:humanize-paper; arc:msr:9c69675] (confirmed)
- Check every finding paragraph for the figure or table sentence; it is the
  move most often missing in the exemplar. [src: note:n06§2.4] (candidate)

Illustrative shape (placeholders, not data):

> **Pooled over the studied groups, category A is the most common, although
> one group departs from this order.** Figure N shows that A accounts for
> X% of all items and for the largest share in every group but G. In G,
> category B is more common, which matches the different role G's
> repositories play (Section 2).

## 5. Summary box

At the end of each RQ subsection, a box titled only "RQn Summary": two to
four sentences, the pooled claim first and then its exception, one or two
exact numbers at most, the same hedges as the body, no recommendations.
[src: arc:msr:9809b8c; note:n06§3] (candidate)

The title went through three forms in the exemplar ("Takeaway for RQn",
"Summary (RQn): <claim>", "RQn Summary"); the last was kept. Use what the
venue's exemplars use when they differ. [src: note:n06§3] (candidate)

## 6. Implications, threats, conclusion, data availability

**Implications**: one sentence naming the audiences; one subsection per
audience; each item a bold imperative, then "RQx shows that ...", then the
consequence or a labelled untested explanation, an optional worked example,
and "<audience> should ...". Each item is operational and tied to an RQ;
no product advice nobody asked for. Implications add no new numbers.
[src: arc:msr:f141169; note:n06§1.8; note:n02§8] (candidate)

**Threats to validity**: one sentence naming the categories with a
citation, one subsection per category, each threat written as threat, then
check or mitigation (with its number), then the residual. Threats are
specific and ordered, never "more data is needed". A reviewer request that
cannot be met goes here with its mechanism.
[src: lit:wohlin2012; note:n06§1.9; skill:se-paper-refinement] (candidate)

**Conclusion**: one paragraph, shorter than the abstract: what was done,
findings in RQ order, one conditional implication ("suggest ... when ..."),
one future direction tied to the main limitation.
[src: note:n06§1.10] (candidate)

**Data Availability** (when the venue asks for it): the anonymous package
link and one inventory sentence whose scope matches what the package really
recomputes. [src: arc:msr:5776349; note:n06§1.12] (candidate)

## 7. Rewrite patterns seen in the exemplar's history

Each pattern is something the senior co-authors changed repeatedly; draft
it right the first time.

- **Why before how.** The reason for a method choice goes in the intro RQ
  block and the methodology step; results start with the finding.
  [src: note:n06§2.1; arc:@senior-a-comments:33-50] (candidate)
- **No study-plan voice.** Remove "the plan predicted", "we keep the
  original wording", "frozen snapshot" process talk. The reader evaluates
  findings, not plan adherence. [src: note:n06§2.2] (candidate)
- **Numbers: no laundry lists, but exact headline numbers.** One number per
  claim sentence, the rest in tables; decide once (in an ADR) whether the
  abstract, RQ headlines, summary boxes and conclusion carry exact numbers.
  The exemplar trimmed and restored them several times.
  [src: note:n06§2.3] (candidate)
- **Finding first.** Bold claim, figure or table sentence, detail.
  [src: note:n06§2.4] (candidate)
- **Figure mirrors methodology.** Number the boxes; one run-in per box.
  [src: note:n06§2.5] (candidate)
- **Soften claims to evidence.** "The first study" becomes "An empirical
  study" plus "to our knowledge"; causal "this happens since" becomes a
  labelled untested reason; text-derived labels carry a reader qualifier
  once per paragraph. [src: note:n06§2.6] (candidate)
- **Lock terms.** Term table with rejected readings; macros for labels;
  search for rejected readings after every co-author pass.
  [src: note:n06§2.8] (candidate)
- **Park visibly.** A parked block carries a one-line restore note and an
  owner, and is listed in the status file. [src: note:n06§2.9] (candidate)
- **No appendix as padding** at venues with an all-in page limit; a compact
  table in the body and a pointer to the package.
  [src: note:n06§2.10; arc:chat:group@2026-10-01T08:56] (confirmed)
- **Plan the page fill.** Expand thin results with explanation and examples
  first, then method detail, then background, then implications and
  threats. [src: note:n06§2.11; arc:chat:group@2026-10-02T22:44] (candidate)
- **Expect late details to fingerprint the paper.** Real issue numbers,
  dataset sizes in the title and topic-named anonymous URLs do not break
  anonymity rules but make the paper recognizable; check them before
  submission. [src: note:n06§2.12] (candidate)

## 8. What not to carry over from the exemplar

- Its domain vocabulary, groups, counts and findings.
- Its exact section lengths as targets (they fit one page budget).
- Its contribution list format: SE sub-venues disagree on itemized
  contributions; the venue profile decides.
  [src: note:n02§10; note:n02§11] (candidate)
- Its threat category set when the venue's exemplars use another one.
