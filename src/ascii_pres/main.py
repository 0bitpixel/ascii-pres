from time import sleep
from sys import exit
import traceback

from ascii_pres import cli
from ascii_pres import config
from ascii_pres import parse
from ascii_pres import draw
from ascii_pres.state import state


CLEAR_SCREEN = "\033[2J"
RESET_STYLE = "\033[0m"
HOME_CURSOR = "\033[H"
RESET_TERMINAL = f"{CLEAR_SCREEN}{RESET_STYLE}{HOME_CURSOR}"


def main():
    input_folder_path = cli.get_input_folder()
    config.parse_config_file(input_folder_path)

    parse.check_slides()

    while state.run:
        slide_data = parse.next_slide()
        if slide_data is None:
            state.run = False
            break
        # FIXME: /s_d.c.a_a/ = placeholder until slide_data structure is known
        if not slide_data.config.auto_advance:
            wait_for_trigger()
        else:
            # FIXME: /s_d.c.a_a_d/ = placeholder until slide_data structure is known
            sleep(slide_data.config.auto_advance_delay)
        draw.non_area(slide_data)
        draw.areas(slide_data)

    wait_for_trigger()


def wait_for_trigger():
    raise NotImplementedError


if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        main()
    except KeyboardInterrupt:
        print(RESET_TERMINAL, end="")
        print("[!] Application interrupted by user")
        exit(0)
    except Exception as ex:
        print(RESET_TERMINAL, end="")
        print(f"[!] An error occurred:")
        traceback.print_exc()
        exit(1)
