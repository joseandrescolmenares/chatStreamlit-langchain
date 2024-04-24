import streamlit as st

from dotenv import load_dotenv


load_dotenv()

# app config
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖")
st.title("Chatbot")

user_query = st.chat_input("your message")
