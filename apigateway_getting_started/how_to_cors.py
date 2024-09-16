import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            # Replace https://www.example.com with your domain
            "Access-Control-Allow-Origin": "https://www.example.com",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        },
        "body": json.dumps("Hello from Lambda!"),
    }
