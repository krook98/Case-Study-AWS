import boto3
from botocore.exceptions import ClientError
import os

SENDER = os.environ.get('SENDER')
RECIPIENT = os.environ.get('RECIPIENT')
AWS_REGION = 'eu-central-1'

SUBJECT='Jakub Sokalski - zadanie rekrutacyjne'
BODY_TEXT = ('Hej, \r\n'
             'Plik został już umieszczony na AWS S3 :)')

BODY_HTML = """<html>
<head></head>
<body>
    <h1>Hej,</h1>
    <p>Plik został już umieszczony na AWS S3 :)</p>
    <p>Ten mail został wysłany dzięki 
        <a href='https://aws.amazon.com/ses/'> Amazon SES </a> i
        <a href='https://aws.amazon.com/sdk-for-python/'> Amazon SDK for Python </a>
</body>
</html>
"""
CHARSET = 'UTF-8'


# Checking if file is in S3
def check_file():
    resource = boto3.resource('s3')

    try:
        resource.Object('onwelo-task-bucket', 'all_data.csv').load()
    except ClientError as error:
        if error.response['Error']['Code'] == '404':
            print("Pliku nie ma w S3")
            return False
    else:
        print('Dane są już w S3 :)')
        return True


def send_email():
    # Sending an email
    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ]
            },
            Message={
                'Body': {
                    'Html': {
                        'Data': BODY_HTML
                    },
                    'Text': {
                        'Data': BODY_TEXT
                    }
                },
                'Subject': {
                    'Data': SUBJECT
                }
            },
            Source=SENDER

        )

    # Checking if email was sent
    except ClientError as error:
        print(f'{error.response["Error"]["Message"]}')
    else:
        print(f'Email sent!')




