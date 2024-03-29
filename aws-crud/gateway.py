from boto3 import client
from prettytable import PrettyTable
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
        case "attach_policy_to_role":
            import crud.attach_iam_policy_to_role as attach_policy_role
            attach_policy_role.do_attach_iam_policy_to_role(json_config)
        case "create_ec2":
            import crud.create_ec2 as ec2_new
            ec2_new.do_create_ec2(json_config)
        case "create_iam_group":
            import crud.create_iam_group as iam_group_new
            iam_group_new.do_create_iam_group(json_config)
        case "create_iam_policy":
            import crud.create_iam_policy as iam_policy_new
            iam_policy_new.do_create_iam_policy(json_config)
        case "create_iam_role":
            import crud.create_iam_role as iam_role_new
            iam_role_new.do_create_iam_role(json_config)
        case "create_iam_user":
            import crud.create_iam_user as iam_user_new
            iam_user_new.do_create_iam_user(json_config)
        case "create_s3_bucket":
            import crud.create_s3_bucket as s3b_new
            s3b_new.do_create_s3_bucket(json_config)
        case "create_sqs_queue":
            import crud.create_sqs_queue as sqs_new
            sqs_new.do_create_sqs_queue(json_config)
        case "read_ec2_instance_types":
            import crud.read_ec2_instance_types as ec2_it
            ec2_it.do_read_ec2_instance_types(json_config)
        case "read_ec2_key_pairs":
            import crud.read_ec2_key_pairs as ec2_kp
            ec2_kp.do_read_ec2_key_pairs(json_config)
        case "read_ec2_security_groups":
            import crud.read_ec2_security_groups as ec2_sg
            ec2_sg.do_read_ec2_security_groups(json_config)
        case "read_iam_groups":
            import crud.read_iam_groups as iam_groups
            iam_groups.do_read_iam_groups(json_config)
        case "read_iam_policies":
            import crud.read_iam_policies as iam_policies
            iam_policies.do_read_iam_policies(json_config)
        case "read_iam_users":
            import crud.read_iam_users as iam_users
            iam_users.do_read_iam_users(json_config)
        case _:
            print(f"Invalid action '{action}'.")
            exit()
    return action


def do_parse_json(file_json):
    with open(file_json, 'r') as file:
        data_json = json.load(file)
    return data_json


def do_setup_prettytable(array_headers):
    return PrettyTable(array_headers)


def do_setup_aws_client(json_data, service):
    aws_client = None
    try:
        aws_access_key = json_data['metadata']['key-aws-access']
        aws_secret_key = json_data['metadata']['key-aws-secret']
        aws_region = json_data['metadata']['aws-region']
        url_endpoint = json_data['metadata']['url-endpoint']

        # Setup AWS client based on endpoint
        if json_data["metadata"]["url-endpoint"] and service:
            print("Endpoint URL configuration found.")
            aws_client = client(service, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                                endpoint_url=url_endpoint, region_name=aws_region)
        else:
            aws_client = client(service, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                                region_name=aws_region)

    except Exception as e:
        print(f"Exception: {e}")
    return aws_client
