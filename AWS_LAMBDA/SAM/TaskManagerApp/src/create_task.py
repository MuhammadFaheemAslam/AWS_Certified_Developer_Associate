import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TaskTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    task_id = str(uuid.uuid4())
    task_name = body.get('name')

    if not task_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Task name is required"})
        }

    table.put_item(Item={"taskId": task_id, "name": task_name})
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Task created", "taskId": task_id})
    }
