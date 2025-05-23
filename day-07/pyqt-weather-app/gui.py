from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
)
from PyQt5.QtCore import Qt

class WeatherAppUI(QWidget):
    def __init__(self, weather_callback):
        super().__init__()
        self.weather_callback = weather_callback
        self.setWindowTitle("Live Weather App")
        self.setGeometry(100, 100, 400, 250)
        self.init_ui()

    def init_ui(self):
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setStyleSheet("font-size: 16px; padding: 8px;")

        self.fetch_button = QPushButton("Get Weather")
        self.fetch_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.fetch_button.clicked.connect(self.fetch_weather)

        self.result_label = QLabel("Weather info will appear here")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px; padding: 10px;")
        self.result_label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def fetch_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.result_label.setText("Please enter a city name.")
            return

        result = self.weather_callback(city)
        self.result_label.setText(result)
