import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "Drama", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the [popcorn](http://www.google.com).", "Never stop learning."])


st.divider()

language_options = {
    '🇺🇸': 'American English',
    '🇬🇧': 'British English',
    '🇧🇷': 'Portugese',
}

selected_language = st.radio('Select a language:', options=language_options)

st.write(f'Selected language: {language_options[selected_language]}')
