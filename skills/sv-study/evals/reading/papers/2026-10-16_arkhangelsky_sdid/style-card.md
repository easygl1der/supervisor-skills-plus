## Paper Style Card: exemplar_001

> Extraction rule: structure and rhetorical patterns only; no quotes, no paraphrase of content.

METADATA
- Paper ID: exemplar_001
- Citation key: lit:arkhangelsky2021synthetic
- Authors: Arkhangelsky, D.; Athey, S.; Hirshberg, D. A.; Imbens, G. W.; Wager, S.
- Year: 2021 (arXiv version July 2021)
- Venue: arXiv preprint (econometrics methods paper)
- Corpus role: user_exemplar (candidate for an econometrics-methods corpus)
- Conversion status: converted_checked (MinerU, pages 1-20 of 69; Table 1 cells merged, verified against text)
- Paper type: technique
- Method type: theory + simulation + empirical illustration

A. ABSTRACT STYLE
- Opening move: positions the contribution as building on two widely used methods, one sentence
- Structure: new estimator -> relation to existing methods -> robustness claimed "theoretically and empirically" -> asymptotic setting -> conditions for consistency and normality
- Tense pattern: present throughout
- Contribution placement: sentence 1 (what) and sentence 3 (what is proved)
- Length: about 100 words
- Register: technical

B. INTRODUCTION ARCHITECTURE
- Hook type: empirical practice (which methods dominate applied work)
- Opening move: setting first (panel data, non-random policy timing), then the two dominant methods with canonical citations
- Contribution placement: early (paragraph 3)
- Contribution format: prose, "like X ... like Y" parallel construction
- Literature positioning: integrated into intro; positioning by equation contrast
- Roadmap: absent in the converted part
- Intro length: about 7 paragraphs plus 3 displayed equations
- Move sequence: P1 M1-territory (practice and centrality); P2 M1-review (two methods, their typical settings); P3 M2-counter-claim then M3-purpose and M3-findings; P4 M3-method (notation and the estimator as an equation); P5-P6 M3-value (why weights help, with a caveat); P7 M2-gap against the closest alternative, then M3-method (what is added and why)
- Paragraph functions and transitions: P2 to P3 by contrast ("although typical settings differ, assumptions are related"); P4 introduces the estimator as a weighted version of a known regression, P5 and P7 contrast it with the two baselines by showing their equations side by side; benefits are always paired with the condition under which they fail

C. CONTRIBUTION EXPRESSION
- Voice: "we propose", "we establish", "we find"
- Claim strength: hedged comparative ("competitive with (or dominates)")
- Number of contributions: 2-3 (method, theory, empirical performance)

D. LITERATURE REVIEW
- Structure: embedded in intro and in each section where a method is compared
- Position in paper: woven throughout (a later section 6 is referenced)
- Organization: by method family
- Critical engagement: compare-contrast at the level of model assumptions and equations

E. METHOD / MODEL
- Entry point: estimator first as an optimization problem, intuition after
- Notation density: heavy
- Exposition style: estimator, then algorithm box, then application, then simulations, then formal results
- Assumption justification: explicit, with what is testable stated in words

F. RESULTS
- Primary vehicle: tables with standard errors, plus figure explaining weights
- Narrative style: result -> mechanism (why weights matter) -> implication for practice
- Paragraph shape: claim, then table reference, then decomposition by design component ("drop M", "drop F")
- Mechanism emphasis: central (ablation of data-generating components)
- Robustness signaling: main text (several designs in one table)

G. DISCUSSION
- Function: mechanism deepening via controlled ablations
- Scope of claims: close to the simulated settings, with explicit failure cases
- Implications language: practitioner-facing (when to prefer which estimator)
- Limitation acknowledgment: proactive ("nontrivial assumptions")

H. LANGUAGE STYLE
- Voice: active-dominant, "we"
- Sentence length: varied; long sentences for setting, short for claims
- Hedging level: medium; hedges on interpretation ("perhaps less intuitively", "likely overstates"), not on table values
- Transition style: explicit connectives and contrastive pairs
- Mathematical density: heavy

I. WHAT THIS PAPER DOES NOT DO
- Does not claim universal dominance; names the setting where the baseline wins
- Does not give a numbered contribution list
- Does not separate related work into its own early section

J. DISTINCTIVE PATTERNS
- Defines the new estimator by writing the baselines as special cases of the same objective (equations side by side)
- Pairs every advantage with the condition under which it disappears
- Uses a simulation table whose rows remove one model component at a time, so readers see which component drives the gain
- Sentence templates:
  - "Like [method A], our method [property A]; like [method B], it [property B]."
  - "Although [the settings where A and B are used] differ, [the assumptions that justify them] are closely related."
  - "This can bring [n] benefits relative to [baseline]. Intuitively, [benefit 1]. Perhaps less intuitively, [benefit 2]. However, [benefit 2] is not guaranteed: if [condition], [it may get worse]."
  - "If we drop [component], [baseline] performs best; if we drop [other component], [other baseline] does best."

K. CLAIMS AND EVIDENCE CONVENTIONS
- Number reporting: exact values with standard errors in parentheses; simulation results to three decimals
- Statistics reported: bias and RMSE over 1000 replications; standard errors by a named method
- Hedging target: interpretations only
- Causal language: used with an explicit outcome model and assignment assumption
- Data and artifact statement: datasets named; artifact statement not in converted part

L. THREATS AND LIMITATIONS
- Placement: inside the formal section and the introduction, not a separate section (in the converted part)
- Framework: assumption-based (signal to noise, serial correlation, stability of factors)
- Order of items: identification assumptions, then practical checks (pre-period balance), then historical context
- Style: operational (says how each can be assessed)
