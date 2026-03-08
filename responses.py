from contact_lookup import get_contact, format_contact


def get_response(text):

    text = text.lower()

    location = "national"

    if "qc" in text or "quezon city" in text:
        location = "quezon_city"

    # detect emergency type
    if "police" in text:
        contact = get_contact(location, "police")
        return format_contact(contact)

    elif "fire" in text or "sunog" in text:
        contact = get_contact(location, "fire")
        return format_contact(contact)

    elif "ambulance" in text or "medical" in text:
        contact = get_contact(location, "ambulance")
        return format_contact(contact)

    elif "mental" in text or "suicide" in text:
        contact = get_contact(location, "mental_health")
        return format_contact(contact)

    elif "women" in text or "abuse" in text:
        contact = get_contact(location, "women_children")
        return format_contact(contact)

    else:
        return (
            "I can help you find emergency contacts.\n\n"
            "Try typing:\n"
            "police\n"
            "fire\n"
            "ambulance\n"
            "mental health"
        )
