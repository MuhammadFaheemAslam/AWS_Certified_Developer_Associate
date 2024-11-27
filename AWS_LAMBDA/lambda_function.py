import json

def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("Event: ", event)
    
    try:
        # Return a simple response
        return {
            "statusCode": 200,
            "body": json.dumps("Hello from Lambda!")
        }
    except Exception as e:
        # Log and return an error response
        print("Error: ", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps("Internal server error")
        }
