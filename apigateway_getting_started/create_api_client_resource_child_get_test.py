import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.test_invoke_method(
        restApiId="abcd1234",
        resourceId="bbb222",
        httpMethod="GET",
        pathWithQueryString="/pets/3",
    )
except botocore.exceptions.ClientError as error:
    logger.exception("Test invoke method on 'GET /pets/{petId}' failed: %s", error)
    raise
print(result)
