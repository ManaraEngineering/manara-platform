# 0008. Telemetry over HTTPS push

- Status: Accepted
- Date: 2026-10-27

## Context

Sites need to send health and inventory to the hub. Running a cloud MQTT broker adds another exposed service, more credentials and another thing to operate.

## Decision

Sites push to `ingest.manara.co.in` over HTTPS, authenticated with a per-site bearer token. When the hub is unreachable, sites buffer payloads and resend them later. There is no MQTT broker in the cloud.

## Consequences

- One simple, stateless endpoint that is easy to put behind the tunnel and to validate against the contracts.
- The buffer has a size or age cap so a long outage can't fill a site's disk. Buffer depth is reported in the `buffer` health group. TODO(verify): the cap values.
- `ingest` requests also pass the `*.manara.co.in` mTLS rule, so a site needs its own client certificate as well as the bearer token. TODO(verify): this is intended, and how site certificates are issued.
- Push intervals are set at site level. TODO(verify): the defaults (for example 60 s for health, daily for inventory).
