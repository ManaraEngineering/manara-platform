# Hub

The Manara office hub: a Xeon D-1541 running Proxmox ([ADR 0007](../docs/adr/0007-hub.md)). It is reachable only through its own Cloudflare Tunnel.

## LXC plan

| LXC | Purpose | Hostname | Phase |
|---|---|---|---|
| `zabbix` | Monitoring, triggers, alerting | internal only | 1 |
| `grafana` | Dashboards over Zabbix (later TimescaleDB) | `grafana.manara.co.in` | 1 |
| `ops-ha` | Manara's own HA; maintainer phones enrol here and get alerts | `ha.ops.manara.co.in` | 1 |
| `ingest` | HTTPS endpoint for site health and inventory, per-site bearer token, schema-validated; pushes to Zabbix | `ingest.manara.co.in` | 1 |
| `timescale` | Long-term time series | internal only | later |
| `ml` | Analytics and anomaly detection | internal only | later |
| Actions runner | Self-hosted GitHub runner holding the APK signing key ([ADR 0010](../docs/adr/0010-free-tier-mvp.md)) | none | 7 |

TODO(verify): hostnames, LXC sizing (vCPU, RAM, disk), the backup target, and whether the Actions runner gets its own LXC.

## Directories

| Path | Will hold |
|---|---|
| [proxmox/](proxmox/) | LXC definitions and provisioning scripts |
| [zabbix/templates/](zabbix/templates/) | Zabbix templates matching `health.v1` groups |
| [ingest/](ingest/) | Ingest service |
| [ops-ha/](ops-ha/) | `ops-ha` configuration (no secrets) |
