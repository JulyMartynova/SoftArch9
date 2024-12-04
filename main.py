from multiprocessing import Process, Queue
import filters.filter1 as filter1
import filters.filter2 as filter2
import filters.filter3 as filter3


def run_filter(filter_func, input_queue, output_queue):
    while True:
        message, user_alias = input_queue.get()
        if message is None:
            break
        print(f"Processing message: {message} with user_alias: {user_alias}")
        processed_message = filter_func(message, user_alias)
        if processed_message and output_queue is not None:
            print(f"Sending processed message: {processed_message}")
            output_queue.put(processed_message)


if __name__ == "__main__":
    queue1 = Queue()
    queue2 = Queue()
    queue3 = Queue()

    p1 = Process(target=run_filter, args=(filter1.process, queue1, queue2))
    p2 = Process(target=run_filter, args=(filter2.process, queue2, queue3))
    p3 = Process(target=run_filter, args=(filter3.process, queue3, None))

    p1.start()
    p2.start()
    p3.start()

    message = "Hello, world!"
    user_alias = "user123"
    queue1.put((message, user_alias))
    print(f"Sent message: {message}")

    # Добавляем None в очередь для завершения работы процессов
    queue1.put((None, None))
    queue2.put((None, None))
    queue3.put((None, None))

    p1.join()
    p2.join()
    p3.join()

    # Вывод результатов
    while not queue3.empty():
        result = queue3.get()
        print(f"Final processed message: {result}")