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

def chat(messages, system = None):
    params = {
        "model" : model,
        "max_tokens" : 1000,
        "messages" : messages,
    }
    
    if system:
        params["system"]=system

    message = client.messages.create(**params)
    return message.content[0].text


#Make an initial list of messages
messages = []

add_user_message(messages, "How do I solve 5x+3=2 for x?")

#Without system prompt
answer = chat(messages)

# With system prompt
system = """You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step."""

answer = chat(messages, system=system)
