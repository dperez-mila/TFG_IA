
from abc import ABC, abstractmethod

class LLMClient(ABC):

    @abstractmethod
    def generate_response(self, prompt: list[dict], **options) -> str:
        pass

