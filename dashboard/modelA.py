import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import os


st.title("Predicting homelessness risk")

st.markdown(":blue[Motivation:] Evictions lead to homelessness and with the lack of affordable housing in Toronto, it will be hard for individuals to get back to stable housing. We use a Random Forest classifier to answer whether the person is at risk of homelessness")

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "modelA.png")

image = Image.open(img_path)
st.image(image, caption="Prediction index by neighbourhood: the darker the blue, the more likely the neighbourhood contains high homelessness", use_container_width=True)
st.markdown(" This map also gives us an idea of the intial social networks - social networks are an integral component for human mental health and often people want to stay within the communities they know. We take this need into account when we create our final shelther recommendation map.")