from sys import argv as command_line_arguments
from time import sleep
from sys import exit
import traceback

from ascii_pres import cli
from ascii_pres import parse
from ascii_pres import areas
from ascii_pres import non_area
from ascii_pres.state import state


CLEAR_SCREEN = "\033[2J"
RESET_STYLE = "\033[0m"
HOME_CURSOR = "\033[H"
RESET_TERMINAL = f"{CLEAR_SCREEN}{RESET_STYLE}{HOME_CURSOR}"


def main():
    state.working_directory = cli.get_input_folder(command_line_arguments)
    state.config = parse.config_file(state.working_directory / "config.toml")

    parse.check_slides(state.working_directory)

    while state.run:
        state.current_slide += 1
        if not state.current_slide_exists:
            state.run = False
            break
        slide_data = parse.slide(state.current_slide)

        # FIXME: None -> slide_data.config.auto_advance = placeholder until slide_data structure is known
        if not None:
            _wait_for_trigger()
        else:
            # FIXME: 0 -> slide_data.config.auto_advance_delay = placeholder until slide_data structure is known
            sleep(0)
        non_area.draw(slide_data)
        areas.draw(slide_data)

    _wait_for_trigger()


def _wait_for_trigger():
    # TODO: implement main._wait_for_trigger()
    print("NOT IMPLEMENTED: main._wait_for_trigger()")

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
