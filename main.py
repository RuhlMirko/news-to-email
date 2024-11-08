import requests
import os
import send_email


topic = "tesla"
api_key = os.getenv("NEWS")
# Look at <f"..."> in each line
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-10-08&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

request = requests.get(url)
content = request.json()


message = "Subject: 'Today news'\n\n"
for article in content['articles'][:10]:
    message += f"{article['title']}\n {article['description']}\n {article['url']}\n\n"

send_email.send_email_w(message)
print(message)


