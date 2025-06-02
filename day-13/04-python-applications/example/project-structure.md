raspi_env_monitor/
│
├── main.py                # Entry point of the application
├── monitor/
│   ├── __init__.py
│   ├── gui.py             # Contains Tkinter GUI code
│   ├── sensor_simulator.py# Simulates sensor data
│   ├── logger.py          # Handles CSV logging
│   └── config.py          # Default configs like refresh interval
└── log.csv                # Generated on first log
