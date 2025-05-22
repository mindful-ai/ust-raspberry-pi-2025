
# PyQt5 Cheat Sheet

## 🧱 Commonly Used Widgets and Their Methods

| Widget        | Description                        | Common Methods                                                                 |
|---------------|------------------------------------|--------------------------------------------------------------------------------|
| `QLabel`      | Display text or images             | `setText()`, `setPixmap()`, `setFont()`, `setAlignment()`, `clear()`           |
| `QPushButton` | Clickable button                   | `setText()`, `click()`, `setEnabled()`, `setStyleSheet()`, `setFont()`         |
| `QLineEdit`   | Single-line text input             | `text()`, `setText()`, `clear()`, `setPlaceholderText()`, `setEchoMode()`      |
| `QTextEdit`   | Multi-line text input              | `toPlainText()`, `setPlainText()`, `clear()`, `append()`                       |
| `QComboBox`   | Dropdown selection                  | `addItem()`, `addItems()`, `currentText()`, `setCurrentIndex()`, `clear()`     |
| `QCheckBox`   | Toggle check box                   | `isChecked()`, `setChecked()`, `setText()`, `toggle()`                         |
| `QRadioButton`| Exclusive selection button         | `isChecked()`, `setChecked()`, `setText()`                                     |
| `QSlider`     | Slider to select value             | `setValue()`, `value()`, `setMinimum()`, `setMaximum()`, `setOrientation()`    |
| `QProgressBar`| Display progress                   | `setValue()`, `value()`, `setMinimum()`, `setMaximum()`, `reset()`             |
| `QListWidget` | List of selectable items           | `addItem()`, `addItems()`, `clear()`, `currentItem()`, `takeItem()`            |
| `QFileDialog` | File selection dialog              | `getOpenFileName()`, `getSaveFileName()`, `getExistingDirectory()`             |
| `QMessageBox` | Dialog for messages                | `information()`, `warning()`, `critical()`, `question()`                        |
| `QFont`       | Font settings                      | `setPointSize()`, `setBold()`, `setItalic()`, `family()`                       |
| `QPixmap`     | Image handling                     | `load()`, `scaled()`, `width()`, `height()`                                    |

## 🧭 Layouts

| Layout         | Description                        | Common Methods                                   |
|----------------|------------------------------------|--------------------------------------------------|
| `QVBoxLayout`  | Vertical stacking of widgets       | `addWidget()`, `addLayout()`, `addStretch()`     |
| `QHBoxLayout`  | Horizontal stacking of widgets     | `addWidget()`, `addLayout()`, `addSpacing()`     |
| `QGridLayout`  | Grid-based widget arrangement      | `addWidget(widget, row, col)`, `setSpacing()`    |

## 🎯 Signals and Slots in PyQt5

| Signal Source       | Signal                          | Typical Connection                                           | Description                                                   |
|---------------------|----------------------------------|--------------------------------------------------------------|---------------------------------------------------------------|
| `QPushButton`       | `clicked`                        | `button.clicked.connect(slot)`                               | Emitted when button is clicked                                |
| `QPushButton`       | `pressed`                        | `button.pressed.connect(slot)`                               | Emitted when mouse button is pressed down on the button       |
| `QPushButton`       | `released`                       | `button.released.connect(slot)`                              | Emitted when mouse button is released                         |
| `QLineEdit`         | `textChanged(str)`               | `line.textChanged.connect(slot)`                             | Emitted when the text changes                                |
| `QLineEdit`         | `returnPressed()`                | `line.returnPressed.connect(slot)`                           | Emitted when Enter/Return key is pressed                     |
| `QLineEdit`         | `editingFinished()`              | `line.editingFinished.connect(slot)`                         | Emitted when editing is finished (focus lost or Enter)       |
| `QComboBox`         | `currentIndexChanged(int)`       | `combo.currentIndexChanged.connect(slot)`                    | Emitted when selection changes                               |
| `QComboBox`         | `activated(int)`                 | `combo.activated.connect(slot)`                              | Emitted when item is selected by user                        |
| `QCheckBox`         | `stateChanged(int)`              | `checkbox.stateChanged.connect(slot)`                        | Emitted when checkbox state changes                          |
| `QRadioButton`      | `toggled(bool)`                  | `radio.toggled.connect(slot)`                                | Emitted when selection state changes                         |
| `QSlider`           | `valueChanged(int)`              | `slider.valueChanged.connect(slot)`                          | Emitted when slider value changes                            |
| `QSlider`           | `sliderPressed()`                | `slider.sliderPressed.connect(slot)`                         | Emitted when slider is pressed                               |
| `QSlider`           | `sliderReleased()`               | `slider.sliderReleased.connect(slot)`                        | Emitted when slider is released                              |
| `QSpinBox`          | `valueChanged(int)`              | `spin.valueChanged.connect(slot)`                            | Emitted when spinbox value changes                           |
| `QPlainTextEdit`    | `textChanged()`                  | `plain.textChanged.connect(slot)`                            | Emitted when text is changed                                 |
| `QTextEdit`         | `textChanged()`                  | `text.textChanged.connect(slot)`                             | Emitted when content changes                                 |
| `QListWidget`       | `itemClicked(QListWidgetItem*)`  | `list.itemClicked.connect(slot)`                             | Emitted when an item is clicked                              |
| `QListWidget`       | `currentItemChanged(...)`        | `list.currentItemChanged.connect(slot)`                      | Emitted when current item changes                            |
| `QTableWidget`      | `cellClicked(int, int)`          | `table.cellClicked.connect(slot)`                            | Emitted when a cell is clicked                               |
| `QTabWidget`        | `currentChanged(int)`            | `tabs.currentChanged.connect(slot)`                          | Emitted when active tab changes                              |
| `QTimer`            | `timeout()`                      | `timer.timeout.connect(slot)`                                | Emitted when timer expires                                   |
| `QDialog`           | `accepted()`                     | `dialog.accepted.connect(slot)`                              | Emitted when accepted() is called                            |
| `QDialog`           | `rejected()`                     | `dialog.rejected.connect(slot)`                              | Emitted when rejected() is called                            |
| `QFileDialog`       | `fileSelected(str)`              | `fileDialog.fileSelected.connect(slot)`                      | Emitted when file is selected                                |
| `QWidget`           | `customEvent(QEvent*)`           | `widget.customEvent.connect(slot)` (requires subclassing)    | Used for handling custom events                              |

> ✅ **Note:** Always ensure the slot function signature matches the signal being connected.



## 🎨 Styling and Fonts

| Method                        | Description                                 |
|------------------------------|---------------------------------------------|
| `setStyleSheet("...")`       | Set custom CSS styles                       |
| `setFont(QFont("Arial", 12))`| Set widget font                             |
| `setAlignment(Qt.AlignCenter)` | Align content                            |

## 📁 File Handling Example
```python
from PyQt5.QtWidgets import QFileDialog

filename, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt)")
with open(filename, 'r') as f:
    content = f.read()
```

## 🧰 Basic Application Structure
```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("PyQt5 Window")
win.resize(400, 300)
win.show()
sys.exit(app.exec_())
```

## ⏲ Timers
```python
from PyQt5.QtCore import QTimer

timer = QTimer()
timer.timeout.connect(my_function)
timer.start(1000)  # in milliseconds
```

## ✅ Tips
- Use `.exec_()` for modal dialogs
- `.show()` is needed to display widgets
- Always close with `sys.exit(app.exec_())`
