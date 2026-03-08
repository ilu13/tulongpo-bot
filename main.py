from fastapi import FastAPI, Request
import requests
import os

from responses import get_response

app = FastAPI()

VERIFY_TOKEN = "tulongpo_verify_123"

# Get token from environment variable (safer)
PAGE_ACCESS_TOKEN = os.getenv("EAFxzvx2kfu4BQZCKnSsWt63dk15PksJyhbI0dCWcsbNxfDKaZCQdlikUg6xwzXsOAjBKq0JuRa9r9P7ZB8RAyz4ZA9bLXdBx2mXBaYNEngj7P8bSTgCRvce9HbK3FqYZA6wj69fngqzHstQURSlQ9SZBSygJJuDqa5NpkuDNKWREQhm44K3ZAwZAa0s2PmIvhSbHc7zatiFPb44QS9IoFLlZA9OwZD")


@app.get("/")
def home():
    return {"status": "Tulong Po Bot is running"}


@app.get("/webhook")
async def verify(request: Request):

    params = request.query_params

    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return int(params.get("hub.challenge"))

    return {"status": "error"}


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    for entry in data.get("entry", []):
        for messaging_event in entry.get("messaging", []):

            sender_id = messaging_event["sender"]["id"]

            if "message" in messaging_event:

                text = messaging_event["message"].get("text", "")

                reply = get_response(text)

                send_message(sender_id, reply)

    return {"status": "ok"}


def send_message(recipient_id, text):

    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }

    requests.post(url, json=payload)
