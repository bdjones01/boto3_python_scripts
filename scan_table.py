import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'Billboard_Top_10'

# Access the DynamoDB table
table = dynamodb.Table(table_name)

# Perform a table scan
response = table.scan()

# Retrieve the scanned items
items = response['Items']

# Process the scanned items
for item in items:
    # Access item attributes using the attribute name
    song_value = item['Song']
    artist_value = item['Artist']
    # ... process other attributes as needed
    print(f"Song: {song_value}, Artist: {artist_value}")

