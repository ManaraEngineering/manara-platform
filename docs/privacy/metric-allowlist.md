# Health metric allowlist

These are the **only** health metrics that may leave a site. The list is fixed in code: [`contracts/health.v1.json`](../../contracts/health.v1.json) rejects any field not listed here (`additionalProperties: false` at every level). Adding a metric needs a new schema version, a PR labelled `privacy`, and an update to this page.

Health data leaves a site by default, and **only with client consent** ([ADR 0002](../adr/0002-data-leaving-a-site.md)).

Never allowed in health payloads: entity states or sensor values, names of people, rooms or devices chosen by users, IP addresses, camera, voice or location data, free text, logs.

## Groups

### `host`: the machine running HA or a collector

| Metric | Type | Unit |
|---|---|---|
| `cpu_percent` | number | % |
| `memory_percent` | number | % |
| `disk_percent` | number | % of the data volume |
| `uptime_s` | integer | seconds |
| `load_1m` | number | — |
| `cpu_temp_c` | number | °C, optional |

### `home_assistant`

| Metric | Type | Notes |
|---|---|---|
| `version` | string | HA core version |
| `integration_count` | integer | Loaded config entries |
| `entity_count` | integer | Total entities |
| `unavailable_entity_count` | integer | Count only, no entity IDs |
| `last_backup_age_s` | integer | Seconds since the last successful backup |
| `manara_home_version` | string | Integration version |

### `connectivity`

| Metric | Type | Notes |
|---|---|---|
| `tunnel_connected` | boolean | cloudflared connected to the edge |
| `ingest_rtt_ms` | integer | Round trip to `ingest.manara.co.in` |
| `wan_up` | boolean | — |

### `fleet`: enrolled Manara devices at the site

| Metric | Type | Notes |
|---|---|---|
| `enrolled_count` | integer | — |
| `online_count` | integer | Seen in the last 15 minutes |
| `cert_expiring_30d_count` | integer | Client certificates expiring within 30 days |
| `app_versions` | object | App version → device count |

### `buffer`: on-site telemetry buffer ([ADR 0008](../adr/0008-telemetry.md))

| Metric | Type | Notes |
|---|---|---|
| `queued_payloads` | integer | — |
| `oldest_queued_age_s` | integer | — |

### `support`: Maintainer switch ([ADR 0009](../adr/0009-support-access.md))

| Metric | Type | Notes |
|---|---|---|
| `maintainer_enabled` | boolean | — |
| `maintainer_expires_at` | date-time | Only when enabled |

## Open questions

- TODO(verify): whether `cpu_temp_c` is reliably available on HA OS and on the target collector hosts.
- TODO(verify): the 15-minute "online" window, measured against real app reconnect behaviour.
