# 0005. Remote access: Cloudflare Tunnel and mTLS

- Status: Accepted
- Date: 2026-10-27

## Context

Clients need to reach their HA from anywhere. Opening inbound ports at client sites is unacceptable, and HA's login alone shouldn't be the only barrier exposed to the internet.

## Decision

- Each site runs a Cloudflare Tunnel published at `ha.<site>.manara.co.in`.
- Each device gets an mTLS client certificate from Cloudflare's managed CA during QR enrolment.
- No site has inbound ports.

## Consequences

- An attacker without a valid certificate never reaches HA; the request is blocked at the edge.
- The private key should be generated on the device and never leave it; enrolment sends a CSR. TODO(verify): the Cloudflare client certificate API accepts a CSR (spike 7).
- Enrolment needs a path that doesn't require a certificate yet. TODO(verify): LAN-only enrolment, or an mTLS-exempt enrolment hostname ([architecture](../architecture.md#device-enrolment-outline)).
- Revoking a certificate cuts a device off at the edge, on top of removing its HA session (Phase 0 spike 6).
- Cloudflare becomes a hard dependency for remote access. LAN access at a site still works without it.
