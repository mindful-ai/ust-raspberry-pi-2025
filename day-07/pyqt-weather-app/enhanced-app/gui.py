from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class WeatherApp(QWidget):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic
        self.setWindowTitle("Live Weather App")
        self.setGeometry(100, 100, 640, 480)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter City Name")
        self.city_input.setStyleSheet("font-size: 16px; padding: 6px;")

        self.icon_label = QLabel()
        self.temp_label = QLabel("Temperature")
        self.desc_label = QLabel("Condition")

        for label in (self.temp_label, self.desc_label):
            label.setStyleSheet("font-size: 18px;")

        self.canvas = FigureCanvas(Figure(figsize=(5, 2)))
        self.ax = self.canvas.figure.add_subplot(111)

        self.refresh_button = QPushButton("Refresh Weather")
        self.refresh_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.refresh_button.clicked.connect(self.update_weather)

        # Layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.city_input)
        input_layout.addWidget(self.refresh_button)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.icon_label)
        top_text_layout = QVBoxLayout()
        top_text_layout.addWidget(self.temp_label)
        top_text_layout.addWidget(self.desc_label)
        top_layout.addLayout(top_text_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

        # Auto-refresh timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(300000)  # 5 min

    def update_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.temp_label.setText("Please enter a city")
            self.desc_label.setText("")
            self.icon_label.clear()
            return

        data = self.logic.get_weather(city)
        if not data:
            self.temp_label.setText("City not found!")
            self.desc_label.setText("")
            self.icon_label.clear()
            return

        self.temp_label.setText(f"{data['temp']} °C")
        self.desc_label.setText(data['desc'])

        icon_path = f"icons/{data['icon']}.png"
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            self.icon_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

        # Plot historical
        temps = self.logic.get_historical_data()
        self.ax.clear()
        self.ax.plot(temps, marker='o')
        self.ax.set_title("Temperature Trend")
        self.ax.set_ylabel("Temp (°C)")
        self.ax.set_xlabel("Last 10 Readings")
        self.canvas.draw()
