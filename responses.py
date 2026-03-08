def get_response(text):

    text = text.lower()

    if "police" in text:
        return "🚓 Philippine National Police\n📞 Dial 911"

    elif "ambulance" in text:
        return "🚑 Emergency Medical Services\n📞 Dial 911"

    elif "fire" in text:
        return "🔥 Bureau of Fire Protection\n📞 Dial 911"

    elif "mental" in text:
        return "🧠 Mental Health Crisis Hotline\n📞 1553"

    else:
        return (
            "I can help you find emergency contacts.\n\n"
            "Choose one below."
        )
