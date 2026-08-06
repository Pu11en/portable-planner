# F-011 — Abstract Choice Without a Literal Example

Fresh Codex session: `019fd41e-500f-7471-834b-d7b53af7896f`.

The corrected pilot started with one ticket, the right trusted-channel scope, canonical `planning/` state, recommendation-first `A/B/C`, and no invented progress count. However, it asked Drew to choose among category labels—`Practical blockers`, `Misconceptions`, and `Timely tool questions`—without first showing a literal example comment he could picture.

This violates C-03 and the conversation contract's abstract-choice rule. Option descriptions are not a substitute for an example input or moment.

Fix: `question-engine.md` now explicitly treats category names, experience qualities, and priorities as abstract and requires one literal project-specific input, output, or moment before the choices.

Completion test: a clean rerun must preserve the corrected scope and one-ticket state while showing a literal example comment before the one `A/B/C` question.

