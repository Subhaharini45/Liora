# Phase 0 Results: Technical Spikes & Foundation

## Executive Summary
Phase 0 successfully laid the foundation for the Liora project. We verified critical assumptions, established the repository structure, and identified environmental blockers (such as the lack of local Docker) before full implementation.

## Evidence Collection

### 1. Python Environment & Foundation
- **Verified**: Project uses Python 3.12 (specifically 3.12.9) via a `.venv` virtual environment.
- **Verified**: Dependencies (Streamlit, Groq, Endee, Pytest, Psycopg) are tracked in `pyproject.toml`.
- **Verified**: Code is structured into Domain-Driven Design (DDD) folders (`app/ui`, `app/domain`, `app/services`, etc.).

### 2. Endee Vector DB Spike
- **Verified**: API contract extracted from the Python module (`endee` v2.2.0). 
- **Verified**: Tenant isolation is fully supported logically via the `filter` metadata parameter (e.g., `{"tenant_id": {"$eq": "user_id"}}`).
- **Blocked**: Local execution was blocked due to missing Docker. `ConnectionError` was confirmed when attempting to hit localhost.

### 3. PostgreSQL Spike
- **Blocked**: Testing local PostgreSQL migrations and connectivity was blocked due to the host lacking Docker and a native `psql` client. We will rely on a cloud PostgreSQL provider for Phase 1.

### 4. Embedding Model Bake-off
- **Verified**: Both `all-MiniLM-L6-v2` and `BAAI/bge-small-en-v1.5` were evaluated using `sentence-transformers`. 
- **Result**: `BAAI/bge-small-en-v1.5` was chosen for its superior semantic matching while retaining a small 384-dimension footprint.

### 5. Groq Provider Spike
- **Verified**: A modular `LLMProvider` interface was created. `GroqProvider` successfully abstracts the Groq API, preventing the application from hardcoding Groq logic everywhere.

### 6. Streamlit Authentication
- **Verified**: Streamlit's execution model makes robust custom authentication difficult. We chose to rely on an external Identity Provider (OAuth) for production, but will use mock session-state authentication for immediate UI development (Phase 1).

### 7. Streamlit UI & Mascot Feasibility
- **Verified**: Glass-style cards, theming, and basic CSS animations are possible.
- **Verified**: A CSS-based static/hover mascot is highly feasible.
- **Blocked/Discouraged**: Global mouse cursor tracking for the mascot's eyes is fragile in Streamlit and has been deprioritized in favor of state-driven animations (e.g. idle, thinking).

## Remaining OPEN Decisions
1. **Database Hosting**: Will we provision a Supabase/Neon cloud Postgres instance, or install Docker locally for development?
2. **Endee Hosting**: Will we use Endee Cloud, or wait for local Docker support?

## Conclusion
Phase 0 is complete. The repository is clean, secrets are managed securely (`.env.example`), assumptions are documented via ADRs, and the architectural blueprint remains intact. We are ready for Phase 1 (Feature Implementation).
