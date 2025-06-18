import boto3

# Client interface is low level, we do direct API call
# that map 1:1 with AWS services API
# we work with raw seponse data
def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)

create_user("testuser") 