from fastapi import FastAPI, Request
import requests
import os

from responses import get_response
from contact_lookup import get_contact, format_contact
from menu import main_menu, location_menu

app = FastAPI()

VERIFY_TOKEN = "tulongpo_verify_123"
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


@app.get("/")
def home():
    return {"status": "Tulong Po bot running"}


@app.get("/webhook")
async def verify(request: Request):

    params = request.query_params

    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return int(params.get("hub.challenge"))

    return {"status": "error"}


def send_message(recipient_id, text, quick_replies=None):

    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }

    if quick_replies:
        payload["message"]["quick_replies"] = quick_replies

    requests.post(url, json=payload)


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    for entry in data.get("entry", []):
        for messaging_event in entry.get("messaging", []):

            sender_id = messaging_event["sender"]["id"]

            if "message" in messaging_event:

                message_obj = messaging_event["message"]

                text = message_obj.get("text", "")

                # --- QUICK REPLY HANDLING ---

                if "quick_reply" in message_obj:

                    payload = message_obj["quick_reply"]["payload"]

                    # --- SECOND STEP: LOCATION SELECTED ---

                    if "|" in payload:

                        emergency_type, location = payload.split("|")

                        contact = get_contact(location, emergency_type)

                        reply = format_contact(contact)

                        send_message(sender_id, reply, main_menu())

                    # --- FIRST STEP: CATEGORY SELECTED ---

                    elif payload in ["police", "fire", "ambulance", "mental_health", "women_children"]:

                        contact = get_contact("national", payload)

                        reply = format_contact(contact)

                        send_message(
                            sender_id,
                            reply + "\n\nDo you need a city-specific hotline?",
                            location_menu(payload)
                        )

                    else:

                        send_message(sender_id, "Sorry, I didn't understand.", main_menu())

                # --- NORMAL TEXT INPUT ---

                else:

                    if text.lower() in ["hi", "hello", "menu", "start", "help"]:

                        send_message(
                            sender_id,
                            "Kumusta! I can help you find emergency contacts.",
                            main_menu()
                        )

                    else:

                        reply = get_response(text)

                        send_message(sender_id, reply, main_menu())

    return {"status": "ok"}
