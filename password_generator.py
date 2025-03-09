import streamlit as st
import random
import string

# Title of the app
st.title("Password Generator")

# Ask the user for the password length
length = st.number_input("**How long should the password be?**", min_value=8, max_value=50, value=12)

# Define all possible characters for the password
characters = string.ascii_letters + string.digits + "!@#$%^&*"

# Generate the password when the button is clicked
if st.button("Generate Password"):
    password = ''.join(random.choice(characters) for _ in range(length))
    st.success("Your password is:")
    st.code(password)