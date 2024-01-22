from gateway import do_parse_json
from boto3 import client


def do_create_s3_bucket(json):
    json_data = do_parse_json(json)
    # AWS credentials
    aws_region = json_data['metadata']['aws-region']
    aws_access_key = json_data['metadata']['key-aws-access']
    aws_secret_key = json_data['metadata']['key-aws-secret']
    bucket_name = json_data['create-s3-bucket']['bucket-name']
    url_endpoint = json_data['metadata']['url-endpoint']

    # Create S3 client
    if url_endpoint:
        print("Endpoint URL configuration found.")
        s3_client = client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                           endpoint_url=url_endpoint, region_name=aws_region)
    else:
        s3_client = client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                           region_name=aws_region)

    try:
        # Create S3 bucket
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")
