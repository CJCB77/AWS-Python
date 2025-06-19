import boto3

db = boto3.client('dynamodb')

response = db.put_item(
        TableName='employee',
        Item = {
            'id':{
                'N':'2'
            },
            'name':{
                'S':'newname'
            },
            'age':{
                'N':'20'
            }
        }
)