# Replication artifact

## Contents
1. What goes in
2. Build from the manifest
3. Clean-clone run
4. Anonymize
5. Anonymous mirror
6. Timing and the statements about the artifact

## 1. What goes in

Everything the paper says is released, and nothing more:

- code that regenerates every printed number (`numbers.json`) and every
  table and figure, with one entry command (`make all` or `run_all.sh`);
- data, or a download script plus `data/MANIFEST.tsv` for data on a host;
- codebook, rule file, reference labels (raw independent sets if an
  inter-rater value is printed), prompts and their version log, model
  outputs;
- a README: what each folder holds, how to run, expected outputs and run
  time, which script prints which table, and the licence.

Analysis code moves into the artifact the day it is written. In the evidence
project, scripts written while revising findings were missing from the
package at the deadline, and its availability statement promised scripts
that recompute every number.
[src: arc:chat:group@2026-10-03T20:20; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; note:n08§5#16] (confirmed)

## 2. Build from the manifest

Keep an artifact manifest (`artifact/MANIFEST.txt`, one source path per
line, or a section of `data/MANIFEST.tsv`) and a build script that copies
exactly those paths into a fresh directory. Never copy the research repo
wholesale: it carries notes, private material, history and local paths.
Copy files, not git history; start the artifact repo with a fresh `git init`
and a neutral committer identity.

## 3. Clean-clone run

1. Clone the artifact into a new directory on a machine or container without
   the research environment.
2. Follow the README alone: install, fetch data, run the entry command.
3. Run `numbers_check.py` with the regenerated `numbers.json` against the
   paper source. Zero mismatches; every printed number is either produced or
   explicitly listed in the README as not reproducible with the reason.
4. Record the run (command, commit, date, summary) in `docs/log/` and the
   result in STATUS.
[src: arc:RP-05@v2; note:n08§5#17] (candidate)

## 4. Anonymize

For double-anonymous venues. Search everything a reviewer can open:

```bash
python scripts/anon_grep.py artifact/ --terms-file private/identity-terms.txt \
       --allow "<mirror domain>" --git-log
```

The terms file (kept private, never in the artifact) lists author names in
every spelling and script, affiliations, lab names, handles, personal
domains, and the venue name if the artifact must stay venue-neutral.

The script reports: user terms, e-mail addresses, home paths
(`/Users/<name>/`), account URLs (`github.com/<account>`,
`<account>.github.io`), author fields in LICENSE, CITATION.cff and package
metadata, PDF author metadata, rendered HTML pages, and git config and
history. Check by hand, and note the check: the hosting account name, the
repository description and topics, image EXIF data.

Fix by removing, not by obscuring: licence holder becomes "Anonymous
authors" for the review copy; paths become relative; account URLs are
dropped. In the evidence project a project web page in the artifact named
all authors and their lab; a read-only check predicted it a day before the
deadline, and it was removed only after the deadline.
[src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; arc:chat:group@2026-10-06T05:09; note:n08§5#12] (confirmed)

Prefer a complete README to a rendered project page; add `index.html` and
page sources to `.gitignore` in the review copy.
[src: arc:chat:group@2026-10-06T05:09; note:n08§5#13] (confirmed)

## 5. Anonymous mirror

1. Keep the source artifact repo private, under an account that is not
   linked from anything a reviewer sees.
2. Create the anonymous mirror (for example an anonymizing mirror service)
   with its own term list, and link only the mirror in the PDF.
   [src: arc:chat:group@2026-10-02T00:45; note:n08§5#14] (confirmed)
3. After every change to the artifact, including after the deadline and
   until reviews end: refresh the mirror, then re-run the search on the
   mirrored copy (download it, run `anon_grep.py`). A stale mirror hides a
   leak in the source; a refresh can publish one.
   [src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; note:n08§2] (confirmed)
4. The artifact name and suggested citation do not name the venue.

## 6. Timing and the statements about the artifact

- The linked package holds code and data from the first day after the
  deadline; the README guide can follow.
  [src: arc:chat:group@2026-10-03T23:16; note:n08§5#15] (confirmed)
- The data availability statement says what is released, why anything is
  not, and follows the reporting rule for numbers (which runs print).
- A project page, if one exists after review, matches the final paper and is
  updated in the same pass.
