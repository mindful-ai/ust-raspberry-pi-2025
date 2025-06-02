import threading

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
def find_highest_prime(start, end, thread_id, results ):
    highest = -1
    for num in range(start, end + 1):
        if is_prime(num):
            highest = num
    results[thread_id] = highest
    print(f"Thread={thread_id} finished. {start}, {end} -> {highest}")

threads = []
results = {}

ranges = [
    (0, 100000),
    (100000, 200000),
    (200000, 300000),
    (300000, 400000)
]

for i, (start, end) in enumerate(ranges):
    t = threading.Thread(target=find_highest_prime, args=(start, end, i, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

max_prime = max(results.values())
print("\nOverall highest -> ", max_prime)

print("Results: \n", results)