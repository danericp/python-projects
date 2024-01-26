from gateway import do_parse_json, do_setup_aws_client


def do_read_ec2_key_pairs(json):
    json_data = do_parse_json(json)
    ec2_client = do_setup_aws_client(json_data, 'ec2')
    try:
        aws_out = ec2_client.describe_key_pairs()
        key_pairs = aws_out['KeyPairs']
        if not aws_out:
            print("No key pairs found in the account.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of Key Pairs:")
            for key_pair in key_pairs:
                print(f"\tKey ID: {key_pair['KeyPairId']}")
                print(f"\t\tKey Created: {key_pair['CreateTime']}")
                print(f"\t\tKey Fingerprint: {key_pair['KeyFingerprint']}")
                print(f"\t\tKey Name: {key_pair['KeyName']}")
                print(f"\t\tKey Tags: {key_pair['Tags']}")
                print(f"\t\tKey Type: {key_pair['KeyType']}")
    except ec2_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    return "test"
