# Collectors

Small host agents that report allowlisted host metrics and hardware identifiers for machines at a site. Stubs only.

| Path | Platform | Scheduling |
|---|---|---|
| [linux/collector.sh](linux/collector.sh) | Linux | systemd timer ([manara-collector.timer](linux/manara-collector.timer)) |
| [windows/collector.ps1](windows/collector.ps1) | Windows | Task Scheduler (TODO) |

Output must validate against [health.v1.json](../contracts/health.v1.json) (group `host` only) and [inventory.v1.json](../contracts/inventory.v1.json).
