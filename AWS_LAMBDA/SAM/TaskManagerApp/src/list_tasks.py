import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TaskTable')

def lambda_handler(event, context):
    response = table.scan()
    tasks = response.get('Items', [])

    return {
        "statusCode": 200,
        "body": json.dumps({"tasks": tasks})
    }
