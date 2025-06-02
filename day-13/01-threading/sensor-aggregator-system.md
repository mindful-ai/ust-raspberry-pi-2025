🧾 Assessment Problem: Real-Time Sensor Data Aggregator
-------------------------------------------------------------------------------------------
🛰️ Context:

You are simulating part of an IoT (Internet of Things) system for a smart factory. Various machines send periodic sensor readings (temperature, vibration, humidity, etc.). Your task is to implement a threaded real-time data aggregation system where:

Producers simulate sensors generating data.
Consumers process and store this data in categorized logs and generate alerts for critical values.

🧠 Your Task:

Build a multithreaded Python program that:

👷‍♂️ Producers (Sensors):

Simulate 3 types of sensors: TemperatureSensor, HumiditySensor, and VibrationSensor.
Each sensor should:
    Generate readings every 0.5 to 1.5 seconds.
    Push messages like: "TEMP: 78.3°C", "HUMID: 41%", "VIBE: 0.03g" into a shared thread-safe queue.
    Run in its own thread.

🛠️ Consumers (Data Processors):

Consume messages from the queue in parallel threads.

For each reading:
    Append the reading to its respective file: temp.log, humidity.log, vibration.log.
    If a reading crosses a critical threshold (e.g., TEMP > 85°C, HUMID < 20%, VIBE > 0.5g), also write it to an alerts.log.

🧹 Graceful Shutdown:

Run the simulation for a fixed time (e.g., 20 seconds).
Cleanly shut down all producer and consumer threads.