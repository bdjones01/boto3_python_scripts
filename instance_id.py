import boto3

instance_id = 'i-00630eafdf6f01e1b'

def stop_instance(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
    ],
)

ec2 = boto3.client('ec2')
