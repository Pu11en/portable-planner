# Orientation and Confusion-Recovery Test

## Setup

A fresh agent received only the canonical skill, an empty validation planning folder, and this idea: build a small local app that turns interview transcripts into a searchable evidence library.

## Opening

```text
Planning: Searchable interview evidence library
We are deciding what to build and how to prove it. This flow will not build it.

Now: Choose the first user and evidence job
Later: Define the core workflow and proof

Who should the first version serve?

- Product researchers reviewing customer interviews — recommended; focused but narrower.
- Founders or consultants reviewing discovery calls — flexible but varied.
- Journalists or academic researchers — rigorous but more specialized.

Or give a different answer.
```

**Result:** PASS. It names the plan, states the planning-only boundary, uses plain current/next language, asks one human-owned preference, and does not invent a fixed progress count.

## Adversarial confusion turn

Input:

```text
I'm confused. What are we doing here? Are you building the app or asking me to plan your planning system? I don't understand these steps.
```

Reply:

```text
Planning: Searchable interview evidence library

We’re planning your app—not planning the planning system, and not building the app yet.

This session will produce a clear build guide: what the first version does, how we’ll prove it works, and the ordered build tasks.

Current step: clarify who the first version should help, because that determines what “useful evidence” means.

Say “continue” when this makes sense, or tell me what remains unclear.
```

**Result:** PASS. It pauses planning, explains the session and output, translates the current step, asks no new planning decision, and waits for understanding or redirection.
