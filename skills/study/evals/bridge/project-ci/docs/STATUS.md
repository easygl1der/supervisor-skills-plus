# STATUS (fictional eval project)

## Research questions
- RQ1: Does adopting a hosted CI tool reduce the time to fix bugs in a repository?

## Design so far
- Unit: open-source repositories; panel by month; outcome: median time from bug-labelled issue opened to closed, per repository-month.
- Treatment: the month the repository first adds the CI tool's config file. Adoption months differ across repositories (staggered).
- A few treated repositories with clean adoption dates; a much larger pool of never-adopting repositories (exact counts not frozen yet).
- Current method: two-way fixed-effects DID with a single post indicator.

## Blockers
- Event-study pre-period coefficients drift before adoption (parallel trends doubtful for the full control pool).
- With few treated repositories, cluster-robust standard errors are unreliable.

## Decisions
- No ADRs yet.
