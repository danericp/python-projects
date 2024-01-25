from gateway import do_parse_json
import boto3


def do_read_iam_users(json):
    json_data = do_parse_json(json)
    # AWS credentials
    aws_region = json_data['metadata']['aws-region']
    aws_access_key = json_data['metadata']['key-aws-access']
    aws_secret_key = json_data['metadata']['key-aws-secret']
    url_endpoint = json_data['metadata']['url-endpoint']

    # Create IAM client
    if url_endpoint:
        print("Endpoint URL configuration found.")
        iam_client = boto3.client('iam', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                                  endpoint_url=url_endpoint, region_name=aws_region)
    else:
        iam_client = boto3.client('iam', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                                  region_name=aws_region)

    try:
        aws_out = iam_client.list_users()
        aws_users = aws_out['Users']
        if not aws_out:
            print("No key pairs found in the account.")
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
