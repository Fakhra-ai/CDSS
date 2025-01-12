import streamlit as st
import pandas as pd
import math
from pathlib import Path
import streamlit as st
# Set page configuration
st.set_page_config(page_title="Smart CDSS", page_icon="🧠", layout="centered")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Function to switch pages
def switch_page(page_name):
    st.session_state.page = page_name

# Welcome Page
if st.session_state.page == "welcome":
    st.markdown(
        """
        <h1 style="text-align: center; color: #4CAF50; font-family: 'Arial';">
            🤖 Welcome to <span style="color: #FF5722;">Smart CDSS</span>! 🩺
        </h1>
        <p style="text-align: center; font-size: 18px; color: #555;">
            Empowering healthcare with intelligent decision-making. 🌟
        </p>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Get Started"):
        switch_page("user_info")

# User Information Page
elif st.session_state.page == "user_info":
    st.markdown(
        """
        <h2 style="text-align: center; color: #4CAF50;">Tell us about yourself</h2>
        """
        , unsafe_allow_html=True)
    
    # Input fields
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    
    if st.button("Submit"):
        if name and age > 0:
            st.success(f"Welcome, {name}! Let's get started.")
            # Store user info in session state for future use
            st.session_state["user_name"] = name
            st.session_state["user_age"] = age
            st.session_state["user_gender"] = gender
            switch_page("main_app")
        else:
            st.error("Please fill in all the fields correctly!")

# Main App Page
elif st.session_state.page == "main_app":
    st.markdown(
        f"""
        <h2 style="text-align: center; color: #4CAF50;">Hello, {st.session_state['user_name']}!</h2>
        <p style="text-align: center; font-size: 16px;">Age: {st.session_state['user_age']} | Gender: {st.session_state['user_gender']}</p>
        <p style="text-align: center;">Start exploring the Smart CDSS features now! 🌟</p>
        """,
        unsafe_allow_html=True,
    )

