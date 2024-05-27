
from . import LLMService

from ...clients import OpenAIClient


class OpenAIService(LLMService):

    def __init__(self, key: str, model: str):
        self._llm_client = OpenAIClient(key, model)
    
    def generate_response(self, prompt: list[dict]) -> str:
        return self._llm_client.generate_response(prompt) 
    
