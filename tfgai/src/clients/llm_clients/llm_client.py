
from abc import ABC, abstractmethod

class LLMClient(ABC):

    def __init__(self, token, model):
        self._token = token
        self._model = model

    @abstractmethod
    def generate_response(self, prompt: list[dict], **kwargs):
        pass

