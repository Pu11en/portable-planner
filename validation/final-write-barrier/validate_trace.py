#!/usr/bin/env python3
"""Replay the domain-neutral final-write barrier pressure cases."""

from __future__ import annotations

import json
from pathlib import Path


TERMINAL_TRANSITIONS = {"final_review", "handoff", "ticket_complete", "testing", "build"}


def accepts(events: list[str]) -> bool:
    """Return whether every terminal transition has proof after the last write."""
    last_write = -1
    last_reconcile = -1
    last_check = -1

    for index, event in enumerate(events):
        if event == "planning_write":
            last_write = index
        elif event == "reconcile":
            last_reconcile = index
        elif event == "check":
            last_check = index
        elif event in TERMINAL_TRANSITIONS and last_write >= 0:
            if last_reconcile < last_write or last_check < last_write:
                return False

    return True


def main() -> None:
    fixture_path = Path(__file__).with_name("fixtures.json")
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for fixture in fixtures:
        actual = "accept" if accepts(fixture["events"]) else "reject"
        if actual != fixture["expected"]:
            failures.append(
                f"{fixture['id']}: expected {fixture['expected']}, observed {actual}"
            )
        else:
            print(f"PASS {fixture['id']} ({fixture['domain']}): {actual}")

    if failures:
        raise SystemExit("\n".join(failures))

    print(f"PASS {len(fixtures)} final-write-barrier fixtures")


if __name__ == "__main__":
    main()
