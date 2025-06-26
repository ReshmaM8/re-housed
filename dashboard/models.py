import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

st.title("Re:Housed | An ideal intersection of social network & service accessibility. ")

st.markdown("SUMMARY")
st.header("Spatially distributed model map", divider=True)

# with open("/home/reshmam/Documents/Documents/GitHub/re-housed/dashboard/images/map.html",'r') as file: 
#     html_data = file.read()
# components.html(html_data, width=1000, height=600)
image = Image.open("/home/reshmam/Documents/Documents/GitHub/re-housed/dashboard/images/final.png")
st.image(image, caption="This is an image", use_container_width=True)


st.markdown("RESULTS")

st.markdown("CONCLUSION")