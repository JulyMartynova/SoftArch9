# publish_service.py
import pika
import smtplib
from email.mime.text import MIMEText

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='screamed_queue')


def send_email(message):
    sender_email = "softarch@mailslurp.xyz"
    receiver_email = "softarchout@mailslurp.xyz"
    password = "d4cARb1404QPnpoNNrTXc70dev3sE1uS"

    msg = MIMEText(message)
    msg['Subject'] = "New Message from RabbitMQ"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('mailslurp.mx', 2465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def callback(ch, method, properties, body):
    message = body.decode()
    send_email(message)


channel.basic_consume(queue='screamed_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Publish service started...')
channel.start_consuming()
