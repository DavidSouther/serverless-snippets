import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.test_invoke_method(
        restApiId="abcd1234",
        resourceId="aaa111",
        httpMethod="GET",
        pathWithQueryString="/",
    )
except botocore.exceptions.ClientError as error:
    logger.exception("Test invoke method on 'GET /pets' failed: %s", error)
    raise
print(result)
