# rabbitmq.py
import multiprocessing
import subprocess
import time

import requests

def run_service(file_name):
    subprocess.run(["python", file_name])

def run_rabbitmq():
    folder = 'services'
    services = ["api_service.py", "filter_service.py", "screaming_service.py", "publish_service.py"]

    processes = []
    for service in services:
        p = multiprocessing.Process(target=run_service, args=(f'{folder}/{service}',))
        processes.append(p)
        p.start()

    # URL вашего API
    url = "http://localhost:5000/send_message"

    # Данные, которые нужно отправить
    data = {
        "alias": "professor",
        "message": "Hello World!555"
    }

    # Заголовки запроса
    headers = {
        "Content-Type": "application/json"
    }

    for i in range(3):
        # Отправка POST-запроса
        while True:
            try:
                response = requests.post(url, json=data, headers=headers)
            except:
                continue
            break

        # Проверка ответа
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        time.sleep(0.1)

    # Ожидаем завершения всех процессов
    for p in processes:
        p.terminate()  # Безопасное завершение процессов
        p.join()  # Дожидаемся завершения каждого процесса

if __name__ == '__main__':
    run_rabbitmq()