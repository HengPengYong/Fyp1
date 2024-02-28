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
    elif option == 'Dataset 1 before hyperparameter tuning':
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
    data = {
        "Method on first 99 features": [" "],
        "Model": ["RF", "Gaussian NB", "DT", "KNN", "SVM"],
        "Accuracy": [0.818, 0.524, 0.883, 0.502, 0.684],
        "Precision": [0.831, 0.710, 0.906, 0.562, 0.664],
        "Recall": [0.818, 0.524, 0.883, 0.502, 0.684],
        "F1 Score": [0.809, 0.572, 0.889, 0.513, 0.662]
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Display the table
    st.table(df)

# Call the function to display the table
display_technique_1()

def display_technique_2():
    st.subheader("Technique 2 Content Goes Here")

if __name__ == "__main__":
    main()

