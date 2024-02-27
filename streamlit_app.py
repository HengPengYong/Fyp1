import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

import streamlit as st

def main():
    st.title("Thesis Defense Presentation")
    
    # Sidebar navigation
    option = st.sidebar.radio('Navigation', ['Home', 'Technique 1', 'Technique 2'])
    
    if option == 'Home':
        display_home()
    elif option == 'Technique 1':
        display_technique_1()
    elif option == 'Technique 2':
        display_technique_2()

def display_home():
    # Display today's date
    st.subheader("Date: February 27, 2024")  # Replace with the current date
    
    # Names of candidate, supervisor, and moderator
    candidate_name = "John Doe"
    supervisor_name = "Dr. Jane Smith"
    moderator_name = "Prof. Michael Johnson"
    
    st.subheader("Names:")
    st.write(f"- Candidate: {candidate_name}")
    st.write(f"- Supervisor: {candidate_name}")
    st.write(f"- Moderator: {candidate_name}")

def display_technique_1():
    st.subheader("Technique 1 Content Goes Here")

def display_technique_2():
    st.subheader("Technique 2 Content Goes Here")

if __name__ == "__main__":
    main()

