import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


# Title for the app
st.title('Image Viewer')

# Load the image from file
image = Image.open('.devcontainer/Screenshot 2021-06-02 141726.png')

# Display the image
st.image(image, caption='Example Image', use_column_width=True)


