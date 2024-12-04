# screaming_service.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='filtered_queue')
channel.queue_declare(queue='screamed_queue')

def callback(ch, method, properties, body):
    message = body.decode().upper()
    channel.basic_publish(exchange='',
                          routing_key='screamed_queue',
                          body=message)

channel.basic_consume(queue='filtered_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('SCREAMING service started...')
channel.start_consuming()
