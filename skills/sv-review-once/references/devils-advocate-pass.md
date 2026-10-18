# Devil's-advocate pass

## Contents
1. Purpose and boundary
2. Procedure
3. When a counter-argument is CRITICAL
4. Challenge lenses
5. Field lens: empirical software engineering
6. Output block
7. Sources

## 1. Purpose and boundary

The five dimensions check whether the paper is well built. This pass asks
whether its main claims survive a reader who wants them to fail. It only
challenges; fixes go to the author or to `sv-feedback-revise`. It runs
after Steps 1 to 7a so it can use their findings, and it never repeats
them: a typo or a missing citation is not a devil's-advocate finding.

The pass is a restatement of the owner's former reviewer skill, whose
counter-argument mechanism came from a larger third-party reviewer suite.
Only the idea is kept here; the wording is new.

## 2. Procedure

1. List the main claims: each contribution bullet, each research-question
   answer, and every headline number in the abstract and conclusion.
2. For each claim, build the strongest counter-argument from material in
   the paper: its own tables, figures, denominators, residual classes,
   per-group results, threats and limitations. An objection that needs
   facts outside the paper is labelled "external" and kept separate.
3. Ask whether the paper already answers it (quote the line), scopes it in
   threats (quote the threat), or leaves it open.
4. Open objections become findings with the severity rules in section 3.
5. Close with one paragraph (about 150 to 250 words): the single strongest
   case against the paper, written as a reviewer would write it. Then one
   sentence on what the paper does well, so the author can see what to
   protect while fixing.

## 3. When a counter-argument is CRITICAL

Mark a devil's-advocate finding CRITICAL only when at least one holds:

- **Broken foundation.** An assumption the main argument needs is false or
  unsupported by the paper's own data.
- **Broken chain.** The evidence may be sound but the conclusion does not
  follow (an association reported as a cause; a sample result stated for
  the whole population).
- **Data against conclusion.** A number in the paper contradicts the claim
  it is cited for.
- **Better explanation.** A simpler account fits the reported data at least
  as well (a selection effect, one dominant group, a filter that creates
  the pattern) and the paper does not rule it out.

Not CRITICAL: a missing peripheral reference, loose wording in a side
claim, a minor limitation left unstated. Those are MAJOR or MINOR.

## 4. Challenge lenses

Use the lenses that apply; skip the rest without comment.

| Lens | Question |
|---|---|
| Core claim | What is the best case against the main claim, and what is left of the paper if it holds? |
| Evidence selection | Were results that cut against the framing dropped, or only favourable examples shown? (TH-10) |
| Framing bias | Do the research questions or analysis choices steer toward the expected answer? Were analyses planned or exploratory? (IN-09) |
| Logic chain | Is each step from data to conclusion valid, with no hidden assumption? |
| Generality | Does any claim reach beyond the sampled population, sources or groups? (TH-01, TH-02) |
| Alternatives | Which explanations or designs did the authors not consider, and why not? (TH-08, TH-09) |
| So what | If every claim holds, what changes for the reader the paper addresses? |

## 5. Field lens: empirical software engineering

With `field: se`, add these questions from the SE profile:

- Each of the four threat categories (conclusion, construct, internal,
  external): which one would a reviewer attack first, and is the paper's
  answer operational with its numbers? (SE-15)
- Constructs: is closed read as fixed, or calendar time as effort? Are the
  denominators named wherever a rate is cited? (SE-03, SE-04)
- Is the residual class reported as a result, or hidden? (SE-06)
- Does a pooled result hold per group, and does one group drive it? (SE-11)
- Are baselines recent and from a comparable domain? (SE-09)
- Could a reader regenerate the headline numbers from the package? (AR-05)

For other fields, take the questions from that profile's "What reviewers
and advisors care about" and "Rigor and threats" sections. For a theory
paper the main claims are theorems: attack the assumptions and the proof
steps, not the absence of experiments.

## 6. Output block

```
### Devil's-advocate pass
Strongest case against the paper: <150-250 words>
What the paper does well: <one sentence>

| Claim (quoted) | Strongest counter-argument | From (table, figure, line) | Answered where | Severity |
|---|---|---|---|---|

Alternative explanations not ruled out:
1. ...
External objections (need facts outside the paper):
- ...
```

Every row quotes the claim and points to the evidence it uses. Report the
result as MA-05 (and SE-19 for SE) in the sub-checklist table.

## 7. Sources

- Counter-argument as the centrepiece and the CRITICAL criteria: owner's
  former reviewer skill, restated. [src: skill:se-paper-reviewer] (candidate)
- Merge decision and the missing SE lens: [src: note:n02§2; note:n02§10] (candidate)
- Gate item and SE item: [src: arc:01-checklist/checklist.md T14; note:n07§B.5] (candidate)
