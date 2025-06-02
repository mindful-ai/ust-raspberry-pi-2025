import threading
import time

def cpu_task():
    print("Starting CPU task")
    count = 0
    for i in range(10**7):
        count += i
    print("Finished CPU task")

start_time = time.time()

'''
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()

t1.join()
t2.join()
'''

cpu_task()
cpu_task()

print(f"CPU-bound total time: {time.time() - start_time:.2f} seconds")
