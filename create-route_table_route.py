import boto3

route_table_id = "rtb-0f2a7b4028a4db400"
internet_gateway_id= "igw-0b537b9ed41b38034"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
