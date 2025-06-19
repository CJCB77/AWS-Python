import boto3
import json

iam = boto3.client('iam')

# 1. Create the role
role_name = "MyEC2Role"
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "ec2.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}

iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)

# 2. Create the instance profile
profile_name = "MyEC2InstanceProfile"
iam.create_instance_profile(InstanceProfileName=profile_name)

# 3. Add the role to the profile
iam.add_role_to_instance_profile(
    InstanceProfileName=profile_name,
    RoleName=role_name
)