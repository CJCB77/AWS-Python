import boto3


def delete_user(username):
    iam = boto3.client('iam')

    res = iam.delete_user(
        UserName=username
    )

    print(res)


delete_user('testupdateduser')