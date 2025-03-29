import boto3
import os


def get_credentials():
    aws_role_arn = os.getenv("AWS_ROLE_ARN")

    session = boto3.Session(profile_name='default')
    sts_client = session.client("sts")

    assumed_role = sts_client.assume_role(
        RoleArn=aws_role_arn,
        RoleSessionName="DynamoDBSession"
    )

    credentials = assumed_role["Credentials"]
    print("Successfully assumed role!")

    return assumed_role["Credentials"]
