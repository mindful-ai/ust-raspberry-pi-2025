import threading
import queue
import time
import random

# Shared task queue
task_queue = queue.Queue()

# Producer function
def producer():
    for i in range(10):
        task = f"Task-{i}"
        print(f"[Producer] Putting {task} into queue")
        task_queue.put(task)
        time.sleep(random.uniform(0.1, 0.5))  # Simulate varying production times
    print("[Producer] Finished producing tasks")
    
    # Signal to consumers to exit
    for _ in range(3):  # Assuming 3 consumers
        task_queue.put(None)

# Consumer function
def consumer(consumer_id):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"[Consumer-{consumer_id}] Received shutdown signal")
            break
        print(f"[Consumer-{consumer_id}] Processing {task}")
        time.sleep(random.uniform(0.2, 0.6))  # Simulate work time
        task_queue.task_done()

# Start the producer
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# Start multiple consumer threads
consumer_threads = []
for i in range(3):
    t = threading.Thread(target=consumer, args=(i,))
    consumer_threads.append(t)
    t.start()

# Wait for all threads to finish
producer_thread.join()
for t in consumer_threads:
    t.join()

print("\n✅ All tasks processed and all threads finished.")
