import os
from abc import ABC, abstractmethod
from typing import Optional

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        pass

class GroqProvider(LLMProvider):
    def __init__(self, model_name: str = "llama3-8b-8192"):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        self.client = Groq(api_key=self.api_key)
        self.model_name = model_name

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model_name,
                timeout=30.0  # Test timeout handling
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during generation: {str(e)}"

if __name__ == "__main__":
    print("--- GROQ PROVIDER SPIKE ---")
    try:
        provider = GroqProvider()
        print("Provider initialized successfully.")
        
        # Test basic generation if API key is valid (which we don't assume here)
        # prompt = "Say hello!"
        # response = provider.generate(prompt)
        # print("Response:", response)
        
    except ValueError as e:
        print("Initialization failed as expected without key:", str(e))
    except Exception as e:
        print("Unexpected error:", str(e))
