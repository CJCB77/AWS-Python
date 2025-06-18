import boto3


def list_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    # We use scope to filter in this case only custom manages(created by us)
    for response in paginator.paginate(Scope='Local'):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            policy_arn = policy['Arn']

            print(f"Policy name: {policy_name}, Policy ARN: {policy_arn}")
    
list_policies()