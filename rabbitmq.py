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

    # URL of API
    url = "http://localhost:5000/send_message"

    # Data to send
    data = {
        "alias": "professor",
        "message": "Hello World!555"
    }

    # Headers of request
    headers = {
        "Content-Type": "application/json"
    }

    for i in range(3):
        # Sending POST - request
        while True:
            try:
                response = requests.post(url, json=data, headers=headers)
            except:
                continue
            break

        # Checking answer
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        time.sleep(0.1)

    # Waiting ending of processes
    for p in processes:
        p.terminate()  # Safe ending
        p.join()  # Waiting of process ending

if __name__ == '__main__':
    run_rabbitmq()