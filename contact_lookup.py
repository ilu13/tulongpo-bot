from contacts import CONTACTS


def get_contact(location: str, emergency_type: str):
    if location in CONTACTS and emergency_type in CONTACTS[location]:
        return CONTACTS[location][emergency_type]

    if "national" in CONTACTS and emergency_type in CONTACTS["national"]:
        return CONTACTS["national"][emergency_type]

    return None


def format_contact(contact):
    if not contact:
        return "Pasensya na, wala akong mahanap na contact para diyan."

    message = f"🚨 {contact['name']}\n"

    if contact.get("description"):
        message += f"{contact['description']}\n"

    phones = contact.get("phones", {})
    landlines = phones.get("landline", [])
    mobiles = phones.get("mobile", [])

    if landlines:
        message += "\n☎ Landline\n"
        for num in landlines:
            message += f"{num}\n"

    if mobiles:
        message += "\n📱 Mobile\n"
        for num in mobiles:
            message += f"{num}\n"

    if contact.get("available_24_7"):
        message += "\n🕒 Available 24/7"

    return message
