import botocore
import boto3
import logging

logger = logging.getLogger()
apig = boto3.client("apigateway")

try:
    result = apig.create_deployment(
        restApiId="ieps9b05sf",
        stageName="test",
        stageDescription="my test stage",
    )
except botocore.exceptions.ClientError as error:
    logger.exception("Error deploying stage  %s.", error)
    raise
print("Deploying API succeeded")
print(result)
