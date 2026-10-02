# LIORA

LIORA is an AI-powered, adaptive, memory-aware learning assistant using Endee Vector DB.

## Current Project Status
- Phase 0 (Foundation & Spikes) is complete.
- Phase 1 (Core Implementation) is in progress. The initial UI shell has been built.

## Architecture Status
- Architecture follows the approved LIORA blueprint.
- PostgreSQL connectivity was verified.
- Groq connectivity was verified.
- Endee Python API/client contract was investigated.
- Endee runtime/cloud access remains pending because workspace access is unresolved.

## Technology Stack
- **Python:** 3.12+
- **Vector Database:** Endee Vector DB (Cloud/Remote)
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
   pip install . # or pip install <requirements>
   ```
4. Copy `.env.example` to `.env` and fill in secrets.

## Running the Application
To run the Liora Streamlit application locally:
```bash
streamlit run app/ui/main.py
```

## Running Tests
To run the test suite:
```bash
python -m pytest tests/
```
