import pika

def callback(ch, method, properties, body):
    message, user_alias = body.decode('utf-8').split('|')
    print(f"Screaming service received: {message}")
    processed_message = message.upper()
    send_to_publish_service(processed_message, user_alias)

def send_to_publish_service(message, user_alias):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='publish_queue')
    channel.basic_publish(exchange='', routing_key='publish_queue', body=f"{message}|{user_alias}")
    connection.close()

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='screaming_queue')
    channel.basic_consume(queue='screaming_queue', on_message_callback=callback, auto_ack=True)
    print('Screaming service is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()