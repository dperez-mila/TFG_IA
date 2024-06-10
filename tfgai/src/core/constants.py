
import os
from pathlib import Path

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

CANVAS_BASE_URL = "https://aula.uoc.edu/api/v1/"

PROMPT_TEMPLATE_FILEPATH = Path(__file__).parent.parent / "messages" / "prompt_template.txt"
PROMPT_FILEPATH = Path(__file__).parent.parent / "messages" / "prompt.json"
PROMPT_LAST_MESSAGE_FILEPATH = Path(__file__).parent.parent / "messages" / "last_message.txt"
RESPONSE_FILEPATH = Path(__file__).parent.parent / "messages" / "response.txt"

DB_FILEPATH = Path(__file__).parent.parent / "data" / "models.db"

