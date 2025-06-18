import boto3

def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

def attach_group_policy(group, policy):
    iam = boto3.client('iam')
    res = iam.attach_group_policy(
        GroupName=group,
        PolicyArn=policy,
    )
    print(res)

# create_group("RDSAdmins")
attach_group_policy("RDSAdmins", "arn")