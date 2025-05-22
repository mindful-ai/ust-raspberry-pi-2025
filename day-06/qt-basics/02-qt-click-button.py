from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

def on_click():
    print("Button was clicked!")

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("QPushButton Example")

btn = QPushButton("Click Me", win)
btn.move(50, 50)
btn.clicked.connect(on_click)

win.resize(200, 150)
win.show()
sys.exit(app.exec_())