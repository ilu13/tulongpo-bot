from contacts import CONTACTS


def get_response(text):

    text = text.lower()

    if "police" in text:
        c = CONTACTS["police"]
        return f"🚓 {c['name']}\n📞 {c['number']}"

    elif "ambulance" in text:
        c = CONTACTS["ambulance"]
        return f"🚑 {c['name']}\n📞 {c['number']}"

    elif "fire" in text:
        c = CONTACTS["fire"]
        return f"🔥 {c['name']}\n📞 {c['number']}"

    elif "mental" in text:
        c = CONTACTS["mental_health"]
        return f"🧠 {c['name']}\n📞 {c['number']}"

    else:
        return (
            "I can help you find emergency contacts.\n\n"
            "Choose one below."
        )
