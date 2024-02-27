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
st.table(df)

"""
 There are two datasets

"""
