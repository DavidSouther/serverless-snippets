(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new PutMethodResponseCommand({
        restApiId: 'abcd1234',
        resourceId: 'aaa111',
        httpMethod: 'GET',
        statusCode: '200'
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("Set up the 200 OK response for the 'GET /pets' method failed:\n", err)
    }
})();