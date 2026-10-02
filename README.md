# LIORA

LIORA is an AI-powered, adaptive, memory-aware learning assistant using Endee Vector DB.

## Current Project Status
- Phase 0 (Technical Spikes, Environment Setup, Repository Foundation, and Evidence Collection) is currently in progress.

## Architecture Status
- Architecture follows the approved LIORA blueprint.
- We are currently verifying assumptions regarding the database (PostgreSQL), vector store (Endee), LLM provider (Groq), UI (Streamlit), and mascot.

## Technology Stack
- **Python:** 3.12+
- **Vector Database:** Endee Vector DB
- **Relational Database:** PostgreSQL 16
- **LLM Provider:** Groq
- **UI Framework:** Streamlit
- **Testing:** pytest

## Development Environment Setup
1. Ensure Python 3.12 is installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt # Or poetry install
   ```
4. Copy `.env.example` to `.env` and fill in secrets.
5. (Docker is currently required for PostgreSQL, but note that Docker is not available in the current environment natively.)

## Open Questions / Assumptions (Phase 0)
- Can Endee be run reliably for local development?
- What is the exact Endee API/client contract?
- Can we safely isolate data by user/tenant in Endee?
- Which embedding model works best for Liora's documents?
- Which Streamlit authentication approach should we use?
- Can we implement the Liora mascot interaction technically in Streamlit?

## Running Phase 0 Experiments
Experiments are located in the `experiments/` directory and can be executed as standalone scripts or via pytest in the `tests/` directory once set up.
