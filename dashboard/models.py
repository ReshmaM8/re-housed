import streamlit as st
import numpy as np
import pandas as pd

import streamlit.components.v1 as components

st.title("Shelter Sites: K-means Clustering")



with open("/home/reshmam/Documents/Documents/GitHub/re-housed/K-Means Clustering/Toronto_existing_shelters_clustered_with_zone_demand/toronto_demand_clusters_map.html",'r') as file: 
    html_data = file.read()


with open("/home/reshmam/Documents/Documents/GitHub/re-housed/K-Means Clustering/Toronto_existing_shelters_clustered_with_zone_demand/toronto_demand_clusters_map.html",'r') as file: 
    html_data1= file.read()


with open("/home/reshmam/Documents/Documents/GitHub/re-housed/K-Means Clustering/Toronto_existing_shelters_clustered_with_zone_demand/toronto_demand_clusters_map.html",'r') as file: 
    html_data2 = file.read()

st.header("By zone demand:", divider=True)
components.html(html_data, width=750, height=600)
st.header("By zone demand:", divider=True)
components.html(html_data1, width=750, height=600)
st.header("By zone demand:", divider=True)
components.html(html_data2, width=750, height=600)


