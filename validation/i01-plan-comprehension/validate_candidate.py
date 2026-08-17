#!/usr/bin/env python3
"""Validate the I-01 candidate grammar in the canonical skill files."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "plugins/portable-planner/skills/portable-planner"
CONTRACT = SKILL / "references/visual-contract.md"
TEMPLATE = SKILL / "templates/PLAN-VIEW.md"


def require(path: Path, fragments: list[str]) -> None:
    content = path.read_text(encoding="utf-8").casefold()
    missing = [fragment for fragment in fragments if fragment.casefold() not in content]
    if missing:
        raise SystemExit(f"{path.relative_to(ROOT)} missing required semantics: {missing}")


def main() -> int:
    require(
        CONTRACT,
        [
            "Journey plus focus lens",
            "five to nine",
            "exactly one milestone `NOW`",
            "current outcome",
            "exact next action",
            "human role",
            "objective proof",
            "recovery behavior",
            "one quiet rail",
            "no more than six",
            "may never require a click, expansion, or file link",
            "same milestones, state labels, and dependency order",
            "regenerate the entire view",
            "cannot introduce or own plan decisions",
        ],
    )
    require(
        TEMPLATE,
        [
            "## Journey",
            "NOW · 3 · {{current milestone outcome}}",
            "## Focus lens",
            "**Current outcome:**",
            "**Next action:**",
            "**Human role:**",
            "**Proof:**",
            "**Recovery:**",
            "## Quiet rail",
            "**Remaining:**",
            "**Guardrails:**",
            "Exactly one starts NOW",
            "Never hide destination, route, current outcome",
        ],
    )

    fixture_validator = Path(__file__).with_name("validate_fixtures.py")
    completed = subprocess.run([sys.executable, str(fixture_validator)], check=False)
    if completed.returncode:
        return completed.returncode

    print("I-01 candidate grammar: canonical contract and template passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
