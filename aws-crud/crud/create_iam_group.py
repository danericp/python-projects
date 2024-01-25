from gateway import do_parse_json
from boto3 import client


def do_create_iam_group(json):
    json_data = do_parse_json(json)
    # AWS credentials
    aws_region = json_data['metadata']['aws-region']
    aws_access_key = json_data['metadata']['key-aws-access']
    aws_secret_key = json_data['metadata']['key-aws-secret']
    iam_group_name = json_data['create-iam-group']['name']
    url_endpoint = json_data['metadata']['url-endpoint']

    # Create IAM client
    if url_endpoint:
        print("Endpoint URL configuration found.")
        iam_client = client('iam', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                            endpoint_url=url_endpoint, region_name=aws_region)
    else:
        iam_client = client('iam', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                            region_name=aws_region)

    try:
        # Create IAM group
        iam_client.create_group(GroupName=iam_group_name)
        print(f"IAM group '{iam_group_name}' created successfully.")
    except Exception as e:
        print(f"Error creating IAM group: {e}")
