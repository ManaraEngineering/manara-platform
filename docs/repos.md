# Repositories

| Repository | Visibility | Purpose | Default branch |
|---|---|---|---|
| [ManaraEngineering/manara-platform](https://github.com/ManaraEngineering/manara-platform) | Private | Docs, ADRs, contracts, hub config, provisioning Worker, collectors | `develop` |
| [ManaraEngineering/manara-home-integration](https://github.com/ManaraEngineering/manara-home-integration) | Private | `manara_home` HA custom integration (HACS) | `develop` |
| [ManaraEngineering/manara-home-android](https://github.com/ManaraEngineering/manara-home-android) | Private | Manara patch layer on `home-assistant/android`; `mobile` and `tv` flavours | `develop` |
| [jangoachayan/manara-ha-addon](https://github.com/jangoachayan/manara-ha-addon) | Existing | FastAPI HA addon: Flutter API and opted-in analytics forwarding. Not managed from here. | — |
| Flutter app (existing) | Existing | Reserved for a later operator app. Not managed from here. TODO(verify): repo URL. | — |
| [home-assistant/android](https://github.com/home-assistant/android) | Public, Apache 2.0 | Upstream for `manara-home-android`; its `upstream` branch mirrors this repo | — |

## How they depend on each other

- `contracts/` in this repo is the single source for data shapes. Other repos consume it at a pinned version; see each repo's README.
- `manara-home-integration` produces enrolment QR codes, device profiles, and health and inventory payloads that must validate against these contracts.
- `manara-home-android` consumes enrolment QR codes and device profiles.
- The hub `ingest` service accepts only health and inventory payloads that validate against these contracts.
