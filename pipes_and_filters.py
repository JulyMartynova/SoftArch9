# main.py
import multiprocessing
from filters.filter_service import filter_service
from filters.screaming_service import screaming_service
from filters.publish_service import publish_service

def run_pipes_and_filters():
    # Создаем каналы (pipes) для передачи данных
    pipe1, pipe2 = multiprocessing.Pipe()  # Канал между API и фильтром
    pipe3, pipe4 = multiprocessing.Pipe()  # Канал между фильтром и сервисом SCREAMING
    pipe5, pipe6 = multiprocessing.Pipe()  # Канал между фильтром и сервисом SCREAMING

    # Создаем процессы для каждого фильтра
    filter_process = multiprocessing.Process(target=filter_service, args=(pipe2, pipe3))
    screaming_process = multiprocessing.Process(target=screaming_service, args=(pipe4, pipe5))
    publish_process = multiprocessing.Process(target=publish_service, args=(pipe6,))

    # Запуск процессов
    filter_process.start()
    screaming_process.start()
    publish_process.start()

    # Отправляем сообщения через pipe1
    pipe1.send("professor:Hello world!")
    pipe1.send("student: bird-watching is fun!")
    pipe1.send("SERVICES FUN!")

    # Завершаем процесс с помощью "END"
    pipe1.send('END')

    # Ожидаем завершения процессов
    filter_process.join()
    screaming_process.join()
    publish_process.join()

if __name__ == '__main__':
    run_pipes_and_filters()
