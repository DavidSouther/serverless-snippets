// snippet-start:[serverless-snippets.javascript.getting_started_lambda]
/** @param {import('aws-lambda').APIGatewayEvent<{myParam: string}>} event */
export const handler = async (event) => {
    let myParam = event.myParam;
    const response = {
        statusCode: 200,
        body: JSON.stringify(myParam)
    };
    return response;
};
// snippet-end:[serverless-snippets.javascript.getting_started_lambda]