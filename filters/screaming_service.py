# filters/screaming_service.py
import time

def screaming_service(input_pipe, output_pipe):
    while True:
        message = input_pipe.recv()  # Получаем сообщение
        if message == 'END':  # Проверка на окончание
            output_pipe.send(message)
            break
        print(f"Received message for screaming: {message}")
        message = message.upper()  # Преобразуем в верхний регистр
        output_pipe.send(message)  # Отправляем дальше