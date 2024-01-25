from gateway import do_parse_json
import boto3


def do_read_iam_groups(json):
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
