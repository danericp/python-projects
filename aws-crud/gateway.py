import json
import os


def do_check_file_exists(path_file):
    if os.path.exists(path_file):
        print(f"The file '{path_file}' exists.")
    else:
        print(f"The file '{path_file}' does not exist.")
        exit()


def do_exec(json_config, action):
    do_check_file_exists(json_config)
    match action:
        case "read-ec2-security-groups":
            import crud.read_ec2_security_groups as ec2_sg
            ec2_sg.do_read_ec2_security_groups(json_config)
        case _:
            print(f"Invalid action '{action}'.")
            exit()
    return action


def do_parse_json(file_json):
    with open(file_json, 'r') as file:
        data_json = json.load(file)
    return data_json
