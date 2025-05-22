import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stylish Calculator")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("background-color: #fefefe;")

        # Inputs
        self.num1_input = QLineEdit()
        self.num2_input = QLineEdit()
        input_style = """
            QLineEdit {
                padding: 8px;
                border: 2px solid #aaa;
                border-radius: 8px;
                font-size: 16px;
            }
        """
        self.num1_input.setStyleSheet(input_style)
        self.num2_input.setStyleSheet(input_style)

        # Operation radio buttons
        self.add_radio = QRadioButton("Add")
        self.sub_radio = QRadioButton("Subtract")
        self.mul_radio = QRadioButton("Multiply")
        self.div_radio = QRadioButton("Divide")
        self.add_radio.setChecked(True)

        radio_style = """
            QRadioButton {
                spacing: 12px;
                font-size: 16px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
            }
        """
        for radio in [self.add_radio, self.sub_radio, self.mul_radio, self.div_radio]:
            radio.setStyleSheet(radio_style)

        # Button
        self.calc_button = QPushButton("Calculate")
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #005999;
            }
        """)
        self.calc_button.clicked.connect(self.calculate_result)

        # Result label
        self.result_label = QLabel("Result will appear here")
        self.result_label.setStyleSheet("""
            QLabel {
                background-color: #F0F0F0;
                padding: 12px;
                border: 2px solid #ccc;
                border-radius: 10px;
                font-size: 18px;
                color: #333;
            }
        """)
        self.result_label.setFont(QFont("Arial", 16))

        # Layouts
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.addWidget(QLabel("Enter Number 1:"))
        main_layout.addWidget(self.num1_input)
        main_layout.addWidget(QLabel("Enter Number 2:"))
        main_layout.addWidget(self.num2_input)

        op_layout = QHBoxLayout()
        for radio in [self.add_radio, self.sub_radio, self.mul_radio, self.div_radio]:
            op_layout.addWidget(radio)

        main_layout.addLayout(op_layout)
        main_layout.addWidget(self.calc_button)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate_result(self):
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
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                result = "Unknown Operation"
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers.")
        except ZeroDivisionError:
            self.result_label.setText("Division by zero error.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
