import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

from mood_detector import detect_mood
from song_recommender import recommend_song
from activity_generator import generate_activity

# Load API key
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Streamlit UI
st.title("😊 Mood Boosting AI Companion")

st.write("Tell me how you feel today")

# User input
user_input = st.text_input("Enter your mood or message")

if st.button("Boost My Mood"):

    if user_input.strip() == "":
        st.warning("Please enter a message about how you feel.")
        st.stop()

    # Detect mood
    mood = detect_mood(user_input)

    # Get song recommendation
    song_name, song_url = recommend_song(mood)

    # Get activity suggestion
    activity = generate_activity(mood)

    # AI prompt
    prompt = f"""
User mood: {mood}
User message: {user_input}

Act as a friendly mood boosting companion.

Respond with:
1 motivational message
1 helpful suggestion
1 inspirational quote
"""

    # Call Groq API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ai_reply = response.choices[0].message.content

    # Display AI response
    st.subheader("✨ Motivation")
    st.write(ai_reply)

    # Activity suggestion
    st.subheader("🧘 Small Activity")
    st.write(activity)

    # Song recommendation
    st.subheader("🎵 Song Recommendation")
    st.write(song_name)

    # Show YouTube video in the app
    st.video(song_url)

    # Button to open YouTube
    st.link_button("▶ Play Full Song on YouTube", song_url)