from openai import OpenAI
import os
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(
  model="dall-e-3",
  prompt="A team photo including a group of people working hard on digital transformation. Background is under Sydney Harbor Bridge with view of ocean and sun. The team members include experts in Data, Human Center Design, eliminate failure demand, business architecture, and business analysis. People are also data scientists, engineers, designers, business analyst, and leaders",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(response)
print(image_url)
