def tokenize(input_sections: dict[str, list[str]]) -> dict[str, list[list[str]]]:
    """
    Splits lines of sections into tokens and joins together {}.

    :param input_sections: dict of section names with their content as a list of lines
    :return: dict with section name with content as list of lines, each a list of tokens
    """

    """
    === PSEUDOCODE ===
    for section in sections
        multiline_mode = False     
        line_collection = []
        if section not in output:
            output[section] = []
        for line in section:
            if "{" in line:
                multiline_mode = True
                line_collection.append(line)
            if line == "}":
                multiline_mode = False
                output[section].append(line_collection.join().)
            if not multiline_mode and not line.endswith("{"):
                output[section].append(line.split())
    return output
    """


    print("ascii_pres.parser.version_1_0.tokenize() not implemented")
    return None