# ADR 0014: One question at a time; question tool when the environment has one

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner (SPEC D7, open question 7), Claude Code (wording per environment)

## Context
The SPEC replaced an upfront placement test with a short multiple-choice
question when a prerequisite has no vault record (D7), and left open how to
ask it in each environment. Long message chains with several questions at once
lose answers.

## Options considered
1. A placement test battery at the start: rejected in D7.
2. Plain text in every environment: works everywhere, clumsy where a picker exists.
3. One question per message; a question tool (AskUserQuestion-like) when
   available, lettered plain-text options otherwise.

## Decision
Option 3. `skills/sv-study/SKILL.md` §1: one short multiple-choice question per
missing prerequisite (not studied / rusty / can use / can explain, plus where
learned), using a question tool when present. `references/protocol.md` §3:
one question per message, never two at the end. `references/learner-profile.md`
says to use the question tool in Claude Code when available and plain options
elsewhere. Questions get fewer as the vault fills.

## Consequences
- Behaviour is the same across tools; only the input widget differs.

## Do not
- Do not open with a test battery. Do not end a message with two questions.

## Sources
`skills/sv-study/SKILL.md` (defaults, §1), `skills/sv-study/references/protocol.md` §3,
`skills/sv-study/references/learner-profile.md` (environments), SPEC D7 and open question 7.
