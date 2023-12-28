from gateway import do_exec
import argparse


def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='AWS CRUD Management',
        description='Manage you AWS services individually.',
        epilog="Tested in Python 3.12"
    )
    obj_parser.add_argument("-a", "--action", dest="action", help="Pre-defined action", required=True)
    options = obj_parser.parse_args()
    return options


if __name__ == "__main__":
    obj_options = get_arguments()
    str_action = obj_options.action
    path_json = "config.json"
    do_exec(path_json, str_action)
