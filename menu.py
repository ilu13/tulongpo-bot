def main_menu():

    return [

        {
            "content_type": "text",
            "title": "🚓 Police",
            "payload": "police"
        },

        {
            "content_type": "text",
            "title": "🚑 Ambulance",
            "payload": "ambulance"
        },

        {
            "content_type": "text",
            "title": "🔥 Fire",
            "payload": "fire"
        },

        {
            "content_type": "text",
            "title": "🧠 Mental Health",
            "payload": "mental_health"
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
