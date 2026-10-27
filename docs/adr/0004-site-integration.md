# 0004. Site side: `manara_home` integration plus existing addon

- Status: Accepted
- Date: 2026-10-27

## Context

Each site runs Home Assistant. Manara needs site-side logic for enrolment, device management and telemetry. A FastAPI addon (`jangoachayan/manara-ha-addon`) already exists and serves the Flutter app's API.

## Decision

A new HA custom integration, `manara_home`, distributed through HACS, handles:

- device enrolment (QR codes, one-time codes, certificate requests through the provisioning Worker)
- device profiles
- TV control (deep link over ADB)
- fleet health
- revocation
- consent switches
- publishing health and inventory

The existing FastAPI addon stays, for the Flutter API and opted-in analytics forwarding.

## Consequences

- The integration runs inside HA, so it can use the device, entity and auth registries and config flows directly.
- There are two site-side components with a clear split: the integration owns devices and consent, and the addon owns analytics and the Flutter API. The addon must check the integration's consent state before forwarding anything. TODO(verify): how the addon reads that state.
- TV control over ADB needs network ADB enabled on each TV. TODO(verify): this works on the Toshiba (Android 11) target.
