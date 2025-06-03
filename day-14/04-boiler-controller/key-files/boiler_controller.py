from simulator.boiler_simulator import BoilerSimulator

class BoilerController:
    def __init__(self):
        self.simulator = BoilerSimulator()

    def start(self):
        self.simulator.running = True

    def stop(self):
        self.simulator.running = False

    def set_fuel_rate(self, rate):
        self.simulator.fuel_rate = rate

    def get_status(self):
        return self.simulator.update()
