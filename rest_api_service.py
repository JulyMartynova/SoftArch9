from flask import Flask, request, jsonify
import pika

app = Flask(__name__)


def send_to_filter_service(message, user_alias):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='filter_queue')
    channel.basic_publish(exchange='', routing_key='filter_queue', body=f"{message}|{user_alias}")
    connection.close()


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    user_alias = data.get('user_alias')
    send_to_filter_service(message, user_alias)
    return jsonify({"status": "Message received"})


if __name__ == "__main__":
    app.run(port=5000)