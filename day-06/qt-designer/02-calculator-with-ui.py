from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QMessageBox
from PyQt5 import uic
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("qt-calculator.ui", self)

        self.calcButton.clicked.connect(self.calculate)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())

            if self.addRadio.isChecked():
                result = num1 + num2
            elif self.subRadio.isChecked():
                result = num1 - num2
            elif self.mulRadio.isChecked():
                result = num1 * num2
            elif self.divRadio.isChecked():
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ValueError("Cannot divide by zero")
            else:
                result = "Select an operation"

            self.resultLabel.setText(f"Result: {result}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.setWindowTitle("Calculator")
    calc.show()
    sys.exit(app.exec_())