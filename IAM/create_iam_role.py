import boto3
import json

iam = boto3.client('iam')

role_name = "MyNewEC2Role"

trust_policy = {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect":"Allow",
            "Principal": {
                "Service":"ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

iam.create_role(
    RoleName= role_name,
    AssumeRolePolicyDocument= json.dumps(trust_policy)
)

policy_name = "MyNewECPolicy"

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn"
        }
    ]
}

iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument=policy_document
)

iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn = "arn"
)