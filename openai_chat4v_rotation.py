from openai import OpenAI
import os
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=OPENAI_API_KEY)
# https://cdn.concreteplayground.com/content/uploads/2018/03/central-station-revamp4-supplied-1920x1080.jpeg
# "What’s in this image? What's the company name and the phone number?"
# https://www.smartsheet.com/sites/default/files/styles/900px/public/IC-Business-Invoice-Template.webp?itok=XR3kFM1T
# What's in this image? Is there any unusual activity in it? What's the status of the escalators? How many people in the image? 
# What is this product? Please return the product name and product brand in a json list
# https://i.postimg.cc/Dfxv4xdf/IMG-8934.jpg
# Choice(finish_reason=None, index=0, message=ChatCompletionMessage(content='```json\n{\n  "product_name": "AERODYNAMIC TRIMMING LINE",\n  "product_brand": "POWERFIT"\n}\n```', role='assistant', function_call=None, tool_calls=None), finish_details={'type': 'stop', 'stop': '<|fim_suffix|>'})
# https://i.postimg.cc/s2L8RZpr/IMG-8934-1.jpg
# Choice(finish_reason=None, index=0, message=ChatCompletionMessage(content='```json\n{\n  "product_name": "DISINFECTING WIPES",\n  "product_brand": "POWER FORCE"\n}\n```', role='assistant', function_call=None, tool_calls=None), finish_details={'type': 'stop', 'stop': '<|fim_suffix|>'})
# https://i.postimg.cc/rwkRQh36/IMG-8934-2.jpg
# Choice(finish_reason=None, index=0, message=ChatCompletionMessage(content='```json\n{\n  "product_name": "Aerodynamic Trimming Line",\n  "product_brand": "PowerFit"\n}\n```', role='assistant', function_call=None, tool_calls=None), finish_details={'type': 'stop', 'stop': '<|fim_suffix|>'})

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
