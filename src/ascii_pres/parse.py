from pathlib import Path
import tomllib

from ascii_pres.slide_parser import data


def config_file(config_file_path: Path) -> dict:
    with open(config_file_path, "+rb") as f:
        config = tomllib.load(f)
        return config

def check_slides(working_directory: Path):
    # TODO: implement parse.check_slides()
    print("NOT IMPLEMENTED: parse.check_slides()")

def slide(current_slide: int) -> data.SlideDict:
    # TODO: implement parse.slide()
    print("NOT IMPLEMENTED: parse.slide()")

    #return slide_data
    return None