import os
import boto3

# get the service resource
dynamoddb = boto3.resource('dynamodb')

# set environment variable
TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    table = dynamoddb.Table(TABLE_NAME)
    # put item in table
    response = table.put_item(
        Item={
            'id': str("Hello there")
        }
    )

    print("PutItem succeeded:")

    return {
        'statusCode': 200,
    }

