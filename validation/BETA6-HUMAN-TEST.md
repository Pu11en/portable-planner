# Beta-6 exact-delegation human test

Status: ready after `0.1.0-beta.6` is published and installed
Test folder: `/home/drewp/main-projects/portable-planner-beta6-acceptance`

## Why this is the best first test

Use a dedicated empty project rather than the Portable Planner repository or
Cinco H Ranch repository. Both existing repositories already contain canonical
`planning/` state, so a fresh task there may resume an old plan and contaminate
the result. The empty folder isolates natural invocation while the scenario is
realistic enough to require more than four reversible human decisions and a
protected final-approval gate.

## Start exactly this way

1. Open the test folder in Codex Desktop.
2. Start a new task; do not continue this task.
3. Paste only this natural request:

> Help me plan a small fall open-house launch for a ranch-products business. I
> want to personally choose the primary audience, featured offer, event format,
> promotion emphasis, and follow-up experience. Ask one meaningful decision at
> a time and make a recommendation, but do not assume permission to choose for
> me.

4. For each of the first three real preference questions, reply with only:

```text
A
```

Do not add punctuation, spaces beyond normal surrounding whitespace, or any
explanation.

## Expected fourth question

The next real reversible question must keep its ordinary recommendation as
`A.` and insert this meaning as `B.`:

```text
B. Use my recommendations for every remaining reversible decision
```

Other ordinary answers to that same question follow as `C.` onward. The set may
not exceed `G.`. A separate “delegate or continue?” question is a failure.

Reply with only:

```text
B
```

## Expected result after B

- The planner records explicit delegation.
- It applies the recommended answer to the current question.
- It resolves every remaining reversible preference without more questions.
- It writes the full route and reaches final review in the same turn when safe.
- It stops for explicit final approval; it does not approve or build merely
  because three `A` replies occurred or because `B` delegated reversible choices.

## Pass or failure report

Reply in the Portable Planner development task with the exact visible turns or
a screenshot and one of:

- `PASS — B appeared in the fourth real question and stopped at approval.`
- `FAIL —` followed by the first moment that differed.

Do not correct the test agent during the run. The first natural failure is the
most useful evidence.
