import sys
from PyQt5.QtWidgets import QApplication
import logic
from gui import WeatherApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WeatherApp(logic)
    win.show()
    sys.exit(app.exec_())
