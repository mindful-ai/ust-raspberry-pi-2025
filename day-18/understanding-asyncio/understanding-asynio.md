
# Understanding `asyncio` in Python – Prime Number Example

This guide demonstrates the difference between synchronous and asynchronous programming in Python using the `asyncio` library. We'll use the task of finding prime numbers to explore the advantages of using `asyncio`.

---

## 🔍 What is `asyncio`?

`asyncio` is Python's library for writing **asynchronous, non-blocking** code using coroutines. It’s ideal for I/O-bound tasks where you need concurrency without threads.

---

## 🧠 Key Concepts

| Concept | Description |
|--------|-------------|
| `async def` | Defines an asynchronous coroutine |
| `await` | Pauses the coroutine until the awaited result is ready |
| `asyncio.create_task()` | Schedules a coroutine to run concurrently |
| `asyncio.run()` | Runs the async event loop |

---

## 🎯 Use Case: Finding Prime Numbers in a Range

We'll simulate a delay while checking if each number is prime, as though it's an I/O-bound operation (e.g., API call or sensor read).

---

## ✅ Version 1: Without `asyncio` (Synchronous)

```python
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    print(f"Finding primes between {start} and {end}...")
    for num in range(start, end):
        time.sleep(0.1)  # Simulate delay
        if is_prime(num):
            print(f"Prime found: {num}")

start_time = time.time()
find_primes(10, 20)
find_primes(30, 40)
end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")
```

⏱️ **Expected Time**: ~2 seconds (0.1s × 20 iterations)

---

## 🚀 Version 2: With `asyncio` (Asynchronous)

```python
import asyncio

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

async def find_primes(start, end):
    print(f"🔍 Async finding primes between {start} and {end}...")
    for num in range(start, end):
        await asyncio.sleep(0.1)  # Simulate I/O delay
        if is_prime(num):
            print(f"✅ Prime: {num}")

async def main():
    task1 = asyncio.create_task(find_primes(10, 20))
    task2 = asyncio.create_task(find_primes(30, 40))
    await task1
    await task2

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")
```

⏱️ **Expected Time**: ~1 second — tasks run concurrently

---

## 📊 Comparison Table

| Feature             | Without `asyncio`      | With `asyncio`              |
|---------------------|------------------------|-----------------------------|
| Execution           | Sequential              | Concurrent (non-blocking)   |
| Suitable for        | CPU-bound tasks         | I/O-bound tasks             |
| Prime loops run     | One after the other     | In parallel (overlap waits) |
| Delay handling      | Blocks the program      | Does not block              |
| Total Time (2×10)   | ~2 seconds              | ~1 second                   |

---

## ⚠️ Notes

- `asyncio` is **not for heavy CPU-bound computation**. Use multiprocessing or threads for that.
- Best used when **waiting on I/O**, such as APIs, file operations, or sensors.

---

## ✅ Summary

Use `asyncio` when:
- Tasks involve delays due to I/O
- You want lightweight concurrency
- You don’t want the overhead of threads

---

## 🛠️ Related Topics

- Python Coroutines
- Event Loop
- Concurrency vs Parallelism
- `await`, `async`, and `yield`

