import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define table name and attributes
table_name = 'Billboard_Top_10'
partition_key = 'Song'
sort_key = 'Artist'

# Create the table
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': partition_key,
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': sort_key,
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': partition_key,
            'AttributeType': 'S'  # String attribute
        },
        {
            'AttributeName': sort_key,
            'AttributeType': 'S'  # String attribute
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

# Check if the table creation was successful
if table.table_status == 'ACTIVE':
    print(f"Table '{table_name}' created successfully!")
else:
    print(f"Table creation failed. Status: {table.table_status}")
