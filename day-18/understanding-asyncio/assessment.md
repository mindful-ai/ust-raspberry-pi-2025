🧪 Assessment Problem Statement: Asynchronous Task Scheduler


Title: Simulate a Concurrent Task Scheduler Using asyncio


Objective:

Create a Python program using the asyncio module that simulates the execution of multiple tasks (e.g., fetching sensor data, logging system health, and sending alerts), all running concurrently and independently.

Scenario:

You are building an IoT monitoring dashboard that needs to perform the following tasks:
Read Sensor Data (every 1 second): Simulate reading temperature and humidity values.
Log System Status (every 3 seconds): Simulate logging CPU usage.
Send Alert (every 5 seconds): Simulate checking a condition and printing an alert if a simulated temperature is over 40°C.

Requirements:

Define each of the above as an async def coroutine.
Use asyncio.sleep() to simulate I/O delays and time-based scheduling.
Run all three tasks concurrently using asyncio.create_task().
Let the program run for 15 seconds and then exit gracefully.

Expected Output:

[1s] Sensor Data: Temp = 28.5°C, Humidity = 40%
[3s] System Status: CPU usage = 32%
[5s] ALERT: High temperature! (42.1°C)
...
(continues until 15 seconds, showing interleaved output)


