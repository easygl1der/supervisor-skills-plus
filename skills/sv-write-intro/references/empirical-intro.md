# Empirical introduction route (RQ-driven studies)

Introduction shape for an RQ-driven empirical paper (mining study, survey,
qualitative study): the paper answers research questions instead of
proposing a method, so there are no challenges to map onto modules. Used
when `research.yaml` has `paper_type: empirical-study`, or when the user's
material is a set of RQs with findings.

Origin: one SE/MSR paper whose introduction was rewritten by two senior
co-authors and then trimmed against an all-in page limit (the evidence
project), generalized. No project names, counts or findings appear here.
Rules use the format `[src: ...] (status)`.

## Contents
1. Inputs before drafting
2. Block sequence and paragraph functions
3. The RQ block
4. Method sentence, contributions, roadmap
5. Lengths
6. Rewrites the exemplar went through
7. Checks before delivery

## 1. Inputs before drafting

- The RQs in their final wording, and for each RQ the two or three
  findings with their ledger rows (number, scope, source). Findings come
  from `sv-write-section` Phase 0 or the author; none are drafted from memory.
  [src: note:n02§11.5; note:n08§5#28] (confirmed)
- For each RQ, the reason a reader outside the niche should care, and the
  prior work or assumption it tests, with citations.
- The phenomenon figure, if one exists (author-supplied; never invented).
- One or two published papers at the target venue that introduce a
  comparable niche topic, to see how they bring the venue's general reader
  in. [src: arc:@senior-a-comments:4; arc:CF-04@v2] (candidate)

Missing inputs are reported after the prose, never filled.

## 2. Block sequence and paragraph functions

[src: note:n06§3; note:n06§1.2; arc:msr:f141169; arc:msr:9809b8c] (candidate)

1. **Context for an outsider.** What the studied object is, with a
   one-clause definition and examples, and why problems in it are costly
   to the venue's general reader. The outsider question ("why should a
   reader who never worked on this care?") is answered here, before any
   method. [src: arc:@senior-a-comments:8-29; arc:CF-01@v2] (candidate)
2. **Phenomenon figure** (optional), referenced from block 1: it shows the
   kinds of problem the study counts; its caption scopes what it assumes.
   [src: arc:msr:6f652b4; note:n07§A.8 FR21] (candidate)
3. **Why this data source matters to the field.** What the field already
   uses such data for (datasets, triage, benchmarks, validity of mining
   studies), and in which ways this domain differs ("departs in three
   ways: first ..., second ..., third ...").
   [src: note:n05§1.1 FB-A-09; arc:msr:5262231] (candidate)
4. **Gap.** What prior work in the field covers and misses; the
   assumptions that practice or prior studies carry over from other
   domains, each with a citation; one sentence "To our knowledge, no prior
   work ..." after them, not before.
   [src: arc:msr:9c69675; arc:RW-01@v2] (candidate)
5. **"To address this gap"**: the study's scope in one or two sentences
   (what was studied, which population), then "We investigate N research
   questions."
6. **One RQ block per research question** (section 3).
7. **Method in one sentence** (section 4).
8. **Contributions** (section 4).
9. **Roadmap** (section 4).

The SE framing point is specific: motivate through maintenance and
evolution uses of the data, not through the domain's importance alone.
[src: note:n05§1.1 FB-A-09; arc:CF-02@v2] (candidate)

## 3. The RQ block

Each research question appears in full in the introduction, not only in
the design section. [src: arc:CF-03@v2] (candidate)

Format, one short paragraph per RQ:

1. **The question in bold**, worded as in the design section.
2. **One why sentence** of the form "<reason the field cares>, so we
   <what this RQ tests>". It names the assumption or use the RQ checks.
3. **Two or three findings**, starting "We find that ...", each scoped
   ("pooled over the studied groups", "in the studied repositories") and
   each matching a ledger row. Whether these sentences carry exact
   numbers is a convention decided once for the paper (abstract, RQ
   headlines, summary boxes and conclusion together).
   [src: arc:msr:9809b8c; note:n06§2.3] (candidate)

Illustrative shape (placeholders, not data):

> **RQ1: Which kinds of configuration problems do users report?**
> Tools that diagnose configuration errors are usually built from
> taxonomies of other platforms, so we first ask which kinds occur on this
> platform and how their mix differs. We find that kind A is the most
> common in the studied projects, followed by B. Kind C, which existing
> taxonomies omit, is about as common as B.

The why sentence carries the motivation that would otherwise sit at the
start of the Results section; Results can then open with the finding.
[src: note:n06§2.1] (candidate)

## 4. Method sentence, contributions, roadmap

- **Method in one sentence**: the data, the instrument (codebook,
  classifier, survey), how it was validated, how it was applied. Detail
  belongs in the methodology section. [src: note:n06§1.2; arc:msr:5262231] (candidate)
- **Contributions** follow the venue: some SE venues expect an itemized
  list (study, instrument, evidence on the tested assumptions, dataset
  and package), while many mining-study exemplars use none. The venue
  profile, or `sv-write-style-mine` reading the venue's exemplars, decides.
  Contributions are claims the paper delivers; each points to a section
  or artifact. [src: note:n02§10; note:n02§11] (candidate)
- **Roadmap**: one paragraph naming the sections in order. It was cut and
  restored for page filling in the exemplar; keep it unless the venue's
  exemplars omit it. [src: arc:msr:9809b8c; arc:msr:1ec1a0f] (candidate)

## 5. Lengths

One exemplar, under an all-in 18-page limit: about 1,100 words of prose in
about ten blocks plus the contribution list and one figure. A reference
point, not a target; the venue and page budget decide.
[src: note:n06§3] (candidate)

## 6. Rewrites the exemplar went through

Draft the end state directly.

- **Study-plan voice and procedure first, to field framing first.** An
  opening that described freezing the data and labeling it was replaced by
  the field context and the data source's role.
  [src: note:n06§1.2; arc:msr:f141169; arc:@senior-a-comments:8-29] (candidate)
- **Findings list, to RQ blocks.** A numbered "our analysis yields the
  following findings" list was replaced by one block per RQ with question,
  why sentence and answer. [src: arc:msr:9809b8c] (candidate)
- **Absolute novelty, to scoped novelty.** "The first empirical study"
  became "An empirical study"; "no prior work" became "To our knowledge,
  no prior work". [src: arc:msr:9c69675; arc:RW-01@v2] (candidate)
- **Uncited assumptions, to cited ones.** Each assumption the study tests
  got a citation and a label (from other domains, or specific to this
  domain). [src: arc:msr:9c69675] (candidate)
- **Unscoped findings, to scoped ones.** "Pooled over ..., although this
  order does not hold in every ..." [src: arc:msr:24d8c65] (candidate)
- **Internal jargon removed.** An advisor reading a draft could not follow
  the introduction because of the project's internal names; replace
  codenames, sample names and tool names with reader language.
  [src: arc:@advisor-glimpse] (candidate)

## 7. Checks before delivery

Run silently; fix the plan, not the prose, when one fails.

- The first block answers the outsider question before any method (WR-03).
- Every RQ appears in full, with a why sentence and findings (WR-04).
- Every finding sentence maps to a ledger row; numbers match the ledger.
- The gap sentence comes after what prior work does and carries "to our
  knowledge" (WR-24).
- The data source's value is stated in the field's own terms (SE-01 for
  SE).
- The contribution format follows the venue profile.
- No internal names, no study-plan voice, no revision narration.
