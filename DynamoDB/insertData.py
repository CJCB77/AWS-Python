import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee') # type:ignore

table.put_item(
    Item = {
        'id':1,
        'name':'test',
        'age':24
    }
)