from gateway import do_parse_json, do_setup_aws_client


def do_read_ec2_security_groups(json):
    json_data = do_parse_json(json)
    ec2_client = do_setup_aws_client(json_data, 'ec2')
    try:
        aws_out = ec2_client.describe_security_groups()
        security_groups = aws_out['SecurityGroups']
        if not aws_out:
            print("No security groups found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of Security Groups:")
            for group in security_groups:
                print(f"\tGroup ID: {group['GroupId']}")
                print(f"\t\tGroup Description: {group['Description']}")
                print(f"\t\tGroup Name: {group['GroupName']}")
                print(f"\t\tGroup Owner Id: {group['OwnerId']}")
                print(f"\t\tGroup VPC Id: {group['VpcId']}")
                print(f"\t\tGroup IP Permissions:")
                for permission in group['IpPermissions']:
                    print(f"\t\t\tProtocol: {permission['IpProtocol']}")
                    print(f"\t\t\t\tIP Ranges: {permission['IpRanges']}")
                    print(f"\t\t\t\tIPv6 Ranges: {permission['Ipv6Ranges']}")
                    print(f"\t\t\t\tPrefixListIds: {permission['PrefixListIds']}")
                    print(f"\t\t\t\tUserIdGroupPairs: {permission['PrefixListIds']}")
                print(f"\t\tGroup IP Permissions Egress:")
                for permission in group['IpPermissionsEgress']:
                    print(f"\t\t\tProtocol: {permission['IpProtocol']}")
                    print(f"\t\t\t\tIP Ranges: {permission['IpRanges']}")
                    print(f"\t\t\t\tIPv6 Ranges: {permission['Ipv6Ranges']}")
                    print(f"\t\t\t\tPrefixListIds: {permission['PrefixListIds']}")
                    print(f"\t\t\t\tUserIdGroupPairs: {permission['PrefixListIds']}")
    except ec2_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
