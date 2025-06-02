
Each producer will randomly generate log messages (e.g., "INFO: User logged in", "ERROR: Timeout while fetching data", etc.).

Log messages will be put into a shared thread-safe queue.

🛠️ Consumers:

Multiple consumers will read from the queue and:
Filter based on log level (e.g., only "ERROR").
Write filtered logs to separate files (e.g., error.log, info.log).
Simulate time-consuming storage operations with a sleep delay.

🔧 Constraints:

Producers and consumers must run concurrently.
Use a queue.Queue() to coordinate communication.
Use sentinel values (e.g., None) to signal consumers to shut down after all logs are produced.

✅ Optional Enhancements for Participants:

Add a timestamp to each log.
Add a separate consumer that aggregates metrics (e.g., number of errors per minute).
Use logging module instead of print statements for realism.
Visualize log flow using a dashboard (e.g., with tkinter or streamlit).

🧪 Sample Output (Console or File):


[Producer-1] Generated log: INFO: User logged in
[Consumer-2] Writing to info.log: INFO: User logged in
[Producer-3] Generated log: ERROR: Timeout while fetching data
[Consumer-1] Writing to error.log: ERROR: Timeout while fetching data