import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

st.title("Predicting homelessness risk")

st.markdown("METHODOLOGY")

image = Image.open("/home/reshmam/Documents/Documents/GitHub/re-housed/dashboard/images/modelA.png")
st.image(image, caption="This is an image", use_container_width=True)