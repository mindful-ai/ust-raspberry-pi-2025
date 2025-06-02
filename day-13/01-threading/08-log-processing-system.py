import threading
import queue
import random
import time
from datetime import datetime

log_queue = queue.Queue()


# Sample log levels and messages
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
sample_messages = [
    "User logged in",
    "File uploaded successfully",
    "Connection timed out",
    "Invalid user input",
    "Database query executed",
    "Cache miss",
    "API call failed",
    "Background job started"
]


def log_producer(producer_id, num_logs=10):
    for i in range(num_logs):
        level = random.choice(log_levels)
        message = random.choice(sample_messages)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"{timestamp} [{level}] {message}"
        log_queue.put(log)
        print(f"[Producer-{producer_id}] Generated: {log}")
        time.sleep(random.uniform(0.2, 0.5))

    print(f"[Producer-{producer_id}] Finished")


def log_consumer(consumer_id):

    while True:

        log = log_queue.get()
        if log is None:
            print(f"[Consumer-{consumer_id}] Shutdown signal received")
            break

        if "[ERROR]" in log:
            filename = 'error.log'
        elif "[INFO]" in log:
            filename = "info.log"
        elif "[WARNING]" in log:
            filename = "warning.log"
        else:
            filename = "debug.log"

        with open(filename, 'a') as f:
            f.write(log + '\n')

        print(f"[Consumer={consumer_id}] Wrote to {filename}: {log}")
        time.sleep(random.uniform(0.2, 0.5))


if __name__ == "__main__":

    NPRODUCERS = 3
    NCONSUMERS = 5
    LOGS_PER_PRODUCER = 10

    producers = []
    for i in range(NPRODUCERS):
        t = threading.Thread(target=log_producer, args=(i+1, LOGS_PER_PRODUCER))
        t.start()
        producers.append(t)

    
    consumers = []
    for i in range(NCONSUMERS):
        t = threading.Thread(target=log_consumer, args=(i+1,))
        t.start()
        consumers.append(t)

    for t in producers:
        t.join()

    for _ in range(NCONSUMERS):
        log_queue.put(None)

    for t in consumers:
        t.join()   

    print("\nAll logs processed. Check the output files")