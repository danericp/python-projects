from gateway import do_parse_json, do_setup_aws_client


def do_create_sqs_queue(json):
    json_data = do_parse_json(json)
    queue_name = json_data['create-sqs-queue']['queue-name']

    # Create SQS client
    sqs_client = do_setup_aws_client(json_data, 'sqs')

    try:
        # Create SQS Queue
        response = sqs_client.create_queue(
            QueueName=queue_name
        )
        print(f"SQS queue '{queue_name}' created successfully.")
        print(response)
    except Exception as e:
        print(f"Error creating SQS queue: {e}")
