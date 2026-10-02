# Architecture Decision Record (ADR-001): Endee API Contract

## Context
Liora uses Endee Vector DB. We needed to verify its API contract and tenant isolation capabilities.

## Decision
We will use the `endee` Python package (v2.2.0) and enforce logical tenant isolation using the `filter` argument in `search()` and `upsert()` calls.

## Alternatives Considered
- Direct HTTP requests: Rejected due to the availability of the official client handling HTTP connection pooling.
- Physical separate collections per user: Rejected due to likely overhead.

## Evidence
- The `endee` module exposes `Endee`, `create_collection`, `Collection.upsert`, `Collection.search(..., filter=[...])`.

## Consequences
- Every data access path must strictly append `{"tenant_id": {"$eq": "current_user"}}` to filters to prevent cross-tenant leakage.

## Status
Approved (Phase 0)
