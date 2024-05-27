
from . import LLMService

from ...clients import GPT4AllClient


class GPT4AllService(LLMService):

    def __init__(self, key: str, model: str):
        self._llm_client = GPT4AllClient(key, model)
    
    def generate_response(self, prompt: list[dict]) -> str:
        return self._llm_client.generate_response(prompt)

