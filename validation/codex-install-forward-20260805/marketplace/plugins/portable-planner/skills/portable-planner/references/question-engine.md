# Question Engine

Keep the full decision structure internal. Show the person only the single best question that is ready now.

## Build the candidate frontier

After reading canonical state, identify unresolved decisions and their prerequisites. A candidate may be asked only when all five checks pass:

1. **Consequential:** Different answers materially change the destination, scope, experience, route, proof, ownership, or important risk.
2. **Ready:** No earlier unsettled decision is required to understand or answer it.
3. **Human-owned:** The answer depends on preference, authority, priorities, or lived constraints—not a fact the agent can inspect or research.
4. **Grounded:** The question uses this project's real language, prior answers, and current state.
5. **Answerable:** The agent can offer multiple genuinely strong routes without manufacturing a weak option.

Discard obvious, repeated, ceremonial, template-driven, factual, technical, architecture, tool, and workflow questions. Route facts to research and derivable mechanics to synthesis.

## Select one

From the ready human-owned frontier, select the question whose answer removes the most downstream uncertainty. Break ties by choosing the question that most affects the person's visible result. Ask exactly that one question and stop.

If no human-owned question is ready, research or synthesize the blocker without asking the person to choose the internal route.

## Write the choices

- Put the recommended answer first as `A.`
- Usually provide `A/B/C`; use `A/B` when only two strong routes exist and add `D` only for a genuinely distinct fourth route.
- Make every option viable, concrete, and mutually distinct.
- Give each option one short consequence or tradeoff.
- End with a visible custom-answer path and the valid reply letters.
- Do not expose expert names, framework jargon, or internal planning logic unless the person asks.

## Resolve the answer

When the person replies with one letter, resolve it against the most recent displayed choice set. Before asking anything else, write the full selected meaning, rationale when given, and every affected route, proof, scope, dependency, or ticket into canonical state. Never ask the person to repeat the option text.

If the answer contradicts earlier state, point out the exact conflict briefly and ask one consequential reconciliation question. Do not silently preserve both answers.
