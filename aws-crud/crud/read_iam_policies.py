from gateway import do_parse_json
import boto3


def do_read_iam_policies(json):
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
        aws_out = iam_client.list_policies(Scope='All')
        aws_policies = aws_out['Policies']
        if not aws_out:
            print("No IAM policies found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of IAM Policies:")
            for aws_policy in aws_policies:
                print(f"\tPolicyName: {aws_policy['PolicyName']}")
                print(f"\t\tPolicyId: {aws_policy['PolicyId']}")
                print(f"\t\tCreateDate: {aws_policy['CreateDate']}")
                print(f"\t\tUpdateDate: {aws_policy['UpdateDate']}")
                print(f"\t\tArn: {aws_policy['Arn']}")
                print(f"\t\tPath: {aws_policy['Path']}")
                print(f"\t\tDefaultVersionId: {aws_policy['DefaultVersionId']}")
                print(f"\t\tAttachmentCount: {aws_policy['AttachmentCount']}")
                # print(f"\t\tUser Id: {aws_user['UserId']}")
                # print(f"\t\tPath: {aws_user['Path']}")
                # print(f"\t\tArn: {aws_user['Arn']}")
                # print(f"\t\tCreateDate: {aws_user['CreateDate']}")
    except iam_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
