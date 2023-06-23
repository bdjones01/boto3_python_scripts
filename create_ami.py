import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(

    InstanceId='i-04edee26be6f280da',
    Name='HandsonLearning',
   
)

print(response["ImageId"])

