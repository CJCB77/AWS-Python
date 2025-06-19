import boto3

ec2_client = boto3.client('ec2')

instance_profile_name = 'MyNewEC2Profile'

response = ec2_client.run_instances(
    ImageId='ami-09e6f87a47903347c',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    IamInstanceProfile={
        'Name': instance_profile_name
    }
)

instance_id = response['Instances'][0]['InstanceId']