# snippet-start:[serverless-snippets.python.http_api_lambda_auth_iam]
def lambda_handler(event, _context):
    try:
        if event["headers"]["authorization"] == "secretToken":
            print("allowed")
            return {
                # The principal user identification associated with the token
                # sent by the client.
                "principalId": "abcdef",
                "policyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "execute-api:Invoke",
                            "Effect": "Allow",
                            "Resource": event["routeArn"],
                        }
                    ],
                },
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
                # The principal user identification associated with the token
                # sent by the client.
                "principalId": "abcdef",
                "policyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "execute-api:Invoke",
                            "Effect": "Deny",
                            "Resource": event["routeArn"],
                        }
                    ],
                },
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
# snippet-end:[serverless-snippets.python.http_api_lambda_auth_iam]