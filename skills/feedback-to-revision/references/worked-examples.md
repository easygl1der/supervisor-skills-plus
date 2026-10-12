# Worked examples

Anonymized from the evidence project (`note:n05§4`). Domain words and counts
are replaced with placeholders.

## Contents
1. Terminology sweep through an inline note
2. A table labelled as a figure
3. A table that should be two sentences
4. Procedural opener rewritten
5. A fast fix that broke a name
6. Counter-example: a change report that never landed

## 1. Terminology sweep through an inline note

Comment (inline, senior co-author A): a note in a subsection title asking to
call the "snapshot" a "dataset".

Change (by senior co-author B, about four hours later):

```
-\subsection{Issue Snapshot and Data Cleaning \todo{do not call it snapshot, call it dataset}}
+\subsection{Issue Collection}
-We analyze a frozen snapshot of the issues ..., taken on <date>, rather than the live API, ...
+We collect the issues ... on <date> and analyze this copy rather than the live API, ...
```

The student re-inserted the note with a Done text listing the remaining
places (threats, data availability); the senior then deleted it.
Lesson: a terminology comment is a sweep, and the Done note listing what
remains is what made it closable. [src: arc:msr:9ef4a07; arc:msr:405bba7; arc:msr:b5c0045]

## 2. A table labelled as a figure

Comment (inline): "It is a table! why label it as a figure? Please format it
as a normal table."

Change (student, next day): the `figure*` holding a tabular and a chart was
split; the tabular became a `table` with its caption above; the chart moved
to the next section.
Lesson: the float type follows the content; split mixed panels.
[src: arc:msr:0f96193; arc:msr:405bba7]

## 3. A table that should be two sentences

Comment (PDF annotation, senior co-author B): the sample allocation table
"is not worth a table; two sentences, saves space".

Change (three days later, during a section rewrite): two sentences stating
the floors and the resulting total replaced the seven-row table.
Lesson: write the replacement sentences in the same commit that deletes the
table, otherwise the content is missing in between; page-budget comments
tend to wait for a rewrite. [src: arc:msr:9c69675; arc:msr:7c705c9]

## 4. Procedural opener rewritten

Comment (written file, senior co-author A): section openings are too
procedural; open with the substantive point; a model sentence was given.

Change:
```
-RQ1 asks which issue types ... are prevalent, because the plan made specific predictions ...
-A good outcome for the plan would be ...
+Before reasoning about defects, we need to know whether these trackers mostly contain defects at all.
+If some repositories are dominated by feature requests ..., any defect census built by
+repository-level sampling will be biased.
```
Lesson: adopting a reviewer's model sentence verbatim is fast but brittle;
this one was rewritten again later. Adapt the move, not the words.
[src: arc:ol:01fcd0f; arc:@senior-a-comments:141-157]

## 5. A fast fix that broke a name

Comment (group chat, about 75 minutes before the deadline): no labels or
macros in the abstract, plain text is safer for the submission form.

Change: macros were expanded by hand; one name containing a special character
lost it. Fixed nine minutes later.
Lesson: after a mechanical replacement, compare the rendered text token by
token. [src: arc:msr:4af1aff; arc:msr:10e2e5f; arc:chat:group@2026-10-03T18:43]

## 6. Counter-example: a change report that never landed

An agent-written revision summary listed all eleven written comments as
addressed, with before and after LaTeX. The after-strings appear only in the
summary file; the section committed alongside still had the before-text.
Lesson: a resolution claim is evidence of intent. Verify each claimed
after-string in the diff before marking a comment resolved.
[src: arc:06-revision/REVISION-SUMMARY.md; arc:msr:815305e]
