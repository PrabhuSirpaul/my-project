import os
import streamlit as st

# Get the port from the environment variable or default to 8501 if not set
port = os.getenv("PORT", 8501)

# Set up the Streamlit page configuration
st.set_page_config(page_title="Your App", page_icon=":guardsman:", layout="centered")

# Your Streamlit UI code goes here
st.title("Welcome to Your Streamlit App")
st.write("This is a basic example of a Streamlit app.")

# Add some other elements like buttons or text fields
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Run Streamlit with the dynamically assigned port
if __name__ == "__main__":
    # Streamlit will automatically detect the correct port, but you can explicitly specify it here
    st.run(port=port)
