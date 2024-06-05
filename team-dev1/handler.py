import json


def hello(event, context):
    body = {
        "message": "Go Serverless from dev2!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
