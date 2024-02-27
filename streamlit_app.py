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

# Sample data for demonstration
data = {
    'Dataset': ['Dataset 1', 'Dataset 2'],
    'Description': ['Description of Dataset 1', 'Description of Dataset 2'],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
st.write(df)

"""
 There are two datasets

"""
