import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.put_integration_response(
        restApiId="abcd1234",
        resourceId="bbb222",
        httpMethod="GET",
        statusCode="200",
        selectionPattern="",
    )
except botocore.exceptions.ClientError as error:
    logger.exception(
        "Set up the integration response of the 'GET /pets/{petId}' method of the API failed: %s",
        error,
    )
    raise
attribute = ["selectionPattern", "statusCode"]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
