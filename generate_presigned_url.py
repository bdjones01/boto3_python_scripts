import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "bjones-boto3-06152023", 'Key': "test_text.txt"}, ExpiresIn=300)
 
print(response)

