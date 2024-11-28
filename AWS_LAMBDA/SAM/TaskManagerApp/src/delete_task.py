import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
eventbridge = boto3.client('events')
table = dynamodb.Table('TaskTable')

def lambda_handler(event, context):
    task_id = event['pathParameters']['taskId']

    # Check if task exists
    response = table.get_item(Key={"taskId": task_id})
    if 'Item' not in response:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found"})
        }

    # Delete the task
    table.delete_item(Key={"taskId": task_id})

    # Send EventBridge event
    eventbridge.put_events(
        Entries=[
            {
                "Source": "com.taskmanager",
                "DetailType": "TaskDeleted",
                "Detail": json.dumps({"taskId": task_id})
            }
        ]
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task deleted"})
    }
