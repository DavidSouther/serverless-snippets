# snippet-start:[serverless-snippets.python.getting_started_lambda]
import json


def lambda_handler(event, _context):
    myParam = event.get("myParam", "")
    return {"statusCode": 200, "body": json.dumps(myParam)}
# snippet-end:[serverless-snippets.python.getting_started_lambda]
