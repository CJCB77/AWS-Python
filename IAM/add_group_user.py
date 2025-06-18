import boto3


def add_user_to_group(username, group):
    iam = boto3.client('iam')

    res = iam.add_user_to_group(
        UserName=username,
        GroupName=group
    )
    print(res)

add_user_to_group("testupdateduser", "RDSAdmins")