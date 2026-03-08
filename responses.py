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
        "mental health",
        "suicide",
        "depressed"
    ],

    "women_children": [
        "abuse",
        "violence",
        "rape",
        "trafficking",
        "kababaihan",
        "bata",
        "women",
        "children"
    ]
}


# -------- LOCATION ALIASES --------

LOCATION_ALIASES = {

    "makati": [
        "makati",
        "makati city",
        "mkt"
    ],

    "quezon_city": [
        "qc",
        "q.c.",
        "quezon city"
    ],

    "manila": [
        "manila",
        "city of manila"
    ]

}


# -------- HELP WORDS --------

HELP_WORDS = [
    "help",
    "menu",
    "start",
    "hello",
    "hi"
]


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


# -------- HELP MESSAGE --------

def get_help_message():

    return (
        "Maaari kitang tulungan hanapin ang tamang emergency contact.\n\n"
        "Subukang i-type ang:\n"
        "🚓 pulis\n"
        "🔥 sunog\n"
        "🚑 ambulansya\n"
        "🧠 mental health\n"
        "👩‍👧 proteksyon sa kababaihan\n\n"
        "Pwede rin lagyan ng lugar, halimbawa:\n"
        "• sunog makati\n"
        "• sunog qc\n"
        "• pulis manila\n"
        "• ambulansya makati"
    )


# -------- MAIN RESPONSE FUNCTION --------

def get_response(text):

    text = text.lower().strip()

    if text in HELP_WORDS:
        return get_help_message()

    location = detect_location(text)

    intent = detect_intent(text)

    if intent:

        contact = get_contact(location, intent)

        return format_contact(contact)

    return get_help_message()
