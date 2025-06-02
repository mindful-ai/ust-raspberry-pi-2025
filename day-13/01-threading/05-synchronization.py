import threading

# Shared variable
counter = 0

def increment_without_lock(n):
    global counter
    for _ in range(n):
        counter += 1

if __name__ == "__main__":
    counter = 0
    n = 100000

    t1 = threading.Thread(target=increment_without_lock, args=(n,))
    t2 = threading.Thread(target=increment_without_lock, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Without Lock - Final Counter:", counter)
