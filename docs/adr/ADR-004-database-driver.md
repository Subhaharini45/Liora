# Architecture Decision Record (ADR-004): Database Driver

## Context
We need to connect to PostgreSQL.

## Decision
We will use `psycopg` (v3) with the `[binary,pool]` extras. 

## Alternatives Considered
- `asyncpg`: Faster, but requires an entirely async architecture which Streamlit doesn't strictly benefit from natively.
- `SQLAlchemy`: Adds ORM overhead. We prefer raw SQL or lightweight query builders for Phase 1.

## Evidence
- `psycopg` 3 is the modern, standard sync/async driver for Postgres in Python.

## Consequences
- Requires standard PostgreSQL environment setups. (Currently blocked on local environment lack of Docker/psql, so cloud DB will be required).

## Status
Approved (Phase 0)
