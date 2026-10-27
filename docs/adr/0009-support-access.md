# 0009. Support access via Maintainer switch

- Status: Accepted
- Date: 2026-10-27

## Context

Manara staff sometimes need to work on a client's HA. Standing access would undermine the client's control and trust.

## Decision

A client-owned Maintainer switch in `manara_home`:

- enables the site's maintainer HA user
- admits Manara staff certificates
- turns itself off after 24 hours

Every session is logged on site and on the hub, and the owner is notified.

## Consequences

- When the switch is off, the maintainer HA user is disabled and staff can't sign in, even with a valid certificate.
- Under the free-tier single mTLS rule ([ADR 0010](0010-free-tier-mvp.md)), staff certificates are valid at the edge for every site all the time. The switch enforces access through HA login only. TODO(verify): per-site admission of staff certificates at the edge needs a paid plan or a different rule design.
- The switch state and expiry are reported in the `support` health group, so the hub can show active support windows.
- Owner notification uses HA's notification system to the owner's enrolled devices.
