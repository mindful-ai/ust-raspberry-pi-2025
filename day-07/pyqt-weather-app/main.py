import sys
from PyQt5.QtWidgets import QApplication
from gui import WeatherAppUI
from logic import get_weather

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherAppUI(get_weather)
    window.show()
    sys.exit(app.exec_())
