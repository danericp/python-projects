from gateway import do_parse_json, do_setup_aws_client

from prettytable import PrettyTable


def do_read_iam_policies(json):
    json_data = do_parse_json(json)
    out_table = PrettyTable(["Name", "Policies"])
    out_table.align["Name"] = "r"
    out_table.align["Policies"] = "l"
    out_table.border = True
    out_table.header = False

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
                out_table.add_row([aws_policy['PolicyName'],
                                   f"\n"
                                   f"PolicyName: {aws_policy['PolicyName']}"
                                   f"PolicyId: \n{aws_policy['PolicyId']}"
                                   f"CreateDate: \n{aws_policy['CreateDate']}"
                                   f"UpdateDate: \n{aws_policy['UpdateDate']}"
                                   f"Arn: \n{aws_policy['Arn']}"
                                   f"Path: \n{aws_policy['Path']}"
                                   f"DefaultVersionId: \n{aws_policy['DefaultVersionId']}"
                                   f"AttachmentCount: \n{aws_policy['AttachmentCount']}"])
                # print(f"\tPolicyName: {aws_policy['PolicyName']}")
                # print(f"\t\tPolicyId: {aws_policy['PolicyId']}")
                # print(f"\t\tCreateDate: {aws_policy['CreateDate']}")
                # print(f"\t\tUpdateDate: {aws_policy['UpdateDate']}")
                # print(f"\t\tArn: {aws_policy['Arn']}")
                # print(f"\t\tPath: {aws_policy['Path']}")
                # print(f"\t\tDefaultVersionId: {aws_policy['DefaultVersionId']}")
                # print(f"\t\tAttachmentCount: {aws_policy['AttachmentCount']}")
    except iam_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print(out_table)
