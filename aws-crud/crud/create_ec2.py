from gateway import do_parse_json, do_setup_aws_client


def do_create_ec2(json):
    json_data = do_parse_json(json)

    # Create EC2 client
    ec2 = do_setup_aws_client(json_data, 'ec2')

    # Specify the parameters for the EC2 instance
    instance_params = {
        'ImageId': json_data['create-ec2']['image-id'],  # Replace with a valid AMI ID
        'InstanceType': json_data['create-ec2']['instance-type'],
        'KeyName': json_data['create-ec2']['key-name'],  # Replace with your key pair name
        'MinCount': json_data['create-ec2']['min-count'],
        'MaxCount': json_data['create-ec2']['max-count']
    }

    # Launch EC2 instance
    response = ec2.run_instances(**instance_params)

    # Get instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Launched instance ID: {instance_id}")
