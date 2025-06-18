import boto3

# The use of resource provides a more abstract way to interact with AWS 
# services, resources are represented by Python objects
# and operations are simplified

def delete_group_user(username, group):
    iam = boto3.resource('iam')

    group = iam.Group(group)

    response = group.remove_user(
        UserName=username
    )

    print(response)

delete_group_user('myuser','mygroup')