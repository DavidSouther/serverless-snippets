# snippet-start:[serverless-snippets.python.how_to_encodings]
import base64
import random

import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    number = random.randint(0, 1)
    if number == 1:
        response = s3.get_object(
            Bucket="bucket-name",
            Key="image.png",
        )
        image = response["Body"].read()
        return {
            "headers": {"Content-Type": "image/png"},
            "statusCode": 200,
            "body": base64.b64encode(image).decode("utf-8"),
            "isBase64Encoded": True,
        }
    else:
        return {
            "headers": {"Content-type": "text/html"},
            "statusCode": 200,
            "body": "&lt;h1&gt;This is text&lt;/h1&gt;",
        }
# snippet-end:[serverless-snippets.python.how_to_encodings]
