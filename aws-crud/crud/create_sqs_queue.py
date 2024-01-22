from gateway import do_parse_json
from boto3 import client


def do_create_sqs_queue(json):
    json_data = do_parse_json(json)
    # AWS credentials
    aws_region = json_data['metadata']['aws-region']
    aws_access_key = json_data['metadata']['key-aws-access']
    aws_secret_key = json_data['metadata']['key-aws-secret']
    queue_name = json_data['create-sqs-queue']['queue-name']
    url_endpoint = json_data['metadata']['url-endpoint']

    # Create SQS client
    if url_endpoint:
        print("Endpoint URL configuration found.")
        sqs_client = client('sqs', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                            endpoint_url=url_endpoint, region_name=aws_region)
    else:
        sqs_client = client('sqs', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                            region_name=aws_region)

    try:
        # Create SQS Queue
        response = sqs_client.create_queue(
            QueueName=queue_name
        )
        print(f"SQS queue '{queue_name}' created successfully.")
        print(response)
    except Exception as e:
        print(f"Error creating SQS queue: {e}")
