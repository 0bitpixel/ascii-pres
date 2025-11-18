from pathlib import Path
import re

from ... import constants
from . import exceptions


SECTION_NAME_REGEX = re.compile(r"STARTSECTION\s+(\S+)$")


def sectionize(input_file_content: list[str]) -> dict[str, list[str]]:
    """
    Splits an input .slide file into it's sections according to its delimiters,
    erroring if duplicate sections are found or if sections are nested.

    :param input_file_content: Content as list of lines to split into sections.
    :return dict[str, list[str]]: dict of sections as {section_name: section_body}.
    """

    # === PSEUDOCODE ===
    # for line in file:
    #     if STARTSECTION:
    #         if section_name in encountered_sections: error (duplicate section)
    #         else: append section_name to encountered_sections; init dict {section_name: None}; section started=true
    #     if not ENDSECTION:
    #         if STARTSECTION: error (nested sections)
    #         else: append line to body
    #     if ENDSECTION:
    #         if not startsection_encountered: error (endsection before startsection)
    #         else: dict: {section_name: section_body}
    # return dict


    section_name: str | None = None
    encountered_sections: list[str] = []
    section_data: dict[str, list[str]] = {}
    startsection_encountered: bool = False

    for line_number, line in enumerate(input_file_content, start=1):
        line = line.strip()
        if not line:
            continue

        if line.startswith("STARTSECTION"):
            if startsection_encountered:
                raise exceptions.NestedSectionError(
                    f"Line {line_number}: "
                     "nested sections"
                )
            if not SECTION_NAME_REGEX.match(line):
                raise exceptions.InvalidSectionError(
                    f"Line {line_number}: '{line}': "
                     "invalid section declaration"
                )
            section_name = SECTION_NAME_REGEX.match(line).group(1)
            if section_name in encountered_sections:
                raise exceptions.DuplicateSectionError(
                    f"Line {line_number}: "
                    f"duplicate sections"
                )
            else:
                encountered_sections.append(section_name)
                section_data[section_name] = []
                startsection_encountered = True
                continue

        elif line == "ENDSECTION":
            if not startsection_encountered:
                raise exceptions.UnopenedSectionError(
                    f"Line {line_number}: "
                    f"ENDSECTION without STARTSECTION"
                )
            else:
                startsection_encountered = False

        else:
            if not startsection_encountered or section_name is None:
                raise exceptions.OutsideSectionError(
                    f"Line {line_number}: "
                     "content outside section"
                )
            else:
                section_data[section_name].append(line)

    if startsection_encountered:
        raise exceptions.UnclosedSectionError("unclosed section")

    return section_data
