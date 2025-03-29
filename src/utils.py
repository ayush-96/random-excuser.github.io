import boto3
import os


def get_credentials():

    session = boto3.Session(profile_name='default')
    sts_client = session.client("sts")

    assumed_role = sts_client.assume_role(
        RoleArn="arn:aws:iam::637423653752:role/service-role/random-excuser-role-fgtbon9b",
        RoleSessionName="DynamoDBSession"
    )

    credentials = assumed_role["Credentials"]
    print("Successfully assumed role!")

    return assumed_role["Credentials"]
