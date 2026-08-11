# Compact Conversation Forward Test

**Date:** 2026-08-05  
**Codex session:** `019fd403-d6e0-72c2-8f10-28c6a2f70ff6`  
**Raw fixture:** [`compact-conversation/`](compact-conversation/)

## Purpose

Test C-03 against actual user-facing planner replies rather than treating the conversation contract as proof. The idea deliberately leaves an abstract, consequential preference unresolved: how structured participation should feel for shy newcomers.

## First ordinary reply

<!-- FIRST-REPLY-START -->
Test drive: we are planning Neighborhood Skill-Share Night to judge the planner; no build work happens here.

Planning: Neighborhood Skill-Share Night  
Now: Choose how guided participation feels  
Later: Turn it into the 90-minute event flow

Picture arriving alone:

A. Guided small-group rounds — Recommended; welcoming, but less free-form.  
B. Two featured mini-lessons — Clearest, but fewer people teach.  
C. Open skill stations — Flexible, but requires more self-starting.

Or give a different answer. Reply A, B, or C.
<!-- FIRST-REPLY-END -->

Observed behavior:

- It makes the abstract structure preference concrete first with `Picture arriving alone`.
- It shows the plan name, current progress, and what happens later.
- It asks exactly one human-owned question.
- It provides three viable lettered choices, recommendation first, short tradeoffs, and a custom-answer path.
- It uses no process jargon or routine file-write narration.

The reply is 78 words by the repository audit below. “Near 60 words” is intentionally a reading-load target rather than a brittle exact cap; this reply stays within one compact screen while carrying the required test-drive boundary and complete choice set.

## Compact post-decision progress reply

The adaptive-map session supplied a second ordinary reply after the saved `A` choice introduced a real blocker:

<!-- SECOND-REPLY-START -->
Planning: Riverside Community Movie Night  
Now: Assess Riverside Park  
Later: Plan the approved park route or indoor fallback

Choice A is saved. The park remains unapproved pending assessment of power distance, sound spill, emergency access, and screen location. Equipment decisions wait; the assessment result remains unknown.

Route: Goal → ✓ indoor fallback chosen → ▶ assess park → manager decides → plan selected venue → finish logistics and proof → human approval.
<!-- SECOND-REPLY-END -->

This reply is 72 words. It states what changed, the current step, the later step, and the complete compact route without asking a factual or technical question.

## Completion reply

After the first fixture's only preference was resolved, the planner completed the plan and showed its Mermaid route, text route, destination, success criteria, safety boundaries, and explicit approval question. That longer output is the required visual artifact and therefore falls under the conversation contract's explicit-artifact exception; it is not counted as an ordinary reply.

## Result

**PASS for C-03.** Actual replies demonstrate a concrete example before an abstract choice, compact ordinary turns, visible current progress, and an explicit next step. Drew later clarified that roughly 60 words is a flexible target and anything under 100 words is acceptable when the content is useful; see [`WORD-LENGTH-CALIBRATION.md`](WORD-LENGTH-CALIBRATION.md).
