import boto3
from pprint import pprint

db = boto3.client('dynamodb')

# # This has a delay as statistics are not update real time
# response = db.describe_table(
#     TableName='employee',
# )

# We can get more accurate item count for example performing a scan
response = db.scan(
    TableName='employee',
    Select='COUNT'
)

print(response['Count'])
print(response['ScannedCount'])
