from pathlib import Path
from typing import Literal

from . import data


def parser(file_path: Path, parser_mode: Literal["parse", "validate"] = "parse") -> data.SlideDict:
    pass
