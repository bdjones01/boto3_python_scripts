import boto3

internet_gateway_id = "igw-0b537b9ed41b38034"

ec2 = boto3.client('ec2')
    
ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)