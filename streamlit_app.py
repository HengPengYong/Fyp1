import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

def main():
    st.title("Thesis Defense Presentation")
    
    # Display today's date
    st.subheader("Date: February 27, 2024")  # Replace with the current date
    
    # Names of candidate, supervisor, and moderator
    candidate_name = "John Doe"
    supervisor_name = "Dr. Jane Smith"
    moderator_name = "Prof. Michael Johnson"
    
    st.subheader("Names:")
    st.write(f"- Candidate: {candidate_name}")
    st.write(f"- Supervisor: {supervisor_name}")
    st.write(f"- Moderator: {moderator_name}")
    
if __name__ == "__main__":
    main()
