import boto3


def update_user(old_name, new_name):
    iam = boto3.client('iam')

    res = iam.update_user(
        UserName=old_name,
        NewUserName=new_name
    )

    print(res)

update_user('testuser','testupdateduser')