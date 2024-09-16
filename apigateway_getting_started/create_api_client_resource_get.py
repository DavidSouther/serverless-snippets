import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.put_method(
        restApiId="abcd1234",
        resourceId="aaa111",
        httpMethod="GET",
        authorizationType="NONE",
    )
except botocore.exceptions.ClientError as error:
    logger.exception("The 'GET /pets' method setup failed: %s", error)
    raise
attribute = ["httpMethod", "authorizationType", "apiKeyRequired"]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
