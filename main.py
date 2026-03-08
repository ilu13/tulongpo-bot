from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
import requests

app = FastAPI()

VERIFY_TOKEN = "tulongpo_verify_123"
PAGE_ACCESS_TOKEN = "EAFxzvx2kfu4BQZCKnSsWt63dk15PksJyhbI0dCWcsbNxfDKaZCQdlikUg6xwzXsOAjBKq0JuRa9r9P7ZB8RAyz4ZA9bLXdBx2mXBaYNEngj7P8bSTgCRvce9HbK3FqYZA6wj69fngqzHstQURSlQ9SZBSygJJuDqa5NpkuDNKWREQhm44K3ZAwZAa0s2PmIvhSbHc7zatiFPb44QS9IoFLlZA9OwZD"


def send_message(recipient_id: str, message_text: str) -> None:
    url = "https://graph.facebook.com/v18.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
    }

    response = requests.post(url, params=params, json=payload, timeout=20)
    print("SEND STATUS:", response.status_code)
    print("SEND RESPONSE:", response.text)


@app.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return PlainTextResponse(params.get("hub.challenge", ""))
    return JSONResponse({"status": "error"}, status_code=403)


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("INCOMING:", data)

    if "entry" in data:
        for entry in data["entry"]:
            for messaging_event in entry.get("messaging", []):
                sender_id = messaging_event["sender"]["id"]

                if "message" in messaging_event:
                    user_message = messaging_event["message"].get("text", "")

                    reply = f"Salamat! You said: {user_message}" if user_message else "Salamat! I received your message."
                    send_message(sender_id, reply)

    return {"status": "ok"}
