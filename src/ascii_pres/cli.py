from sys import argv as arguments
from pathlib import Path


def get_input_folder() -> Path:
    if len(arguments) < 2:
        raise TypeError("Not enough arguments")
    input_folder_path = Path(arguments[1])

    if not input_folder_path.exists():
        raise FileNotFoundError("Input folder not found")

    if not input_folder_path.is_dir():
        raise ValueError("Not a directory")

    return input_folder_path
