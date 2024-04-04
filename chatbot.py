# import the packages
import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Provide the api key
api_key = "AIzaSyDmosAr83VL2gH0-ld5bBJ4rLIhyvO_okw"
genai.configure(api_key=api_key)

# Read the Model

# Streamlit UI Parameters
st.title("Chatbot Via Streamlit")


def generate_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    output = response.text
    return output


# create chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'bot_history' not in st.session_state:
    st.session_state['bot_history'] = []

input_container = st.container()
response_container = st.container()

# capture user input and display bot response
user_input = st.text_input("You: ", "", key="input")

with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state['chat_history'].append(user_input)
        st.session_state['bot_history'].append(response)

    num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
    if num_messages > 0:
        for i in range(num_messages):
            message(st.session_state['chat_history'][i], is_user=True, key=str(i) + '_user', avatar_style="initials",
                    seed="Me")
            message(st.session_state['bot_history'][i], key=str(i), avatar_style="initials", seed="AI", )

with input_container:
    display_input = user_input
    
