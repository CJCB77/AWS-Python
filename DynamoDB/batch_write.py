import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee') # type:ignore

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'id': 3,
            'name':'John',
            'age':35
        }
    )

    batch.put_item(
        Item = {
            'id': 4,
            'name':'Silvia',
            'age':25
        }
    )