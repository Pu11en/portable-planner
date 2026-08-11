# P-001 — Define the shared inbox contract

- Status: complete
- Depends on: none

## Decision

Define the people, capture-to-decision experience, proof, boundaries, safety, and implementation route for the first useful shared project inbox.

## Viable options

- A. Drew and his AI agents — Recommended; keeps the first version lightweight and useful across devices and agent sessions, but does not support human collaboration yet.
- B. Drew and a small invited team — Enables human collaboration, but adds ownership, permissions, and coordination.
- C. Drew plus outside contributors — Creates a submission funnel, but adds intake quality, privacy, and moderation.

## Recommendation

A — Treat the inbox as a shared workspace between Drew and his AI agents. Use a private Telegram bot as a thin phone-capture adapter and the existing Business Brain `INBOX.md` as the canonical record. Let normal workspace agents perform search and comparison instead of adding another AI service.

## Confirmed decision

Drew delegated all remaining planning choices to the recommended answers.

- Participants: Drew is the only human user; agents with authorized access to the Business Brain are the other participants.
- Capture: any plain-text message or text containing a link in one dedicated private Telegram chat creates one idea. Voice, images, files, and public/group intake wait until a later version.
- Runtime: a small local long-polling worker receives messages while Drew's computer/runtime is online; no hosted 24/7 service is required for version one.
- Source of truth: the root Business Brain `INBOX.md` remains canonical. New captures use a managed section and stable `I-YYYYMMDD-NNN` IDs without rewriting legacy entries.
- Record: preserve the exact original text, source link when present, capture time, Telegram message ID, status, and a short derived title. Enrichment may add a summary or tags later but never replace the original.
- Acknowledgement: say “Saved” only after an atomic write succeeds. On an offline runtime, unauthorized sender, parse conflict, or write failure, do not claim the idea was saved; leave the Telegram message as the recoverable original and give one retry instruction.
- Find: any workspace agent can read or search the Markdown inbox in a later session by ID, words, link, status, or date. Finding is read-only.
- Compare: when asked what deserves attention next, the agent presents no more than three candidates and explains each using current-goal fit, likely value or evidence, and the smallest useful proof.
- Select: the agent recommends one but changes no status until Drew explicitly confirms. Confirmation records one idea as `selected` with the reason and date; it does not edit `NOW.md`, create a project, delete other ideas, or begin work.
- Security: allow only Drew's numeric Telegram user and private chat IDs; store the bot token outside tracked files; avoid logging secrets; fail closed on identity or write uncertainty.
- Operating assumption: the local worker must be running to process queued messages. Setup must state the Telegram account, bot token, local runtime, expected waiting behavior, and failure recovery plainly.
- Proof: use a fixture with at least 20 ideas, then a live phone capture and a fresh agent session. Exact originals must survive; unauthorized input and forced write failure must not create false saves; only the confirmed idea may become selected.

## Evidence

- [Telegram feasibility evidence](../evidence/P-001-telegram-feasibility.md)

## Effects

- The build route is data safety first, then phone capture, agent retrieval, human-confirmed comparison, and a live end-to-end proof.
- The implementation must preserve the workspace rule that `INBOX.md` owns rough ideas and must not silently promote a proposal into active work.
- No decision-changing factual uncertainty remains; provider details are rechecked against the official API during integration.

## Complete when

The participants, capture-to-decision experience, success proof, boundaries, dependencies, safety behavior, and five session-sized execution tickets agree across `PLAN.md`, `PLAN-VIEW.md`, `NEXT.md`, and the execution files.
