import boto3

# Create DynamoDB client (credentials will come from AWS CLI or IAM Role)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# ------------------ USERS TABLE ------------------
print("Creating 'users' table...")

users_table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'  # On-demand mode (recommended)
)

# ------------------ TASKS TABLE ------------------
print("Creating 'tasks' table...")

tasks_table = dynamodb.create_table(
    TableName='tasks',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'taskName',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'taskName',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Waiting for tables to be created...")
users_table.wait_until_exists()
tasks_table.wait_until_exists()

print("DynamoDB tables 'users' and 'tasks' created successfully.")
