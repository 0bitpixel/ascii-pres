from pathlib import Path
import tomllib

from ascii_pres.state import state


def parse_config_file(input_folder_path: Path):
    with open(input_folder_path / 'config.toml', "+rb") as f:
        config = tomllib.load(f)
        state.update_config(config)
