    # Example using a hypothetical 'streamlit_card' component
    # You would need to install this component first: pip install streamlit-card
import streamlit as st
from streamlit_card import card


st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([4,4,4])
col4,col5,col6= st.columns([4,4,4])

with col1: 
    hasClicked = card(
            key="key1",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)" 
                },
               
            },
            on_click=lambda: st.write("Card clicked!")
        )



with col2: 
    hasClicked1 = card(
            key="key2",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)"  # <- make the image not dimmed anymore
                },
            },
            on_click=lambda: st.write("Card clicked!")
        )



with col3: 
    hasClicked2 = card(
            key="key3",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)"  # <- make the image not dimmed anymore
                },
            },
            on_click=lambda: st.write("Card clicked!")
        )

with col4 :
    hasClicked = card(
            key="key4",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)" 
                },
               
            },
            on_click=lambda: st.write("Card clicked!")
        )



with col5: 
    hasClicked1 = card(
            key="key5",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)"  # <- make the image not dimmed anymore
                },
            },
            on_click=lambda: st.write("Card clicked!")
        )



with col6:
      hasClicked1 = card(
            key="key6",
            title="Product Name",
            text="A brief description of the product.",
            styles={
            "card": {
                "width": "100%",
                "height": "191px",
                "border-radius": "12px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "filter": {
                    "background-color": "rgba(165, 195, 222, 1)"  # <- make the image not dimmed anymore
                },
            },
            on_click=lambda: st.write("Card clicked!")
        )