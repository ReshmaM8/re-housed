import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os

st.title("Understand service demand for encampment.")


st.markdown(" :blue[Motivation:] We look at existing encampments and public services(washrooms,health centre, etc) in Toronto and predict the future encampment sizes. Essentially, what we are trying to answer is :blue[what services tend to create larger encampments?] ")


base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "modelB.png")
img_path2 = os.path.join(base_dir, "images", "modelB2.png")

img_path3 = os.path.join(base_dir, "images", "modelB3.png")
image = Image.open(img_path)
image2 = Image.open(img_path2)
image3 = Image.open(img_path3)
# image = Image.open("../dashboard/images/modelB.png")
st.image(image, caption="Predicted encampment size", use_container_width=True)
st.markdown("### But how well does it compare to actual encampment sizes ?")
st.image(image3, caption="Predicted encampment size vs actual", use_container_width=True)
# image2 = Image.open("../dashboard/images/modelB2.png")
st.markdown("Our model prediction is on the right path, showing intuition of where the encampment size are strongest - with additional fine tuning, we could get it to predict at a better accuracy!")
st.image(image2, caption="Feature Importance map", use_container_width=True)

