# Agent instructions: manara-platform

Read by AI coding agents (Antigravity, Claude Code and others). Humans: see [README.md](README.md).

## What this repo is

Source of truth for the Manara smart-building platform, built on Home Assistant: architecture, ADRs, versioned JSON Schema contracts, hub plan, provisioning Worker and collectors. Other repos are listed in [docs/repos.md](docs/repos.md).

## Ground rules

- **The ADRs in [docs/adr/](docs/adr/) are locked decisions.** Don't propose designs that contradict them. If a task seems to need that, stop and ask, or draft a new ADR marked `Proposed`.
- **Never commit secrets:** tokens, API keys, certificates, keystores, `.env` or `.dev.vars` files. Gitleaks runs in pre-commit and CI; don't bypass it.
- **Privacy is enforced by schema.** [contracts/health.v1.json](contracts/health.v1.json) must match [docs/privacy/metric-allowlist.md](docs/privacy/metric-allowlist.md) exactly. Never add metrics, loosen `additionalProperties: false`, or add fields that could carry camera, voice, location, IP addresses, hostnames or user-chosen names. Such changes need a new schema version and a human-reviewed PR labelled `privacy`.
- **Contracts are versioned.** Never make breaking edits to a `*.v1.json`; add `*.v2.json`. Every schema needs a valid example in `contracts/examples/`, and privacy rules need an invalid example in `contracts/examples/invalid/`.
- Mark anything unconfirmed `TODO(verify)` rather than guessing.
- Work on `develop` or a branch off it. Never commit to `main` directly.

## Commands

```sh
python scripts/validate_contracts.py              # schemas + examples
npx markdownlint-cli2                             # markdown lint (CI runs this)
python -m pre_commit run --all-files              # all hooks
```

On this Windows machine, set `VIRTUALENV_OVERRIDE_APP_DATA=%USERPROFILE%\.cache\venvdata` before running pre-commit (path-length workaround).

## Style

- Markdown: sentence-case headings, tables for structured facts, no line wrapping.
- ADRs: Context, Decision, Consequences, numbered sequentially.
- Domain is `manara.co.in`; site hosts are `ha.<site>.manara.co.in`.
