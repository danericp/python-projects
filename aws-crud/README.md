# AWS CRUD Management

An automated solution for managing your AWS resources. This ultimately eliminates the tedious memorization of GUI, CLI and resource prerequisites.

## Usage

1. Refer to [config.json](config.json) to see all prerequisites required by each action.
2. Run `python main.py -h` or `python main.py --help` to see the required parameters.

```commandline
options:
  -h --help            show this help message and exit
  -a ACTION --action ACTION
                        Pre-defined action
```

For the actions, please see [Action Features](#action-features) for details.

## Action Features

### Read

All read-based actions are formatted in a user-friendly manner.

| Action                   | Description                                                   |
|--------------------------|---------------------------------------------------------------|
| create_ec2               | Create an EC2 machine.                                        |
| create_iam_group         | Create an IAM group.                                          |
| create_iam_policy        | Create an IAM policy.                                         |
| create_iam_role          | Create an IAM role.                                           |
| create_iam_user          | Create an IAM user.                                           |
| create_s3_bucket         | Create an S3 bucket.                                          |
| create_sqs_queue         | Create an S3 queue.                                           |
| read_ec2_instance_types  | Checks your AWS Account, and lists down EC2 > Instance Types  |
| read_ec2_key_pairs       | Checks your AWS Account, and lists down EC2 > Key Pairs       |
| read_ec2_security_groups | Checks your AWS Account, and lists down EC2 > Security Groups |
| read_iam_groups          | Checks your AWS Account, and lists down IAM > Groups          |
| read_iam_users           | Checks your AWS Account, and lists down IAM > USers           |