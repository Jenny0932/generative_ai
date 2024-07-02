from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
client = OpenAI(api_key=OPENAI_API_KEY)

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you?"}
    ]


    
if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
            ai_msg = response.choices[0].message.content
            st.write(ai_msg)
            message = {"role": "assistant", "content": ai_msg}
            st.session_state.messages.append(message) # Add response to message history