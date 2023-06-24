import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'Billboard_Top_10'

# Access the DynamoDB table
table = dynamodb.Table(table_name)

# Define the items to add to the table
items = [
    {
        'Song': "Last Night",
        'Artist': 'Morgan Wallen',
    },
    {
        'Song': "Flowers",
        'Artist': 'Miley Cyrus',
    },
    {
        'Song': "Karma",
        'Artist': 'Taylor Swift',
    },
    {
        'Song': "Fast Car",
        'Artist': 'Luke Combs',
    },
    {
        'Song': "Calm Down",
        'Artist': 'Rema and Selena Gomez',
    },
    {
        'Song': "Last Night",
        'Artist': 'Morgan Wallen',
    },
    {
        'Song': "All My Life",
        'Artist': 'Lil Durk',
    },
    {
        'Song': "Favorite Song",
        'Artist': 'Toosii',
    },
    {
        'Song': "Kill Bill",
        'Artist': 'SZA',
    },
    {
        'Song': "Creepin",
        'Artist': 'Metro Boomin',
    },
    {
        'Song': "Ella Baila Sola",
        'Artist': 'Eslabon Armado',
    },
    
]

# Add items to the table
for item in items:
    response = table.put_item(Item=item)
    
    # Check if item addition was successful
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Item added successfully!")
    else:
        print("Failed to add item.")