def main_menu():

    return [

        {
            "content_type": "text",
            "title": "🚨 Emergency Mode",
            "payload": "emergency_mode"
        },

        {
            "content_type": "text",
            "title": "🚓 Pulis",
            "payload": "police"
        },

        {
            "content_type": "text",
            "title": "🚑 Ambulansya",
            "payload": "ambulance"
        },

        {
            "content_type": "text",
            "title": "🔥 Sunog",
            "payload": "fire"
        },

        {
            "content_type": "text",
            "title": "🧠 Mental Health",
            "payload": "mental_health"
        },

        {
            "content_type": "text",
            "title": "👩‍👧 Proteksyon sa Kababaihan",
            "payload": "women_children"
        }

    ]


def location_menu(emergency_type):

    return [

        {
            "content_type": "text",
            "title": "📍 Makati",
            "payload": f"{emergency_type}|makati"
        },

        {
            "content_type": "text",
            "title": "🇵🇭 National",
            "payload": f"{emergency_type}|national"
        },

        {
            "content_type": "text",
            "title": "🏙 Other City",
            "payload": "other_city"
        }

    ]


def emergency_menu():

    return [

        {
            "content_type": "text",
            "title": "🚓 Pulis",
            "payload": "police"
        },

        {
            "content_type": "text",
            "title": "🚑 Ambulansya",
            "payload": "ambulance"
        },

        {
            "content_type": "text",
            "title": "🔥 Sunog",
            "payload": "fire"
        },

        {
            "content_type": "text",
            "title": "🇵🇭 Pambansang Hotline",
            "payload": "national_hotline"
        }

    ]
