import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.put_method(
        restApiId="abcd1234",
        resourceId="bbb222",
        httpMethod="GET",
        authorizationType="NONE",
        requestParameters={"method.request.path.petId": True},
    )
except botocore.exceptions.ClientError as error:
    logger.exception("The 'GET /pets/{petId}' method setup failed: %s", error)
    raise
attribute = ["httpMethod", "authorizationType", "apiKeyRequired", "requestParameters"]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
