# 0002. Data leaving a site

- Status: Accepted
- Date: 2026-10-27

## Context

Manara needs enough data to monitor and support sites. Clients' homes and buildings produce sensitive data: presence, routines, images and audio. Trust depends on a rule that is simple, visible to clients, and enforced in code rather than policy.

## Decision

| Data class | Leaves the site? |
|---|---|
| Health (allowlisted metrics) | By default, with client consent |
| Inventory (hardware identifiers) | By default, with client consent |
| Analytics: sensor history, energy, occupancy | Only with per-site, per-data-class opt-in |
| Cameras, voice, location | Never |

The health metric allowlist is fixed in code. [`contracts/health.v1.json`](../../contracts/health.v1.json) is the reference implementation and [privacy/metric-allowlist.md](../privacy/metric-allowlist.md) the human-readable copy.

## Consequences

- `manara_home` exposes consent switches for health, inventory and each analytics class. Publishing stops immediately when a switch is turned off.
- The hub `ingest` service rejects payloads that fail schema validation, so extra fields can't slip through on the receiving end.
- Adding a metric means a new schema version and a PR labelled `privacy`.
- Analytics forwarding stays in the existing FastAPI addon ([ADR 0004](0004-site-integration.md)) and is off unless opted in.
- No contract or component may carry camera, voice or location data off site.
