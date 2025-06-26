import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os


st.title("Re:Housed | An ideal intersection of social network & service accessibility. ")

st.markdown("SUMMARY")
st.header("Spatially distributed model map", divider=True)

# with open("/home/reshmam/Documents/Documents/GitHub/re-housed/dashboard/images/map.html",'r') as file: 
#     html_data = file.read()
# components.html(html_data, width=1000, height=600)

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "final.png")

image = Image.open(img_path)
st.image(image, caption="This is an image", use_container_width=True)


st.markdown("RESULTS")

st.markdown("CONCLUSION")