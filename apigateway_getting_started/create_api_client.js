import * as apigw from "@aws-sdk/client-api-gateway";

const apig = new apigw.APIGatewayClient({ region: "us-east-1" });

// snippet-start:[apigateway_getting_started.javascript.create_api_client]
async function createRestApi() {
    const command = new apigw.CreateRestApiCommand({
        name: "Simple PetStore (JavaScript v3 SDK)",
        description: "Demo API created using the AWS SDK for JavaScript v3",
        version: "0.00.001",
        binaryMediaTypes: ['*']
    });
    try {
        const results = await apig.send(command)
        console.log(results)
        const { id, rootResourceId } = results;
        return { id, rootResourceId };
    } catch (cause) {
        throw new Error("Couldn't create REST API", { cause })
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource]
async function createResource(restApiId, rootResourceId, pathPart) {
    const command = new apigw.CreateResourceCommand({
        restApiId,
        parentId: rootResourceId,
        pathPart
    });
    try {
        const results = await apig.send(command)
        const { id } = results;
        console.log(results)
        return { id };
    } catch (cause) {
        throw new Error("The '/pets' resource setup failed", { cause })
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get]
async function putMethod(restApiId, resourceId) {
    const command = new apigw.PutMethodCommand({
        restApiId,
        resourceId,
        httpMethod: 'GET',
        authorizationType: 'NONE'
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (cause) {
        throw new Error("The 'GET /pets' method setup failed", { cause })
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_response]
async function putMethodResponse(restApiId, resourceId, statusCode) {
    const command = new apigw.PutMethodResponseCommand({
        restApiId,
        resourceId,
        httpMethod: 'GET',
        statusCode
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (cause) {
        throw new Error("Set up the 200 OK response for the 'GET /pets' method failed", { cause })
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_response]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_test]
async function testMethod(restApiId, resourceId, path) {
    const command = new apigw.TestInvokeMethodCommand({
        restApiId: restApiId,
        resourceId: resourceId,
        httpMethod: 'GET',
        pathWithQueryString: path,
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (cause) {
        throw new Error("The test on 'GET /pets' method failed:\n", { cause })
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_test]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http]
async function putIntegration(restApiId, resourceId, uri, requestParameters) {
    const command = new apigw.PutIntegrationCommand({
        restApiId,
        resourceId,
        httpMethod: 'GET',
        type: 'HTTP',
        integrationHttpMethod: 'GET',
        uri,
        requestParameters: requestParameters ?? {}
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (cause) {
        throw new Error("Set up the integration of the 'GET /pets' method of the API failed", {cause})
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http_response]
async function putIntegrationResponse(restApiId, resourceId, statusCode) {
    const command = new apigw.PutIntegrationResponseCommand({
        restApiId,
        resourceId,
        httpMethod: 'GET',
        statusCode,
        selectionPattern: ''
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (cause) {
        throw new Error("The 'GET /pets' method integration response setup failed", {cause})
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http_response]

// snippet-start:[apigateway_getting_started.javascript.create_api_client_deploy_stage]
async function createDeployment(restApiId, stageName, stageDescription) {
    const command = new apigw.CreateDeploymentCommand({
        restApiId,
        stageName,
        stageDescription,
    });
    try {
        const results = await apig.send(command)
        console.log("Deploying API succeeded", results)
    } catch (cause) {
        throw new Error("Deploying API failed", {cause})
    }
}
// snippet-end:[apigateway_getting_started.javascript.create_api_client_deploy_stage]

async function main() {
    const { id, rootResourceId } = await createRestApi();
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource.parent_call]
    const { id: petsResourceId } = await createResource(id, rootResourceId, "pets")
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource.parent_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource.child_call]
    const { id: petsChildResourceId } = await createResource(id, petsResourceId, "{petId}")
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource.child_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get.parent_call]
    await putMethod(id, petsResourceId);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get.parent_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_response.parent_call]
    await putMethodResponse(id, petsResourceId, 200);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_response.parent_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get.child_call]
    await putMethod(id, petsChildResourceId);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get.child_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_response.child_call]
    await putMethodResponse(id, petsChildResourceId, 200);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_response.child_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_test.parent_call]
    await testMethod(id, petsResourceId, '/pets');
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_test.parent_call]
    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_get_test.child_call]
    await testMethod(id, petsChildResourceId, '/pets/3');
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_get_test.child_call]

    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http.parent_call]
    await putIntegration(id, petsResourceId, 'http://petstore-demo-endpoint.execute-api.com/petstore/pets');
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http.parent_call]

    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http.child_call]
    await putIntegration(id, petsChildResourceId, 'http://petstore-demo-endpoint.execute-api.com/petstore/pets{id}', {
        "integration.request.path.id": "method.request.path.petId"
    });
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http.child_call]

    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http_response.parent_call]
    await putIntegrationResponse(id, petsResourceId, 200);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http_response.parent_call]

    // snippet-start:[apigateway_getting_started.javascript.create_api_client_resource_http_response.child_call]
    await putIntegrationResponse(id, petsChildResourceId, 200);
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_resource_http_response.child_call]

    // snippet-start:[apigateway_getting_started.javascript.create_api_client_deploy_stage.call]
    await createDeployment(id, 'test', 'test deployment')
    // snippet-end:[apigateway_getting_started.javascript.create_api_client_deploy_stage.call]
}

await main();