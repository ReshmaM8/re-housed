import streamlit as st

# Define the pages
main_page = st.Page("models.py", title="Final Model")
page_2 = st.Page("modelA.py", title="Predicting homelessness risk")
page_3 = st.Page("modelB.py", title="Understanding encampment service demand")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()
