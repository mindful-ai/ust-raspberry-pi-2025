import os
from datetime import datetime

class MotorLogger:
    def __init__(self, log_file="logs/motor_log.txt"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(line)
        print(line.strip())  # Optional: Show in terminal too
