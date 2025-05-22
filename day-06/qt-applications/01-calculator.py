from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton,
    QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup
)
from PyQt5.QtGui import QFont
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setup_ui()

    def setup_ui(self):
        font = QFont("Arial", 14, QFont.Bold)

        # Input fields
        self.num1_label = QLabel("Number 1:")
        self.num1_label.setFont(font)
        self.num1_input = QLineEdit()
        self.num1_input.setFont(font)
        self.num1_input.setFixedHeight(40)

        self.num2_label = QLabel("Number 2:")
        self.num2_label.setFont(font)
        self.num2_input = QLineEdit()
        self.num2_input.setFont(font)
        self.num2_input.setFixedHeight(40)

        # Radio buttons
        self.add_radio = QRadioButton("Add")
        self.sub_radio = QRadioButton("Subtract")
        self.mul_radio = QRadioButton("Multiply")
        self.div_radio = QRadioButton("Divide")

        for rb in [self.add_radio, self.sub_radio, self.mul_radio, self.div_radio]:
            rb.setFont(font)
            rb.setMinimumHeight(30)

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.add_radio)
        self.radio_group.addButton(self.sub_radio)
        self.radio_group.addButton(self.mul_radio)
        self.radio_group.addButton(self.div_radio)
        self.add_radio.setChecked(True)

        # Button
        self.calc_button = QPushButton("Calculate")
        self.calc_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.calc_button.setFixedHeight(50)

        self.calc_button.clicked.connect(self.calculate)

        # Result
        self.result_label = QLabel("Result:")
        self.result_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.result_label.setMinimumHeight(50)

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Padding
        layout.setSpacing(15)  # Space between widgets

        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)

        layout.addWidget(self.add_radio)
        layout.addWidget(self.sub_radio)
        layout.addWidget(self.mul_radio)
        layout.addWidget(self.div_radio)

        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setMinimumSize(400, 500)  # Overall window size

    def calculate(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())

            if self.add_radio.isChecked():
                result = num1 + num2
            elif self.sub_radio.isChecked():
                result = num1 - num2
            elif self.mul_radio.isChecked():
                result = num1 * num2
            elif self.div_radio.isChecked():
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.result_label.setText("Result: Cannot divide by zero")
                    return

            self.result_label.setText(f"Result: {result:.2f}")

        except ValueError:
            self.result_label.setText("Result: Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
