# Plan: AI Video Comment Question Finder

## Destination

A reusable skill that finds worthwhile questions in comments on AI-related YouTube videos, presents Drew with a short list of directly linked questions he is qualified to answer, and stops before creating any answer.

## Success

- In a real run, the skill returns several distinct, useful question options with working comment links and a clear basis for Drew's ability to answer each one, without drafting, recording, opening, or posting a response.

## Boundaries

- In: choose the video-source mode, inspect eligible YouTube comments, identify genuine questions, judge worth and answer fit, and present concise linked options.
- Out: answer writing, scripts, hooks, recording, editing, publishing, replying to comments, or selecting a final question for Drew.
- Drew manually opens a chosen comment and records a short 9:16 talking-head answer for YouTube Shorts or TikTok.

## Map

`0/1`

- ▶ [P-001 — Define the finder contract](decisions/P-001-define-finder-contract.md) — depends on: none

## Confirmed decisions

- [P-001](decisions/P-001-define-finder-contract.md): The skill only finds and presents linked, answerable comment questions; Drew chooses, opens, and answers one manually.

## Execution

- Execution tickets will be generated after the operating contract is settled.

## Now

- Current: P-001 — Define the finder contract
- Next: Decide how each run receives or discovers its source videos.
