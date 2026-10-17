# Paper-talk mode

Length: 12 to 18 slides for 15 to 25 min (about 1 slide per 1.5 to 2 min).
Rebuild the paper's section tree first, then map blocks to slide groups.
Keep the paper's order unless a readability reason is stated on the outline.

## Inputs

The `paper-quickread` nine-section card when it exists; otherwise MinerU
markdown of the paper. Copy numbers with table or page. Harvest the paper's
macros into a side `paper-macros.tex` when notation must compile unchanged.

## Spine

1. Title (paper, authors, venue, presenter).
2. Question (say causal if the aim is causal).
3. Paper card: Question, Estimand, Identification, Key assumption, Main
   result, Robustness, Biggest threat, External validity. Unstated estimand
   is a warning. Label our reading "presenter's interpretation" when the
   paper is vague (details in causal-slides.md).
4. Target estimand in potential-outcome notation (Ding defaults).
5. Identifying assumptions ranked by strength; knowledge vs convenience.
6. Method overview (one figure or DAG).
7. Estimator and uncertainty, distinct from identification.
8. Main results as numbers (no causal verb on this slide).
9. Causal reading, sensitivity, what breaks under violation.
10. Link to our project (`research-bridge` if a memo exists).
11. Reproducibility: rerun, or simulate an assumption violation.
12. Optional replication segment (60 min slots): simulation of a violation
    plus a main-table match/mismatch column. Materials posted 24 h before.
13. Limitations and external validity.
14. Discussion question for the group (not a slogan).
15. References, then thank-you, then `\appendix` backup (3 to 5 slides).

Claim vs evidence tags come from the quickread card (proved / empirical /
conjectured). A slide may narrow a paper's claim; it may never strengthen it.

## Critique substitute

There is no Critic attack checklist in this library. Use
`pre-submission-reviewer` `devils-advocate-pass.md` plus
`research-core` `fields/causal.md` "What reviewers and advisors care about".
