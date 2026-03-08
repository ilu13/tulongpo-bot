import requests
from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "tulongpo_verify_123"
PAGE_ACCESS_TOKEN = "EAFxzvx2kfu4BQZCKnSsWt63dk15PksJyhbI0dCWcsbNxfDKaZCQdlikUg6xwzXsOAjBKq0JuRa9r9P7ZB8RAyz4ZA9bLXdBx2mXBaYNEngj7P8bSTgCRvce9HbK3FqYZA6wj69fngqzHstQURSlQ9SZBSygJJuDqa5NpkuDNKWREQhm44K3ZAwZAa0s2PmIvhSbHc7zatiFPb44QS9IoFLlZA9OwZD"


@app.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return {"status": "error"}


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    for entry in data.get("entry", []):
        for messaging_event in entry.get("messaging", []):

            sender_id = messaging_event["sender"]["id"]

            if "message" in messaging_event:
                text = messaging_event["message"].get("text", "").lower()

                if "police" in text:
                    reply = "🚓 Philippine National Police\n📞 Dial 911"

                elif "ambulance" in text:
                    reply = "🚑 Emergency Medical Services\n📞 Dial 911"

                elif "fire" in text:
                    reply = "🔥 Bureau of Fire Protection\n📞 Dial 911"

                else:
                    reply = (
                        "Salamat! I can help you find emergency contacts.\n\n"
                        "Type:\n"
                        "🚓 police\n"
                        "🚑 ambulance\n"
                        "🔥 fire\n"
                        "🧠 mental health"
                    )

                send_message(sender_id, reply)

    return {"status": "ok"}


def send_message(recipient_id, text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }

    requests.post(url, json=payload)
