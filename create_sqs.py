# import boto3
import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue 
queue = sqs.create_queue(QueueName='bjones_week15')

# Print queue url
print(queue.url)

