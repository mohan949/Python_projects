import requests
import json

# Your URL with API Key
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=dc8d6c1572e644c7883421ed765efae7"

response = requests.get(url)

# Parse the JSON response
data = response.json()

# Check if articles exist in the response and print each author
if 'articles' in data:
    for article in data['articles']:
        # Print the author's name
        print("Author:", article.get("author", "No author"))
else:
    print("No articles found.")
