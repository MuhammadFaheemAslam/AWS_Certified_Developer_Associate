import json

def lambda_handler(event, context):
    for record in event['Records']:
        detail = json.loads(record['body'])
        print(f"Task Deleted: {detail['taskId']}")
    return {"statusCode": 200}
