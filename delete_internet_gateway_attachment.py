import boto3

internet_gateway_id = "igw-0b537b9ed41b38034"
vpc_id = "vpc-0b32c00dc06e21c20"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
