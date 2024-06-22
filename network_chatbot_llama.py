# import streamlit as st


# import ollama
 
# # Custom page style


# page_style = '''


# <style>


# [data-testid="stAppViewContainer"] {


#     background-image: url("https://images.unsplash.com/photo-1545987796-200677ee1011?q=80&w=2970&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");


#     background-size: cover;


#     background-repeat: no-repeat;


#     background-attachment: fixed;


# }
 
# .output-block {
#     background-color: white;
#     border-radius: 15px;
#     padding: 20px;
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#     margin-top: 20px;
# }


# </style>


# '''
 
# st.markdown(page_style, unsafe_allow_html=True)
 
# # Title of the app


# st.title("Network Support Chatbot")
 
# # Input for user query


# query = st.text_input("Ask your network related question:")
 
# # Display response if query is entered


# if query:


#     response = ollama.chat(model='llama3', messages=[


#         {


#             'role': 'user',


#             'content': query,


#         },


#     ])


#     # st.write(response['message']['content'])
    
#     # Display the response in a styled div
#     st.markdown(f'<div class="output-block">{response["message"]["content"]}</div>', unsafe_allow_html=True)

# import streamlit as st
# import ollama

# # Define the model creation script
# modelfile = '''
# FROM llama3
# SYSTEM You are a subject matter expert in networks especially cisco and mikrotik devices
# '''

# # Create the model (assuming the 'ollama.create' function works synchronously)
# ollama.create(model='network_chatbot_llama', modelfile=modelfile)

# # Title of the app
# st.title("Network Support Chatbot")

# # Initialize session state for conversation history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Input for user query
# query = st.text_input("Ask your network-related question:")

# # Display response if query is entered
# if query:
#     response = ollama.chat(model='network_chatbot_llama', messages=[
#         {
#             'role': 'user',
#             'content': query,
#         },
#     ])
#     # Update conversation history
#     st.session_state.history.append({'role': 'user', 'content': query})
#     st.session_state.history.append({'role': 'bot', 'content': response['message']['content']})

# # Display the conversation history
# for message in st.session_state.history:
#     if message['role'] == 'user':
#         st.markdown(f"**You:** {message['content']}")
#     else:
#         st.markdown(f"**Bot:** {message['content']}")






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
    background-color: #4a90e2;
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
</style>
'''

st.markdown(page_style, unsafe_allow_html=True)

# Add a banner with your name and NU ID
st.markdown('<div class="banner"><h2>Network Support Chatbot</h2><p>Created by Emmanuel Chibua | NU ID: 002799484</p></div>', unsafe_allow_html=True)

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Input for user query
query = st.text_input("Ask your network-related question:")

# Display response if query is entered and submit button is pressed
if st.button("Submit"):
    response = ollama.chat(model='network_chatbot_llama', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    # Update conversation history
    st.session_state.history.append({'role': 'user', 'content': query})
    st.session_state.history.append({'role': 'bot', 'content': response['message']['content']})

# Display the conversation history
for message in st.session_state.history:
    if message['role'] == 'user':
        st.markdown(f'<div class="message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message"><strong>Bot:</strong> {message["content"]}</div>', unsafe_allow_html=True)

# Add a footer to th chatbot application
st.markdown('<div class="footer">© 2024 Emmanuel Chibua. All rights reserved.</div>', unsafe_allow_html=True)
