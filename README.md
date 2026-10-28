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

TODO: `main` is not protected yet. GitHub Free does not allow branch protection on private repos. Once the account is on GitHub Pro (or the repos move to a paid org), require a PR and the `contracts`, `markdown` and `secrets` checks on `main`. Until then, follow the rule by convention: no direct pushes to `main`.

## Local setup

```sh
pip install pre-commit jsonschema
pre-commit install
python scripts/validate_contracts.py
```

### IDE

Open [manara.code-workspace](manara.code-workspace) in Antigravity or VS Code (File → Open Workspace from File). It opens every Manara repo, assuming they're cloned side by side, and adds recommended extensions, live schema validation for contract examples, and tasks for each repo's checks (Terminal → Run Task). Agent instructions are in each repo's `AGENTS.md`.

Never commit secrets: tokens, keys, certificates, keystores or `.env` files. Gitleaks runs as a pre-commit hook and in CI.
