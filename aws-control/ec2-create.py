from boto3 import client

# AWS credentials
aws_access_key = ''
aws_secret_key = ''
region = 'us-east-1'

# Create EC2 client
ec2 = client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

# Specify instance details
instance_type = 't2.micro'
image_id = 'ami-0d68f0bd4c34d63a2'  # Specify the AMI ID for the instance
key_name = 'test'  # Specify your key pair name
security_group_ids = ['sg-00fe19126381796fa']  # Specify the security group IDs

# Launch EC2 instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1
)

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"Launched instance ID: {instance_id}")
