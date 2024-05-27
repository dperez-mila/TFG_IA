
from pathlib import Path


def read_txt_file(filepath: Path):
    with open(filepath, 'r') as txt_file:
        content = txt_file.read()
    return content 

def write_txt_file(filepath: Path, content: str):
    try:
        with open(filepath, 'w') as txt_file:
            txt_file.write(content)
    except OSError as e:
        print(f"An error occured while opening the file: {e}")

