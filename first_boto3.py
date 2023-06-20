import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='bjones-boto3-06152023'
)

print(response)
 
   