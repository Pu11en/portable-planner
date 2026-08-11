# P-001 — Define the Finder Contract and Route

- Status: complete
- Depends on: none

## Decision

Settle the complete product contract and execution route for a portable skill that turns comments from Drew's chosen AI YouTube channels into credible short-video question opportunities. This controls source fidelity, qualification, quality, safety, portability, and the final report.

## Viable options

- Not applicable — Drew confirmed the product decisions; ordinary mechanics were synthesized and factual access choices were researched directly.

## Recommendation

Use a conservative, read-only, public-access-first workflow with a strict allowed-channel lock, bounded recent-first review, a project-local Drew qualification profile, hard rejection gates before scoring, transparent provenance, and a graceful shortfall rather than padding.

## Confirmed decision

The build will implement this contract:

1. **Invocation and input.** Drew speaks naturally and supplies channel display names, handles, or URLs. No command syntax is required. The skill resolves each input to a canonical channel URL/handle and channel ID when visible, keeps an immutable allowed-channel set for the run, and never searches or returns another channel. Display names are not assumed unique. If one name cannot be resolved unambiguously, the skill pauses only for that channel and asks for its handle or URL rather than guessing.
2. **Drew qualification.** A small project-local reference records only substantiated areas Drew can answer from experience: beginner-friendly AI workplaces and agents, agentic building, turning ideas into working products, practical use of existing GitHub projects, and the documented course-building process. The profile may be extended only from a confirmed source. The skill rejects requests for licensed medical, legal, regulated financial, clinical, or other credentials the profile does not establish, and rejects specialist claims it cannot tie to that profile.
3. **Video discovery.** Discovery is relevant to that qualification profile and limited to the locked channels. It begins with recent uploads and rotates across channels before going deeper. It may add an older video only when its topic fit is exceptional. Every candidate is verified against the canonical channel identity before comment review. A run uses a bounded, human-scale inspection budget documented in the skill; it never bulk-crawls a channel, downloads media, or uses transcripts.
4. **Comment review.** On eligible public video pages, the skill reviews public comments recent-first and may inspect top comments or replies when they contain stronger questions. It records exact visible comment text, displayed age/date, video title, direct video URL, canonical channel identity, and the timestamp-generated highlighted-comment URL when YouTube exposes one. It does not collect commenter profiles or unrelated personal data.
5. **Hard rejection gates.** Reject spam or promotion, vague praise, statements with no answerable question, trolling or abuse, copied/near-duplicate questions, engagement bait, requests unrelated to the video/Drew's scope, questions needing unsubstantiated credentials, and questions too broad or context-free for a useful short answer.
6. **Selection.** Eligible candidates are compared on specificity, Drew-fit, practical audience value, distinctness, and whether Drew can answer usefully in roughly 30–90 seconds. Recency is a preference and tie-breaker, not an absolute gate. An older question survives only when its substantive score clearly exceeds the recent alternatives. Semantic duplicates collapse to the single strongest sourced version.
7. **Output.** Continue bounded review until five qualifying distinct questions are found or the documented source/access limit is reached. Return the five strongest when available. Never weaken the gates to manufacture five; if fewer survive, say how many qualified and why the run stopped. Each result contains channel, video title and direct link, exact comment, direct highlighted-comment link when available (otherwise an explicit unavailable note), why it is worth answering, and a brief high/medium/low confidence note tied to source clarity and Drew-fit. A compact coverage note states the allowed channels resolved and any inaccessible/disabled comments.
8. **Human handoff.** Drew manually opens one result and records his answer. The skill does not reply, post, like, subscribe, download video/audio/transcripts, record, publish, schedule, or run in the background.
9. **Access and compliance.** The no-account/no-paid-service core uses only public information exposed through the harness's compliant browsing/search capabilities. It does not scrape, evade controls, defeat rate limits, or emulate an unofficial API. If access is blocked, comments are disabled, a sign-in wall appears, or the harness lacks a permitted reading path, it records the limitation and returns a shortfall instead of bypassing it. The official YouTube Data API is not a core dependency because it requires a Google account/project and credentials.
10. **Portability.** The deliverable is one Agent Skill package containing `SKILL.md` plus only the references, fixtures, and validation helpers needed for this workflow. State is per run; there is no database or external service. The package validates locally and explains capability/failure behavior in plain language.

## Evidence

- [P-001 evidence](../evidence/P-001-evidence.md)

## Effects

- Creates an eight-ticket execution route from package foundation through live acceptance.
- Makes source provenance, channel locking, qualification, and read-only behavior cross-cutting acceptance requirements.
- Excludes API credentials, automated scraping, media/transcript download, accounts, paid providers, persistence, and publishing from the core.
- Makes a disclosed result shortfall valid when quality or access prevents five; fabricated or padded results are always a failure.

## Complete when

The destination, input, sourcing route, qualification rule, rejection gates, ranking behavior, output fields, access failures, exclusions, portability shape, evidence, and dependency-ordered execution tickets agree across `PLAN.md`, `PLAN-VIEW.md`, and every `E-*` ticket, with no unresolved product choice left for implementation.
