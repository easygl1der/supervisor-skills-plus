# Response formats (venue-neutral)

## Contents
1. Shared base: the response table
2. Conference rebuttal with a length limit
3. Journal revision letter
4. Internal co-author or advisor response
5. Unmet requests as limitations
6. Rules for every format
7. Evidence status and sources

## 1. Shared base: the response table

Every format is rendered from the round's table in `docs/feedback/<round>.md`
(built by `feedback-to-revision` from the research-core
`response-table.md` template). One row per comment:

| Column | Used for |
|---|---|
| ID (`FB-R1-03`) and the reviewer's own number (`R1.W2`) | Ordering and cross-reference |
| Comment (short quote) | Quoted back to the reviewer |
| Type | Choice of template A / B / C |
| Decision (accept / partial / decline with reason / superseded by) | The stance of the answer |
| Change made | What the answer reports as done |
| Location after change (section, label, page, line) | Where the reviewer can check it |
| Commit | Internal trace; never shown to reviewers at a double-anonymous venue |
| Verified (by diff / pending) | Pending changes are written as plans |

A comment with no row gets one before any text is drafted.
[src: note:n05§6] (candidate)

## 2. Conference rebuttal with a length limit

- Read the limit from the venue call (words, characters, or one page) and
  the rules on new results and links. Record them in the venue profile.
- Order: a two-sentence summary of the main changes or clarifications,
  then the concerns that can change the decision (shared by several
  reviewers, or about the main claim), then the rest grouped by reviewer.
- Each answer: two to four sentences, a pointer to the paper, one number
  when a number settles it. Questions get short answers with a pointer.
- Keep a running count against the limit; cut repeated context first.
- OpenReview-specific practice (threaded replies per reviewer, follow-up
  rounds, score changes visible) applies to ML venues only; Steps 3 and 4
  of the skill cover it.

## 3. Journal revision letter

- **Opening:** one paragraph thanking the editor and reviewers and listing
  the main changes, with how revisions are marked (for example coloured
  text in a marked-up version).
- **Per reviewer, per comment:** the comment quoted in full or closely
  paraphrased, then the response: decision, what changed, and where
  (section, page and line of the marked-up version). Nothing is skipped,
  including comments that need no change; those get the reason.
- **Summary table per reviewer:** comment number, revised content, revised
  section, as in the upstream handbook's revision template, which also
  shows margin notes (`R1.W1`) in the revised paper so each change can be
  found from the letter. [src: up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- **Declined requests:** state the reason with evidence; when the reason is
  that the request cannot be met, use section 5.
- **Editor's own points** come first if the editor raised any.

## 4. Internal co-author or advisor response

- Short: one line per comment with decision, change and location, plus the
  commit.
- Conflicts between commenters are shown with both positions and a
  proposed option; the decision and its owner are recorded (an ADR when it
  sets a rule). [src: note:n05§5.4; note:n05§6] (candidate)
- Mark comments made on an outdated version, and say which current text
  replaces what they read. [src: note:n05§6] (candidate)
- Open questions for the commenter are listed at the end.

## 5. Unmet requests as limitations

When a request cannot be met in this revision (data that does not exist, a
design that cannot be rerun, a population the sample does not cover):

1. Narrow the attacked claim where it is made.
2. State the limitation in threats or limitations with its mechanism, its
   likely effect, and any partial check (research-core TH-01, TH-04,
   TH-08).
3. In the response: acknowledge the point, say what was narrowed and
   where the limitation now stands. Avoid "future work" without a plan.

Example shape (wording to adapt): "We agree that the study cannot
establish X for populations outside the sampled ones. We narrowed the
claim in Section 5.2 to the sampled population and added the reason and
its expected effect to the threats (Section 7, external validity)."

[src: skill:se-paper-refinement; note:n02§10] (candidate)

## 6. Rules for every format

- No number in a response that is not in the paper or in a logged new run
  (research-core IN-01; ML-08 for ML venues).
- A change marked done is in the diff; a pending one is a plan.
- No "you misunderstood"; locate the misreading in the paper's wording and
  fix that wording.
- At a double-anonymous venue, the response follows the same anonymity
  rules as the paper (DB-01 to DB-03): no names, no author-revealing links.
- Promise only what the team will do before the camera-ready or the next
  round, and record each promise as a TODO with an owner.

## 7. Evidence status and sources

No reviewer reports exist in the evidence project yet, so none of the
rules above is tested on real reviews from an SE venue. Rules from the
response table and internal rounds come from the internal review history.
[src: note:n03§5; arc:GAPS.md; note:n05§6] (confirmed)
