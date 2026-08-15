# Beta-6 exact-delegation release-candidate test

Tested: 2026-08-15
Candidate: `0.1.0-beta.6`
Change source: Drew's exact bare-key and option-`B` clarification

## Method

The unchanged candidate ran through two independent read-only forward tests, an
affected rerun after one state-enum ambiguity was corrected, a fresh natural
Codex invocation through the locally installed beta-6 plugin, package validators,
an isolated ZCode install, and repository audits. These objective checks do not
replace Drew's fresh human run.

## Positive shortcut case

Starting state: three separate complete replies—`A`, `a`, and `  A  `—selected
the displayed recommendation. Canonical state recorded streak `3` and shortcut
`ready`. The next real reversible question was event format, whose ordinary
routes were recommended `A`, ordinary `B`, and ordinary `C`.

Raw user-facing output:

> Planning: Event plan
> Now: Choose the event format
> Later: Settle the remaining preferences
>
> Picture guests arriving throughout the afternoon: should they join a guided
> block, wander freely, or gather once?
>
> A. Guided open-house blocks — Recommended; structured, while allowing
> flexible arrival times.
> B. Use my recommendations for every remaining reversible decision — I’ll
> answer this and the rest, then stop for protected gates.
> C. Free-flow drop-in — Most flexible, but with less shared structure.
> D. One scheduled presentation — One clear focal moment, but the least arrival
> flexibility.
>
> Or give a different answer. Reply A, B, C, or D.

Result: pass. The real question remained intact, `A` remained its recommendation,
`B` was the shortcut, ordinary routes shifted consecutively, and no separate
delegation question appeared.

## Reset and boundary matrix

| Case | Expected durable result | Observed result |
| --- | --- | --- |
| Streak `1`; reply `A because that sounds right` | Resolve ordinary A, reset to `0 / not ready`, no shortcut | Pass |
| Streak `2`; reply `A.` | Resolve ordinary A, punctuation resets to `0 / not ready` | Pass |
| Streak `2`; bare ordinary `B` | Resolve non-recommended B, reset to `0 / not ready` | Pass |
| Streak `3 / ready`; only final approval remains | Reset to `0 / not ready`, create no meta-question, proceed to approval | Pass after targeted wording revision and rerun |
| Streak `3 / ready`; six ordinary routes A–F | Insert B and relabel all ordinary routes as A, C–G; emit no H and drop nothing | Pass |
| Shortcut offered; bare `B`; two reversible choices remain | Record explicit delegation, apply current A, synthesize both, stop at final approval | Pass |
| Chat memory empty; saved ticket says `3 / ready` | Canonical state controls; next real reversible question inserts B | Pass |

The initial boundary review found that the never-offered shortcut's enum was not
explicit when final approval followed streak three. The candidate was revised to
require `0 / not ready`; the affected final-approval and accepted-`B` cases then
passed on reread.

## Choice ceiling

Two or three choices remain the default. The insertion algorithm permits
consecutive `A.` through `G.` only. When six ordinary routes exist, inserting the
shortcut produces exactly seven choices without loss. If seven ordinary routes
exist, overlapping or least-consequential ordinary routes are combined or
omitted while preserving the recommendation, shortcut, meaningful tradeoffs,
and custom path. `H.` is prohibited.

## Fresh natural invocation

The exact candidate was installed locally as
`portable-planner@portable-planner 0.1.0-beta.6`. A fresh empty temporary project
received only the ranch-products open-house request from
[the human runbook](BETA6-HUMAN-TEST.md).

The session naturally selected Portable Planner, created only the minimum
canonical `planning/` artifacts, recorded interaction state as `0 / not ready`,
preserved all five user-owned preferences and the planning/build boundary, and
asked one recommendation-first `A/B/C` audience question. No skill command was
present in the request.

The Codex catalog again initially pointed one directory above the installed
skill. The agent located the installed canonical copy and continued. This known
host-path limitation remains recorded rather than causing a second skill copy.

## Package and portability checks

- Skill Creator quick validation: pass.
- Plugin Creator validation: pass.
- Active root, Claude, Codex, and ZCode versions all equal
  `0.1.0-beta.6`.
- JSON parsing and current-product Markdown links: pass.
- `git diff --check`: pass.
- Installer compilation and isolated ZCode install: pass.
- Isolated ZCode plugin bytes equal the candidate source: pass.
- Secret-pattern scan outside historical validation evidence: pass.
- Canonical skill remains 112 lines; no second skill, state tree, service,
  renderer, database, MCP server, or domain pack was added.

## Result

C-02, C-12, and C-13 pass the affected objective beta-6 rerun. The candidate is
ready for an honest public-preview prerelease and the exact fresh human run in
[BETA6-HUMAN-TEST.md](BETA6-HUMAN-TEST.md). Other previously open human checks
remain open; beta 6 is not production-proven.
