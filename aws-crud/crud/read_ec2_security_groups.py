from gateway import do_parse_json
import boto3


def do_read_ec2_security_groups(json):
    json_data = do_parse_json(json)
    ec2_client = boto3.client('ec2', region_name=json_data["metadata"]["aws-region"])
    try:
        aws_sg = ec2_client.describe_security_groups()
        security_groups = aws_sg['SecurityGroups']
        if not aws_sg:
            print("No security groups found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of Security Groups:")
            for group in security_groups:
                print(f"\tGroup ID: {group['GroupId']}")
                print(f"\t\tGroup Name: {group['GroupName']}")
                print(f"\t\tDescription: {group['Description']}")
    except ec2_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
