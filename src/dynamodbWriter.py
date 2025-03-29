import boto3
import json
from utils import get_credentials

credentials = get_credentials()
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)


def read_json_file(file_loc='../data/list_of_excuses.json'):
    try:
        with open(file_loc, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


def batch_write_items(items=None):
    table = dynamodb.Table('excuses')
    if not items:
        items = read_json_file()
    try:
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)
        print("Batch write successful!")
    except Exception as e:
        print(f"Error writing batch items: {e}")


batch_write_items()
