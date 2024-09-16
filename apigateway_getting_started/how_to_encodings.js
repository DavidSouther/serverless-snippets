import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3"

const client = new S3Client({});

export const handler = async (event) => {
    const randomint = function (max) {
        return Math.floor(Math.random() * max);
    }
    const number = randomint(2);
    if (number == 1) {
        const input = {
            "Bucket": "bucket-name",
            "Key": "image.png"
        }
        let base64body = "";
        try {
            const command = new GetObjectCommand(input)
            const response = await client.send(command);
            const bodyStr = await response.Body.transformToByteArray();
            base64body = Buffer.from(bodyStr).toString('base64');
        } catch (err) {
            console.error(err);
        }
        return {
            'headers': { "Content-Type": "image/png" },
            'statusCode': 200,
            'body': base64body,
            'isBase64Encoded': true
        }
    } else {
        return {
            'headers': { "Content-Type": "text/html" },
            'statusCode': 200,
            'body': "&lt;h1&gt;This is text&lt;/h1&gt;",
        }
    }
}