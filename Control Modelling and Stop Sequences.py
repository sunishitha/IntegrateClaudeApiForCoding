#Load env variables
from dotenv import load_dotenv
load_dotenv()

#Create an API Client
from anthropic import Anthropic

client = Anthropic()

model = "claude-sonnet-4-0"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system = None, stop_sequences=[]):
    params = {
        "model" : model,
        "max_tokens" : 1000,
        "messages" : messages,
        "stop_sequences" : stop_sequences,
    }
    
    if system:
        params["system"]=system

    message = client.messages.create(**params)
    return message.content[0].text

#Make initial list of messages
messages = []


#Controlled Modelling

add_user_message(messages, "Is tea or coffee better at breakfast?")

add_assistant_message(messages, "Coffee is better because")

answer = chat(messages)


#How to use Stop sequences

add_user_message(messages, "Count from 1 to 10")

answer = chat(messages, stop_sequences=["5"])