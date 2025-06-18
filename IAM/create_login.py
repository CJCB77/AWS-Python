import boto3

def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_profile(
        Password = 'Mypassword@1',
        PasswordNotRequired = False,
        UserName = username
    )
    print(login_profile)