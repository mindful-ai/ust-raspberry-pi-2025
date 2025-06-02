import threading
import time

def io_task_1():
    print("Starting I/O Task 1")
    time.sleep(2)  # Simulating I/O (e.g., reading file or waiting for network)
    print("Finished I/O Task 1")

def io_task_2():
    print("Starting I/O Task 2")
    time.sleep(2)
    print("Finished I/O Task 2")

start_time = time.time()

t1 = threading.Thread(target=io_task_1)
t2 = threading.Thread(target=io_task_2)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"I/O-bound total time: {time.time() - start_time:.2f} seconds")
