from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont 
import sys

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("QPushButton Example")

label = QLabel("Hello, PyQt!")

# Set large font
font = QFont()
font.setPointSize(24)  # You can adjust the size as needed
label.setFont(font)

label.show()
sys.exit(app.exec_())
