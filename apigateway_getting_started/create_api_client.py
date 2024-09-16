import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.create_rest_api(
        name="Simple PetStore (Python SDK)",
        description="Demo API created using the AWS SDK for Python",
        version="0.00.001",
        binaryMediaTypes=["*"],
    )
except botocore.exceptions.ClientError as error:
    logger.exception("Couldn't create REST API %s.", error)
    raise
attribute = [
    "id",
    "name",
    "description",
    "createdDate",
    "version",
    "binaryMediaTypes",
    "apiKeySource",
    "endpointConfiguration",
    "disableExecuteApiEndpoint",
    "rootResourceId",
]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
