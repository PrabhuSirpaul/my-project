import streamlit as st

# Your other Streamlit code goes here, like widgets, inputs, etc.

# Example Streamlit code
st.title("Your Streamlit App")
st.write("This is a simple Streamlit app.")

# Example widgets
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)

# Display the inputs
if name and age:
    st.write(f"Hello, {name}! You are {age} years old.")
