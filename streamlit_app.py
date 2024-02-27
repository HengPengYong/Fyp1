import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

"""
# Multiclass Classification with Many Categories

"""
# Title for the app
st.title('Entire Architecture Diagram')

# Load the image from file
image = Image.open('.devcontainer/Screenshot 2021-06-02 141726.png')

# Display the image
st.image(image, caption='Example Image', use_column_width=True)

st.write('## Datasets')

# Create a list of tuples containing data for the table
data = [
    ('Dataset 1', 'Description of Dataset 1'),
    ('Dataset 2', 'Description of Dataset 2'),
]

df = pd.DataFrame(data)
# Display the table
st.write(df)

"""
 There are two datasets

"""

# Title for the table
st.write('## Techniques Used On Feature Variables')

# Data for the table
data = {
    'Dataset': ['Dataset 1', 'Dataset 2'],
    'Label Encoding': ['Label Encoding', 'Label Encoding'],
    'Word Embedding': ['all-MiniLM-L6-v2', 'all-MiniLM-L6-v2'],
    '': ['all-MiniLM-L12-v2','']
}

# Display the table
st.table(data)

# Define the data for both techniques
data_technique_1 = {
    'Dataset': ['Dataset 1', 'Dataset 2'],
    'Label Encoding': ['Label Encoding', 'Label Encoding'],
    'Word Embedding': ['all-MiniLM-L12-v2', 'all-MiniLM-L6-v2'],
    'Model': ['all-MiniLM-L12-v2', 'all-MiniLM-L6-v2']
}

data_technique_2 = {
    'Dataset': ['Dataset 1', 'Dataset 2'],
    'Label Encoding': ['Label Encoding', 'Label Encoding'],
    'Word Embedding': ['all-MiniLM-L6-v2', 'all-MiniLM-L6-v2'],
    'Model': ['all-MiniLM-L12-v2', 'all-MiniLM-L6-v2']
}

# Radio button to select technique
selected_technique = st.radio("Techniques Used", ['Technique 1', 'Technique 2'])

# Display table based on selected technique
if selected_technique == 'Technique 1':
    st.write('## Techniques Used - Technique 1')
    st.table(data_technique_1)
elif selected_technique == 'Technique 2':
    st.write('## Techniques Used - Technique 2')
    st.table(data_technique_2)
