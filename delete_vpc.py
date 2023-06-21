import boto3

vpc_id = 'vpc-0b32c00dc06e21c20'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

