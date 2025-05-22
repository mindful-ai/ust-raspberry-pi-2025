# Step-by-Step Guide: Create a Calculator with PyQt5 Designer

## Part 1: Design the Calculator UI Using Qt Designer

### Step 1: Launch Qt Designer

* Open Terminal or Command Prompt.
* Run the command:

  ```bash
  pyqt5-tools designer
  ```
* Or navigate to:

  ```
  C:\Users\<your-username>\.pyqt5-tools\pyqt5-tools\designer.exe
  ```

  and double-click to launch it.

---

### Step 2: Create a New Form

* In the dialog box, choose **"Main Window"** or **"Dialog without Buttons"**.
* Click **"Create"**.

---

### Step 3: Add Widgets

From the Widget Box (left panel), drag and drop the following widgets onto the form:

| Widget       | Object Name | Properties to Set                       |
| ------------ | ----------- | --------------------------------------- |
| QLineEdit    | input1      | Placeholder Text: "Enter first number"  |
| QLineEdit    | input2      | Placeholder Text: "Enter second number" |
| QRadioButton | addRadio    | Text: "Add"                             |
| QRadioButton | subRadio    | Text: "Subtract"                        |
| QRadioButton | mulRadio    | Text: "Multiply"                        |
| QRadioButton | divRadio    | Text: "Divide"                          |
| QPushButton  | calcButton  | Text: "Calculate"                       |
| QLabel       | resultLabel | Text: "Result will appear here"         |

#### Layout Tips

* Use a **QGroupBox** or **QHBoxLayout** for organizing the radio buttons.
* Use a **QVBoxLayout** or **Grid Layout** for the entire form.

---

### Step 4: Apply Layout

* Select the main window or form.
* Use **Form > Lay Out in a Grid/Vertically** to auto-arrange widgets.
* Adjust spacing and alignment.

---

### Step 5: Save the UI File

* Save the file as `calculator.ui`.

---

## Part 2: Load and Connect UI in Python

### Step 1: Convert `.ui` to Python (Optional)

```bash
pyuic5 -x calculator.ui -o calculator_ui.py
```

Or use `uic.loadUi()` directly in your Python script.

### Step 2: Python Code Example

```python
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QMessageBox
from PyQt5 import uic
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculator.ui", self)

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
```

---

## ✅ Final Notes

* You can customize fonts, padding, and colors using `setStyleSheet()` in code or Qt Designer's property editor.
* Use Qt Designer's "Preview" feature to see how your layout looks.

Happy Coding! ✨
