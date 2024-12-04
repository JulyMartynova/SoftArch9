# filters/filter_service.py
import time

stop_words = ['bird-watching', 'ailurophobia', 'mango']

def filter_service(input_pipe, output_pipe):
    while True:
        message = input_pipe.recv()  # Get message from channel
        if message == 'END':  # Check for ending
            output_pipe.send(message)
            break
        print(f"Received message for filtering: {message}")
        if any(word in message for word in stop_words):
            print(f"Message blocked: {message}")
        else:
            output_pipe.send(message)  # Send message to other process