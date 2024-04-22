import smtplib, ssl
import email_config


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = email_config.username
    password = email_config.password

    receiver = email_config.receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)