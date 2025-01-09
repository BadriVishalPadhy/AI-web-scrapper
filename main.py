import streamlit as st
from scrape import scrape_website

st.title("AI web scraper")
url = st.text_input("Enter Site URL:")

if st.button("Scrape Site"):
    st.write("Write Something")
    result =scrape_website(url)
    print(result)