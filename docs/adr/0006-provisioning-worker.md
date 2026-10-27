# 0006. Provisioning Worker

- Status: Accepted
- Date: 2026-10-27

## Context

Issuing and revoking client certificates needs a Cloudflare API token with zone-level permissions. Putting that token on every site would mean one compromised site could issue or revoke certificates for any site.

## Decision

A Cloudflare Worker is the only holder of the zone API token. Sites call it with a per-site credential, and it issues or revokes certificates for that site's own devices only.

## Consequences

- The Worker keeps a record of which certificate belongs to which site and refuses cross-site actions. TODO(verify): where that record lives on the free tier (KV, D1, or certificate metadata).
- Per-site credentials are created when a site is onboarded, stored only in the site's HA and as a Worker secret or binding, and can be rotated on their own.
- The Worker is a single point of failure for enrolment and revocation, but not for day-to-day access.
- The Worker logs every issue and revoke call, with site ID and device ID.
