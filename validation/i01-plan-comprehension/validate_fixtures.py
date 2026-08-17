#!/usr/bin/env python3
"""Validate the frozen I-01 semantic fidelity fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"
EXPECTED_IDS = {f"F-{number:02d}" for number in range(1, 7)}
REQUIRED_KEYS = {
    "id",
    "claim",
    "source",
    "valid_view",
    "malformed_view",
    "contract",
    "expected_failure",
    "expected_behavior",
    "prohibited_behavior",
}


def _path(value: dict[str, Any], dotted: str) -> Any:
    current: Any = value
    for part in dotted.split("."):
        if not isinstance(current, dict) or part not in current:
            raise KeyError(dotted)
        current = current[part]
    return current


def _validate_view(case: dict[str, Any], view: dict[str, Any]) -> list[str]:
    source = case["source"]
    contract = case["contract"]
    errors: list[str] = []

    for dotted in contract.get("equal", []):
        try:
            source_value = _path(source, dotted)
            view_value = _path(view, dotted)
        except KeyError:
            errors.append(f"equal:{dotted}")
            continue
        if source_value != view_value:
            errors.append(f"equal:{dotted}")

    bounds = contract.get("route_bounds")
    if bounds is not None:
        route = view.get("route")
        minimum, maximum = bounds
        if not isinstance(route, list) or not minimum <= len(route) <= maximum:
            errors.append("route_bounds")

    required_now = contract.get("now_count")
    if required_now is not None:
        route = view.get("route", [])
        actual_now = sum(
            1
            for milestone in route
            if isinstance(milestone, dict) and milestone.get("state") == "NOW"
        )
        if actual_now != required_now:
            errors.append("now_count")

    required_visible = set(contract.get("visible_fields", []))
    if required_visible:
        visible = view.get("visible_fields")
        if not isinstance(visible, list) or not required_visible.issubset(visible):
            errors.append("visible_fields")

    maximum_safety = contract.get("max_safety_rules")
    if maximum_safety is not None:
        safety = view.get("safety")
        if not isinstance(safety, list) or len(safety) > maximum_safety:
            errors.append("max_safety_rules")

    for left, right in contract.get("parity", []):
        try:
            if _path(view, left) != _path(view, right):
                errors.append(f"parity:{left}:{right}")
        except KeyError:
            errors.append(f"parity:{left}:{right}")

    serialized = json.dumps(view, sort_keys=True).casefold()
    for term in contract.get("prohibited_terms", []):
        if term.casefold() in serialized:
            errors.append(f"prohibited:{term}")

    return errors


def _load_fixture(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Fixture must be a JSON object: {path}")
    missing = REQUIRED_KEYS - value.keys()
    if missing:
        raise ValueError(f"Fixture missing {sorted(missing)}: {path}")
    if not isinstance(value["source"], dict):
        raise ValueError(f"Fixture source must be an object: {path}")
    if not isinstance(value["valid_view"], dict):
        raise ValueError(f"Fixture valid_view must be an object: {path}")
    if not isinstance(value["malformed_view"], dict):
        raise ValueError(f"Fixture malformed_view must be an object: {path}")
    if not isinstance(value["contract"], dict):
        raise ValueError(f"Fixture contract must be an object: {path}")
    return value


def main() -> int:
    paths = sorted(FIXTURE_DIR.glob("f-*.json"))
    fixtures = [_load_fixture(path) for path in paths]
    ids = [fixture["id"] for fixture in fixtures]
    claims = [fixture["claim"] for fixture in fixtures]

    if set(ids) != EXPECTED_IDS or len(ids) != len(EXPECTED_IDS):
        raise SystemExit(f"Expected exactly {sorted(EXPECTED_IDS)}, found {ids}")
    if len(set(claims)) != len(claims):
        raise SystemExit("Every I-01 fixture must map to a unique failure claim")

    for fixture in fixtures:
        valid_errors = _validate_view(fixture, fixture["valid_view"])
        if valid_errors:
            raise SystemExit(f"{fixture['id']} valid view failed: {valid_errors}")

        malformed_errors = _validate_view(fixture, fixture["malformed_view"])
        expected = [fixture["expected_failure"]]
        if malformed_errors != expected:
            raise SystemExit(
                f"{fixture['id']} malformed view produced {malformed_errors}; "
                f"expected {expected}"
            )
        print(f"PASS {fixture['id']} valid; malformed -> {expected[0]}")

    print("I-01 fidelity contract: 6 valid fixtures and 6 malformed controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
