import { APIGatewayClient, TestInvokeMethodCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new TestInvokeMethodCommand({
        restApiId: 'abcd1234',
        resourceId: 'aaa111',
        httpMethod: 'GET',
        pathWithQueryString: '/',
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The test on 'GET /pets' method failed:\n", err)
    }
})();
