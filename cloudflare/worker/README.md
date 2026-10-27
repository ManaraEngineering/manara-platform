# Provisioning Worker

The only holder of the Cloudflare zone API token ([ADR 0006](../../docs/adr/0006-provisioning-worker.md)). Sites call it with a per-site credential to issue or revoke client certificates for their own devices only.

Skeleton only: every route returns `501 Not Implemented`.

## Planned routes

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/v1/sites/:site_id/certificates` | Sign a device CSR for this site |
| `DELETE` | `/v1/sites/:site_id/certificates/:cert_id` | Revoke a certificate belonging to this site |
| `GET` | `/v1/sites/:site_id/certificates` | List this site's certificates |

## Secrets

Never put these in `wrangler.toml` or commit them:

- `CF_API_TOKEN`: zone token with SSL and Certificates edit permissions. Set with `wrangler secret put CF_API_TOKEN`.
- Per-site credentials. TODO(verify): store as hashed values in KV or D1.

For local development, use `.dev.vars`, which is gitignored.

## Develop

```sh
npm install
npm run typecheck
npm run dev
```
