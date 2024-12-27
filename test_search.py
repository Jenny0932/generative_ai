from tools import search, get_search_results

from dotenv import load_dotenv
import os

load_dotenv('.env')

api_key = os.getenv('GOOGLE_API_KEY')
cse_id = os.getenv('CSE_ID')

search_term = "openai"

search_items = search(search_item=search_term, 
                      api_key=api_key, 
                      cse_id=cse_id, 
                      search_depth=10)

results = get_search_results(search_items, search_term)

for result in results:
    print(f"Search order: {result['order']}")
    print(f"Link: {result['link']}")
    print(f"Snippet: {result['title']}")
    print(f"Summary: {result['Summary']}")
    print('-' * 80)