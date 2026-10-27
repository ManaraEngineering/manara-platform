# 0001. One platform, two tiers

- Status: Accepted
- Date: 2026-10-27

## Context

Manara serves building operators (offices, residential complexes, facilities) and individual homes. Building two products would double the app, integration and support work for one small team.

## Decision

There is one platform. Residential is a lighter tier of the operator product, not a separate product. The two tiers share the same app, integration, contracts, hub and remote-access model. They differ in configuration: device profiles, enabled features and support terms.

## Consequences

- Every feature is designed for operators first and then reduced for residential, never forked.
- Tier is a site-level setting that profiles and features can check. TODO(verify): whether tier needs to appear in any contract, or stays local to the integration.
- Residential sites carry the same privacy and security guarantees as operator sites.
