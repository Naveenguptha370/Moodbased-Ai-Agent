import random

def generate_activity(mood):

    activities = {

        "happy":[
        "Write 3 things you are grateful for.",
        "Share your happiness with a friend.",
        "Take a short walk."
        ],

        "sad":[
        "Take 5 deep breaths.",
        "Listen to calming music for 5 minutes.",
        "Write your feelings in a journal."
        ],

        "neutral":[
        "Stretch your body for 2 minutes.",
        "Drink a glass of water.",
        "Take a small break."
        ]
    }

    return random.choice(activities[mood])