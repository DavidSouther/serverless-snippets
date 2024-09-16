import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.create_resource(
        restApiId="abcd1234", parentId="efg567", pathPart="pets"
    )
except botocore.exceptions.ClientError as error:
    logger.exception("The '/pets' resource setup failed: %s.", error)
    raise
attribute = [
    "id",
    "parentId",
    "pathPart",
    "path",
]
filtered_result = {key: result[key] for key in attribute}
print(filtered_result)
