import random
import time
from threading import Thread
from monitor.config import TEMP_RANGE, HUMIDITY_RANGE, REFRESH_INTERVAL

class SensorSimulator(Thread):
    def __init__(self, callback, stop_event):
        super().__init__()
        self.callback = callback
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            temperature = round(random.uniform(*TEMP_RANGE), 2)
            humidity = round(random.uniform(*HUMIDITY_RANGE), 2)
            self.callback(temperature, humidity)
            time.sleep(REFRESH_INTERVAL)
