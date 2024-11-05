import smtplib
import ssl
import os


def send_email_w(message):
    encoded_message = message.encode('utf-8')

    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    username = "ruhlmirkojoel@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "mirkaapo.709@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, encoded_message)

    print("Message Sent.")

