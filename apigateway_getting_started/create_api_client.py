import botocore
import boto3
import json
import logging
import sys

logger = logging.getLogger()
apig = boto3.client("apigateway")


# snippet-start:[apigateway_getting_started.python.create_api_client]
def create_rest_api():
    try:
        result = apig.create_rest_api(
            name="Simple PetStore (Python SDK)",
            description="Demo API created using the AWS SDK for Python",
            version="0.00.001",
            binaryMediaTypes=["*"],
        )
        json.dump(result, sys.stdout, indent="  ")
        return (result["id"], result["rootResourceId"])
    except botocore.exceptions.ClientError as error:
        logger.exception("Couldn't create REST API %s.", error)
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource]
def create_rest_api_resource(restApiId, rootResourceId, pathPart):
    try:
        result = apig.create_resource(
            restApiId=restApiId, parentId=rootResourceId, pathPart=pathPart
        )
        json.dump(result, sys.stdout)
        return result["id"]
    except botocore.exceptions.ClientError as error:
        logger.exception("The '/pets' resource setup failed: %s.", error)
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource_get]
def putMethod(restApiId, resourceId):
    try:
        result = apig.put_method(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod="GET",
            authorizationType="NONE",
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception("The 'GET /pets' method setup failed: %s", error)
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_response]
def putMethodResponse(restApiId, resourceId, statusCode):
    try:
        result = apig.put_method_response(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod="GET",
            statusCode=statusCode,
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception(
            "Set up the 200 OK response for the 'GET /pets' method failed %s.", error
        )
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_response]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_test]
def testMethod(restApiId, resourceId, path):
    try:
        result = apig.test_invoke_method(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod="GET",
            pathWithQueryString=path,
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception("Test invoke method on 'GET /pets' failed: %s", error)
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_test]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource_http]
def putIntegration(restApiId, resourceId, uri, requestParameters={}):
    try:
        result = apig.put_integration(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod="GET",
            type="HTTP",
            integrationHttpMethod="GET",
            uri=uri,
            requestParameters=requestParameters,
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception(
            "Set up the integration of the 'GET /' method of the API failed %s.", error
        )
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http]


# snippet-start:[apigateway_getting_started.python.create_api_client_resource_http_response]
def putIntegrationResponse(restApiId, resourceId, statusCode):
    try:
        result = apig.put_integration_response(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod="GET",
            statusCode=statusCode,
            selectionPattern="",
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception(
            "Set up the integration response of the 'GET /pets' method of the API failed: %s",
            error,
        )
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http_response]


# snippet-start:[apigateway_getting_started.python.create_api_client_deploy_stage]
def createDeployment(restApiId, stageName, stageDescription):
    try:
        result = apig.create_deployment(
            restApiId=restApiId,
            stageName=stageName,
            stageDescription=stageDescription,
        )
        json.dump(result, sys.stdout)
    except botocore.exceptions.ClientError as error:
        logger.exception("Error deploying stage  %s.", error)
        raise
        # snippet-end:[apigateway_getting_started.python.create_api_client_deploy_stage]


if __name__ == "__main__":
    (id, rootResourceId) = create_rest_api()
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource.parent_call]
    petsResourceId = create_rest_api_resource(id, rootResourceId, "pets")
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource.parent_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource.child_call]
    petsChildResourceId = create_rest_api_resource(id, petsResourceId, "{petId}")
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource.child_call]
    putMethod(id, petsResourceId)
    putMethodResponse(id, petsResourceId, 200)
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get.parent_call]
    putMethod(id, petsResourceId)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get.parent_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_response.parent_call]
    putMethodResponse(id, petsResourceId, 200)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_response.parent_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get.child_call]
    putMethod(id, petsChildResourceId)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get.child_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_response.child_call]
    putMethodResponse(id, petsChildResourceId, 200)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_response.child_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_test.parent_call]
    testMethod(id, petsResourceId, "/pets")
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_test.parent_call]
    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_get_test.child_call]
    testMethod(id, petsChildResourceId, "/pets/3")
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_get_test.child_call]

    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_http.parent_call]
    putIntegration(
        id, petsResourceId, "http:#petstore-demo-endpoint.execute-api.com/petstore/pets"
    )
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http.parent_call]

    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_http.child_call]
    putIntegration(
        id,
        petsChildResourceId,
        "http:#petstore-demo-endpoint.execute-api.com/petstore/pets{id}",
        {"integration.request.path.id": "method.request.path.petId"},
    )
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http.child_call]

    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_http_response.parent_call]
    putIntegrationResponse(id, petsResourceId, 200)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http_response.parent_call]

    # snippet-start:[apigateway_getting_started.python.create_api_client_resource_http_response.child_call]
    putIntegrationResponse(id, petsChildResourceId, 200)
    # snippet-end:[apigateway_getting_started.python.create_api_client_resource_http_response.child_call]

    # snippet-start:[apigateway_getting_started.python.create_api_client_deploy_stage.call]
    createDeployment(id, "test", "test deployment")
    # snippet-end:[apigateway_getting_started.python.create_api_client_deploy_stage.call]
