import boto3

db = boto3.client('dynamodb')

res = db.list_tables()

print(res)