import streamlit as st

# Define the pages
main_page = st.Page("models.py", title="Models")
page_2 = st.Page("shelter_sites_management.py", title="Shelter Sites")


# Set up navigation
pg = st.navigation([main_page, page_2])

# Run the selected page
pg.run()
