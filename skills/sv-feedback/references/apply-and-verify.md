# Apply and verify

## Contents
1. Commit discipline
2. Marker lifecycle
3. Verification procedure
4. After merges and syncs
5. Response table rules

## 1. Commit discipline

- One ID per commit, message `FB-<id>: <what changed, where>`. Group only
  true duplicates. [src: note:n05§6.3] (confirmed)
- No comment fix inside a sync merge, an agent checkpoint, or a commit whose
  subject describes something else. In the evidence project, subjects such as
  "add todo" and "checkpoint before destructive delete" hid a restored result,
  a deleted caveat and two resolved notes. [src: arc:msr:5262231; arc:msr:815305e; note:n05§5.5] (confirmed)
- Checkpoint before any agent-driven destructive edit, as a separate commit.
  [src: note:n08§5#6] (candidate)

## 2. Marker lifecycle

| Situation | Agent may | Agent must not |
|---|---|---|
| Note macro marked `agent_may_resolve: true` | Fix and delete the marker in the same commit | Delete without the fix |
| Any other note | Draft the fix; append `(Done: <what>, <where>; remaining: <what>)` inside the marker | Delete, comment out, or move the marker |
| Note display switch | Leave it as the authors set it | Switch notes off while any note is unresolved |
| Parked block | List it in STATUS with owner | Delete it without a decision |

Evidence: two student-only notes vanished in an agent checkpoint commit;
three notes were commented out instead of resolved; note display was
switched off while a note was open and the senior switched it back 66
minutes later; Done notes worked well, because the next reviewer deleted
exactly those markers. [src: arc:msr:815305e; arc:msr:ac172bd; arc:msr:5776349; arc:msr:0f96193; arc:msr:405bba7; note:n05§5.2] (confirmed)

## 3. Verification procedure

For each ID marked done:

1. Extract the claimed after-text or claimed action.
2. Search it in `git diff <base>..HEAD -- <files>`; for figures check the
   source and the regenerated PDF; for global renames count remaining
   occurrences of the old term in sources and captions.
3. For mechanical replacements compile and compare the rendered text of the
   changed sentences.
4. Check that labels and references still resolve (clean log).
5. Mark `by diff` with the commit, or `pending` with what is missing.

A claim with no matching diff is not done, whatever the report says.
[src: arc:06-revision/REVISION-SUMMARY.md; note:n05§5.5] (confirmed)

## 4. After merges and syncs

Re-run step 3 for all closed IDs after every merge, pull or sync with the
co-edited copy. In the evidence project a stale-base push reverted lowercase
labels, hedges and a figure removal; a sync action overwrote a senior's edits
minutes before the deadline. [src: arc:msr:9809b8c; arc:ol:a610d1d; arc:ol:214cc0c; note:n05§5.3] (confirmed)

## 5. Response table rules

- Decision values: `accept`, `partial: <what was not done and why>`,
  `decline: <reason>`, `superseded by <ID>`.
- Location after change: section name and label, never page numbers.
- Every `decline` and `partial` has a reason a reviewer could read.
- Unfixable requests that need new work become an explicit limitation in the
  threats section, and the response says so. [src: skill:se-paper-refinement] (candidate)
- The table is the base for the rebuttal or response letter; keep quotes short
  and neutral.
