import time
import psutil
from pipes_and_filters import run_pipes_and_filters
from rabbitmq import run_rabbitmq


def measure_performance(func, iterations=1):
    start_time = time.time()


    cpu_usage = []
    memory_usage = []

    for i in range(iterations):
        print(f'[ITERATION] {i + 1}')
        process = psutil.Process()


        cpu_usage.append(process.cpu_percent(interval=0.1))
        memory_usage.append(process.memory_info().rss / (1024 * 1024))

        func()
        print('///////////////------------------')
        print()

    end_time = time.time()

    total_time = end_time - start_time
    avg_time = total_time / iterations

    avg_cpu_usage = sum(cpu_usage) / len(cpu_usage)
    avg_memory_usage = sum(memory_usage) / len(memory_usage)

    peak_cpu_usage = max(cpu_usage)
    peak_memory_usage = max(memory_usage)

    return total_time, avg_time, avg_cpu_usage, avg_memory_usage, peak_cpu_usage, peak_memory_usage


def main():
    iterations = 1

    print("Testing Pipes-and-Filters Architecture...")
    pf_total_time, pf_avg_time, pf_avg_cpu, pf_avg_mem, pf_peak_cpu, pf_peak_mem = measure_performance(
        run_pipes_and_filters, iterations)
    print(f"Pipes-and-Filters Total Time: {pf_total_time:.2f} sec")
    print(f"Pipes-and-Filters Average Time per Run: {pf_avg_time:.4f} sec")
    print(f"Pipes-and-Filters Avg CPU Usage: {pf_avg_cpu}%")
    print(f"Pipes-and-Filters Avg Memory Usage: {pf_avg_mem:.2f} MB")
    print(f"Pipes-and-Filters Peak CPU Usage: {pf_peak_cpu}%")
    print(f"Pipes-and-Filters Peak Memory Usage: {pf_peak_mem:.2f} MB\n")

    print('\n\n')


    print("Testing RabbitMQ Architecture...")
    rmq_total_time, rmq_avg_time, rmq_avg_cpu, rmq_avg_mem, rmq_peak_cpu, rmq_peak_mem = measure_performance(
        run_rabbitmq, iterations)
    print(f"RabbitMQ Total Time: {rmq_total_time:.2f} sec")
    print(f"RabbitMQ Average Time per Run: {rmq_avg_time:.4f} sec")
    print(f"RabbitMQ Avg CPU Usage: {rmq_avg_cpu:.2f}%")
    print(f"RabbitMQ Avg Memory Usage: {rmq_avg_mem:.2f} MB")
    print(f"RabbitMQ Peak CPU Usage: {rmq_peak_cpu:.2f}%")
    print(f"RabbitMQ Peak Memory Usage: {rmq_peak_mem:.2f} MB\n")

    print("Performance Comparison Report:")
    print(f"- Pipes-and-Filters Avg Time: {pf_avg_time:.4f} sec")
    print(f"- RabbitMQ Avg Time: {rmq_avg_time:.4f} sec")
    if pf_avg_time < rmq_avg_time:
        print("Pipes-and-Filters is faster.")
    else:
        print("RabbitMQ is faster.")

    print("\nResource Utilization Comparison:")
    print(f"- Pipes-and-Filters Avg CPU Usage: {pf_avg_cpu:.2f}%")
    print(f"- RabbitMQ Avg CPU Usage: {rmq_avg_cpu:.2f}%")
    print(f"- Pipes-and-Filters Avg Memory Usage: {pf_avg_mem:.2f} MB")
    print(f"- RabbitMQ Avg Memory Usage: {rmq_avg_mem:.2f} MB")
    print(f"- Pipes-and-Filters Peak CPU Usage: {pf_peak_cpu:.2f}%")
    print(f"- RabbitMQ Peak CPU Usage: {rmq_peak_cpu:.2f}%")
    print(f"- Pipes-and-Filters Peak Memory Usage: {pf_peak_mem:.2f} MB")
    print(f"- RabbitMQ Peak Memory Usage: {rmq_peak_mem:.2f} MB")


if __name__ == "__main__":
    main()
