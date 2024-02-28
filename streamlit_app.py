import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

import streamlit as st

def main():
    
    st.title("Multiclass Classification with Many Categories")
    
    # Sidebar navigation
    option = st.sidebar.radio('Navigation', ['Home', 'Dataset 1 before hyperparameter tuning', 'Dataset 1 after hyperparameter tuning'])
    
    if option == 'Home':
        display_home()
    elif option == 'Dataset 1 before hyperparameter tuning':
        display_technique_1()
    elif option == 'Dataset 1 after hyperparameter tuning':
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
    st.subheader("Comparing the weighted average of precision, recall and f1-score before hyperparameter tuning ")
    data = {
        "Method on first 99 features": ["Label Encoder", "Label Encoder", "Label Encoder", "Label Encoder", "Label Encoder"],
        "Model": ["RF", "Gaussian NB", "DT", "KNN", "SVM"],
        "Accuracy": [0.818, 0.524, 0.883, 0.502, 0.684],
        "Precision": [0.831, 0.710, 0.906, 0.562, 0.664],
        "Recall": [0.818, 0.524, 0.883, 0.502, 0.684],
        "F1 Score": [0.809, 0.572, 0.889, 0.513, 0.662]
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Display the table
    st.write(df)

# Call the function to display the table
#display_technique_1()

def display_technique_2():
    st.subheader("Comparing the weighted average of precision, recall and f1-score after hyperparameter tuning")
    data = {
        'Method on first 99 features': ['Label Encoder', 'Label Encoder', 'Label Encoder', 'Label Encoder', 'Label Encoder'],
        'Model': ['RF', 'Gaussian NB', 'DT', 'KNN', 'SVM'],
        'Accuracy': [0.804, 0.665, 0.883, 0.519, 0.694],
        'Precision': [0.815, 0.727, 0.906, 0.547, 0.682],
        'Recall': [0.804, 0.665, 0.883, 0.519, 0.694],
        'F1 Score': [0.794, 0.682, 0.889, 0.526, 0.673]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the table
    st.write(df)


if __name__ == "__main__":
    main()






