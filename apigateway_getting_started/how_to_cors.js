// snippet-start:[serverless-snippets.javascript.how_to_cors]
export const handler = async (event) => {
    const response = {
        statusCode: 200,
        headers: {
            // Replace https://www.example.com with your domain.
            "Access-Control-Allow-Origin": "https://www.example.com",
            "Access-Control-Allow-Headers": "Content-Type</replaceable>",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
// snippet-end:[serverless-snippets.javascript.how_to_cors]