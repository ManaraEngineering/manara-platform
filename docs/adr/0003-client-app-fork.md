# 0003. Client app: fork of `home-assistant/android`

- Status: Accepted
- Date: 2026-10-27

## Context

Clients need a branded app for phones, tablets, wall panels and TVs that works fully with HA. The official HA Android app (Apache 2.0) already handles the frontend, WebSockets, notifications, sensors and client certificates. Writing an app from scratch in Flutter would mean rebuilding all of that.

## Decision

- Fork `home-assistant/android`, building on its upstream `minimal` flavour (no Google Play Services).
- Ship two flavours:

  | Flavour | Application ID |
  |---|---|
  | `mobile` | `in.co.manara.home` |
  | `tv` | `in.co.manara.home.tv` |

- Keep Manara's changes as a thin patch layer, rebased onto each upstream release by CI. The allowed patch surface is listed in the repo's `MANARA.md`: a Gradle flavour block, resource overrides, one config class, a TV manifest/activity, and small documented hooks.
- Keep Flutter for a later operator app.

## Consequences

- Upstream fixes and features arrive by rebase. The patch layer has to stay small, or rebases become expensive.
- The `minimal` flavour has no FCM, so notifications depend on HA's persistent WebSocket. Phase 0 spike 3 checks this through Cloudflare Tunnel.
- Apache 2.0 obligations apply: keep `LICENSE` and `NOTICE`, and record changes in `CHANGES.md`.
- The repo is private and not a GitHub fork, because forks of public repos can't be private.
