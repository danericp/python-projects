from gateway import do_parse_json, do_setup_aws_client


def do_create_iam_user(json):
    json_data = do_parse_json(json)

    # IAM prerequisites
    iam_user_name = json_data['create-iam-user']['name']

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        # Create IAM user
        iam_client.create_user(UserName=iam_user_name)
        print(f"IAM user '{iam_user_name}' created successfully.")
    except Exception as e:
        print(f"Error creating IAM user: {e}")
