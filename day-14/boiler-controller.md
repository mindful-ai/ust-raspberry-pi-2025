🧪 Assessment Problem Statement: Boiler Controller HMI with Simulator
-------------------------------------------------------------------------------------------

💡 Problem Title:

Design and Implement a Tkinter-Based Boiler Controller HMI with Simulation

🏭 Scenario / Background:

In a thermal power plant, a boiler control system is used to maintain safe and efficient operation by adjusting parameters like steam pressure, feed water flow, oxygen level, and temperature. As a trainee automation engineer, your task is to build a graphical HMI application for controlling and monitoring a simulated industrial boiler.

🎯 Objective:

    Develop a Tkinter-based GUI application that simulates a Boiler Controller HMI with:
    Parameter controls (via user inputs/sliders)
    Real-time monitoring of boiler metrics
    Live boiler simulation
    Logging of user inputs and simulated values
    Modular and maintainable code structure

🔧 Requirements

1. GUI Features
    Allow user input/control for:
    Feed Water Flow Rate (liters/min) — range: 10–100
    Fuel Flow Rate (kg/hr) — range: 50–300
    Air Flow Rate (m³/min) — range: 20–200
    Display real-time monitored values:
    Steam Pressure (bar)
    Boiler Temperature (°C)
    Oxygen Level (%)

    Use sliders or spinboxes for inputs and labels for monitored values. GUI should update every second.

2. Boiler Simulator (Backend Logic)

    Create a Python class BoilerSimulator that updates internal state every second using basic rules:

    # Sample update logic
    pressure += (feed_water_flow * 0.05 + fuel_flow * 0.02 - steam_pressure * 0.03)
    temperature += (fuel_flow * 0.1 - air_flow * 0.05)
    oxygen = 21 - (fuel_flow * 0.02) + (air_flow * 0.1)


    Clamp values to realistic ranges:

    Pressure: 0–100 bar
    Temperature: 100–600°C
    Oxygen: 0–21%

3. Logging

    Every change in user input or simulator update should be logged with timestamps
    Log file: logs/boiler_log.txt

    Example log line:

    [2025-06-02 10:45:02] Feed water flow set to 70 L/min
    [2025-06-02 10:45:03] Updated: Pressure=15.2 bar, Temp=320°C, Oxygen=18.3%


4. Code Structure (Multifile)

    Organize your solution using the following folder layout:

    boiler_hmi/
    ├── main.py
    ├── controller/
    │   ├── boiler_controller.py
    │   ├── boiler_simulator.py
    │   └── logger.py
    ├── ui/
    │   └── hmi_view.py
    └── logs/
        └── boiler_log.txt

🏆 Bonus Tasks

    Add a safety feature: if pressure > 80 bar or temperature > 550°C, the simulator should:
    Automatically trigger an emergency shutdown (turn off fuel and water flow)
    Display a red alert label in the GUI
    Log the emergency shutdown event

✨ Simulator Logic Stub


    class BoilerSimulator:
        def __init__(self):
            self.pressure = 10.0
            self.temperature = 120.0
            self.oxygen = 20.0

        def update(self, feed_water, fuel, air):
            self.pressure += (feed_water * 0.05 + fuel * 0.02 - self.pressure * 0.03)
            self.pressure = max(0, min(self.pressure, 100))

            self.temperature += (fuel * 0.1 - air * 0.05)
            self.temperature = max(100, min(self.temperature, 600))

            self.oxygen = 21 - (fuel * 0.02) + (air * 0.1)
            self.oxygen = max(0, min(self.oxygen, 21))

            return {
                "pressure": round(self.pressure, 2),
                "temperature": round(self.temperature, 1),
                "oxygen": round(self.oxygen, 2)
            }
