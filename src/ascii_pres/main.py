from ascii_pres import cli
from ascii_pres import config


def main():
    input_folder_path = cli.get_input_folder()
    configuration = config.parse_config_file(input_folder_path)

if __name__ == '__main__':
    main()