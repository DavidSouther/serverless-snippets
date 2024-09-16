import { APIGatewayClient, TestInvokeMethodCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new TestInvokeMethodCommand({
        restApiId: 'abcd1234',
        resourceId: 'bbb222',
        httpMethod: 'GET',
        pathWithQueryString: '/pets/3',
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The test on 'GET /pets/{petId}' method failed:\n", err)
    }
})();