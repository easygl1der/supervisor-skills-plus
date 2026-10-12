# Submission-day runbook

## Contents
1. How to use this runbook
2. One day before (T minus 24 h or earlier)
3. The last 24 hours
4. The last hour
5. After the deadline
6. Runbook record template
7. Sources

## 1. How to use this runbook

Copy section 6 into `docs/STATUS.md` (or the day's log) and mark each step
done, skipped with a reason, or open. Times are relative to the official
deadline converted to every author's time zone (VS-01). The steps exist
because each one failed or nearly failed in the evidence project; the
sources are in section 7 and inline.

## 2. One day before (T minus 24 h or earlier)

1. **Read-only full check.** Run `pre-submission-reviewer` against a named
   commit and its PDF; every Blocker becomes a TODO with an owner the same
   day (MA-01). The evidence project's final check predicted the artifact
   identity leak; nobody owned that Blocker, and it was fixed only after
   the deadline. [src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B2; note:n08§5#37] (confirmed)
2. **Form metadata entered.** Authors, conflicts of interest with the
   program committee, topics and the corresponding author go into the
   submission system now, not in the last hours; the co-author who knows
   the institutional ties enters the conflicts (VS-09). In the evidence
   project the conflict form was finished about two and a half hours
   before the deadline, by a senior co-author. [src: arc:chat:group@2026-10-01T21:05; arc:chat:group@2026-10-03T17:28; note:n08§5#31] (confirmed)
3. **Plain-text abstract prepared.** Write the form abstract as plain text
   with no macros, labels or markup and keep it in the repository (VS-10).
   [src: arc:chat:group@2026-10-03T18:40; arc:chat:group@2026-10-03T18:43; note:n08§5#30] (confirmed)
4. **Venue facts re-read** from the dated copy of the official call: page
   limit, template options, required sections, anonymity rules (VS-01).
   A deadline heard in a meeting is not a source. [src: note:n08§5#32] (candidate)
5. **Anonymous mirror refreshed and searched.** Refresh the mirror, then run
   the identity search on the mirrored copy: README, licence, any rendered
   page, repository description, account name, metadata (DB-04, DB-06).
   Prefer a complete README over a project web page (DB-05). The PDF links
   only the mirror (DB-03). [src: arc:chat:group@2026-10-02T00:45; arc:chat:group@2026-10-06T05:09; note:n08§5#12; note:n08§5#13; note:n08§5#14] (confirmed)

## 3. The last 24 hours

1. **One writable source, named.** State in chat and in `docs/STATUS.md`
   which copy is the source of truth (git or the online editor) until the
   upload. Switch off or pause any automatic mirror into the online editor.
   [src: note:n08§5#1; note:n08§5#2] (confirmed)
2. **One editor at a time.** Pass the pen explicitly in chat ("I have the
   pen for Sections 4 and 5 until 18:00"; "pen released"). In the evidence
   project, twenty minutes before the deadline, a sync bot pushed one
   author's version ten seconds after a senior co-author had saved edits to
   seven files in the online editor, and the push reverted all of them.
   [src: arc:ol:a610d1d; arc:ol:214cc0c; arc:chat:group@2026-10-03T19:41; arc:chat:group@2026-10-03T19:42; note:n08§5#3; note:n08§1.3] (confirmed)
3. **No merge storms.** Merges, sync commits and content fixes do not
   interleave; batch fixes per editor turn and re-read the diffstat after
   every merge. [src: note:n08§1.3; note:n08§5#5] (candidate)
4. **Re-run the cheap checks after each batch:** page count on the compiled
   PDF (VS-04), template and fonts (VS-05), compile log (VS-08), no
   reviewer-visible markers (MA-02). Late edits re-introduced removed font
   shrinking in the evidence project. [src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G3; note:n08§5#10] (confirmed)

## 4. The last hour

1. **Upload a complete PDF early, then replace it.** Upload a full,
   submittable PDF well before the deadline (the evidence project's seniors
   asked for the first upload about ten minutes before, then again at five);
   later versions replace it (VS-11). The submission site went down at the
   deadline minute. When the form shows errors, the PDF being right is what
   matters most. [src: arc:chat:group@2026-10-03T19:45; arc:chat:group@2026-10-03T19:59; note:n08§5#4; note:n08§3] (confirmed)
2. **Paste the prepared plain-text abstract** and check the form preview.
3. **Record what was uploaded:** the commit or online-editor version, the
   PDF file hash, the page count and the upload time. The evidence project
   kept none of these, so its final page count is unknown.
   [src: note:n03§5; note:n08§3] (candidate)

## 5. After the deadline

1. **Sync the submitted version back and tag it.** Bring the submitted text
   into the repository the team treats as the record, and tag the commit
   (for example `submitted-<venue>-<year>`). Record any source-of-truth
   switch in an ADR or `docs/STATUS.md`. In the evidence project the paper
   repository stopped at the last push before the deadline while the
   online editor kept receiving edits, including a new title, when the
   site reopened; the archive now holds two diverging lines and no tagged
   submitted version. [src: arc:msr:87bf139; arc:ol:ba3f1ee; note:n08§5#40; note:n08§1.2] (candidate)
2. **Artifact not empty on day one.** Code and data are in the package the
   day after the deadline; the README guide may follow (AR-07).
   [src: arc:chat:group@2026-10-03T23:16; note:n08§5#15] (confirmed)
3. **Keep the mirror clean until reviews end.** Every artifact change is
   followed by a mirror refresh and a new identity search (DB-06). In the
   evidence project the predicted leak was removed three days after the
   deadline, before reviewers opened the artifact.
   [src: arc:chat:group@2026-10-06T05:09; note:n07§B.3; note:n08§2.7] (confirmed)
4. **If the site reopens or the deadline moves**, the same rules hold: one
   editor at a time, replace the PDF, re-run the cheap checks.
   [src: note:n08§3] (candidate)
5. **Open items to TODO.** Anything skipped today goes to `docs/TODO.md`
   with an owner; lessons go to `lessons-harvest` later.

## 6. Runbook record template

```
## Submission runbook: <venue> <year>, deadline <ISO time, source>
| Step | Status (done / skipped: reason / open) | Evidence (commit, time, hash, output) |
|---|---|---|
| Read-only check, Blockers owned (MA-01) | | |
| Form metadata and conflicts (VS-09) | | |
| Plain-text abstract (VS-10) | | |
| Venue facts re-read (VS-01) | | |
| Mirror refreshed and searched (DB-04, DB-06) | | |
| Source of truth named, mirrors paused | | |
| Pen holder log | | |
| Cheap checks after last batch (VS-04, VS-05, VS-08, MA-02) | | |
| First complete upload (VS-11) | | |
| Final upload: version, hash, pages, time | | |
| Submitted version synced and tagged | | |
| Artifact non-empty day one (AR-07) | | |
```

## 7. Sources

Rule sources are inline. Background: venue hardening table and candidate
lessons in `note:n08§3` and `note:n08§5`; status at submission in
`note:n07§B.3`.
