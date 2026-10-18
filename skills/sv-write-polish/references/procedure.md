<!-- Moved from skills/paper-polish/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Paper Polish

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Faithfulness
- One polishing pass
- Field- and venue-aware pass
- Polish by section conventions
- Calibration: do not let the author overclaim
- Be fair to prior work
- Removing AI tone
- Working on files versus pasted text
- Long documents
- Content you cannot read
- How to deliver
- When the problem is deeper than language
- Output language
- Checklist
- Outputs
- Hand-offs

## Overview

This skill polishes the language of an existing draft: it repairs grammar,
clarifies sentences, makes the prose idiomatic, strips AI tone, and rewrites
Chinese drafts into submission-quality English.

The role is a patient senior advisor who helps the author say what the author
means, better. Not someone who replaces it with what the advisor would have
said.

## When to use this skill

- The user has written sentences, paragraphs, or a full draft and wants the
  language improved.
- The user asks to "polish this", "fix the wording", "make this sound less
  AI-generated", "translate my Chinese draft into English for submission",
  or "is this claim too strong".

## When NOT to use this skill

- No prose exists yet and the user wants a section written from an idea. Use
  `sv-write-section` (or `sv-write-intro` for Introductions).
- The user wants the paper's logic skeleton planned. Use `sv-write-skeleton`.
- The user wants a reviewer-style audit of the manuscript. Use
  `sv-review-once`.
- The user wants repeated rounds until the text passes (research fit, then
  venue fit, then language), or a whole-manuscript loop with a round
  budget. Use `sv-review-loop`. This skill stays a single pass.

## Step 0: Load context

Load `research-core` and follow its Step 0:

1. Read `research.yaml`: `field`, `venue`, `paper_type`, `review` (page
   budget, appendix rule), `style.overlays`.
2. Load the core rules `precedence.md`, `claims-evidence.md`,
   `body-text.md` and `deai.md`.
3. Load the field profile `fields/<field>.md` ("Tone and phrasing",
   "Typical structure", "Known disagreements"), the venue profile
   `venues/<venue>.md` when it exists, and only the overlays that
   `style.overlays` names.
4. Load the `writing` checklist and the field additions whose scope
   matches.
5. If a term table exists in the project (from `sv-write-section` or the
   appendix), load it: polishing never changes a locked term.

Without `research.yaml`, polish with the generic conventions below and say
that no field or venue profile was applied.

## Faithfulness

The overriding rule, never fabricate, and conservative by default now live in
`skills/sv-write/references/faithfulness.md` (shared with sv-write-translate);
they apply to every pass below.

## One polishing pass

A workable sequence; it is a method, not a ritual:

1. **Understand first.** Before touching anything, work out what the passage is
   trying to say and what role it plays in the paper (positioning in the
   Introduction? a statement of results?). If you cannot understand a sentence,
   ask; do not guess and edit.
2. **Find the real problem.** Is it surface grammar and wording, or is the
   logic itself broken (several points crammed into one paragraph, claims
   without evidence, correlation stated as causation)? If the problem is
   structural, sentence-polishing will not save it; tell the author it needs
   redrafting rather than polishing (route to `sv-write-section`).
3. **Edit.** Within the faithfulness rule, make the language clearer and more
   idiomatic. Section conventions, calibration, and AI-tone guidance follow
   below.
4. **Account for the changes.** Deliver clean polished text, then briefly state
   the main edits, especially any that might have touched meaning. Details in
   "How to deliver".

This is one pass. When the author wants the text checked again after the
edits, or wants research fit and venue fit checked before language, hand
off to `sv-review-loop`, which runs rounds with an oscillation guard and a
round budget. Do not loop here.

## Field- and venue-aware pass

The loaded profiles change what "better" means in step 3:

- **Section shapes** come from the field profile when it has them (for an
  empirical SE paper: bold scoped finding, figure or table sentence with
  its numbers, detail; an "RQn Summary" box without recommendations). The
  generic section conventions below apply where the profile is silent. A
  conflict is settled by the precedence order in research-core.
- **Tone, tense and hedging** follow the field profile's "Tone and
  phrasing"; where the profile lists a point as Unknown (for example
  tense of findings in SE), keep the author's choice and make it
  consistent.
- **Venue rules**: page budget, abstract limit, anonymity wording,
  required sections. Report the page effect of large cuts or expansions.
- **Overlays only when switched on.** Punctuation bans (semicolons,
  dashes, colons) and similar team or advisor preferences apply only when
  `style.overlays` or the venue profile names them; otherwise do not
  enforce them, because blanket bans produce uniform prose.
- **Reader logic.** For Results, Methods and RQ transitions, also check
  analysis units, number density, comparison words, metric definitions,
  attribution and hedging, implications leaking into Results, and RQ
  chaining. Fix what is pure language; flag what touches a claim.

See also `reader-logic.md`

## Polish by section conventions

Different sections speak differently; do not apply one register everywhere.
Know which section the passage belongs to: the Introduction positions, Methods
enable reproduction, Results state observations in past tense, Discussion
interprets and hedges, the Abstract is a miniature paper, the Title must be
searchable and restrained.

See also `skills/sv-write/references/section-conventions.md` for per-section conventions and common
faults.

## Calibration: do not let the author overclaim

Credibility comes from proportion. Help the author hold the line, and equally:
**only adjust language strength; never invent evidence to support a strong
conclusion.**

Watch for words that outrun the data, and soften or flag them: prove,
conclusively, unprecedented, best, superior, state-of-the-art, groundbreaking,
first (without evidence), and their Chinese counterparts. If the author's own
draft contains them, do not silently keep them; soften or ask.

Match verbs to evidence strength: strong verbs (show, demonstrate, establish)
only on solid evidence; medium (suggest, indicate, be consistent with) for
reasonable-but-open findings; weak (may reflect, appears to) for speculation.

See also `skills/sv-write/references/academic-phrasebank.md` for the full verb ladder and phrase
alternatives.

## Be fair to prior work

Do not flatten prior studies into a straw man to make the present paper look
better. Reviewers see through it, and it is dishonest.

Instead of "previous methods all fail", state the difference precisely:
"Although previous studies showed X, their performance under Y remains
unclear." This keeps integrity and still makes the gap plain.

## Removing AI tone

If the text was AI-generated or heavily AI-assisted, it often carries
recognizable AI flavor. The goal is to make it read like a working researcher
wrote it.

Before delivering, scan against the typical signals (grandiose framing, shallow
-ing tails, marketing adjectives, high-frequency AI words, forced triads,
formatting noise) and rewrite hits.

See also `skills/sv-write/references/ai-tone-guardrails.md` for the complete checklist and the
inflated-claim wordlist.

One warning: after stripping every signal, prose can become clean but lifeless.
The remedy, still without inventing facts: vary sentence length, carry weight
with exact facts rather than adjectives, and state real trade-offs and
limitations plainly. Life comes from precision and honesty.

## Working on files versus pasted text

When the draft lives in files in the workspace (LaTeX or Markdown), work on the
files directly: make the edits in place, and let the version diff serve as the
precise change record. Then give the author a short note listing only the
meaning-risk items to confirm. This beats a prose description of edits, because
every change is inspectable.

When the user pastes text into the conversation, return the full polished text
in the reply, followed by the change notes.

## Long documents

Treat long texts as seriously as short ones; never polish the first pages
carefully and coast on the rest. If the text must be processed in chunks, label
each chunk ("part i of N") and make each chunk a complete, usable product.
Never claim a document was fully polished when parts were skipped.

## Content you cannot read

If part of the source is unreadable (a formula embedded as an image in a Word
export, a corrupted table, an unreadable figure), do not guess its content and
write something plausible into the text. Tell the author exactly where the
unreadable element is and that it needs their manual check.

## How to deliver

The core of the delivery is always **clean polished text** the author can use
immediately.

- Give the polished text first, as flowing prose, not annotated line by line.
- After the text, briefly note the main edits: three to five items are enough.
  Say clearly whether any edit might have touched scientific meaning and needs
  confirmation, and where you recommended adding data or argument but did not
  invent it.
- For meaning-risk edits, the clearest form is a short before/after list:
  original sentence, revised sentence, why, and the risk, side by side, so the
  author can decide at a glance.
- If a paragraph cannot be fixed without adding content, say so honestly
  instead of papering over it with nicer words.

Keep the notes light; they support the text, they do not dominate it.

## When the problem is deeper than language

Two situations mean "this cannot be polished", and they are handled
differently:

1. **The text is beyond sentence repair.** A broken logic chain, a Discussion
   about something unrelated to the key idea: this is a content problem, not a
   language problem. Say so, and suggest redrafting that section with
   `sv-write-section`, then returning to polish.
2. **The core claim itself may not hold.** For example, the author's own
   reported data show the method matched or beaten by a simple baseline. Do not
   write a defense for it and do not invent an optimistic reading. State it
   plainly and suggest a proper audit with `sv-review-once` (for a
   manuscript) or `sv-idea` (for the underlying idea) before further
   polishing.

Pointing out the problem honestly helps the author more than polishing it away.

## Output language

Follow an explicit language request first. If the target venue is a Chinese
journal or a Chinese thesis, polish into Chinese; otherwise default to English.
Do not infer the output language from the language the user typed in: many
researchers discuss in Chinese and submit in English.

## Checklist

After the pass, run the research-core `writing` checklist items this skill
owns, plus the field additions whose scope matches, on the polished text:

- Structure and framing: WR-06, WR-07, WR-08, WR-09, WR-10, WR-11.
- Terms: WR-12, WR-14, WR-15.
- Numbers and hedging: WR-16, WR-18.
- Abstract and conclusion: WR-25, WR-26, WR-27.
- Bibliography: WR-29, WR-30 (when the bibliography is in scope).
- Style: WR-31 (de-AI contract), WR-32 (punctuation bans only from an
  overlay or the venue), WR-33 (no scaffolding or preambles).
- Field additions: SE-04, SE-07, SE-12, SE-13, SE-18 for `field: se`;
  MT-02, MT-04, MT-05 for `field: math`.

Report each item as pass, fail, n/a or unknown with evidence (file and
line or the quoted sentence). `candidate` items are advisory. Items the
pass could not fix without changing meaning are listed for the author,
not forced.

## Outputs

- Polished text (in place in files, or in the reply for pasted text).
- Three to five change notes, plus the before/after list for
  meaning-risk edits.
- The checklist report, kept out of the manuscript.

## Hand-offs

- Multi-round checking, or a re-check after these edits: `sv-review-loop`.
- Heavy AI tone, or a de-AI audit under the full contract: `sv-write-humanize-paper`.
- Comments from co-authors, advisors or reviewers to work through:
  `sv-feedback-revise`.
- A section that needs redrafting rather than polishing: `sv-write-section`.
- A claim the data may not support: `sv-review-once` or
  `sv-idea`.
