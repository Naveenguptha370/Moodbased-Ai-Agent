from textblob import TextBlob

def detect_mood(text):

    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score > 0.3:
        return "happy"

    elif score < -0.3:
        return "sad"

    else:
        return "neutral"