import os
import json
import requests

def handler(event, context):
    body = json.loads(event['body'])
    user_input = body.get("prompt", "")
    model_name = body.get("model", "deepseek-ai/DeepSeek-R1")

    HF_TOKEN = os.environ.get("HF_TOKEN")  # ✅ Securely read from Netlify secrets

    if not HF_TOKEN:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "HF_TOKEN not set in environment"})
        }

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": user_input}

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{model_name}",
        headers=headers,
        json=payload
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response.json())
    }
