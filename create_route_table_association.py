import boto3

route_table_id ='rtb-0f2a7b4028a4db400'
subnet_id = 'subnet-0aaf479fb6132307a'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(association["AssociationId"])