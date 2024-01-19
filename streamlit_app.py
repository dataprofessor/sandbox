import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "Drama", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the [popcorn](http://www.google.com).", "Never stop learning."])


