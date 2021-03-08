import json
import csv
import os
import datetime

import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = os.environ['BUCKET_NAME']
KEY = os.environ['KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
TARGET_EMAIL = os.environ['TARGET_EMAIL']

s3 = boto3.resource('s3')
ses = boto3.client('ses')

def get_latest_info():
    filename = '/tmp/' + KEY
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, filename)
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f'The object {KEY} does not exist in bucket {BUCKET_NAME}')
        else:
            raise
        
    #get latest daily update for vaccine information
    with open(filename, 'r') as fi:
        reader = fi.readlines()
        data = reader[0:4]
        return data

        
def verify_email_identity():
    response = ses.verify_email_identity(
        EmailAddress=f'{SENDER_EMAIL}'
    )
    print(response)

def lambda_handler(event, context):
    #send info to all recipients
    recipients = ses.list_identities()
    yday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    daily_update = str(get_latest_info())
    print(daily_update)
    
    subject = 'Vaccine Updates for: ' + str(yday)
    body = """
    <br>
    <h1>Hello There!</h1><br>
    <h2>Here are the current updates as of {}:</h2><br><br>
    <b>{}</b>
    """.format(yday, daily_update)
    
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    
    response = ses.send_email(Source=f'{SENDER_EMAIL}', \
    Destination={"BccAddresses": [f'{TARGET_EMAIL}']}, Message=message)
    
    return {
        "statusCode": 200,
        "body": daily_update
    }
