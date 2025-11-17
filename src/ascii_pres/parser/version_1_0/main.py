from pathlib import Path

def main(input_path: Path, single_file: str=None):
    """
    Main data router and caller for version 1.0 parser.

    :param input_path: Path to a folder containing files-to-be-parsed.
    :param single_file: Optional value specifying a single file to parse.
    :return: Parsed Data.
    """

    # === PSEUDOCODE ===
    # main(input_path, single_file=None):
    # if single_file:
    #     data = parse(input_path / single_file)
    #     return data
    # else:  # intended only for file validation
    #     for slide_file in input_path:
    #         _ = parse(input_path / slide_file)
    #     return
    #
    #     parse(input_file):
    #     sections = sectionize(input_file)
    #     tokens = tokenize(sections)
    #     collection = collectify(tokens)
    #     data = dataify(collection)
    ##### valid_data = validate(data)
    # return valid_data


    print("ascii_pres.parser.version_1_0.main.main() not implemented")
    return None