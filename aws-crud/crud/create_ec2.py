from gateway import do_parse_json
from boto3 import client


def do_create_ec2(json):
    json_data = do_parse_json(json)
    # AWS credentials
    aws_access_key = json_data['metadata']['key-aws-access']
    aws_secret_key = json_data['metadata']['key-aws-secret']
    aws_region = json_data['metadata']['aws-region']
    url_endpoint = json_data['metadata']['url-endpoint']

    # Create EC2 client
    if json_data["metadata"]["url-endpoint"]:
        print("Endpoint URL configuration found.")
        ec2 = client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                     endpoint_url=url_endpoint, region_name=aws_region)
    else:
        ec2 = client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                     region_name=aws_region)

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
