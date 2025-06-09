import asyncio
import random
import time

async def read_sensor():
    while True:
        temp = round(random.uniform(20, 45), 1)
        humidity = round(random.uniform(30, 60), 1)
        print(f"[{int(time.time() % 100)}s] Sensor Data: Temp = {temp}°C, Humidity = {humidity}%")
        await asyncio.sleep(1)

async def log_status():
    while True:
        cpu_usage = random.randint(10, 90)
        print(f"[{int(time.time() % 100)}s] System Status: CPU usage = {cpu_usage}%")
        await asyncio.sleep(3)

async def send_alert():
    while True:
        temp = round(random.uniform(20, 50), 1)
        if temp > 40:
            print(f"[{int(time.time() % 100)}s] 🚨 ALERT: High temperature! ({temp}°C)")
        await asyncio.sleep(5)

async def main():
    tasks = [
        asyncio.create_task(read_sensor()),
        asyncio.create_task(log_status()),
        asyncio.create_task(send_alert())
    ]
    await asyncio.sleep(15)  # Run the tasks for 15 seconds
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    print("✅ Monitoring stopped.")

if __name__ == "__main__":
    asyncio.run(main())

'''
How it works:

Three async coroutines simulate sensor reading, system logging, and alerting.
Each runs in its own task with different periodic delays (1s, 3s, and 5s).
The main coroutine runs them concurrently for 15 seconds and then cancels them gracefully.

'''