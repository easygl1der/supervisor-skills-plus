# Body text: current content only

## Contents
1. The paper says what is true now
2. Why before how
3. Terms and definitions
4. Openings and order
5. Parked material

## 1. The paper says what is true now

- The manuscript holds only the newest correct content. No revision
  narration ("we now", "as updated"), no history of the study plan ("the plan
  predicted", "a good outcome for the plan"). History lives in `docs/`.
  [src: skill:anti-accretive-docs; arc:@senior-a-comments:54-75; arc:ol:5ecaf3f] (confirmed)
- Rewrite, do not append. When a fact changes, replace the sentence; do not
  stack a correction after it. Test: would a reader who never saw the old
  version understand the paragraph? [src: skill:anti-accretive-docs] (confirmed)

## 2. Why before how

Each method choice opens with the reason it is needed, then the procedure,
then the number it produced. In results, the finding comes first and the
reason sits in the introduction's RQ block and in the method step.
[src: arc:@senior-a-comments:33-50; arc:ol:5ecaf3f; arc:msr:0f96193; note:n06§2.1] (candidate)

## 3. Terms and definitions

- Keep a term table (term, definition, rejected readings). Use one name per
  concept throughout; never switch. After every co-author pass, search the
  text for the rejected readings. [src: arc:@senior-a-comments:1-3; arc:msr:fd0b7cd; note:n06§2.8] (candidate)
- Define each concept before a later passage relies on it.
  [src: skill:writing-shape] (confirmed)
- Use macros for repeated labels and category names so one edit propagates;
  then check spacing in the compiled PDF. Never use macros in text pasted into
  a submission form. [src: arc:chat:group@2026-09-29T12:26; arc:msr:c93ef1f; arc:chat:group@2026-10-03T18:43] (candidate)
- Replace internal jargon (project codenames, tool names, internal sample
  names) with reader language. An outside reader is the test.
  [src: arc:@advisor-glimpse; arc:ol:e03c20a] (candidate)

## 4. Openings and order

- Sections and paragraphs open with substance, not procedure.
  [src: arc:@senior-a-comments:141-157] (candidate)
- Paragraphs build on each other; avoid list-like sequences of disconnected
  paragraphs. [src: arc:CF-22@v2] (candidate)
- Merge a paragraph that adds nothing; "if we have nothing to talk, talk
  nothing". [src: arc:msr:0f96193] (candidate)

## 5. Parked material

Material set aside with `\iffalse`, `%% PARKED` or comment markers gets a
one-line note (why, owner, restore condition) and is listed in
`docs/STATUS.md`. Parked blocks are decided before the final pass. A parked
result can silently disappear from the paper: in the evidence project one
research question had no result for about a day after its tables were
parked. [src: arc:msr:7c705c9; arc:msr:5262231; note:n06§2.9] (candidate)
