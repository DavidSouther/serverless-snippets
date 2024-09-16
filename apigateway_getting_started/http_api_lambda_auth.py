# snippet-start:[serverless-snippets.python.http_api_lambda_auth_simple]
def lambda_handler(event, _context):
    try:
        if event["headers"]["authorization"] == "secretToken":
            print("allowed")
            return {
                "isAuthorized": True,
                "context": {
                    "stringKey": "value",
                    "numberKey": 1,
                    "booleanKey": True,
                    "arrayKey": ["value1", "value2"],
                    "mapKey": {"value1": "value2"},
                },
            }
        else:
            print("denied")
            return {
                "isAuthorized": False,
                "context": {
                    "stringKey": "value",
                    "numberKey": 1,
                    "booleanKey": True,
                    "arrayKey": ["value1", "value2"],
                    "mapKey": {"value1": "value2"},
                },
            }
    except BaseException:
        print("denied")
        raise
# snippet-end:[serverless-snippets.python.http_api_lambda_auth_simple]
