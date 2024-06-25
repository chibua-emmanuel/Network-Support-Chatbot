import streamlit as st
import ollama

# Define the model creation script
modelfile = '''
FROM llama3
SYSTEM You are a subject matter expert in networks especially Cisco and Mikrotik devices
'''

# Create the model (assuming the 'ollama.create' function works synchronously)
ollama.create(model='network_chatbot_llama', modelfile=modelfile)

# Custom page style
page_style = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f2f6;
}

.banner {
    background-color: #80eede;
    color: white;
    padding: 10px;
    text-align: center;
    border-radius: 10px;
    margin-bottom: 20px;
}

.footer {
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 10px;
    text-align: center;
    border-radius: 10px;
    margin-top: 20px;
}

.message {
    background-color: white;
    border-radius: 10px;
    padding: 10px;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-message {
    background-color: #d1e7dd;
}

.bot-message {
    background-color: #f8d7da;
}

.stTextInput > div > input {
    border: 2px solid #4a90e2;
    border-radius: 5px;
    padding: 5px;
}
</style>
'''

st.markdown(page_style, unsafe_allow_html=True)

# Add a banner with your name and NU ID
st.markdown('<div class="banner"><h2>Network Support Chatbot</h2><p>Created by Emmanuel Chibua | NU ID: 002799484</p></div>', unsafe_allow_html=True)

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to handle new user query
def handle_query():
    query = st.session_state.query
    if query:
        response = ollama.chat(model='network_chatbot_llama', messages=[
            {
                'role': 'user',
                'content': query,
            },
        ])
        # Update conversation history
        st.session_state.history.append({'role': 'user', 'content': query})
        st.session_state.history.append({'role': 'bot', 'content': response['message']['content']})
        # Clear the input box
        st.session_state.query = ''

# Input for user query with on_change callback
st.text_input("Ask your network-related question:", key='query', on_change=handle_query)

# Display the conversation history in reverse order
for message in reversed(st.session_state.history):
    if message['role'] == 'user':
        st.markdown(f'<div class="message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message"><strong>Bot:</strong> {message["content"]}</div>', unsafe_allow_html=True)

# Add a footer
st.markdown('<div class="footer">© 2024 Emmanuel Chibua. All rights reserved.</div>', unsafe_allow_html=True)




