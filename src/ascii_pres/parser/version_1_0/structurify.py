def structurify(tokenized_sections: dict[str, list[list[str]]]) -> dict[str, dict[str, dict[str, str]]]:
    """
    Structures tokens from token list into:
    {
    <section>: {
        <keyword>: {
            <option> = <value>
    }}}

    :param tokenized_sections: dict of section_names and _bodies
    :return: data: {section: {keyword: {option: value=<value>}}}
    """

    # === PSEUDOCODE ===
    # keyword_collection = {}
    #
    # for section in tokenized_sections:
    #     if section_name = content:
    #         data["content"] = section_body
    #         continue
    #     # =====
    #     if section_name not in keyword_collection:
    #         keyword_collection[section_name] = {}
    #     # =====
    #     for line in section_body:
    #         for token in line
    #             if token in "{}":
    #                 continue
    #
    #             elif token.endswith(":"):
    #                 keyword = token.strip(":")
    #                 options = {}
    #
    #             else:
    #                 option, value = token.split("=")
    #                 options[option] = value
    #
    #         keyword_collection[section_name][keyword] = options
    #
    # return keyword_collection

    print("ascii_pres.parser.version_1_0.structurify.structurify() not implemented")
    return None