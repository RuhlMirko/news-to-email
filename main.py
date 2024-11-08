import requests
import os
import send_email

api_key = os.getenv("NEWS")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-10-08&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()


message = "Subject: 'News of tesla'\n\n"
for article in content['articles']:
    # message += article['title'] + "\n" + article['description'] + "\n\n"

    message += f"{article['title']}\n {article['description']}\n {article['url']}\n\n"
# send_email.send_email_w(message)
print(message)


