import csv
from datetime import datetime

def log_data_to_csv(filename, temperature, humidity):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), temperature, humidity])
