# Plan: Shared project inbox

**Status:** awaiting approval

## Destination

Drew can send a text idea or link to one private Telegram chat, have it safely recorded in the Business Brain `INBOX.md`, and later use any workspace agent to find, compare, and explicitly select the idea that deserves attention next.

## Success

- In one live pilot, Drew captures text and a link from his phone, a fresh agent session retrieves the exact originals from at least 20 ideas, explains a three-idea shortlist, and records only Drew's confirmed selection without losing or changing any other content.
- Unauthorized messages, offline runtime, and failed writes never produce a false “saved” confirmation or expose the bot token.

## Boundaries

- In: one-user private Telegram capture, text and links, the existing Markdown inbox, read-only finding, agent-assisted comparison, and explicit selection.
- Out: teams, public submissions, voice or media transcription, hosted 24/7 service, automatic project creation, automatic `NOW.md` changes, deletion, reminders, and building during planning.

## Map

`1/1`

- ✓ [P-001 — Define the shared inbox contract](decisions/P-001-define-shared-inbox-contract.md) — depends on: none

## Confirmed decisions

- [P-001](decisions/P-001-define-shared-inbox-contract.md): Drew delegated the remaining choices; use one private Telegram capture channel for Drew and his agents, keep `INBOX.md` canonical, preserve raw input, fail closed, and require Drew's confirmation before recording a selected idea.

## Execution

- [E-001 — Protect and structure the inbox](execution/E-001-protect-and-structure-inbox.md)
- [E-002 — Capture privately from the phone](execution/E-002-capture-privately-from-phone.md)
- [E-003 — Find ideas from any agent session](execution/E-003-find-ideas-from-agents.md)
- [E-004 — Compare and confirm the next idea](execution/E-004-compare-and-confirm-next-idea.md)
- [E-005 — Prove the complete live flow](execution/E-005-prove-complete-live-flow.md)

## Approval

- Visual review: awaiting approval
- Build handoff: not authorized

## Now

- Current: Drew reviews the completed route and boundaries.
- Next: Drew explicitly approves the plan or names one change.
