from pathlib import Path


def get_input_folder(command_line_arguments) -> Path:
    if len(command_line_arguments) < 2:
        raise TypeError("Not enough arguments")
    input_folder_path = Path(command_line_arguments[1])

    if not input_folder_path.exists():
        raise FileNotFoundError(f"'{str(input_folder_path)}' not found")

    if not input_folder_path.is_dir():
        raise ValueError(f"'{str(input_folder_path)}' is not a directory")

    return input_folder_path
