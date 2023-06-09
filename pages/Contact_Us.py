import streamlit as st
from send_email import send_email


st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area(" your message")
    message = f"""\
Subject : New email form {user_email}
    
From : {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
