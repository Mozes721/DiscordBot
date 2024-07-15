import os
import streamlit as st
import time
import random

class LocalBot:
    def __init__(self) -> None:
       self.initialze_session_state()
       st.title("Simple chat")

    def  initialze_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
    def response_generator(self):
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        ) 
        for word in response.split():
            yield word + " "
            time.sleep(0.05)
            
    def display_chat_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def get_user_input(self):
        return st.chat_input("What is up?")
    
    def run(self):
        self.display_chat_history()

        if prompt := self.get_user_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = st.write_stream(self.response_generator())
            st.session_state.messages.append({"role": "assistant", "content": response})

