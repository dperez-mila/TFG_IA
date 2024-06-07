
import json
from pathlib import Path


def load_json_file(filepath: Path):
    try:
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"The file {filepath} does not exist!")
        return None
    except json.JSONDecodeError:
        print(f"The file {filepath} contains invalid JSON!")
        return None

def dump_json_file(filepath: Path, data: list[dict] | dict):
    if not isinstance(data, (list, dict)):
        raise ValueError("Expected data type to be a list of dictionaries or a dictionary!")
    try:
        with open(filepath, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"An error occured while writting to the file: {e}")

def clear_json_file(filepath: Path, roles_to_clear: list[str] = []):
    try:
        prompt = load_json_file(filepath)
        filtered_data = [message for message in prompt if message.get('role') not in roles_to_clear]
        with open(filepath, 'w') as json_file:
            json.dump(filtered_data, json_file, indent=4)
    except IOError as e:
        print(f"An error occured while clearing the file: {e}")

