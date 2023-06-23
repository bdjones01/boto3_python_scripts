import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-06ced6416fc4ea02a',
)

print(response)