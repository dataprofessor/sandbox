import streamlit as st

selected_options = st.multiselect("Select one or more options:",
    ['A', 'B', 'C'])

all_options = st.button("Select all options")

if all_options:
    selected_options = ['A', 'B', 'C']

selected_options
