# manara-platform

Source of truth for the Manara platform: architecture, decisions (ADRs), shared data contracts, hub configuration and the Cloudflare provisioning Worker.

> Proprietary. See [LICENSE](LICENSE).

## Layout

| Path | What |
|---|---|
| [docs/architecture.md](docs/architecture.md) | One-page overview and component diagram |
| [docs/adr/](docs/adr/) | Architecture decision records 0001–0010 |
| [docs/repos.md](docs/repos.md) | Map of all Manara repositories |
| [docs/privacy/metric-allowlist.md](docs/privacy/metric-allowlist.md) | The only health metrics that may leave a site |
| [contracts/](contracts/) | Versioned JSON Schemas (draft 2020-12) shared by all repos |
| [hub/](hub/) | Proxmox LXC plan for the Manara office hub |
| [cloudflare/worker/](cloudflare/worker/) | Provisioning Worker skeleton |
| [collectors/](collectors/) | Host collectors for Linux and Windows (stubs) |

## Branching

- `develop` is the default branch; all work lands here by PR.
- `main` is stable; changes arrive by PR from `develop` and CI must pass.

## Local setup

```sh
pip install pre-commit jsonschema
pre-commit install
python scripts/validate_contracts.py
```

Never commit secrets: tokens, keys, certificates, keystores or `.env` files. Gitleaks runs as a pre-commit hook and in CI.
