
from openai import OpenAI

from . import LLMClient


class OpenAIClient(LLMClient):

    def __init__(self, token: str, model: str):
        self._token = token
        self._model = model

    def generate_response(self, prompt: list[dict], **options) -> str:
        client = OpenAI(api_key=self._token)
        response = client.chat.completions.create(
            model=self._model,
            messages=prompt,
            **options
        )
        
        return response.choices[0].message.content
    
