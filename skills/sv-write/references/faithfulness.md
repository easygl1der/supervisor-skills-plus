<!-- Moved from skills/sv-write-polish/references/procedure.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged. Shared by sv-write-polish, sv-write-translate and sv-write-style-apply. -->
# Faithfulness rules for editing existing prose

## Contents

- The overriding rule: stay faithful to the author's meaning
- Never fabricate content
- Conservative by default

## The overriding rule: stay faithful to the author's meaning

This outranks everything else in polishing, and it is what authors fear most:
an editor silently changing what the text claims.

**Never silently make an edit that changes scientific meaning.** Concretely:

- Do not strengthen or weaken the author's conclusion (turning "suggests" into
  "proves", or "may be associated with" into "causes") unless you tell the
  author and ask them to confirm.
- Do not turn a correlation into a causal claim.
- Do not quietly drop qualifiers such as "on this dataset", making a bounded
  conclusion look general.
- Do not delete or heavily compress one of the author's arguments because it
  feels verbose. Suggest the cut; do not perform it and call it polishing.

The test is simple. **Pure language edits** (grammar, word order, a smoother
phrasing with identical meaning) are yours to make freely. **Edits that might
touch meaning** are either not made, or made and explicitly flagged for the
author to confirm. When unsure which class an edit falls into, treat it as the
second class.

A useful self-check: after polishing, put your version beside the original and
ask, sentence by sentence, "is the scientific meaning of this sentence the same
one the author wrote?" Every "not quite" is a place you must flag.

## Never fabricate content

Polishing means saying what the author already wrote, better. It does not mean
completing the content.

Add nothing that is not in the original:

- no data, numbers, thresholds, or parameters;
- no equations (if the original has none, do not "helpfully add one");
- no experimental results or comparisons;
- no citations;
- no method names, framework names, or mechanistic explanations. Humanities and
  qualitative fragments are especially easy to damage this way: if the original
  only describes a phenomenon, do not dress it in "discourse analysis" or
  "unlike prior work" that the author never wrote.

If a passage genuinely lacks a piece of evidence or argument, **do not invent
it**. Leave a short parenthetical note addressed to the author instead, for
example: "(consider adding the supporting data for this claim here)" or "(this
step is my inference; the original does not state it; please confirm)". The
judgment and the filling-in stay with the author.

## Conservative by default

Not every author wants a heavy rewrite. Often they want a grammatically clean,
readable version of what they wrote.

So default to the light touch: **prefer the small edit over the big one, and no
edit over the small one.** When the author's own wording is already hedged
("may", "to some extent"), do not "improve" it back into a stronger claim.

If you believe the text deserves a structural rewrite beyond the sentence
level, stop and say so, and let the author choose between "light polish" and
"deep rewrite". Do not default to the deep end.

