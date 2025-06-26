import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os


st.title("Re:Housed | An ideal intersection of social network & service accessibility. ")

st.markdown(" :blue[TL;DR] We create two models and overlay them atop each other to create a a final geospatial map that shows optimized shelter locations based on service demands and most amount of people served")
st.header("Spatially distributed model map", divider=True)

# with open("/home/reshmam/Documents/Documents/GitHub/re-housed/dashboard/images/map.html",'r') as file: 
#     html_data = file.read()
# components.html(html_data, width=1000, height=600)

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "final.png")

image = Image.open(img_path)
st.image(image, caption="Spatially distributed model map", use_container_width=True)

st.divider()
st.markdown("RESULTS")
st.markdown("The analysis successfully identified 20 spatially distributed areas that exhibit a high combined score from the two prediction layers. These areas are suggested as potential priority locations based on the input data and the defined criteria for selection (high combined prediction and spatial separation).")