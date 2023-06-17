import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket="bjones-boto3-06152023")

for content in response["Contents"]:
    if(".txt" in content["Key"][-4:]):
        print(content["Key"])