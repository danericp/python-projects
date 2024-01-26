from gateway import do_parse_json, do_setup_aws_client


def do_create_s3_bucket(json):
    json_data = do_parse_json(json)
    bucket_name = json_data['create-s3-bucket']['bucket-name']

    # Create S3 client
    s3_client = do_setup_aws_client(json_data, 's3')

    try:
        # Create S3 bucket
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")
