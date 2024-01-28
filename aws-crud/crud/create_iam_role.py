from gateway import do_parse_json, do_setup_aws_client
import json


def do_create_iam_role(json_entry):
    json_data = do_parse_json(json_entry)

    # IAM prerequisites
    iam_role_name = json_data['create-iam-role']['name']

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        print(json_data['create-iam-role']['content'])
        # Create IAM role
        iam_client.create_role(
            RoleName=iam_role_name,
            AssumeRolePolicyDocument=json.dumps(json_data['create-iam-role']['content'])
        )
        print(f"IAM role '{iam_role_name}' created successfully.")
    except Exception as e:
        print(f"Error creating IAM role: {e}")
