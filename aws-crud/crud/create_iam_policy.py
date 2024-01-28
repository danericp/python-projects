from gateway import do_parse_json, do_setup_aws_client
import json


def do_create_iam_policy(json_entry):
    json_data = do_parse_json(json_entry)

    # IAM prerequisites
    iam_policy_name = json_data['create-iam-policy']['name']

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        print(json_data['create-iam-policy']['document'])
        # Create IAM policy
        iam_client.create_policy(
            PolicyName=iam_policy_name,
            PolicyDocument=json.dumps(json_data['create-iam-policy']['document'])
        )

        print(f"IAM policy '{iam_policy_name}' created successfully.")
    except Exception as e:
        print(f"Error creating IAM policy: {e}")
