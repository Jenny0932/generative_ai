from openai import OpenAI
import os
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What is this product? Please return the product name and product brand in a json list."},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://i.postimg.cc/rwkRQh36/IMG-8934-2.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
