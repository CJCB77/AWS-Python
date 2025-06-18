import boto3


def detach_group_policy(group, policy_arn):
    iam = boto3.client('iam')

    res = iam.detach_group_policy(
        GroupName=group,
        PolicyArn=policy_arn
    )
    print(res)

detach_group_policy('RDSAdmins', 'arn:aws:iam::aws:policy/AmazonRDSFullAccess')