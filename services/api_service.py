# api_service.py
from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# Настройка соединения с RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_alias = data.get('alias')
    message = data.get('message')

    # Отправка сообщения в очередь
    channel.basic_publish(exchange='',
                          routing_key='message_queue',
                          body=f"{user_alias}:{message}")
    return jsonify({"status": "Message sent to queue"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
