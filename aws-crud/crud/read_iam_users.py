from gateway import do_parse_json, do_setup_aws_client
import boto3


def do_read_iam_users(json):
    json_data = do_parse_json(json)

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        aws_out = iam_client.list_users()
        aws_users = aws_out['Users']
        if not aws_out:
            print("No users found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of IAM Users:")
            for aws_user in aws_users:
                print(f"\tUser Name: {aws_user['UserName']}")
                print(f"\t\tUser Id: {aws_user['UserId']}")
                print(f"\t\tPath: {aws_user['Path']}")
                print(f"\t\tArn: {aws_user['Arn']}")
                print(f"\t\tCreateDate: {aws_user['CreateDate']}")
    except iam_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
