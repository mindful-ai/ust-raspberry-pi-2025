import threading
import time
import random

class ThreadSafeStack:
    def __init__(self):
        self.stack = []
        self.lock = threading.Lock()

    def push(self, item):
        with self.lock:
            self.stack.append(item)
            print(f"[{threading.current_thread().name}] Pushed: {item}")

    def pop(self):
        with self.lock:
            if not self.stack:
                print(f"[{threading.current_thread().name}] Tried to pop but stack is empty.")
                return None
            item = self.stack.pop()
            print(f"[{threading.current_thread().name}] Popped: {item}")
            return item

    def size(self):
        with self.lock:
            return len(self.stack)


# Producer thread function
def producer(stack, count):
    for _ in range(count):
        item = random.randint(1, 100)
        stack.push(item)
        time.sleep(random.uniform(0.1, 0.3))

# Consumer thread function
def consumer(stack, count):
    for _ in range(count):
        stack.pop()
        time.sleep(random.uniform(0.1, 0.3))


# Main function
if __name__ == "__main__":
    shared_stack = ThreadSafeStack()

    # Create producers and consumers
    producers = [threading.Thread(target=producer, name=f"Producer-{i+1}", args=(shared_stack, 5)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, name=f"Consumer-{i+1}", args=(shared_stack, 5)) for i in range(2)]

    # Start all threads
    for t in producers + consumers:
        t.start()

    # Wait for all threads to finish
    for t in producers + consumers:
        t.join()

    print("\n✅ All threads completed.")
    print("Final stack size:", shared_stack.size())
