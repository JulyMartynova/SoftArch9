import pika
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'


def send_email(message, user_alias):
    msg = MIMEText(f"User {user_alias} sent: {message}")
    msg['Subject'] = 'New Message'
    msg['From'] = SMTP_USERNAME
    msg['To'] = SMTP_USERNAME

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, SMTP_USERNAME, msg.as_string())


def callback(ch, method, properties, body):
    message, user_alias = body.decode('utf-8').split('|')
    print(f"Publish service received: {message}")
    send_email(message, user_alias)


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='publish_queue')
    channel.basic_consume(queue='publish_queue', on_message_callback=callback, auto_ack=True)
    print('Publish service is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()