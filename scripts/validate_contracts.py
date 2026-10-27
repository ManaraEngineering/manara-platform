"""Validate contract schemas and their examples.

- Every contracts/*.json must be a valid draft 2020-12 schema.
- Every contracts/examples/<schema>.example.json must validate against <schema>.json.
- Every contracts/examples/invalid/<schema>.<case>.json must fail validation.
- Every schema must have at least one valid example.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent / "contracts"


def load(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    errors: list[str] = []
    validators: dict[str, Draft202012Validator] = {}

    for schema_path in sorted(ROOT.glob("*.json")):
        schema = load(schema_path)
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{schema_path.name}: invalid schema: {e}")
            continue
        validators[schema_path.stem] = Draft202012Validator(schema, format_checker=FormatChecker())

    covered: set[str] = set()
    for example in sorted((ROOT / "examples").glob("*.example.json")):
        name = example.name.removesuffix(".example.json")
        validator = validators.get(name)
        if validator is None:
            errors.append(f"examples/{example.name}: no schema {name}.json")
            continue
        covered.add(name)
        for err in validator.iter_errors(load(example)):
            errors.append(f"examples/{example.name}: {err.json_path}: {err.message}")

    for bad in sorted((ROOT / "examples" / "invalid").glob("*.json")):
        name = bad.name.rsplit(".", 2)[0]
        validator = validators.get(name)
        if validator is None:
            errors.append(f"examples/invalid/{bad.name}: no schema {name}.json")
            continue
        if validator.is_valid(load(bad)):
            errors.append(f"examples/invalid/{bad.name}: expected to fail but validated")

    for name in sorted(set(validators) - covered):
        errors.append(f"{name}.json: no valid example in examples/")

    for line in errors:
        print(f"FAIL {line}")
    print(f"{len(validators)} schemas checked, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
