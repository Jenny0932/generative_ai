from openai import OpenAI
import os
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
import os
from dotenv import load_dotenv
import base64

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=OPENAI_API_KEY)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "image.png"
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image? Is there any unusual activity in it? What's the status of the escalators? How many people in the image? Note that B stands for Bus, T stands for Train, L stands for Lightrail, and M stands for Metro"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
            },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
