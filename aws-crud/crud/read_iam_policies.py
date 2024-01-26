from gateway import do_parse_json, do_setup_aws_client
import boto3


def do_read_iam_policies(json):
    json_data = do_parse_json(json)

    # Create IAM client
    iam_client = do_setup_aws_client(json_data, 'iam')

    try:
        aws_out = iam_client.list_policies(Scope=json_data['read-iam-policies']['scope'])
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
    except iam_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
