import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

from groq import Groq
import fulltext
import os

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)
#from openai import OpenAI
#client = OpenAI(
    #base_url="https://api.groq.com/openai/v1",
    #api_key=os.environ.get("GROQ_API_KEY"),
    #)

text = fulltext.get(args.filename)
#with open(args.filename) as f:
    #text = f.read()

chunksize = 1024
chunks = [text[i:i+chunksize] for i in range(0, len(text), chunksize)]
user_messages = [{'role': 'user', 'content': chunk} for chunk in chunks]

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Summarize the following text in only a single paragraph, at most 3 sentences and written at a 3rd grade level. Do not include any intro text, only the summary itself.",
        },
    ]+user_messages,
    model="llama3-8b-8192",
    stream=True,
)
#print(chat_completion.choices[0].message.content)
for chunk in chat_completion:
    print(chunk.choices[0].delta.content, end='')

