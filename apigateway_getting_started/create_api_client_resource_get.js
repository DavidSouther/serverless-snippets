import { APIGatewayClient, PutMethodCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new PutMethodCommand({
        restApiId: 'abcd1234',
        resourceId: 'aaa111',
        httpMethod: 'GET',
        authorizationType: 'NONE'
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The 'GET /pets' method setup failed:\n", err)
    }
})();