# Author profile and author/venue conflicts

## Contents
1. Why an author profile is separate
2. Style vault layout
3. Picking author exemplars
4. Author profile format
5. Author/venue conflict table and overlay order

## 1. Why an author profile is separate

A venue profile says what a journal accepts; an author profile says how one
person writes (problem first, numbered contributions, how evidence is
hedged). The two stack: a manuscript for JASA by a student of that author
uses both. Merging them would let one author's habits pose as a journal
rule, or a journal's genre override the author's voice without anyone
noticing. So an author profile is its own file, built from Paper Style
Cards (fields A to L, `references/style-card.md`) like a venue profile, and
it never changes a venue profile. [src: user:2026-10-17] (confirmed)

## 2. Style vault layout

Cards, profiles and the intake queue live in a private style vault, not in
this repository. The vault root is `$STYLE_VAULT`; when unset, ask the owner
and suggest `./style-vault`. Nothing assumes where it sits: it can be its
own repository or a folder inside an author's research repository
(for example `<author-repo>/style/`), and moving it means changing one variable.

```
<STYLE_VAULT>/
  monitor/queue.jsonl                 intake queue (references/intake.md)
  venues/<venue-slug>/cards/*.md      Paper Style Cards per venue
  venues/<venue-slug>/profile.md      venue Style Profile (draft until confirmed)
  authors/<author-slug>/exemplars.md  table from the publication list, with picks
  authors/<author-slug>/cards/*.md    cards of the picked exemplars
  authors/<author-slug>/profile.md    author profile (section 4)
  authors/<author-slug>/conflicts.md  author/venue conflict table (section 5)
  CHANGELOG.md                        what was confirmed, when, by whom
```

## 3. Picking author exemplars

1. Start from the owner-curated publication list (`exemplars` in
   `references/intake.md`); never type a paper list from memory or from an
   API author profile, which can contain homonyms.
2. For voice, prefer published papers where the author is first or
   corresponding; last-author papers show the group's style and count with
   lower weight; middle-author papers do not count.
3. Spread the picks over venues: at least two venues, so a venue habit is
   not mistaken for the author's.
4. Record each pick with its role, venue and year in `exemplars.md`.
   Unpublished group drafts may be read but get `proj:` keys and never
   support a shared rule.
5. Text comes through MinerU or an existing LaTeX transcript, like any
   corpus paper (SKILL.md, Input check).

## 4. Author profile format

Same shape as a venue Style Profile (`references/style-profile.md`): every
pattern names its supporting cards by `lit:` key with a k/n count, and the
consensus threshold applies (three cards minimum, majority support). Added
fields:

| Field | Content |
|---|---|
| Register | `en-stats`, `zh-academic`, or both, with the cards for each |
| Voice markers | habits that recur across venues (for example problem stated before related work; contributions numbered; "we" for the authors) |
| Venue-dependent habits | patterns seen in one venue only; listed, not promoted to author voice |
| Role weight | how many supporting cards are first or corresponding author |
| Status | `draft` until the owner confirms; `confirmed` with date |

No quotes or paraphrases from the papers (hard rule 3): structure and
rhetoric only.

## 5. Author/venue conflict table and overlay order

When both profiles apply, the order is: venue call and author instructions
> venue genre rules (structure, length, required sections) > author voice
(register, phrasing, hedging) > field profile > core rules. Genre wins over
voice; voice fills everything the venue leaves open. A conflict is logged,
never silently resolved:

| Dimension | Venue rule (`lit:` support) | Author habit (`lit:` support) | Resolution for this manuscript | Decided by, date |
|---|---|---|---|---|
| e.g. contribution list | venue cards rarely number contributions | author numbers them | keep numbered, shorten to three | owner, 2026-10-17 |

Conflicts stay in `authors/<slug>/conflicts.md`; a resolution that should
hold for every manuscript is recorded as an ADR in the project
(`research-records`).
