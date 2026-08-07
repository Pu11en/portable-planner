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

Also discard a question when another verbal answer is unlikely to alter the destination, route, proof, or protected tradeoff. Residual uncertainty alone does not justify continuing to grill.

For a new no-idea or thin-idea software/AI start, run the eligibility and permission gate in [idea-discovery.md](idea-discovery.md) before building the ordinary frontier. The permission is a human-owned choice about whether public possibility research should happen. Once granted, ask for a real-world anchor only if the user's existing words cannot support a privacy-safe one-sentence search brief; ask no preferred stack, architecture, search term, or repository question.

## Select one

From the ready human-owned frontier, select the question whose answer removes the most downstream uncertainty. Break ties by choosing the question that most affects the person's visible result. Ask exactly that one question and stop.

If no human-owned question is ready, research or synthesize the blocker without asking the person to choose the internal route.

If the person has explicitly delegated the remaining reversible decisions to the agent's recommendations, treat ready decisions inside that recorded scope as synthesis: save the recommended choice and reconcile its effects without asking. Repeated acceptance is convergence evidence, not delegation. Do not extend authority to irreversible commitments, materially personal tradeoffs, conflicts, implementation authorization, or final approval.

If the remaining uncertainty concerns dynamic behavior, look and feel, interaction, or effectiveness that words cannot discriminate, stop asking and run one bounded planning trial. Name one decision question; use an ordinary case, a materially contrasting case, and a failure or prohibited-action case by default. Preserve every input or starting state, variation, observed output, surprise or failure, verdict, and decision changed. Make one targeted planning revision after failure and rerun affected cases; return persistent tradeoffs to the person.

## Write the choices

- Treat category names, experience qualities, priorities, and other labels as abstract. Before those choices, show one literal project-specific input, output, or moment the person can picture. Option descriptions do not count as this example.
- Put the recommended answer first as `A.`
- Usually provide `A/B/C`; use `A/B` when only two strong routes exist and add `D` only for a genuinely distinct fourth route.
- Make every option viable, concrete, and mutually distinct.
- Give each option one short consequence or tradeoff.
- End with a visible custom-answer path and the valid reply letters.
- Do not expose expert names, framework jargon, or internal planning logic unless the person asks.

## Resolve the answer

When the person replies with one letter, resolve it against the most recent displayed choice set. Before asking anything else, write the full selected meaning, rationale when given, and every affected route, proof, scope, dependency, or ticket into canonical state. Never ask the person to repeat the option text.

When the person replies `yes`, `no`, `approved`, or equivalent to the most recent direct yes/no question, resolve it the same way. A direct `yes` to “Do you approve this plan for build?” is explicit build authorization; update state and immediately enter normal harness execution when safe instead of requesting a second command.

If the answer contradicts earlier state, point out the exact conflict briefly and ask one consequential reconciliation question. Do not silently preserve both answers.

An idea-stage research recommendation is provisional, even when the person delegated routine choices to the agent. Before ordinary planning adopts it, ask one grounded direction question whose viable answers are confirm, combine with a materially different surfaced alternative, or redirect. Omit any alternative unsupported by the evidence; never manufacture three choices. Save the selected direction and its evidence before continuing.

When a message introduces work that does not support the current destination, preserve current state and ask whether to switch plans or keep the new idea separate. Never merge unrelated destinations merely because they appeared in one conversation.
