# Diagnosis vocabulary and modes

The structural layer of `sv-write-humanize-paper`: the seven syndromes (S1 to S7), the
two operational tests, the claim ledger, and the input and output of each
mode. Adapted from the owner's former `deai-paper-writing` prompt kit, made
field-neutral (the kit was written from the viewpoint of ML venue reviewers),
with per-field notes added. [src: skill:deai-paper-writing; note:n02§3; note:n02§10]

## Contents
1. Hard constraints
2. The seven syndromes (S1 to S7)
3. Why generated drafts look like this: two tests
4. Three principles for close calls
5. Mode `diagnose` (no rewriting)
6. Mode `full` (five ordered passes)
7. Mode `section` (per-section contracts)
8. Mode `numbers` (reporting hygiene)
9. Mode `audit` (scores and gate, no edits)
10. Guardrails: reject an edit that...
11. What only the author can add
12. Limits
13. Per-field notes

## 1. Hard constraints

Breaking any of these invalidates the whole output.

1. Do not change any technical claim, definition, theorem, parameter, dataset
   name, metric or number.
2. Do not invent facts, citations, results or motivation. A gap that needs
   content becomes `[AUTHOR: <specific question>]` (Markdown) or
   `% TODO: verify <what>` (LaTeX). Never fill it.
3. Do not rotate terminology. Terms in the project term table stay identical
   everywhere; "varying word choice" on a technical term is a defect.
4. Preserve LaTeX exactly: math, `\cite`, `\ref`, `\label`, environments,
   macros, comments. If a sentence that carries a citation is cut, move the
   citation or flag it.
5. Do not delete substantive limitations, negative results or failure
   analyses. The target is the defensive performance of honesty, not honesty.
6. Do not add anything a reader could infer from the surrounding text.
7. Do not soften a strong claim the evidence supports. Do not inflate a weak one.
8. Most edits are deletions and demotions. If the output is longer than the
   input, the pass failed (unless the user asked for expansion).

## 2. The seven syndromes (S1 to S7)

Diagnose against this list, not against impressions.

**S1 Over-closed narrative loop.** Every motivation maps to exactly one
component, every component to one analysis, every analysis to one result,
and every result closes by restating the core claim. Real research is
uneven; a sealed 1:1:1:1 lattice is the strongest structural sign of a
machine-shaped draft.
- Symptoms: each subsection ends with a callback sentence; each contribution
  has a matching subsection of the same size; "which confirms our design of
  X" after every result.
- Fix: at most one closing callback per major section, at its end. Let the
  structure be uneven. Delete callbacks the preceding table already implies.

**S2 Restatement redundancy (density inversion).** The same selling point is
paraphrased in the abstract, introduction, related work, method, results and
conclusion; word count rises while information stays flat.
- Symptoms: a sentence that could move between two sections without either
  noticing; "As mentioned, ..."; a method section that opens with an
  introduction paragraph; a conclusion that is the abstract in past tense.
- Fix: build the claim ledger (section 5). Each claim gets one canonical
  location at the granularity that location needs. Non-canonical
  restatements are cut, not reworded.

**S3 Preemptive defensiveness.** The draft argues with an imagined reviewer.
Once or twice this is scholarship; repeated, it teaches the reader to distrust
the result.
- Symptoms: "One might argue that..."; "To address potential concerns...";
  "While we do not claim..."; "We acknowledge that..." more than twice;
  disclaimers on results nobody challenged; a limitations section that lists
  the limits of the whole field.
- Fix: keep an anticipated objection only if (a) a competent reader would
  raise it on first reading and (b) the paper answers it with its own
  evidence. Cap: two objection-response moves in the main text, none in the
  abstract. The rest goes to the appendix, the rebuttal, or nowhere.
- Field note: a threats-to-validity section is not S3. It is required in
  empirical SE and must stay specific (see section 13).

**S4 Missing storyline, analysis dumping.** No argument for why the problem
matters, and a pile of analyses with no hierarchy.
- Symptoms: an introduction that describes the area but never says what was
  not possible or not known before; results subsections of equal weight; no
  statement of what result would have refuted the claim; research questions
  that list what was measured rather than what is at issue.
- Fix: force a spine: what was unknown or impossible before, what this paper
  makes possible, the one analysis that establishes it, what would have
  refuted it. Rank each analysis PRIMARY (establishes the claim), SUPPORTING
  (removes an alternative explanation) or DUE DILIGENCE (appendix or package,
  one sentence and a pointer in the text).

**S5 Reporting hygiene failure.** The raw lab-notebook tell; a model reviewer
praises it as rigour, a human reviewer does not.
- Symptoms: six decimal places; decimals or units inconsistent across
  tables; raw p-values, intervals and test statistics inline in prose; every
  analysis reported at equal length, including those that end in "no robust
  conclusion"; a test narrated but never interpreted.
- Fix: mode `numbers`.

**S6 Padding to page count.** Related work that surveys instead of
positioning; enlarged figures; long generic future work; restated setup.
- Fix: every related-work paragraph ends in a positioning clause (what that
  line of work cannot do, or how this paper differs) or collapses into a
  citation cluster; future work keeps only directions specific to this
  paper's findings. Page filling follows the project's priority order
  (writing checklist WR-11), never padding.

**S7 Surface style.** Lexicon, rhythm, metadiscourse. Least important per
instance, most visible in aggregate. Word lists and thresholds are in the
pattern catalog (`patterns.md`). Syntactic patterns:
- triads where two items are load-bearing and the third is filler;
- "not only ... but also ...";
- sentence-initial Moreover / Furthermore / Additionally where no connective
  is needed (about one per page at most, none opening a paragraph);
- "Specifically," / "In particular," before a sentence that is not more
  specific;
- uniform paragraph shape (topic sentence, three supports, restatement) and
  uniform subsection shape and length;
- "Our contributions are threefold" followed by three symmetric bullets
  when the real contributions are two or four of different size;
- roadmap metadiscourse beyond one sentence in the introduction;
- "As shown in Figure X, we can observe that ..." instead of saying what it
  shows;
- stacked hedges ("may potentially contribute to"), one hedge per claim;
- dash density above about one per paragraph (a density judgment, not a ban;
  bans come only from an overlay or the venue).

## 3. Why generated drafts look like this: two tests

1. **Plausible continuation.** A model tends to say everything the context
   makes sayable, including what a competent author leaves out.
   **Information-gain test:** for each sentence, could a competent reader of
   the preceding text have produced its content? If yes, delete it (not
   shorten: delete).
2. **Reward for looking thorough.** Preference tuning rewards balanced,
   hedged, complete-looking text; reviewers reward commitment and priority.
   **Asymmetry test:** does the draft say anywhere that one thing matters much
   more than another? If every part is presented as equally important, the
   text was shaped for a reward model, not a reader.

## 4. Three principles for close calls

- **Say it once, in the strongest place.** Repetition is a missing decision
  about where the claim belongs.
- **Earn the closure.** A callback is worth a sentence only when the reader
  may have lost the thread.
- **Concrete beats comprehensive.** One specific number, mechanism or
  failure does more than a paragraph of coverage.

## 5. Mode `diagnose` (no rewriting)

Produce only these artifacts. No revised text, no rewrites phrased as
suggestions, no praise.

1. **Claim ledger.** Every distinct substantive claim and every location.

   | # | Claim (at most 15 words) | Appears in (section + first 8 words) | Occurrences | Canonical location | Cut / demote |
   |---|---|---|---|---|---|

   Flag claims that appear three or more times and near-verbatim sentences in
   two sections (quote both). If the project has a claim ledger
   (`research-core` template `claim-ledger.md`), extend it rather than start
   a new one; the number and source columns come from there.
2. **Closure map (S1).** Every callback or "validates / confirms / supports
   our design" sentence: location, quote, KEEP or CUT (at most one KEEP per
   major section). One sentence on whether the
   motivation-component-analysis-result mapping is 1:1 and which link is the
   most artificial.
3. **Defensiveness inventory (S3).** Every anticipated objection, disclaimer
   and non-claim: location, quote, would a real reviewer raise it (Y/N), is it
   answered with evidence in this paper (Y/N), verdict (KEEP / APPENDIX / CUT
   / MOVE-TO-REBUTTAL).
4. **Density and spine audit.** Words per section and an estimate of what
   each should be; the spine in four sentences (write MISSING for any part
   the text lacks); each analysis classed PRIMARY / SUPPORTING / DUE
   DILIGENCE with its current word count; S5 violations.
5. **Surface counts (S7).** Catalog hits with counts and locations;
   transitions per page; dashes per page; paragraph length distribution;
   triads; roadmap sentences; subsection-closing summaries.

Verdict, three sentences: the most visible tell; the cheapest fix with the
largest effect; the one thing that reads as unmistakably human and must be
protected.

## 6. Mode `full` (five ordered passes)

Structure first: structural edits make most sentence edits unnecessary.

1. **Structure (S1, S2, S4).** Assign each ledger claim one canonical
   location and delete the other restatements. Remove callbacks beyond one per
   major section. Merge subsections that exist only because two contributions
   were claimed. If the spine is missing, do not invent motivation: insert
   `[AUTHOR: state what was not possible before this paper, one concrete
   sentence]` where it belongs. Re-rank analyses and move DUE DILIGENCE to a
   one-line mention and a pointer; say where each result went.
2. **Defence (S3).** Apply the cap. Keep the limitations or threats section,
   rewritten to hold only limitations specific to this work, stated without
   apology.
3. **Paragraphs (S6, S7).** Information-gain test on every sentence. Vary
   paragraph length where the argument allows. Remove subsection-closing
   summaries and extra roadmap sentences. Related-work paragraphs end in a
   positioning clause or collapse.
4. **Sentences (S7).** Catalog words and syntax under the context profile.
   When a flagged word does no work, delete it rather than substitute.
   Collapse stacked hedges. Keep terms frozen.
5. **Numbers (S5).** Run the `numbers` rules without changing any value.

Output:
1. Revised text, LaTeX preserved, author markers where content is needed.
2. Change log:

   | # | Location | Syndrome or pattern | Original (at most 20 words) | Action (CUT / MERGE / MOVE / REWRITE / DEMOTE) | Why (at most 12 words) |

   Every structural edit appears; lexical swaps may be aggregated by type
   with locations.
3. Statistics: words before and after per section; counts before and after
   of callbacks, restated claims, objection-response moves, catalog hits,
   transitions, roadmap sentences, subsection summaries.
4. Open items for the author: every marker with its question; anything that
   looked wrong but was technical content and was left alone.
5. What was deliberately not changed (three to six items) and why: the
   human-sounding parts, and redundancy that is load-bearing (a repeated
   theorem statement, abstract and introduction overlap at different
   granularity, a repeated term).
6. The verification block (`editing-contract.md`).

## 7. Mode `section` (per-section contracts)

Run on the sections `diagnose` flagged worst. Output: revised section, change
log, then each contract item with PASS or FAIL. Where the field or venue
profile gives a different section shape, the profile wins (precedence order
in `research-core`).

**Abstract.** No anticipated objections, disclaimers or "we believe". The
core claim once, with the quantity that makes it non-trivial. At most one
sentence of setup; no field-history opening. Name the result instead of
"extensive experiments demonstrate". No promises about future impact.

**Introduction.** States what was not possible or not known before, within
the first one and a half paragraphs. Motivation is not enumerated 1:1 against
components. Contributions at their real sizes (not necessarily three, not
necessarily bulleted; the venue profile decides the list format). At most one
roadmap sentence. At most one anticipated objection, answered with evidence.
Nothing restated later in the same words.

**Related work.** Positioning, not survey. Each paragraph ends with what that
line of work cannot do or how this paper differs, specifically. No paragraph
exists only to cite. Does not restate this paper's contributions.

**Method or study design.** Opens with the mechanism or procedure, not a
motivation recap. Each step says why it is needed, then what was done, then
the number it produced (writing checklist WR-06). No closing sentences
asserting the design works. Arbitrary choices are labelled arbitrary; a
choice justified without evidence gets `[AUTHOR: was this choice empirical,
inherited from prior work, or arbitrary?]`.

**Results.** Says what would have refuted the claim. PRIMARY results get the
most space; SUPPORTING are compressed; DUE DILIGENCE gets a sentence and a
pointer. An inconclusive analysis gets at most two sentences. No sentence
after each result restating the core claim. Raw statistics in tables. At
least one sentence of honest asymmetry, or `[AUTHOR: which result carries the
claim, and which contributes least?]`.

**Conclusion.** Not the abstract in past tense. Restates the headline claim
at most once and adds the non-obvious consequence. No new defensiveness, no
"we hope this inspires". Future work only where specific to the findings.

## 8. Mode `numbers` (reporting hygiene)

Numbers must not change in value. Go through every table, caption and
sentence with a number.

1. **Precision follows variance.** No more precision than the spread
   justifies; one precision per metric everywhere, abstract included.
2. **Uniform format.** One decimal convention per metric, one style for the
   plus-minus sign, one unit per quantity, consistent separators, percent or
   fraction consistently.
3. **Raw statistics out of prose.** p-values, intervals, test statistics,
   degrees of freedom and per-seed numbers go to tables or the appendix; prose
   states the interpretation and points to them. The analysis stays.
4. **Conventions stated once** (what the plus-minus means, how many runs,
   which test, how bold is assigned).
5. **Inconclusive results kept and compressed**, grouped when several.
6. **No statistics theatre.** A test narrated and never interpreted is either
   interpreted or moved.
7. **Comparison integrity.** Bold the best only under a stated rule; flag a
   bolded method within noise of a baseline.
8. **Traceability.** Every printed number has a row in the claim ledger or
   the project's numbers file (`source_of_truth.numbers`). A number with no
   row is flagged, never corrected from memory.

Output:

| Location | Issue | Current | Same value, new presentation | Rule # |

Then the conventions sentence or caption to adopt, and every number whose
printed precision implies more confidence than the data supports. A number
that looks inconsistent with another becomes
`[AUTHOR: possible inconsistency: X in Table 2 vs Y in text]`; stop there.

## 9. Mode `audit` (scores and gate, no edits)

Report-only. Used by `sv-review-loop` round check 3 and before submission.

Score each axis 0 to 5 (5 = no trace). For any score of 3 or less, quote the
two worst instances with locations.

| Axis | Score | Worst instances |
|---|---|---|
| S1 Closure / 1:1 lattice | | |
| S2 Restatement | | |
| S3 Defensiveness | | |
| S4 Storyline and hierarchy | | |
| S5 Reporting hygiene | | |
| S6 Padding | | |
| S7 Surface style | | |

Five tests, PASS or FAIL with evidence:

1. **Topic-sentence test.** Read only the first sentence of each paragraph in
   order. One argument, or a list of promises and recaps? Quote the sequence
   for the introduction.
2. **Movability test.** Any sentence that could move to another section
   without either noticing is a FAIL instance.
3. **Asymmetry test.** Quote the sentence that says one thing matters more
   than another. None: FAIL.
4. **Falsifier test.** Quote the sentence that says what would have refuted
   the claim. None: FAIL.
5. **Deletion test.** Name the three paragraphs whose removal costs the reader
   least. Any in method or results: FAIL.

Gate: PASS only if every axis is 4 or more and all five tests pass;
otherwise FAIL with the smallest set of changes that would flip it, in
priority order.

Finding list (the part `sv-review-loop` consumes): one row per finding.

| Finding id | Location (file:line or section + first words) | Syndrome / pattern | Severity (P0 / P1 / P2) | Rule source | Proposed edit | Edit class |
|---|---|---|---|---|---|---|

Edit class: `authorized-if-run` (a style or deletion edit the `full` or
`section` mode would make under the contract), `needs-author` (needs content,
a decision or a locked span), `report-only` (judgment call or protected).

## 10. Guardrails: reject an edit that...

- removes a real limitation, negative result or honest uncertainty (apply the
  S3 test; both answers yes means keep);
- removes statistical analysis instead of relocating it;
- breaks terminology consistency;
- drops a citation with the sentence that carried it;
- turns necessary overlap into a gap (abstract, introduction and conclusion
  share the headline claim at different granularity; definitions and theorem
  statements may repeat; a one-sentence method recap before results is fine);
- makes prose informal to sound human (contractions, jokes, first-person
  asides are not the fix; commitment and specificity are);
- shortens by deleting content instead of scaffolding (if CUT actions land
  mostly on results, mechanisms or numbers, the pass optimized word count);
- adds anything the author cannot verify.

Finish with a fresh read of the whole text, aloud if possible: each syndrome
survives a model pass more easily than a human read-aloud.

## 11. What only the author can add

A model can remove tells; it cannot supply presence. Ask the author to add
some of these by hand; never write them on the author's behalf.

1. One number that surprised the authors, stated as a surprise.
2. One design choice rejected, and why (pragmatic reasons count).
3. One honest asymmetry: which component carries the result, which is
   nearly free.
4. One arbitrary choice, labelled arbitrary.
5. One failure with a mechanism, not a hedge.
6. One contestable judgment, stated as the authors' own.
7. Deliberate unevenness: one short section, one small contribution.
8. The authors' own sentence rhythm (if every sentence is 18 to 25 words,
   it reads as generated).

## 12. Limits

- **Style is a proxy, and proxies move.** Optimizing against today's
  detectors is a treadmill. The defensible target is redundancy,
  defensiveness and false symmetry, which cost the reader whether or not a
  model was involved.
- **No pass can supply a missing argument.** If the draft does not know what
  was impossible before it, S4 cannot be fixed by rewriting. That is author
  work (section 11), or `sv-write-section` and `sv-idea` work.

## 13. Per-field notes

- **Empirical SE (`se`).** Research questions are the spine; each RQ section
  opens with the finding (field profile). A threats-to-validity section is
  required and is not S3, but generic field-wide threats are S3 inside it.
  Implications live in their own section, not inside results (field profile
  "Known disagreements"). Hedge readings of model-labelled or text-derived
  data once per paragraph ("as the tracker text describes"), never the
  measured counts. [src: note:n06§2.6; note:n02§11.1] (candidate)
- **AI/ML (`ai-ml`).** The kit's original setting: ablations, seeds and
  baselines. S1 often shows as one ablation row per claimed component and
  nothing else. [src: skill:deai-paper-writing] (candidate)
- **Mathematics (`math`).** Theorem statements and definitions repeat
  verbatim by design; never count them as S2. Proof sketches are not padding.
  [src: skill:deai-paper-writing] (candidate)
- Other fields: use the field profile's "Tone and phrasing" section; if it is
  a stub, apply the core syndromes only and report profile items as unknown.
