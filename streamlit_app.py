import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Title for the app
st.title('Image Viewer')

# Load the image from file
image = Image.open('.devcontainer/Screenshot 2021-06-02 141726.png')

# Display the image
st.image(image, caption='Example Image', use_column_width=True)


