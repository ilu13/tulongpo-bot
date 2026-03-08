from contact_lookup import get_contact, format_contact


# -------- INTENT ALIASES --------

INTENT_ALIASES = {

    "police": [
        "police",
        "pulis",
        "holdap",
        "robbery",
        "crime",
        "magnanakaw"
    ],

    "fire": [
        "fire",
        "sunog",
        "nasusunog",
        "may sunog",
        "bumbero"
    ],

    "ambulance": [
        "ambulance",
        "ambulansya",
        "medical",
        "hospital",
        "nasugatan",
        "injured"
    ],

    "mental_health": [
        "mental",
        "suicide",
        "depressed",
        "tulong"
    ],

    "women_children": [
        "abuse",
        "violence",
        "rape",
        "trafficking"
    ]
}


# -------- LOCATION ALIASES --------

LOCATION_ALIASES = {

    "makati": [
        "makati",
        "makati city",
        "mkt"
    ]

}


# -------- INTENT DETECTOR --------

def detect_intent(text):

    text = text.lower()

    for intent, keywords in INTENT_ALIASES.items():

        for word in keywords:

            if word in text:
                return intent

    return None


# -------- LOCATION DETECTOR --------

def detect_location(text):

    text = text.lower()

    for location, aliases in LOCATION_ALIASES.items():

        for alias in aliases:

            if alias in text:
                return location

    return "national"


# -------- MAIN RESPONSE FUNCTION --------

def get_response(text):

    text = text.lower()

    location = detect_location(text)

    intent = detect_intent(text)

    if intent:

        contact = get_contact(location, intent)

        return format_contact(contact)

    return (
        "I can help you find emergency contacts.\n\n"
        "Try typing:\n"
        "🚓 police\n"
        "🔥 fire\n"
        "🚑 ambulance\n"
        "🧠 mental health\n\n"
        "You can also include a city like:\n"
        "fire makati"
    )
