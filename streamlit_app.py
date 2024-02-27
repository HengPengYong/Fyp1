import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

import streamlit as st

def main():
    st.title("Multiclass Classification with Many Categories")
    
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
    candidate_name = "Heng Peng Yong"
    supervisor_name = "Ts. Dr. Goh Hui Ngo"
    moderator_name = "Prof. Ts. Dr. Ting Choo Yee"
    
    st.subheader("Names:")
    st.write(f"- Candidate: {candidate_name}")
    st.write(f"- Supervisor: {supervisor_name}")
    st.write(f"- Moderator: {moderator_name}")

def display_technique_1():
    st.subheader("Technique 1 Content Goes Here")

def display_technique_2():
    st.subheader("Technique 2 Content Goes Here")

if __name__ == "__main__":
    main()

