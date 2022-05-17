import boto3
import os


def upload_file():
    client = boto3.client('s3')

    for file in os.listdir():
        if '.csv' in file:
            upload_file_bucket = 'onwelo-task-bucket'
            upload_file_key = f'{str(file)}'
            client.upload_file(file, upload_file_bucket, upload_file_key)