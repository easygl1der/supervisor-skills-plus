# Pattern catalog for papers

Surface-level candidates (syndrome S7 and parts of S2, S3, S6), with tiers,
severity and context profiles. Entries are candidates, not automatic edits:
apply the editing contract (`editing-contract.md`) before any change.

Adapted and condensed from `references/patterns.md` of `avoid-ai-writing` by
Conor Bronsdon (MIT License, text in `LICENSE-avoid-ai-writing.txt` at the
skill root; github.com/conorbronsdon/avoid-ai-writing). Its sources are
credited there and kept here: `blader/humanizer`, `brandonwise/humanizer`
(word tiers), `Aboudjem/humanizer-skill` (reshuffle and treadmill tests),
`isatimur/de-slop`, `welttowelt/stop-slop-refined`, and Simon Willison's LLM
cliche highlighter. Entries aimed at social, marketing and crypto copy were
dropped; the `academic` profile and the paper-specific thresholds are new.
The rationed-word caps come from the owner's former `deai-paper-writing` kit.
[src: skill:avoid-ai-writing; skill:deai-paper-writing; note:n02§10]

## Contents
1. How to read the catalog
2. The canonical banned-word list
3. Word tiers
4. Rationed words and phrases in papers
5. Sentence and paragraph patterns
6. Whole-text tests
7. Severity tiers
8. Context profiles and the tolerance matrix
9. Figures that look generated

## 1. How to read the catalog

- **Tier 1: review every match** in the listed sense. Split into two bands:
  - **1A, frequency markers:** words reported to be much more frequent in
    model output. The ratio is inherited from `brandonwise/humanizer` and was
    not measured by either skill; treat it as a convention, not a statistic.
  - **1B, clarity edits:** wordiness and inflated formality. Fixing them is
    good writing, but a 1B hit is **not** evidence of machine authorship.
    Report 1A and 1B separately.
- **Tier 2: flag in clusters**, two or more in one paragraph.
- **Tier 3: flag by density**, roughly 3% of words or more.
- Each entry covers inflected forms (`leverage`, `leveraging`, `leveraged`)
  unless a variant has a separate honest sense.
- A replacement column gives wording, never new facts.

## 2. The canonical banned-word list

The library keeps one canonical list: `sv-write-polish`
`references/ai-tone-guardrails.md`, copied byte-identical into this skill as
`ai-tone-guardrails.md` (synced by `scripts/check_shared_sync.py`). Read it
with this catalog; this file adds tiers, thresholds and the academic profile
rather than a second list. [src: up:skills/sv-write/references/ai-tone-guardrails.md] (confirmed)

The words that `sv-review-once` `references/forbidden-patterns.md`
section 2 flagged beyond the canonical list are now merged into it (Tier 2).
[src: up:skills/sv-review-once/references/forbidden-patterns.md] (confirmed)

That file's blanket em-dash ban is not adopted as a default: in the
`academic` profile punctuation defers to the venue and overlays (section 8).
[src: note:n02§11.4; user:2026-10-13] (confirmed)

## 3. Word tiers

### Tier 1A (frequency markers)

| Candidate | Plain direction |
|---|---|
| delve (into) | examine, study, look at |
| landscape (metaphor) | field, area (keep literal: loss or fitness landscape) |
| tapestry, symphony (metaphor) | name the actual combination |
| realm | area, field |
| paradigm (metaphor) | approach, model (keep: programming paradigm) |
| embark | start |
| testament to | shows |
| pivotal | important, key, or cut |
| underscore(s) | shows, or cut |
| meticulous(ly) | careful, or name the procedure |
| seamless(ly) | name the property (no manual step, no restart) |
| intricate, intricacies | complex, or name the complexity |
| holistic | complete, or list what is included |
| interplay | relation, interaction |
| at its core, at its essence | cut |
| showcasing | showing, or cut the clause |
| game-changing, watershed | say what changed |
| genuine(ly) as intensifier | cut |
| load-bearing (metaphor on claim, assumption) | essential, or say what breaks without it |
| robust (non-statistical) | reliable, or name the property (keep: robust statistics, robust to X when tested) |
| comprehensive (unmeasured) | name the coverage (keep when the coverage is defined) |
| leverage (verb) | use (keep: financial leverage) |
| cutting-edge | recent, or cite the comparison |

### Tier 1B (clarity edits, not authorship evidence)

| Candidate | Plain direction |
|---|---|
| utilize | use |
| in order to | to |
| due to the fact that | because |
| serves as, stands as | is |
| boasts, features (verb) | has |
| commence | start |
| ascertain | determine, find |
| endeavor | effort, attempt |

### Tier 2 (two or more in a paragraph)

harness (verb; keep: test or evaluation harness), navigate, foster, elevate,
unleash, streamline, empower, bolster, spearhead, resonate, revolutionize,
facilitate, underpin, nuanced, crucial, multifaceted, ecosystem (as metaphor;
keep the literal software or package ecosystem), myriad, plethora,
encompass, catalyze, reimagine, cultivate, illuminate, elucidate, cornerstone,
paramount, poised, burgeoning, nascent, overarching, transformative, plus
the reviewer words merged into the canonical list (section 2).

### Tier 3 (density only)

significant(ly) (in papers: reserve for statistical significance; see
section 4), innovative, effective(ly), dynamic(s), scalable, compelling,
unprecedented, exceptional, remarkable, sophisticated, instrumental,
state-of-the-art (bare adjective). Fix by replacing some hits with the
number, comparison or mechanism the source already gives.

## 4. Rationed words and phrases in papers

Counts per paper, from the former `deai-paper-writing` kit. Above the cap is
a finding; at or below is fine. [src: skill:deai-paper-writing] (candidate)

| Item | Cap |
|---|---|
| novel | 2 |
| to the best of our knowledge / to our knowledge | 1 per distinct novelty claim (and required on each, writing checklist WR-24) |
| we believe | 1 |
| In summary / In conclusion closing a subsection | 1 |
| roadmap sentence ("In this section, we first...") | 1, in the introduction |
| sentence-initial Moreover / Furthermore / Additionally | about 1 per page, none opening a paragraph |
| significantly without a test | 0 |
| it is worth noting / it is important to note / notably / interestingly | 0 |
| shed light on, pave the way, bridging the gap, opens new avenues | 0 |
| in the era of, with the rapid development of, plays a vital role | 0 |
| extensive experiments demonstrate, carefully designed, principled (no principle named), effectively and efficiently | 0 |
| we hope this work will inspire | 0 |

## 5. Sentence and paragraph patterns

Severity in brackets (section 7). Pass conditions follow each entry.

- **Chatbot artifacts and cutoff disclaimers** [P0]. "Great question", "I hope
  this helps", "as of my last update". Always delete. Also leaked citation
  markup from chat tools and unfilled placeholders ("[insert result]").
- **Process preambles and reasoning traces** [P0]. "Based on the evidence
  collected...", "Let us now consider", notes to self, ledger rows left in
  prose (writing checklist WR-33).
- **Vague attribution** [P0]. "Studies show", "experts argue" with no
  citation. Cite the source or delete; never invent the citation.
- **Significance and novelty inflation** [P0 in abstract and introduction,
  P1 elsewhere]. "A pivotal step", "the first study to" without a check. Use
  the scoped form or `% TODO: verify` (editing contract section 7).
- **Revision narration (diff-anchored writing)** [P1]. "We now", "as updated",
  "this section was revised to". The paper states what is true now
  (writing checklist WR-07). Version-scoped documents (response letters,
  changelogs) are exempt.
- **Negative parallelism** [P1]. "It is not X, it is Y", "not only X but also
  Y", and the multi-negation countdown. State the positive claim. One real
  correction passes.
- **Superficial -ing tails** [P1]. "..., highlighting the importance of X"
  hung on a sentence to fake depth. Make it a real clause with a subject, or
  cut.
- **Copula avoidance** [P2]. "serves as", "stands as", "represents" for "is".
- **Hedge stacking** [P1]. "may potentially", "could possibly suggest". One
  hedge per claim, placed on the interpretation, not on the measurement.
- **Synonym cycling** [P1]. One object under three names in a passage. In a
  paper this also breaks the term table (writing checklist WR-12): pick the
  table's term.
- **False ranges** [P2]. "From X to Y" where X and Y are not on one scale.
- **Figure narration** [P2]. "As shown in Figure 3, we can observe that...".
  Say what the figure shows; the reference goes in the same sentence.
- **Fragmented heading** [P2]. A heading followed by one line restating it.
- **Bold overuse** [P2]. Mechanical bold. Pass: bold claim sentences where the
  field profile prescribes finding-first paragraphs.
- **Excessive bullets** [P2]. Bulleted prose that is not list-shaped. Pass:
  contribution lists where the venue profile expects them, procedures,
  parameter lists.
- **Colon into a triple** [P2, judgment]. A colon opening exactly three
  items when the content has two or four. Technical writing often has true
  triples; weigh by genre.
- **Same-opener runs** [P2, judgment]. Three or more consecutive sentences on
  the same first word or skeleton, when the repetition does no work.
- **Aphorism formulas** [P1]. "X is the currency of Y", "data is the new...".
  Replace with the claim the source supports.
- **Stranded contrasts and staccato drama** [P2]. Clipped fragments staged as
  reveals. Fold into ordinary sentences.

## 6. Whole-text tests

- **Rhythm and uniformity.** A run of sentences of the same length and shape,
  or paragraphs of the same size whose boundaries do not follow the argument.
  Fix by clarifying the content, never by a length quota or by chopping
  fragments.
- **Over-polishing.** Editing out every irregularity pushes human prose toward
  a generated profile. Keep the author's idiosyncratic but clear choices.
- **Paragraph-reshuffle immunity.** If two body paragraphs can swap without
  breaking anything, the text is a list of points, not an argument (writing
  checklist WR-09). Report it; restructure only in `full` or `section` mode.
- **Treadmill effect.** For each paragraph name the new fact, claim or turn.
  A paragraph that restates its premise in new words is S2.
- **Patch or rebuild.** Five or more justified vocabulary findings across
  categories, three or more pattern categories, and uniform structure support
  a structural diagnosis. Report it; rebuild only when the mode permits.

## 7. Severity tiers

- **P0, credibility:** chatbot artifacts, process preambles, vague
  attribution, unverified novelty or superiority claims in the abstract or
  introduction. Fix in every mode that edits; always reported.
- **P1, obvious tells:** Tier 1A words, rationed items over cap, negative
  parallelism, -ing tails, hedge stacks, synonym cycling, revision
  narration, aphorisms.
- **P2, polish:** Tier 1B, Tier 2 clusters, Tier 3 density, copula
  avoidance, figure narration, bold and bullets, rhythm, punctuation density.

Quick passes use P0 and P1. A full audit covers all three.

## 8. Context profiles and the tolerance matrix

Profiles decide whether a rule applies and how strictly.

- **`academic`** (new; default for manuscripts, theses and assignments):
  formal register, terms frozen, hedges carry real uncertainty, and
  punctuation is decided by the venue profile and project overlays.
- **`academic-response`** (new; response letters and rebuttals): as
  `academic`, but version narration is expected ("we revised Section 4") and
  polite openers are allowed once.
- **`docs`** (from upstream): project READMEs and `docs/` files. Clarity over
  voice.
- **`technical-blog`** (from upstream): public write-ups of the work.
- **`slides`** (new; Beamer decks from `group-beamer`): frame titles and
  frame bodies only; `\note{}` text is checked under `academic`. Terse
  fragments and bullets are expected and are not findings. What is checked:
  one hedge per claim (no stacked hedges, no unhedged causal claim); a selling
  point is stated once per deck, not repeated across title, bullets and the
  summary slide; no "not X but Y" contrasts; no punchy closer or slogan as the
  last bullet or final slide (end on a discussion question); marketing
  adjectives (novel, powerful, remarkable, seamless) rationed to one per deck;
  title verb strength at or below the claim level of the slide's evidence:
  proved ("shows", "proves") / numerical evidence ("suggests", "in our
  simulations") / causal under stated assumptions ("under A1 to A3, X raises
  Y") / exploratory ("we explore", "first look"). A causal verb on a slide
  whose assumptions are not listed on that slide or the one before is P0.
  [src: up:docs/handoff/group-beamer-notes.md] (candidate)

| Rule | academic | academic-response | docs | technical-blog | slides |
|---|---|---|---|---|---|
| Em-dashes | defer: venue or overlay; else density P2 (about 1 per paragraph) | same | relaxed | strict (about 1 per 1,000 words) | relaxed (titles and bullets) |
| Semicolons, colons | defer: venue or overlay; never a default ban | same | skip | skip | skip |
| Bold | relaxed (field-prescribed bold claims pass) | relaxed | relaxed | strict | relaxed (one emphasis per slide) |
| Bullets | relaxed (venue contribution lists pass) | relaxed | skip | relaxed | skip (bullets are the form) |
| Hedging | special: hedge interpretations, not measurements | same | relaxed | relaxed | strict: one hedge per claim; title verb at or below claim level |
| Tier 1A words | strict, with the technical keeps in section 3 | strict | relaxed | partial | strict |
| Rationed items (section 4) | strict | relaxed | skip | relaxed | strict, counted per deck |
| Revision narration | strict | skip | relaxed | relaxed | strict |
| Significance and novelty inflation | extra strict | strict | relaxed | strict | extra strict (titles too) |
| Copula avoidance | strict | relaxed | skip | relaxed | skip |
| Uniform paragraph length | strict, except where the field profile fixes a shape | relaxed | relaxed | strict | skip |
| Transition chains | strict | relaxed | relaxed | strict | skip (transitions live in `\note{}`) |
| Rhetorical questions | strict (research questions themselves pass) | strict | strict | strict | relaxed (one discussion question on the last slide passes) |
| Chatbot artifacts, placeholders | extra strict | extra strict | strict | strict | extra strict (`TODO` for missing data passes) |

"Defer" means: apply the rule exactly as the venue profile or the overlay in
`research.yaml` `style.overlays` states it; with neither, report only density
outliers as P2 judgment calls. "Extra strict" means every instance is
reviewed, not only repeats. "Skip" means the rule does not apply in that
profile.

Inference when no profile is named: a `.tex` file whose `\documentclass`
is `beamer` (or that contains `\begin{frame}`) uses `slides` for frames and
`academic` for `\note{}`; other `.tex` files and manuscript Markdown use
`academic`; a file named like a response or rebuttal uses
`academic-response`; files under `docs/` use `docs`. Say which profile was
used when it changed a finding.

## 9. Figures that look generated

Figures carry tells too: a detail line under every box, gradient pastel
frames, numbered badges, a palette chosen for decoration. Report them to
`sv-figure-design`; this skill does not edit figures.
[src: note:n07§A.8; arc:msr:0f96193; arc:chat:group@2026-10-02T22:28] (candidate)
