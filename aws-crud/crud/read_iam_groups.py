from gateway import do_parse_json, do_setup_aws_client


def do_read_iam_groups(json):
    json_data = do_parse_json(json)

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        aws_out = iam_client.list_groups()
        aws_groups = aws_out['Groups']
        if not aws_out:
            print("No groups found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of IAM Groups:")
            for aws_group in aws_groups:
                print(f"\tGroup Name: {aws_group['GroupName']}")
                print(f"\t\tGroup Id: {aws_group['GroupId']}")
                print(f"\t\tPath: {aws_group['Path']}")
                print(f"\t\tArn: {aws_group['Arn']}")
                print(f"\t\tCreateDate: {aws_group['CreateDate']}")
    except iam_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
