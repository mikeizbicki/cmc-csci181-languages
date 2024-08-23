from openai import OpenAI
import os
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    )

response = client.completions.create(
  model="llama3-8b-8192",
  prompt="Write a tagline for an ice cream shop."
)

print(response)
