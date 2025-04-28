import streamlit as st
import requests

st.title("Text Summarizer App 🚀")

input_text = st.text_area("Enter your paragraph here:")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/summarize",
            json={"text": input_text}
        )
        
        if response.status_code == 200:
            result = response.json()
            st.subheader("Summary:")
            st.success(result['summary'])
        else:
            st.error("Error occurred while summarizing. Please try again.")
