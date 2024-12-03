from multiprocessing import Process, Queue
import filters.filter1 as filter1
import filters.filter2 as filter2
import filters.filter3 as filter3

def run_filter(filter_func, input_queue, output_queue):
    while True:
        message, user_alias = input_queue.get()
        if message is None:
            break
        processed_message = filter_func.process(message, user_alias)
        if processed_message:
            output_queue.put(processed_message)

if __name__ == "__main__":
    queue1 = Queue()
    queue2 = Queue()
    queue3 = Queue()

    p1 = Process(target=run_filter, args=(filter1, queue1, queue2))
    p2 = Process(target=run_filter, args=(filter2, queue2, queue3))
    p3 = Process(target=run_filter, args=(filter3, queue3, None))

    p1.start()
    p2.start()
    p3.start()

    message = "Hello, world!"
    user_alias = "user123"
    queue1.put((message, user_alias))
    print(f"Sent message: {message}")

    p1.join()
    p2.join()
    p3.join()