import { APIGatewayClient, PutIntegrationCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new PutIntegrationCommand({
        restApiId: 'abcd1234',
        resourceId: 'bbb222',
        httpMethod: 'GET',
        type: 'HTTP',
        integrationHttpMethod: 'GET',
        uri: 'http://petstore-demo-endpoint.execute-api.com/petstore/pets/{id}',
        requestParameters: {
            "integration.request.path.id": "method.request.path.petId"
        }
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("Set up the integration of the 'GET /pets/{petId}' method of the API failed:\n", err)
    }
})();