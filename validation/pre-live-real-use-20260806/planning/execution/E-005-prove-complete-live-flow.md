# E-005 — Prove the complete live flow

- Outcome: The full phone-to-fresh-agent experience passes its safety, recovery, and usefulness proof and is ready for ordinary use.
- Depends on: P-001, E-002, E-003, E-004

## Context

- [Plan](../PLAN.md)
- [Confirmed product contract](../decisions/P-001-define-shared-inbox-contract.md)
- [Telegram feasibility evidence](../evidence/P-001-telegram-feasibility.md)

## In scope

- Prepare a reversible fixture with at least 20 varied ideas and a backup of the real inbox.
- Run authorized phone text and link captures, duplicate replay, unauthorized input, unsupported media, offline/restart, and forced-write-failure cases.
- Start a fresh agent session that loads only repository instructions, retrieves the new captures, compares at most three candidates, and waits for Drew's decision.
- Confirm one idea, verify the intended status/rationale/date change, and verify all other content remains intact.
- Write a short operating guide covering accounts, bot-token handling, local runtime start/stop, when captures are processed, unsupported inputs, recovery, backup, and how to disable access.
- Record objective results and Drew's final experience judgment.

## Out of scope

- Adding features during the pilot, public deployment, background auto-start without separate approval, automatic commits, or beginning work on the selected idea.

## Constraints

- Back up before the live test, expose no secrets, and restore only with Drew's approval if an unexpected mutation occurs.
- Failed checks reopen the responsible execution ticket; they do not get waived.

## Proof

- Every success and failure condition in P-001 has recorded pass evidence.
- The canonical inbox contains the exact originals, exactly one confirmed selection, no unauthorized capture, and no unrelated diff.
- A context-reset agent can repeat the find-and-compare flow from local files alone.

## If blocked or disproven

- Preserve all captures and record the exact failed condition. Reopen the earliest responsible ticket; return to planning only if the destination, boundary, or human decision must change.

## Human review

- Drew performs the phone capture, judges retrieval and comparison clarity, and explicitly accepts or rejects the complete experience.

## Next eligible ticket

- Plan complete.
