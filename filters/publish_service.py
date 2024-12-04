# filters/publish_service.py
import time
import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender_email = "softarch@mailslurp.xyz"
    receiver_email = "softarchout@mailslurp.xyz"
    password = "d4cARb1404QPnpoNNrTXc70dev3sE1uS"

    msg = MIMEText(message)
    msg['Subject'] = "New Message"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('mailslurp.mx', 2465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent!")


def publish_service(pipe):
    while True:
        message = pipe.recv()  # Get message
        if message == 'END':  # Check for ending
            break
        print(f"Sending email for message: {message}")
        send_email(message)  # Send message