from pathlib import Path


def sectionize(input_file_path: Path) -> dict[str, list[str]]:
    """
    Splits an input .slide file into it's sections according to its delimiters,
    erroring if duplicate sections are found or if sections are nested.

    :param input_file_path: File to split into sections.
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
    #         if not section_started: error (endsection before startsection)
    #         else: dict: {section_name: section_body}
    # return dict

    print("ascii_pres.parser.version_1_0.sectionize.sectionize() not implemented")
    return None