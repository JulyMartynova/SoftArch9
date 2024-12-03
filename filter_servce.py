import pika

STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]


def callback(ch, method, properties, body):
    message, user_alias = body.decode('utf-8').split('|')
    print(f"Filter service received: {message}")
    if any(word in message for word in STOP_WORDS):
        print("Message contains stop words, discarding.")
    else:
        send_to_screaming_service(message, user_alias)


def send_to_screaming_service(message, user_alias):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='screaming_queue')
    channel.basic_publish(exchange='', routing_key='screaming_queue', body=f"{message}|{user_alias}")
    connection.close()


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='filter_queue')
    channel.basic_consume(queue='filter_queue', on_message_callback=callback, auto_ack=True)
    print('Filter service is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()