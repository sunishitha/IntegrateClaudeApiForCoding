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

messages = []

add_user_message(messages, "Write 1 sentence description of a fake database")

with client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        stream = True
    ) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass
        print(text, end="")
    
    # Get the complete message for database storage 
    stream.get_final_message()



