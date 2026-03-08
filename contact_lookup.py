from contacts import CONTACTS


def get_contact(location: str, emergency_type: str):

    # Try city first
    if location in CONTACTS and emergency_type in CONTACTS[location]:
        return CONTACTS[location][emergency_type]

    # Fallback to national
    if "national" in CONTACTS and emergency_type in CONTACTS["national"]:
        return CONTACTS["national"][emergency_type]

    return None


def format_contact(contact):

    if not contact:
        return "Pasensya na, wala akong mahanap na contact para diyan."

    name = contact.get("name", "Emergency Contact")

    message = f"🚨 {name}\n"

    if contact.get("description"):
        message += f"{contact['description']}\n"

    phones = contact.get("phones", {})

    for phone_type, numbers in phones.items():

        if not numbers:
            continue

        title = phone_type.replace("_", " ").title()

        message += f"\n☎ {title}\n"

        for num in numbers:
            message += f"{num}\n"

    if contact.get("available_24_7"):
        message += "\n🕒 Available 24/7"

    return message
