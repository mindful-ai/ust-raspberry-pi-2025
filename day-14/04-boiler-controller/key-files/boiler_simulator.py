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
            self.pressure -= 0.1
            self.water_level += 0.1

        # Clamp values
        self.temperature = max(20, min(200, self.temperature))
        self.pressure = max(1, min(40, self.pressure))
        self.water_level = max(0, min(100, self.water_level))

        # Add some noise
        self.temperature += random.uniform(-0.5, 0.5)
        self.pressure += random.uniform(-0.2, 0.2)
        self.water_level += random.uniform(-0.3, 0.3)

        return {
            "Running": self.running,
            "Fuel Rate": round(self.fuel_rate, 2),
            "Pressure": round(self.pressure, 2),
            "Temperature": round(self.temperature, 2),
            "Water Level": round(self.water_level, 2),
        }

