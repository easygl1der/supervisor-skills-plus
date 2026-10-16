# --style: dissect one paper's writing

## Contents
1. What it produces
2. Steps
3. Rules
4. Hand-off to style-mine

## 1. What it produces

One Paper Style Card in `style-mine`'s format (fields A to L in
`skills/style-mine/references/style-card.md`), saved as `style-card.md` in
the paper folder. There is no separate format for quickread: one style
memory only. [src: user:2026-10-16] (confirmed)

## 2. Steps

1. State the extraction rule aloud: structure and rhetoric only; no quotes,
   no paraphrase of content.
2. Assign the paper ID (`exemplar_NNN`, or `<venue>_NNN` when the user names
   the target venue) and a `lit:<firstauthor><year><firstword>` key.
3. Fill fields A to L. For field B add the **move sequence** of the abstract
   and introduction, one CARS tag per paragraph (M1 territory, M2 niche, M3
   occupy), and one line per paragraph on its function and its transition to
   the next.
4. In field J give 3 to 5 **sentence templates** abstracted with
   placeholders, for example "Although [prior approach] handles [case], it
   requires [assumption], which fails when [condition]." No topic words left
   in a template; never a copied sentence.
5. Field H: hedging (which claims are hedged and with which verbs), sentence
   length (short, long, varied) and register.
6. Optional focus (`--style intro|method|results|rebuttal`): fill the named
   area in more detail, leave the others brief.

## 3. Rules

- Describe moves, never content: "opens with a failure of an existing
  estimator in one sentence" is fine; naming the estimator is not.
- No sentence from the paper appears on the card, even in quotes.
- The card is a candidate observation. It does not change any profile.

The field names for patterns (writing patterns, structure signals,
reusable phrasing, venue signals) and the per-section dimensions follow
existing paper-mining tools; the move labels follow Swales' CARS model.
Details in `notes/10-reading-sources.md`. [src: lit:swales1990genre] (confirmed)

## 4. Hand-off to style-mine

Tell the user the card's path and which venue or field corpus it could join.
`style-mine` accumulate counts it only when 5 to 10 cards for that venue
exist and the consensus threshold is met.
