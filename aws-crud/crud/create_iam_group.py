from gateway import do_parse_json, do_setup_aws_client


def do_create_iam_group(json):
    json_data = do_parse_json(json)

    # IAM prerequisites
    iam_group_name = json_data['create-iam-group']['name']

    # Setup IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        # Create IAM group
        iam_client.create_group(GroupName=iam_group_name)
        print(f"IAM group '{iam_group_name}' created successfully.")
    except Exception as e:
        print(f"Error creating IAM group: {e}")
