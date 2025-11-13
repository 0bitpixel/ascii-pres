from typing import Literal
from pathlib import Path

from .. import data
from ..exceptions import SlideSyntaxError
from . import format1_0


def choose_parser(
        file_path: Path,
        file_format: str,
        parser_mode: Literal["parse", "validate"] = "parse"
) -> data.SlideDict:
    match file_format:
        case "1.0":
            return format1_0.parse(file_path, parser_mode)
        case _:
            raise SlideSyntaxError(f"unimplemented FORMAT declaration in {file_path}: {file_format}")