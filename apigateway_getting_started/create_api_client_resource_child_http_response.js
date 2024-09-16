import { APIGatewayClient, PutIntegrationResponseCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new PutIntegrationResponseCommand({
        restApiId: 'abcd1234',
        resourceId: 'bbb222',
        httpMethod: 'GET',
        statusCode: '200',
        selectionPattern: ''
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The 'GET /pets/{petId}' method integration response setup failed:\n", err)
    }
})();