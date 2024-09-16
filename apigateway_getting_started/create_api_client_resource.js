import { APIGatewayClient, CreateResourceCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new CreateResourceCommand({
        restApiId: 'abcd1234',
        parentId: 'efg567',
        pathPart: 'pets'
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.log("The '/pets' resource setup failed:\n", err)
    }
})();