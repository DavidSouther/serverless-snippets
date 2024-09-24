import {
    ApiGatewayManagementApiClient,
    PostToConnectionCommand,
} from "@aws-sdk/client-apigatewaymanagementapi";

export const handler = async (event) => {
    const domain = event.requestContext.domainName;
    const stage = event.requestContext.stage;
    const connectionId = event.requestContext.connectionId;
    const callbackUrl = `https://${domain}/${stage}`;
    const client = new ApiGatewayManagementApiClient({ endpoint: callbackUrl });

    const requestParams = {
        ConnectionId: connectionId,
        Data: "Hello!",
    };

    const command = new PostToConnectionCommand(requestParams);

    try {
        await client.send(command);
    } catch (error) {
        console.log(error);
    }

    return {
        statusCode: 200,
    };
};