# E-001 — Create the Portable Skill Foundation

- Outcome: A locally valid Agent Skill package triggers from natural language and encodes the confirmed question-finder contract plus Drew's substantiated qualification profile.
- Depends on: P-001

## Context

- [Confirmed product and access contract](../decisions/P-001-define-finder-contract.md)
- [YouTube access and provenance evidence](../evidence/P-001-evidence.md)

## In scope

- Create the final project-local skill directory with `SKILL.md` and the minimum necessary `references/`, `fixtures/`, and validation helpers.
- Write natural-language triggers for requests that supply channel names, handles, or URLs and ask for short-video questions.
- Encode the end-to-end flow, capability checks, read-only boundary, shortfall behavior, and output contract without requiring command syntax.
- Create a maintainable Drew qualification reference using only substantiated workspace/public sources; separate confirmed expertise from exclusions and unknowns.
- Route detailed logic to references so `SKILL.md` stays concise and portable.

## Out of scope

- Channel lookup, video discovery, comment retrieval, scoring implementation, live YouTube access, installation into another harness, and any publishing/recording behavior.

## Constraints

- No account, API key, paid service, database, server, scheduler, or background process.
- Do not claim credentials or expertise that a canonical source does not substantiate.
- The skill must explicitly prohibit replies, posts, engagement actions, media/transcript downloads, recording, and publishing.

## Proof

- The official/local skill validator accepts the package structure and frontmatter.
- A contract checklist maps every numbered P-001 behavior to one authoritative instruction/reference location with no contradiction.
- Clean-context trigger examples work from ordinary phrasing without slash commands or internal workflow vocabulary.

## If blocked or disproven

- Return to planning only if the target Agent Skill format cannot express a confirmed behavior; otherwise fix package structure or wording in this ticket.

## Human review

- Drew reviews the qualification profile for factual overreach before live acceptance; no new product preference is requested.

## Next eligible ticket

- E-002 — Resolve and lock the supplied channels.
