import boto3


def list_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            arn = user['Arn']
            print(f"Username: {username}, ARN:{arn}")

list_users()