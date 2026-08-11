# P-001 evidence — Telegram feasibility

**Accessed:** 2026-08-06

## Direct sources

- [Telegram Bot API](https://core.telegram.org/bots/api/): Telegram provides an HTTP Bot API, `getUpdates` for incoming updates through long polling, and `sendMessage` for acknowledgements. The documentation also says long polling and webhooks are mutually exclusive, so version one can deliberately use only local long polling.
- [Telegram Bots FAQ](https://core.telegram.org/bots/faq): bots receive messages sent by users in private chats, supporting a dedicated one-person capture conversation.

## Decision effect

- Confirms that a private Telegram capture adapter with a local polling worker and saved/failed reply is feasible without choosing a hosted webhook service.
- Confirms text messages and URLs are available to the adapter. It does not establish application-level authorization, secret storage, or safe file writes; those remain mandatory safeguards in P-001 and the execution tickets.

## Recheck

- Recheck the official Bot API methods and token setup during E-002 before connecting Drew's real bot. Return to planning only if private message receipt, long polling, or acknowledgement is no longer supported.
