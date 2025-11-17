from pathlib import Path

def start_parser(input_path: Path, single_file: str=None):
    """
    Chooses and starts the appropriate parser.

    :param input_path: Path to a folder containing files-to-be-parsed.
    :param single_file: Optional value specifying a single file to parse, not the whole directory like by default.
    :return:
    """

    # === PSEUDOCODE ===
    # if single file:
    #     check type by extension
    #     check format if .slide, else error (not supported)
    #     call appropriate parser
    # else:
    #     for file in path:
    #         check format if .slide, else skip
    #         call appropriate parser
    # return parsed_data or None

    print("ascii_pres.parser.start_parser.start_parser not implemented")
    return None