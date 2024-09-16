import { APIGatewayClient, CreateDeploymentCommand } from "@aws-sdk/client-api-gateway";
(async function () {
    const apig = new APIGatewayClient({ region: "us-east-1" });
    const command = new CreateDeploymentCommand({
        restApiId: 'abcd1234',
        stageName: 'test',
        stageDescription: 'test deployment'
    });
    try {
        const results = await apig.send(command)
        console.log("Deploying API succeeded\n", results)
    } catch (err) {
        console.log("Deploying API failed:\n", err)
    }
})();