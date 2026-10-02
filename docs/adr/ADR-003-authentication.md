# Architecture Decision Record (ADR-002): Authentication Strategy

## Context
Liora requires user authentication compatible with Streamlit.

## Decision
We will abstract authentication behind a provider interface, starting with mocked local environment variables for Phase 1, but designed to easily plug into an OAuth provider (e.g., Supabase Auth) for production.

## Alternatives Considered
- Streamlit-Authenticator: Cookie based, harder to secure at a database level.
- Custom Email/Pass: High security risk.

## Evidence
- Streamlit reruns require session state to hold auth tokens. IdPs handle the heavy lifting securely.

## Consequences
- We must build a `get_current_user()` function that the rest of the application uses seamlessly.

## Status
Approved (Phase 0)
