import requests
import os

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-10-05&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
print(content)

# for article in content['articles']:
#     print(article['title'])
#     print(article['description'])
#     print()

