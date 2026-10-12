# Research integrity

These rules protect the claims a paper makes about its own data. They come
from failures in the evidence project and from venue policies that list
hallucinated results and undisclosed AI use as desk-reject grounds.
[src: arc:10-requirements/venue/fse-2027-requirements.md]

1. **Agreement numbers need raw label sets.** Every inter-rater or
   model-versus-reference agreement value has the independent label sets and
   a script that recomputes it, kept with the data. If the label sets do not
   exist, rewrite the method to describe what was done and drop the number.
   In the evidence project a human-agreement value replaced a sentence that
   said no human agreement was reported, and no computation record exists.
   [src: arc:msr:393f596; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B1; note:n04§1.6; note:n06§0] (confirmed)
2. **Name each agreement value.** Say which comparison it is (human with
   human, model with reference, reporting bar); never merge them into one
   headline. [src: arc:10-requirements/DECISION-HINTS.md U1] (candidate)
3. **Freeze the evaluation reference before looking at model output.** If the
   reference is corrected after seeing model output, log every change, report
   results before and after, and disclose it. [src: arc:11-mining-github-issue-audit/tree/docs/notes/gold-review/overlay-high14-review.md; note:n08§5#20] (confirmed)
4. **Set acceptance bars before the run** and enforce them in the run script.
   [src: note:n08§5#21] (confirmed)
5. **Disclose AI use in the method**: model, version, settings, prompts, and
   any AI help in building reference data or analysis code that conclusions
   rely on. [src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G9] (confirmed)
6. **Every printed number is traceable** to a script, its input data version
   and a code commit. [src: note:n08§5#17] (confirmed)
7. **Numbers in figures follow the same rule.** A value copied from a sketch
   or an image is not data. [src: note:n07§A.1] (confirmed)
8. **Do not drop results that contradict the framing.** [src: arc:CF-18@v2] (candidate)
9. **Write the reporting rule once** (which values print, which run, where),
   and apply it everywhere including the data availability statement.
   [src: arc:msr:9c69675; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H1] (candidate)
