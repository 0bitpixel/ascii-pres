from pathlib import Path
from typing import Literal
import re

from ..exceptions import SlideSyntaxError
from ... import constants
from .. import data


def parse(file_path: Path, parser_mode: Literal["parse", "validate"] = "parse") -> data.SlideDict:
    slide_data = data.get_default_slide()

    with open(file_path, encoding=constants.DEFAULT_ENCODING) as file:
        file_content = file.readlines()

    slide_data = extract_ascii_escape(file_path, file_content, slide_data, parser_mode)
    parse_sections(file_path, file_content, slide_data, parser_mode)

    return slide_data


def extract_ascii_escape(
        file_path: Path,
        file_content: list[str],
        slide_data: data.SlideDict,
        parser_mode: Literal["parse", "validate"] = "parse",
):
    escapers = []
    for line_number, line in enumerate(file_content):
        if m := re.search(r"@@@!!!\s*(\d+),(\d+)\s*!!!@@@", line):
            escapers.append(m)
    if len(escapers) == 0:
        return slide_data
    if len(escapers) > 1:
        raise SlideSyntaxError(f"More than one ASCII-escaper in {file_path}")
    if parser_mode == "parse":
        start, end = map(int, escapers[0].groups())
        slide_data["slide"] = "\n".join(file_content[start-1:end-1])
    return slide_data


def parse_sections(
        file_path: Path,
        file_content: list[str],
        slide_data: data.SlideDict,
        parser_mode: Literal["parse", "validate"] = "parse"
):
    for section in split_into_sections(file_path, file_content):
        match section["type"]:
            case "SLIDE":
                if parser_mode == "parse":
                    slide_data["slide"] = section["content"]
                continue
            case "AREAS":
                parse_area(file_path, section["content"], slide_data, parser_mode)


def split_into_sections(file_path: Path, file_content: list[str]):
    section = {}
    start_found = False

    for line_number, line in enumerate(file_content):
        section_start_match = re.match(r"^(SLIDE|AREAS|CONFIG)\[\[\[$", line.strip())
        if section_start_match:
            section = {
                "type":section_start_match.group(1), "start":line_number,
            }
            start_found = True

        section_end_match = re.match(r"^]]]$", line.strip())
        if section_end_match:
            if not start_found:
                raise SlideSyntaxError(
                    f"Found closing delimiter ]]] before opening delimiter in {file_path} at line {line_number}"
                )
            section["end"] = line_number

            yield{
                "type": section["type"],
                "content": file_content[section["start"]:section["end"]],
            }

            start_found = False

    if start_found:
        raise SlideSyntaxError(f"File {file_path} ends before closing section {section["type"]}")


def parse_area(
        file_path: Path,
        section_content: list[str],
        slide_data: data.SlideDict,
        parser_mode: Literal["parse", "validate"] = "parse"
):
    for line in section_content:
        tokens = line.split()
        slide_data["areas"][int(tokens[0])] = data.get_default_area()

        coord1 =  (int(tokens[2].split(",")[0]), int((tokens[2].split(",")[1])))
        coord2 = (int(tokens[3].split(",")[0]), int((tokens[3].split(",")[1])))
        # TODO: Parse Area Content
        # identify token -> write

        slide_data["areas"][int(tokens[0])]["coord1"] = coord1
        slide_data["areas"][int(tokens[0])]["coord2"] = coord2

# TODO: Parse Config Content


