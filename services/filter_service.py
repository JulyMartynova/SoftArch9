# filter_service.py
import pika

# Настройка соединения
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')
channel.queue_declare(queue='filtered_queue')

stop_words = ['bird-watching', 'ailurophobia', 'mango']

def callback(ch, method, properties, body):
    message = body.decode()
    if any(word in message for word in stop_words):
        print(f"Message blocked: {message}")
    else:
        channel.basic_publish(exchange='',
                              routing_key='filtered_queue',
                              body=message)

channel.basic_consume(queue='message_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Filter service started...')
channel.start_consuming()
