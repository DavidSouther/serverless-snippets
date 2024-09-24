// snippet-start:[serverless-snippets.javascript.http_api_lambda_auth_simple]
export const handler = async (event) => {
    if (event.headers.authorization === "secretToken") {
        console.log("allowed");
        return {
            "isAuthorized": true,
            "context": {
                "stringKey": "value",
                "numberKey": 1,
                "booleanKey": true,
                "arrayKey": ["value1", "value2"],
                "mapKey": { "value1": "value2" }
            }
        };
    }
    else {
        console.log("denied");
        return {
        "isAuthorized": false,
        "context": {
            "stringKey": "value",
            "numberKey": 1,
            "booleanKey": true,
            "arrayKey": ["value1", "value2"],
            "mapKey": { "value1": "value2" }
        }
    };
    }
};
// snippet-end:[serverless-snippets.javascript.http_api_lambda_auth_simple]