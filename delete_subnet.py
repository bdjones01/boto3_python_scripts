import boto3

subnet_id = "subnet-0aaf479fb6132307a"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

