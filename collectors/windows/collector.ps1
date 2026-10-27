# Manara host collector (Windows). Stub: no collection yet.
# Will gather allowlisted host metrics (contracts/health.v1.json, group "host")
# and hardware identifiers (contracts/inventory.v1.json) and hand them to the
# site's manara_home integration. TODO(verify): local transport and scheduling (Task Scheduler).
$ErrorActionPreference = 'Stop'

Write-Error 'manara collector: not implemented' -ErrorAction Continue
exit 0
