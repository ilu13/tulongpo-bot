from fastapi import FastAPI, Request
import requests

app = FastAPI()

VERIFY_TOKEN = "tulongpo_verify_123"

PAGE_ACCESS_TOKEN = "EAFxzvx2kfu4BQZCKnSsWt63dk15PksJyhbI0dCWcsbNxfDKaZCQdlikUg6xwzXsOAjBKq0JuRa9r9P7ZB8RAyz4ZA9bLXdBx2mXBaYNEngj7P8bSTgCRvce9HbK3FqYZA6wj69fngqzHstQURSlQ9SZBSygJJuDqa5NpkuDNKWREQhm44K3ZAwZAa0s2PmIvhSbHc7zatiFPb44QS9IoFLlZA9OwZD"

def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v18.0/me/messages"
    
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    requests.post(url, params=params, json=payload)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print(data)

    if "entry" in data:
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                
                sender_id = messaging_event["sender"]["id"]
                
                if "message" in messaging_event:
                    user_message = messaging_event["message"].get("text", "")
                    
                    send_message(sender_id, "Salamat! I received your message.")

    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}
