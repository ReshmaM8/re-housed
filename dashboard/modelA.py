import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os


st.title("Predicting homelessness risk")

st.markdown("METHODOLOGY")

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "modelA.png")

image = Image.open(img_path)
st.image(image, caption="This is an image", use_container_width=True)