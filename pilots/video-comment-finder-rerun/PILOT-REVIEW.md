# Video Comment Finder Pilot — Clean Rerun

**Status:** Stopped after the session boundary became confusing
**Evidence class:** Does not count as Drew's human live pilot. The separate simulation task owns that evidence; Drew's channel-pool answer here is excluded from live acceptance.
**Skill version:** One-ticket-first revision
**Fresh-context test:** `/root/simple_pilot_rerun` received only the skill path, empty pilot path, and loose idea.

## Turn 1

```text
0/1  ▶ Finder contract
Next: Qualification rule

Example: Drew pastes a link to a new AI video; the skill scans its comments and returns candidate questions.

How should each run get videos?

A. Drew pastes links — recommended; simplest, but manual.
B. Scan saved channels — repeatable, but needs upkeep.
C. Discover recent AI videos — broadest, but noisier.

Or describe a mix.
```

**Drew's answer:** He will supply and maintain a group of AI channel names that he expects to have good comments. The skill should discover relevant videos and comments within that trusted channel pool.

## Turn 2

```text
0/1  ▶ Finder contract
Next: Worthwhile-question rule

Example: “Which AI coding agent should a beginner use?” What should make you qualified to answer?

A. Personal use or teaching — recommended; safest, fewer matches.
B. Direct or closely related experience — more matches, more judgment.
C. Any question in an approved topic list — simplest, loosest proof.

Custom rule welcome.
```

## Checks so far

- PASS: one planning ticket; no multi-session map was invented before a blocker appeared.
- PASS: one high-leverage product-direction question, concrete example, three viable choices, concise recommendation, and custom-answer path.
- PASS: 41-word ordinary reply with current and next step.
- PASS: destination, success, boundaries, current decision, and exact fresh-session starter are durable.
- PASS: the already explicit stopping boundary was derived and saved rather than asked again.
- PASS: separate fresh-agent probes resumed from files alone and regenerated a deliberately missing `NEXT.md`; the demonstrated path and custom-choice failures were fixed and passed clean reruns.
- PASS: Drew's custom source-mode answer was saved precisely and reconciled into `PLAN.md`, P-001, and `NEXT.md` before the next question.
- PASS: Turn 2 asks one consequential trust-boundary preference rather than asking Drew to choose implementation mechanics.

## Failures

- **F-004 — Session ownership was unclear.** This implementation task began asking sample-project questions that belong in the separate simulation task. Drew could not tell which session planned the plugin and which test-drove it.

## Drew feedback

- Turn 1 answer: trusted saved channel pool with in-pool video and comment discovery.
- Experience feedback: pending until the simple plan is complete.
