from gateway import do_parse_json, do_setup_aws_client


def do_attach_iam_policy_to_role(json_entry):
    json_data = do_parse_json(json_entry)

    # IAM prerequisites
    iam_policy_name = json_data['attach-policy-to-role']['policy']
    iam_role_name = json_data['attach-policy-to-role']['role']

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        # Attach IAM policy to role
        iam_client.attach_role_policy(
            RoleName=iam_role_name,
            PolicyArn=f'arn:aws:iam::000000000000:policy/{iam_policy_name}'
        )
        print(f"IAM policy '{iam_policy_name}' has been attached to '{iam_role_name}'.")
    except Exception as e:
        print(f"Error creating IAM policy: {e}")
