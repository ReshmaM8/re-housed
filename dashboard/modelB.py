import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os

st.title("Understand service demand for encampment.")

st.markdown("METHODOLOGY")

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "modelB.png")
img_path2 = os.path.join(base_dir, "images", "modelB2.png")
image = Image.open(img_path)
image2 = Image.open(img_path2)
# image = Image.open("../dashboard/images/modelB.png")
st.image(image, caption="This is an image", use_container_width=True)

# image2 = Image.open("../dashboard/images/modelB2.png")
st.image(image2, caption="This is an image", use_container_width=True)