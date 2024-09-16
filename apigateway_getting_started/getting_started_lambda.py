import json


def lambda_handler(event, _context):
    myParam = event.get("myParam", "")
    return {"statusCode": 200, "body": json.dumps(myParam)}
