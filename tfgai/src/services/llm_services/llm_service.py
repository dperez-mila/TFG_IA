
from abc import ABC, abstractmethod

from ...clients import LLMClient


class LLMService(ABC):

    def __init__(self, key: str, model: str):
        self._llm_client = LLMClient(key, model)

    @abstractmethod
    def generate_response(self, prompt: list[dict]) -> str:
        pass

