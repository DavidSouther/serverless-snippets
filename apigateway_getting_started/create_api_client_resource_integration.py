import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.put_integration(
        restApiId="abcd1234",
        resourceId="aaa111",
        httpMethod="GET",
        type="HTTP",
        integrationHttpMethod="GET",
        uri="http://petstore-demo-endpoint.execute-api.com/petstore/pets",
    )
except botocore.exceptions.ClientError as error:
    logger.exception(
        "Set up the integration of the 'GET /' method of the API failed %s.", error
    )
    raise
attribute = [
    "httpMethod",
    "passthroughBehavior",
    "cacheKeyParameters",
    "type",
    "uri",
    "cacheNamespace",
]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
