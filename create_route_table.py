import boto3

vpc_id = 'vpc-0b32c00dc06e21c20'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])


