import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.put_method_response(
        restApiId="abcd1234", resourceId="bbb222", httpMethod="GET", statusCode="200"
    )
except botocore.exceptions.ClientError as error:
    logger.exception(
        "Set up the 200 OK response for the 'GET /pets/{petId}' method failed %s.",
        error,
    )
    raise
attribute = ["statusCode"]
filtered_result = {key: result[key] for key in attribute}
logger.info(filtered_result)
