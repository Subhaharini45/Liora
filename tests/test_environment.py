import os
import pytest
from app.config import config

def test_environment_variables():
    # In a real run, this would verify that the configuration layer loads correctly.
    # For Phase 0, we just ensure the test suite is wired up.
    assert True

def test_groq_provider_initialization():
    from experiments.llm_spike import GroqProvider
    
    # If API key is missing, it should raise ValueError
    if not os.getenv("GROQ_API_KEY"):
        with pytest.raises(ValueError):
            provider = GroqProvider()
    else:
        provider = GroqProvider()
        assert provider.model_name == "llama3-8b-8192"
