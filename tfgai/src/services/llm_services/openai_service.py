
from . import LLMService

from ...clients import OpenAIClient


class OpenAIService(LLMService):

    def __init__(self, token: str, model: str):
        self._llm_client = OpenAIClient(token, model)
    
    def generate_response(self, prompt: list[dict],  **options) -> str:
        return self._llm_client.generate_response(prompt, **options) 
            
