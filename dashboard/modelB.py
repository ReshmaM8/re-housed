import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

st.title("Understand service demand for encampment.")

st.markdown("METHODOLOGY")

image = Image.open("../dashboard/images/modelB.png")
st.image(image, caption="This is an image", use_container_width=True)

image2 = Image.open("../dashboard/images/modelB2.png")
st.image(image2, caption="This is an image", use_container_width=True)