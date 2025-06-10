#importing streamlit library for creating web app
import streamlit as st

#setting title of the app
st.title("one simple bot")

#Function to generate bot response based on user input
def get_bot_response(user_input):
    user_input = user_input.lower() #convert user_input into lower, for better matching

#using simple "if else" so that bot respond according to the input provided
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! how can I help you?"
    elif "how are you?" in user_input:
        return "Yes, I'm doing great and how about you?"
    elif "bye" in user_input:
        return "Goodbye! have a nice day"
    else:
        return "Sorry I don't understand"

#text input box for user to type a message
user_input = st.text_input("You:")

#when send button is clicked and user input is not empty
if st.button("Send") and user_input:
    st.markdown(f"**You:** {user_input}") #displays user input
    bot_response = get_bot_response(user_input)
    st.markdown(f"**Bot:** {bot_response}") #displays bot response