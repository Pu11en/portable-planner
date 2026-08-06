# Keyed Choice Forward Tests

Date: 2026-08-05

## Observed failure

The planner presented answer choices as bullets. Drew could not answer with a short stable key and had to refer to or repeat an option. This is a concrete conversation failure.

## Fix

The conversation contract now requires `1/2/3` by default, permits `A/B/C` only when numbers would be ambiguous, bans unlabeled answer-choice bullets, and requires a one-character reply to resolve to the most recent choice set.

## Fresh-context test

A fresh agent loaded the canonical skill and began planning a neighborhood skill-swap day. Its first preference question offered three viable choices labeled `1.`, `2.`, and `3.`, named a recommendation and tradeoffs, offered a custom path, and ended with `Reply 1, 2, or 3.`

The only follow-up input was:

```text
2
```

The agent resolved `2` to `Practical help traded`, saved that full decision in `planning/decisions/P-001-define-the-event.md`, reconciled `PLAN.md` and `NEXT.md`, and continued to the next preference question without asking the user to repeat the option.

## Result

**PASS:** numbered selection and one-character decision resolution work in a fresh context. The generated fixture remains under `validation/keyed-choice-forward-20260805/` as raw evidence.

## Letter-key correction

Drew then clarified that answer choices should always use letters, not numbers. The contract was corrected to require `A/B/C`, with `D` available only for a necessary fourth choice.

A second fresh agent planned a practical AI meetup. Its first question used `A.`, `B.`, and `C.`, then ended with `Reply A, B, or C.` The only follow-up input was:

```text
B
```

The agent resolved `B` to the full decision `Prioritize practical problem-solving and learning within a trusted local peer group`, saved it in the decision file and plan overview, and continued without asking for repetition.

**CURRENT PASS:** lettered selection and one-character decision resolution work in a fresh context. Raw evidence is under `validation/letter-choice-forward-20260805/`. The earlier numeric test is historical evidence of the iteration, not the current interface.

## Recommendation-first correction

Drew then confirmed that the recommendation must always be the first answer, labeled `A`. The earlier letter-key run proves lettered one-character resolution but does not prove this ordering rule. `C-02` is reopened until a new fresh-context test verifies recommendation-first choices and full decision write-through.

## Recommendation-first fresh-context rerun

A fresh Codex context loaded the revised canonical skill and began planning a monthly neighborhood skill night in `validation/recommendation-first-forward-20260805/`.

The opening:

- asked one consequential human-owned question;
- placed the recommendation first as `A`;
- offered three viable distinct routes and a custom-answer path;
- kept planning separate from running the event; and
- wrote the exact pending choices to canonical project-local state.

A second fresh Codex context received only the canonical skill, that planning directory, and the one-letter reply `A`. It resolved the saved choice without chat history, wrote the full primary-experience decision and its downstream effects into `PLAN.md`, `NEXT.md`, and P-001, then asked exactly one new consequential question whose recommendation was again `A`.

**CURRENT PASS:** recommendation-first lettered choices, one-character resolution, immediate full decision write-through, and fresh-session continuation are proven by the raw planning state under `validation/recommendation-first-forward-20260805/`.
