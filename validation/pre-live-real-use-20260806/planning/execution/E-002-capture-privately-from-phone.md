# E-002 — Capture privately from the phone

- Outcome: Drew can send text or a link in one private Telegram chat and receive a truthful saved-or-failed reply tied to one inbox ID.
- Depends on: P-001, E-001

## Context

- [Confirmed product contract](../decisions/P-001-define-shared-inbox-contract.md)
- [Telegram feasibility evidence](../evidence/P-001-telegram-feasibility.md)

## In scope

- Recheck the official Bot API methods, then implement one local long-polling worker for private text messages.
- Allowlist Drew's numeric user and private chat IDs before any write.
- Accept plain text and text containing links; reject unsupported media with a clear version-one boundary.
- Derive a short title without replacing the original, call the safe inbox core, de-duplicate by Telegram message ID, and acknowledge only the committed result.
- Add untracked environment configuration, startup/stop instructions, health output without secrets, and offline/retry behavior.

## Out of scope

- Webhooks, cloud hosting, group chats, multiple users, voice transcription, images, files, automatic AI calls, and 24/7 guarantees.

## Constraints

- Never store, print, commit, or echo the bot token.
- Unauthorized senders and uncertain writes fail closed and must never receive a “Saved” acknowledgement.

## Proof

- Tests cover authorized text, URL, duplicate update, unauthorized sender, unsupported media, offline API, and forced inbox failure.
- Two real authorized messages create exactly two IDs; replay creates no duplicates.
- Unauthorized and forced-failure tests create no record and return no false success.

## If blocked or disproven

- Keep E-001 intact. Return to planning only if the official API no longer supports private messages, local long polling, or acknowledgement; otherwise fix the adapter within this ticket.

## Human review

- Drew creates or chooses the private bot, supplies credentials outside tracked files, and confirms the phone capture wording feels fast enough.

## Next eligible ticket

- E-003 — Find ideas from any agent session.
