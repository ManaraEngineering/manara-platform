# Contracts

Versioned JSON Schemas (draft 2020-12) shared by every Manara repository. This directory is the source of truth for data shapes.

| Schema | Producer | Consumer |
|---|---|---|
| [enrolment-qr.v1.json](enrolment-qr.v1.json) | `manara_home` | Manara Home app |
| [device-profile.v1.json](device-profile.v1.json) | `manara_home` | Manara Home app |
| [health.v1.json](health.v1.json) | `manara_home`, collectors | Hub `ingest` |
| [inventory.v1.json](inventory.v1.json) | `manara_home`, collectors | Hub `ingest` |

## Rules

- Every object sets `additionalProperties: false`. Unknown fields are errors.
- Breaking changes get a new file (`*.v2.json`). Never edit a released version in a breaking way.
- `health.v1.json` must match [docs/privacy/metric-allowlist.md](../docs/privacy/metric-allowlist.md). Changes to it need the `privacy` label.
- Fields still to be confirmed are marked `TODO(verify)` in their `description`.

## Examples

- `examples/<schema>.example.json` must validate against `<schema>.json`.
- `examples/invalid/<schema>.<case>.json` must **fail** validation. These guard the privacy rules: no extra metrics, no certificates in QR codes, no IP addresses or hostnames in inventory.

Run the checks locally:

```sh
pip install "jsonschema[format]"
python scripts/validate_contracts.py
```
