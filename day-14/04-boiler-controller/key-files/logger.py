import datetime
import os
import csv

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "boiler_log.txt")
CSV_FILE = os.path.join(LOG_DIR, "boiler_log.csv")

def log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def log_csv(data_dict):
    os.makedirs(LOG_DIR, exist_ok=True)
    is_new = not os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp"] + list(data_dict.keys()))
        if is_new:
            writer.writeheader()
        data_dict["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(data_dict)
