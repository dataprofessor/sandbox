import streamlit as st

cols = st.columns(3)

with cols[0]:
    st.header('Option 1')
    selected_options = st.multiselect("Select one or more options:",
        ['A', 'B', 'C'], key='option')
    
    all_options = st.button("Select all options")
    
    if all_options:
        selected_options = ['A', 'B', 'C']
    
    selected_options

with cols[1]:
    st.header('Option 2')
    selected_option_2 = st.multiselect("Select one or more options:",['A', 'B', 'C', 'All'], key='option_2')

    if "All" in selected_option_2:
        selected_option_2 = ['A', 'B', 'C']
    
    selected_option_2

with cols[2]:
    st.header('Option 3')
    container = st.container()
    all = st.button("Select all")
     
    if all:
        selected_options_3 = container.multiselect("Select one or more options:",
             ['A', 'B', 'C'],['A', 'B', 'C'], key='option_3')
    else:
        selected_options_3 =  container.multiselect("Select one or more options:",
            ['A', 'B', 'C'], key='option_3')



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***[Drama](http://www.google.com)***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])


