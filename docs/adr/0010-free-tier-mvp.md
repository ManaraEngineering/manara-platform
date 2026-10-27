# 0010. Free-tier MVP

- Status: Accepted
- Date: 2026-10-27

## Context

The MVP should run without recurring platform costs while the number of sites and devices is small.

## Decision

- Use the Cloudflare free plan, which allows at most 100 client certificates per zone.
- Apply a single mTLS rule across `*.manara.co.in`: the client certificate must be valid and not revoked.
- Separation between sites comes from HA login.
- Distribute APKs through GitHub releases and sideloading.
- A self-hosted GitHub Actions runner on the hub holds the APK signing key.

## Consequences

- 100 certificates covers the MVP only. Devices, maintainer phones, staff and any site certificates all count. The hub reports certificate usage. Moving to a paid plan, or splitting zones, is the planned way out.
- Any valid Manara certificate reaches the edge of any site. A certificate from site A can reach `ha.<site-b>`, but can't sign in there. This is an accepted risk for the MVP.
- TODO(verify): whether free-plan WAF rules can use certificate fingerprint fields (spike 1). If they can, finer rules may be possible.
- Sideloading needs "install unknown apps" on client devices, and updates are manual until there's an in-app updater or a store listing.
- The signing key never leaves the hub runner. Release workflows that sign must run on that runner only.
