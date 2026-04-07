import os
import base64
import mimetypes

def lambda_handler(event, context):
    # Path from API Gateway HTTP API
    raw_path = event.get("rawPath")

    # API Gateway v1 fallback
    if not raw_path:
        raw_path = event.get("path", "/")

    path = raw_path if raw_path != "/" else "/index.html"

    file_path = "." + path

    if not os.path.isfile(file_path):
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "text/plain"},
            "body": "Not found"
        }

    with open(file_path, "rb") as f:
        body = f.read()

    mime = mimetypes.guess_type(file_path)[0] or "application/octet-stream"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": mime},
        "isBase64Encoded": True,
        "body": base64.b64encode(body).decode()
    }
