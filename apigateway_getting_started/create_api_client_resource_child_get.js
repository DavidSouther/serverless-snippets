import { APIGatewayClient, PutMethodCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new PutMethodCommand({
        restApiId: 'abcd1234',
        resourceId: 'bbb222',
        httpMethod: 'GET',
        authorizationType: 'NONE'
    requestParameters: {
            "method.request.path.petId": true
        }
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The 'GET /pets/{petId}' method setup failed:\n", err)
    }
})();