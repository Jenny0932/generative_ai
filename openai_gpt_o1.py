from openai import OpenAI
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_PROJECT_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)


response = client.chat.completions.create(
    model="o1-mini-2024-09-12",
    messages=[
        {
            "role": "user", 
            "content": "Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format."
        }
    ]
)

print(response.choices[0].message.content)