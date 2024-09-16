import { APIGatewayClient, CreateRestApiCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new CreateRestApiCommand({
        name: "Simple PetStore (JavaScript v3 SDK)",
        description: "Demo API created using the AWS SDK for JavaScript v3",
        version: "0.00.001",
        binaryMediaTypes: [
            '*']
    });
    try {
        const results = await apig.send(command)
        console.log(results)
    } catch (err) {
        console.error("Couldn't create API:\n", err)
    }
})();