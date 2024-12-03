import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

def process(message, user_alias):
    print(f"Filter 3 received: {message}")
    send_email(message, user_alias)

def send_email(message, user_alias):
    msg = MIMEText(f"User {user_alias} sent: {message}")
    msg['Subject'] = 'New Message'
    msg['From'] = SMTP_USERNAME
    msg['To'] = SMTP_USERNAME

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, SMTP_USERNAME, msg.as_string())