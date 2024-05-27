
from openai import OpenAI

from . import LLMClient


class OpenAIClient(LLMClient):

    def __init__(self, token, model):
        super().__init__(token, model)

    def generate_response(self, prompt: list[dict], **kwargs):
        client = OpenAI(api_key=self._token)
        response = client.chat.completions.create(
            model=self._model,
            messages=prompt,
            **kwargs
        )
        return response.choices[0].message.content
    
