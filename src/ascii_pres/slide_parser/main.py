from pathlib import Path
from typing import Literal
import re

from .. import constants
from . import data
from .exceptions import SlideSyntaxError
from .parsers.choose_parser import choose_parser


FORMAT_PATTERN = r"###\s*FORMAT\s*=\s*([0-9]+\.[0-9]+)\s*###"


def parser(file_path: Path, parser_mode: Literal["parse", "validate"] = "parse") -> data.SlideDict:
    with open(file_path, encoding=constants.DEFAULT_ENCODING) as file:
        slide_file_content = file.read()

    format_match = re.match(FORMAT_PATTERN, slide_file_content)
    if not format_match:
        raise SlideSyntaxError(f"missing FORMAT declaration in {file_path}")

    file_format = format_match.group(1)
    if file_format not in constants.VALID_FORMATS:
        raise SlideSyntaxError(f"invalid FORMAT declaration in {file_path}: {file_format}")

    slide_data = choose_parser(file_path, file_format, parser_mode)

    return slide_data
