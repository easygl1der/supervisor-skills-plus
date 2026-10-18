# Phase 2: manuscript revision

## Contents
1. Inputs and order
2. Round 1: diagnosis
3. Round 2: revision
4. Round 3: revision log
5. Outputs and rule candidates

Phase 2 loads only `dynamic_writing_skill.md` and the manuscript. Do not
re-read corpus papers or style cards.

## 1. Inputs and order

- Manuscript: Markdown, text, LaTeX, or a PDF converted first (see the
  conversion step in SKILL.md).
- Sections: ask which ones. "Full paper" means every section present, in
  the order Abstract, Introduction, Related work / Literature review,
  Methods / Model, Results, Discussion, Threats, Conclusion.
- One section at a time: diagnose, revise and log a section completely
  before starting the next.

## 2. Round 1: diagnosis

For each paragraph record:

- **Problem type**: STYLE | JOURNAL-MISMATCH | AI-TASTE | LOGIC
- **Severity**: HIGH (blocks acceptance) | MED (weakens fit) | LOW (minor)
- **Specific issue**: which rule (`DS-nn`, P5 item, or research-core rule)
  the paragraph violates and how
- **Venue match score**: 1 to 5 (1 very unlike the target venue, 5 well
  matched)

Output the diagnosis before writing any revision. LOGIC problems that need
new content (a missing argument, an unsupported claim) are reported, not
fixed: hand them to `sv-write-section` or the authors.

## 3. Round 2: revision

Apply P1 to P5 from the dynamic skill:

- P2 beats P3 and P4 when they conflict; log the conflict.
- P3 beats P4 when relevant and not contradicted by P2.
- Never add new content; only rewrite what is there.
- Preserve every P1 element verbatim.
- Do not flip a decision recorded in `docs/adr/` or the term table.

Output form:

- Markdown or text input: the full revised section as Markdown.
- LaTeX in a git repository: with the user's consent, edit the section file
  in place with a minimal diff (no reflowing of untouched lines), then show
  the diff. Without consent, output the revised section as a separate file.

## 4. Round 3: revision log

One entry per changed paragraph:

```
---
Paragraph: <N>
Severity: HIGH | MED | LOW
Problem types: STYLE | JOURNAL-MISMATCH | AI-TASTE | LOGIC
Issues: <what was wrong>
Rules applied:
  - <DS-nn or rule name>: source <target venue | secondary corpus | exemplar | static base | field profile | cleanup>
Conflict resolved: yes | no (if yes, which rule won and why)
Preserved verbatim: <citations, equations, notation, numbers kept>
Rule candidate: YES | NO (if YES, one actionable sentence and the scope you expect: venue | field | general)
---
```

Section summary at the end of each log:

- Venue match score before and after (averages)
- Key patterns improved
- Remaining issues not revised, with reasons

## 5. Outputs and rule candidates

```
<style.dynamic_skill or manuscript folder>/<manuscript>_revised/
  dynamic_writing_skill.md     reviewed temporary skill for this manuscript
  style_profile.md             corpus-derived profile
  <section>_revised.md         one per revised section (if not edited in place)
  <section>_revision_log.md    one per section
  revision_summary.md          all rule candidates in one table
```

`revision_summary.md`:

```
| Section | Paragraph | Rule candidate | Expected scope | Evidence (single / pattern) | Supporting DS rule or exemplars |
|---|---|---|---|---|---|
```

Rule candidates are inputs for `sv-supervisor-harvest`, which dedupes them against
research-core and proposes where they go. They are never written into
research-core by this phase.

Close with: sections revised, number of rule candidates, output path, and a
reminder to transfer Markdown revisions into the LaTeX or Word source when
they were not edited in place.
