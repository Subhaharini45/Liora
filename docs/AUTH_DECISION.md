# Authentication Decision (Phase 0)

## Context
Liora requires authentication for users to manage their profiles, documents, and interactions. We must choose an authentication strategy compatible with Streamlit.

## Options Evaluated
1. **Custom Email/Password in Streamlit + Database**:
   - *Pros*: Full control, no third-party lock-in.
   - *Cons*: High security risk (handling passwords, hashing, sessions, CSRF, password resets) in Streamlit.
   - *Feasibility*: Technically possible via session state, but fragile.

2. **Streamlit-Authenticator (3rd party lib)**:
   - *Pros*: Easy to implement, built for Streamlit.
   - *Cons*: Cookie-based, sometimes struggles with multi-page apps, stores hashes locally or in basic DB.

3. **OAuth Provider (Auth0 / Google / Supabase Auth)**:
   - *Pros*: Maximum security, offloads identity management, handles MFA and password resets.
   - *Cons*: Requires setting up a third-party application, OAuth callback handling in Streamlit can be tricky (requires query params or a redirect proxy).

4. **Streamlit Native Auth (Streamlit Community Cloud)**:
   - *Pros*: Built-in if deployed on Streamlit Cloud.
   - *Cons*: Restricts deployment options.

## Decision
We recommend **Option 3: OAuth Provider (via Supabase Auth or a similar identity provider)**, but for the immediate prototype (Phase 1), we will use a **Mock Authentication Layer** controlled by environment variables or simple session state toggles.

Why? 
Streamlit's execution model (re-running top to bottom) makes native session management complex. Outsourcing to an Identity Provider (IdP) is the safest route for production. However, to avoid blocking core feature development in Phase 1, we will abstract authentication behind a `get_current_user()` interface, which currently returns a mocked user ID, and will later be swapped for an IdP token verifier.

## Tenant Isolation Implications
Regardless of the authentication mechanism, the resulting `user_id` MUST be injected as a filter (e.g., `tenant_id`) into every database and Endee Vector DB query. This ensures logical data isolation at the storage layer.
