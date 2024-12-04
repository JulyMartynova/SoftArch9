# filters/screaming_service.py
import time

def screaming_service(input_pipe, output_pipe):
    while True:
        message = input_pipe.recv()  # Get message
        if message == 'END':  # Check for ending
            output_pipe.send(message)
            break
        print(f"Received message for screaming: {message}")
        message = message.upper()  # Make for upper case
        output_pipe.send(message)  # Send further