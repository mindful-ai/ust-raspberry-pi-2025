import time
from .logger import MotorLogger

class MotorController:
    def __init__(self):
        self.running = False
        self.speed = 0  # RPM
        self.direction = 0
        self.logger = MotorLogger()

    def start_motor(self):
        if not self.running:
            self.running = True
            self.logger.log("Motor started")

    def stop_motor(self):
        if self.running:
            self.running = False
            self.logger.log("Motor stopped")

    def set_speed(self, value):
        if self.running:
            self.speed = value
            self.logger.log(f"Motor speed set to {value} RPM")
        else:
            self.logger.log("Speed change ignored: motor not running")

    def get_status(self):
        return {
            "running": self.running,
            "speed": self.speed
        }
