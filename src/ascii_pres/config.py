from pathlib import Path
import tomllib


def parse_config_file(input_folder_path: Path) -> dict:
    with open(input_folder_path / 'config.toml', "+rb") as f:
        configuration = tomllib.load(f)

    return configuration
