import random

class BoilerSimulator:
    def __init__(self):
        self.running = False
        self.fuel_rate = 5.0  # in arbitrary units
        self.pressure = 10.0  # bar
        self.temperature = 80.0  # °C
        self.water_level = 100.0  # %

    def update(self):
        if self.running:
            self.temperature += self.fuel_rate * 0.5
            self.pressure += self.fuel_rate * 0.3
            self.water_level -= self.fuel_rate * 0.4
        else:
            self.temperature -= 0.2
            self.pressure
