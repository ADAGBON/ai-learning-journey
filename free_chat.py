import streamlit as st
import requests
import json

st.title("🤖 My First AI Chat App (Free Version)")
st.write("Built on Day 1 of my AI journey!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response using Hugging Face free API
    with st.chat_message("assistant"):
        try:
            # Using Hugging Face's free inference API
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            
            response = requests.post(API_URL, 
                json={"inputs": prompt},
                headers={"Authorization": "Bearer hf_your_token_here"}  # We'll make this work without token
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result[0]['generated_text'] if result else "I'm thinking... try again!"
            else:
                ai_response = f"I'm a simple echo bot for now: {prompt}"
            
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            ai_response = f"Echo: {prompt} (Free version working!)"
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
