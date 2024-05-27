
from . import LLMClient

class GPT4AllClient(LLMClient):
    
    def __init__(self, token, model, model_path):
        super().__init__(token, model)
        self._model_path = model_path
        
    def generate_response(self):
        return super().generate_response()
    
    