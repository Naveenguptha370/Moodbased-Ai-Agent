def recommend_song(mood):

    songs = {
        "happy": ("Happy – Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),

        "sad": ("Fix You – Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),

        "angry": ("Stronger – Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),

        "relaxed": ("Perfect – Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g"),

        "excited": ("On Top of the World – Imagine Dragons", "https://www.youtube.com/watch?v=w5tWYmIOWGk"),

        "stressed": ("Weightless – Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),

        "bored": ("Counting Stars – OneRepublic", "https://www.youtube.com/watch?v=hT_nvWreIhg"),

        "lonely": ("Someone Like You – Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),

        "motivated": ("Hall of Fame – The Script", "https://www.youtube.com/watch?v=mk48xRzuNvA"),

        "tired": ("Let Her Go – Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA")
    }

    return songs.get(mood, ("Believer – Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"))